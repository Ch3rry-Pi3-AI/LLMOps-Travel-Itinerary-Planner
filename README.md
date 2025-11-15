# 📊 **Centralised Logging Deployment — LLMOps Travel Itinerary Planner**

This branch introduces a complete **centralised logging pipeline** for the Travel Itinerary Planner using the **ELK stack**:

* **Filebeat** — Collects logs from every container/pod
* **Logstash** — Processes, transforms, and routes logs
* **Elasticsearch** — Stores logs in a powerful, searchable index
* **Kibana** — Visualises logs through dashboards and search

These four components work together to provide full observability of the application and cluster.
This is the first stage where the project gains **production-grade, cluster-wide log monitoring**.

## 🗂️ **Project Structure (Updated)**

```text
LLMOPS-TRAVEL-ITINERARY-PLANNER/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── img/
│   └── streamlit/
│       └── streamlit_app.gif
├── llmops_travel_itinerary_planner.egg-info/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
├── main.py
├── app.py
├── Dockerfile
├── k8s-deployment.yaml
├── filebeat.yaml           # 📡 Collects container logs from all cluster nodes
├── logstash.yaml           # 🔄 Receives logs and forwards them to Elasticsearch
├── elasticsearch.yaml      # 🗄️ Stores logs in indexed search-optimised storage
├── kibana.yaml             # 📊 Web UI for searching and visualising logs
├── src/
│   ├── chains/
│   │   └── itinerary_chain.py
│   ├── core/
│   │   └── planner.py
│   ├── config/
│   │   ├── config.py
│   │   └── README.md
│   └── utils/
│       ├── custom_exception.py
│       ├── logger.py
│       └── README.md
└── README.md
```

Only the following files are new in this branch and are annotated here:

* `filebeat.yaml` 📡
* `logstash.yaml` 🔄
* `elasticsearch.yaml` 🗄️
* `kibana.yaml` 📊

## 🧩 **Overview of the Logging Pipeline**

This stage introduces a full **ELK-style logging workflow** that enables:

* Cluster-wide log collection
* Central storage of logs
* Indexable log search
* Visual dashboards
* Debugging of failures in real time

Below is a clear beginner-friendly breakdown of what each component does and why it matters.

### 📡 **Filebeat — Log Collector**

Filebeat runs as a **DaemonSet**, meaning **one pod per Kubernetes node**, ensuring:

* Every pod’s logs (`/var/log/containers/*.log`) are collected
* Kubernetes metadata (namespace, pod name, container name) is added
* Logs are forwarded to **Logstash**

**Intuition:**
Imagine Filebeat as a “tiny agent” sitting on every machine, picking up every log file and forwarding it reliably.

### 🔄 **Logstash — Log Router & Transformer**

Logstash receives logs from Filebeat and can:

* Filter them
* Parse them
* Transform them
* Route them

In this project, the configuration:

* Accepts logs on port **5044** (standard Beats input)
* Sends them straight to Elasticsearch

**Intuition:**
If Filebeat is the courier, Logstash is the post office—it sorts, organises, and routes deliveries.

### 🗄️ **Elasticsearch — Log Storage & Search Engine**

Elasticsearch stores logs as **documents** in an index.
It is optimised for:

* Full-text search
* Time-series queries
* Filtering & aggregation
* High-speed retrieval

In this deployment:

* Runs as a **single node** for simplicity
* Stores logs in a persistent volume
* No security enabled (development mode)

**Intuition:**
Elasticsearch is like a giant, super-fast search engine for your logs.

### 📊 **Kibana — Log Viewer & Dashboard Tool**

Kibana connects to Elasticsearch and provides:

* A web UI for viewing logs
* Filters, queries, dashboards
* Time-series visualisations
* Error and performance insights

Exposed via a **NodePort** so you can open it in your browser.

**Intuition:**
Kibana is your “control centre”—search logs, view charts, identify errors.

:

## 🔄 **How the Log Flow Works (Simple Example)**

Consider your Streamlit app pod writes:

```
2025-11-21 14:21:05 INFO Itinerary generated successfully
```

Here is what happens:

1. **Filebeat** (on the node) reads `/var/log/containers/app-xyz.log`.
2. It attaches metadata:

   ```
   namespace=default
   pod=streamlit-app-123
   container=streamlit-container
   ```
3. Filebeat forwards the enriched log to **Logstash**.
4. Logstash receives it and sends it to **Elasticsearch**.
5. Elasticsearch stores it as a document in an index:

   ```
   filebeat-2025.11.21
   ```
6. You open **Kibana**, search:

   ```
   app:streamlit AND level:INFO
   ```
7. You immediately see the log with filters and timestamps.

This provides real production-grade observability.

:

## 🚀 **How to Deploy the Logging Stack**

Assuming your cluster has the `logging` namespace:

```bash
kubectl create ns logging
```

Apply all four components:

```bash
kubectl apply -f elasticsearch.yaml
kubectl apply -f logstash.yaml
kubectl apply -f filebeat.yaml
kubectl apply -f kibana.yaml
```

Check pods:

```bash
kubectl get pods -n logging
```

Once Kibana is running:

```bash
minikube service kibana -n logging
```

Or, for cloud clusters:

```
http://<NODE_IP>:30601
```

## 🧰 **Integration Notes**

| Component            | Purpose                                                        |
| -------------------- | -------------------------------------------------------------- |
| `filebeat.yaml`      | Collects logs from all pods and forwards to Logstash           |
| `logstash.yaml`      | Receives Filebeat logs and forwards them to Elasticsearch      |
| `elasticsearch.yaml` | Stores logs in searchable indices                              |
| `kibana.yaml`        | Web UI for querying logs and building dashboards               |
| `app.py`             | Application producing logs                                     |
| `logger.py`          | Structured logging used by Filebeat → Logstash → Elasticsearch |

## ✅ **In summary**

This branch adds a **complete cluster-wide logging pipeline**, elevating your LLMOps Travel Itinerary Planner from a deployed app to a **monitorable, observable, production-ready service**.
