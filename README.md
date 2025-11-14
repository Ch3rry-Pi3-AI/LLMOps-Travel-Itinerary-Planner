# 🐳 **Docker & Kubernetes Deployment — LLMOps Travel Itinerary Planner**

This branch packages the **Streamlit-based Travel Itinerary Planner** into a **Docker container** and provides a **Kubernetes deployment + service** for running it in a cluster.

The new `Dockerfile` defines how to build a Python 3.12-based image that runs the Streamlit app, and `k8s-deployment.yaml` describes how to deploy that image and expose it via a LoadBalancer service.

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
├── Dockerfile                 # 🐳 Container image definition for the Streamlit app
├── k8s-deployment.yaml        # ☸️ Kubernetes Deployment + Service manifest
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

> 💡 Only `Dockerfile` and `k8s-deployment.yaml` are annotated, as they are the new components introduced in this branch.

## 🧩 **Overview**

This stage turns the Travel Itinerary Planner into a **deployable service**:

* The **Dockerfile**:

  * Uses `python:3.12-slim` as the base image
  * Installs system dependencies (e.g. `build-essential`, `curl`)
  * Copies the project into `/app`
  * Installs the package in editable mode with `pip install -e .`
  * Exposes port **8501** for Streamlit
  * Starts the app via `streamlit run app.py`

* The **Kubernetes manifest** (`k8s-deployment.yaml`):

  * Creates a `Deployment` that runs the Streamlit container
  * Mounts environment variables from the `llmops-secrets` Kubernetes Secret
  * Exposes the app via a `Service` of type `LoadBalancer` on port **80 → 8501**

This is the first stage where the app is fully prepared for **containerised, cloud-native deployment**.

## 🐳 **Docker Image Details**

The `Dockerfile`:

* Uses environment settings:

  ```dockerfile
  ENV PYTHONDONTWRITEBYTECODE=1 \
      PYTHONUNBUFFERED=1
  ```

* Sets the working directory:

  ```dockerfile
  WORKDIR /app
  ```

* Installs OS-level dependencies and cleans up APT cache:

  ```dockerfile
  RUN apt-get update && apt-get install -y \
      build-essential \
      curl \
      && rm -rf /var/lib/apt/lists/*
  ```

* Copies the project and installs Python deps:

  ```dockerfile
  COPY . .
  RUN pip install --no-cache-dir -e .
  ```

* Exposes port **8501** and runs Streamlit:

  ```dockerfile
  EXPOSE 8501
  CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
  ```

### 🔨 Build & Run Locally with Docker

From the project root:

```bash
# Build image
docker build -t llmops-travel-planner:latest .

# Run container
docker run -p 8501:8501 --env-file .env llmops-travel-planner:latest
```

Then open `http://localhost:8501` in your browser.

## ☸️ **Kubernetes Deployment Details**

The `k8s-deployment.yaml` file defines two resources: a `Deployment` and a `Service`.

### Deployment

* Runs one replica of the Streamlit app:

  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: streamlit-app
    labels:
      app: streamlit
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: streamlit
    template:
      metadata:
        labels:
          app: streamlit
      spec:
        containers:
          - name: streamlit-container
            image: streamlit-app:latest
            imagePullPolicy: IfNotPresent
            ports:
              - containerPort: 8501
            envFrom:
              - secretRef:
                  name: llmops-secrets
  ```

* Assumes you have a Kubernetes `Secret` called `llmops-secrets` providing the required environment variables (e.g. `GROQ_API_KEY`).

### Service

* Exposes the app externally via a LoadBalancer:

  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: streamlit-service
  spec:
    type: LoadBalancer
    selector:
      app: streamlit
    ports:
      - protocol: TCP
        port: 80
        targetPort: 8501
  ```

* Traffic to port **80** on the LoadBalancer is forwarded to port **8501** on the pod.

## 🚀 **How to Deploy to Kubernetes**

Assuming your image is pushed to a registry (or available on the node), and your kube context is set:

1. **Create the secret** (example):

   ```bash
   kubectl create secret generic llmops-secrets \
     --from-literal=GROQ_API_KEY="your_groq_api_key_here"
   ```

   Add other environment variables as needed.

2. **Apply the manifest**:

   ```bash
   kubectl apply -f k8s-deployment.yaml
   ```

3. **Check resources**:

   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get svc
   ```

4. Once the `streamlit-service` has an external IP (for a cloud LoadBalancer), open:

   ```text
   http://<EXTERNAL_IP>/
   ```

to access the Travel Itinerary Planner in your browser.

## 🧰 **Integration Notes**

| Component                       | Role                                                   |
| ------------------------------- | ------------------------------------------------------ |
| `Dockerfile`                    | Builds a Python 3.12-based image for the Streamlit app |
| `k8s-deployment.yaml`           | Defines Kubernetes Deployment + LoadBalancer Service   |
| `app.py`                        | Streamlit UI entry point inside the container          |
| `src/core/planner.py`           | Orchestrates city and interests → itinerary            |
| `src/chains/itinerary_chain.py` | LCEL chain that generates the itinerary text           |
| `src/config/config.py`          | Reads environment variables (e.g. from `.env`/secrets) |

## ✅ **In summary**

This branch transforms the LLMOps Travel Itinerary Planner into a **containerised, cluster-ready service**.
With the new `Dockerfile` and `k8s-deployment.yaml`, the Streamlit app can be built into an image, pushed to a registry, and deployed behind a LoadBalancer in a Kubernetes environment, making it ready for scalable, production-style use.
