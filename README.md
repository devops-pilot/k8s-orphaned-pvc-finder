# 📦 Kubernetes Orphaned PVC Finder

This tool scans your Kubernetes cluster and finds **orphaned PVCs** — Persistent Volume Claims not mounted by any pods.

---

## 🔍 Features

- Lists all PVCs in all namespaces
- Detects PVCs not attached to any pods
- Shows:
  - Namespace
  - PVC Name
  - Size
  - Status (Bound/Pending)
  - Age (days)
  - Mount Status
- Color-coded output
- Helpful for cleanup and storage cost control

---

## 📁 Project Structure

```
k8s-orphaned-pvc-finder/
├── pvc_inspector.py
├── requirements.txt
├── .gitignore
└── README.md
```


---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
## 2. Set your kube context
```
kubectl config current-context
```
##### Make sure your context has access to all namespaces you want to inspect.
## 3. Run the script
```
python3 pvc_inspector.py
```
## 🧪 Sample Output
```
🔍 Scanning all namespaces for orphaned PVCs...

+-------------+-------------------------+---------+--------+-------------+---------------+
| Namespace   | PVC Name                | Storage | Status | Age (days) | Mount Status  |
+-------------+-------------------------+---------+--------+-------------+---------------+
| dev         | redis-pvc               | 1Gi     | Bound  | 98          | ❌ Orphaned    |
| uat         | postgres-data           | 10Gi    | Bound  | 12          | ✔️ Mounted     |
| staging     | unused-claim            | 5Gi     | Bound  | 204         | ❌ Orphaned    |
+-------------+-------------------------+---------+--------+-------------+---------------+
```
## ⚠️ Notes
- Only shows volumes of type persistentVolumeClaim
- No changes are made — read-only inspection
- PVCs with status Pending are shown as well
## 📝 License
- MIT
## 🙌 Contributions
- Star it ⭐ | Fork it 🍴 | Improve it 🚀 PRs are welcome!
