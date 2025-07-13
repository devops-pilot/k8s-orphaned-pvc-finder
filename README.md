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

