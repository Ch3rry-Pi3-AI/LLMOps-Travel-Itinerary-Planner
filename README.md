# 🚀 **Kubernetes Deployment — LLMOps Travel Itinerary Planner**

In this stage, we deploy the **LLMOps Travel Itinerary Planner** onto a **Kubernetes cluster** running on our **Minikube setup within a GCP VM**.
This stage brings the entire project to life — containerising the Streamlit application and serving it publicly via Kubernetes services.

## 🧭 **Step 1 — Connect Docker to Minikube**

In your VM terminal, run:

```bash
eval $(minikube docker-env)
```

This command ensures Docker points to Minikube’s internal environment so your image builds **directly inside Minikube’s Docker daemon**.

Now, build your Docker image:

```bash
docker build -t streamlit-app:latest .
```

Once complete, confirm the image exists:

```bash
docker images
```

Example output:

```
IMAGE                                             ID             DISK USAGE   
gcr.io/k8s-minikube/storage-provisioner:v5        6e38f40d628d       31.5MB      
streamlit-app:latest                              bd292243bb00        964MB      
registry.k8s.io/coredns/coredns:v1.12.1           52546a367cc9         75MB      
registry.k8s.io/etcd:3.6.4-0                      5f1f5298c888        195MB      
...
```

Your **streamlit-app:latest** image is now ready to deploy.

## 🔐 **Step 2 — Inject Secrets into Kubernetes**

This project uses **Groq only**, so create a secret containing just the Groq API key:

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=""
```

Replace `""` with your real API key.

You should see:

```
secret/llmops-secrets created
```

## 🧩 **Step 3 — Deploy the Application**

Apply your Kubernetes deployment and service file:

```bash
kubectl apply -f k8s-deployment.yaml
```

Example output:

```
deployment.apps/streamlit-app created
service/streamlit-service created
```

Check that your pod is running:

```bash
kubectl get pods
```

Example:

```
NAME                              READY   STATUS    RESTARTS   AGE
streamlit-app-58b5995844-66kth    1/1     Running   0          32s
```

## 💻 **Step 4 — Forward Ports and Access the App**

Run:

```bash
kubectl port-forward svc/streamlit-service 8501:80 --address 0.0.0.0
```

This forwards **external traffic → port 8501** on your Streamlit app inside Kubernetes.

Keep this terminal open.

Now, in your browser, visit:

```
http://<YOUR_EXTERNAL_IP>:8501
```

Example:

```
http://136.114.199.97:8501
```

Your **Travel Itinerary Planner Streamlit interface** will now be accessible from anywhere.

## ✅ **In Summary**

You have successfully:

* Built and containerised your **Streamlit** application using Docker
* Deployed it to Kubernetes running on Minikube
* Injected your Groq API key securely
* Exposed the service externally via port forwarding

Your **LLMOps Travel Itinerary Planner** is now running in a fully functional Kubernetes environment on **Google Cloud Platform**, completing your end-to-end deployment workflow.