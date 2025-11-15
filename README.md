# 🔗 **GitHub Integration and Firewall Configuration — LLMOps Travel Itinerary Planner**

In this stage, we connect the **LLMOps Travel Itinerary Planner** GitHub repository to the **Google Cloud Platform (GCP) Virtual Machine**, allowing direct version control operations from the VM.
We also configure a **firewall rule** to ensure the VM can communicate securely with GitHub and external services.

## 🧭 **Step 1 — Clone the GitHub Repository**

Go to your project’s GitHub repository.
Click the green **“<> Code”** dropdown and copy the **HTTPS URL** of the repository.

Example:

```
https://github.com/Ch3rry-Pi3-AI/LLMOps-Travel-Itinerary-Planner.git
```

Now, in your GCP VM terminal, run:

```bash
git clone https://github.com/Ch3rry-Pi3-AI/LLMOps-Travel-Itinerary-Planner.git
```

(Replace this URL with your real repository link.)

Next, navigate into the cloned directory:

```bash
cd LLMOps-Travel-Itinerary-Planner
```

You are now inside your project folder within the VM.

## ⚙️ **Step 2 — Configure Git Identity**

Set up your Git global configuration so commits made from the VM are correctly attributed to you.

```bash
git config --global user.email "the_rfc@hotmai.co.uk"
git config --global user.name "Roger J. Campbell"
```

Verify the configuration:

```bash
git config --list
```

You should now see your email and username.

## 🔑 **Step 3 — Generate a GitHub Personal Access Token**

1. Go to **GitHub → Settings**.

2. Scroll to **Developer Settings**.

3. Click **Personal access tokens → Tokens (classic)**.

4. Select **Generate new token → Generate new token (classic)**.

5. Give it a name, e.g., `travel-itinerary`.

6. Select the following scopes:

   * `repo`
   * `workflow`
   * `admin:org`
   * `admin:repo_hook`
   * `admin:org_hook`

7. Click **Generate token**.

⚠️ **Copy the token immediately** — GitHub will never show it again.

## 🚀 **Step 4 — Authenticate and Pull from GitHub**

Now that you have a token, pull from GitHub:

```bash
git pull origin main
```

When prompted:

* **Username:** your GitHub username
* **Password:** your personal access token

Authentication will complete and the pull will succeed.

## 🔥 **Step 5 — Create a GCP Firewall Rule**

Next, configure a firewall rule in GCP to ensure your VM can communicate with GitHub and other external services.

1. In the **Google Cloud Console**, search for **Network Security**.
2. Under **Cloud NGFW**, click **Firewall rule → + Create firewall policy**.
3. Set **Policy name** to:

```
allow-llmops
```

4. Configure:

| Field                   | Setting                      |
| ----------------------- | ---------------------------- |
| **Targets**             | All instances in the network |
| **Source IPv4 ranges**  | `0.0.0.0/0`                  |
| **Protocols and ports** | Allow all                    |

5. Click **Create**.

Your firewall policy now allows full outbound communication between your VM and GitHub.

## ✅ **In Summary**

You have now successfully:

* Cloned the **LLMOps Travel Itinerary Planner** repo into your GCP VM
* Configured Git identity for authenticated pushes
* Created a **GitHub personal access token** for secure auth
* Created a **GCP firewall rule** for proper connectivity

Your VM is now fully connected to GitHub and ready for container builds, logging deployment, CI/CD, and Kubernetes orchestration.
