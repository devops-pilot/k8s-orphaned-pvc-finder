from kubernetes import client, config
from tabulate import tabulate
from colorama import Fore, Style
from datetime import datetime, timezone

# Load kubeconfig
config.load_kube_config()

core = client.CoreV1Api()

print(f"\n🔍 Scanning all namespaces for orphaned PVCs...\n")

results = []

# Get all namespaces
namespaces = [ns.metadata.name for ns in core.list_namespace().items]

for ns in namespaces:
    # Get all PVCs in the namespace
    pvcs = core.list_namespaced_persistent_volume_claim(namespace=ns).items
    if not pvcs:
        continue

    # Get all pods in the namespace
    pods = core.list_namespaced_pod(namespace=ns).items
    mounted_volumes = set()

    for pod in pods:
        for vol in pod.spec.volumes or []:
            if vol.persistent_volume_claim:
                mounted_volumes.add(vol.persistent_volume_claim.claim_name)

    for pvc in pvcs:
        pvc_name = pvc.metadata.name
        storage = pvc.spec.resources.requests.get("storage", "N/A")
        status = pvc.status.phase
        creation_time = pvc.metadata.creation_timestamp
        age_days = (datetime.now(timezone.utc) - creation_time).days
        is_orphaned = pvc_name not in mounted_volumes

        color = Fore.RED if is_orphaned else Fore.GREEN
        results.append([
            ns,
            pvc_name,
            storage,
            status,
            age_days,
            f"{color}{'❌ Orphaned' if is_orphaned else '✔️ Mounted'}{Style.RESET_ALL}"
        ])

# Display table
print(tabulate(
    results,
    headers=["Namespace", "PVC Name", "Storage", "Status", "Age (days)", "Mount Status"],
    tablefmt="pretty"
))
