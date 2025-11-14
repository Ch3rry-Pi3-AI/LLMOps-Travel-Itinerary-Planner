# ⚙️ **Configuration Overview — LLMOps Travel Itinerary Planner**

This folder contains configuration modules that manage **environment variables** and **API credentials** for the **LLMOps Travel Itinerary Planner**.
It ensures that all sensitive keys and integration settings are **loaded securely and consistently** across the project.

## 📁 Folder Overview

```text
config/
├─ __init__.py   # Marks the directory as a package
└─ config.py     # Loads environment variables and stores API credentials
```

## 🔑 `config.py` — Environment Variable Management

### Purpose

The `config.py` module centralises the loading of all **API keys** and **environment variables** used throughout the application.
It leverages the `.env` file for secure credential storage, keeping sensitive values out of the source code.

### Key Features

* Automatically loads variables from a `.env` file using `python-dotenv`.
* Provides clean, programmatic access to API keys for the **Groq inference service**.
* Acts as a single point of reference for future expansion (e.g., database endpoints, embedding models).

### Example Usage

```python
from config.config import GROQ_API_KEY

print("Using Groq API Key:", GROQ_API_KEY[:6] + "...")
```

### 🧩 Notes

* Ensure that a `.env` file exists in the project root before running the application.

* Example `.env` entry:

  ```bash
  GROQ_API_KEY="your_api_key_here"
  ```

* For security, never commit `.env` files or credentials to version control.
