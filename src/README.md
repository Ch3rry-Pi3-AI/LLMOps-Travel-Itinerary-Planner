# 🧠 **Source Code Overview — LLMOps Travel Itinerary Planner**

The `src/` directory contains the **core source code** for the **LLMOps Travel Itinerary Planner**.
It is structured to maintain **clarity**, **scalability**, and **separation of concerns**, ensuring that configuration, utilities, and future logic are modular and easy to maintain.

## 📁 Folder Overview

```text
src/
├── chains/                     # 🔄 Placeholder for itinerary generation workflows
├── core/                       # 🧩 Placeholder for core LLM orchestration and reasoning logic
├── config/                     # ⚙️ Configuration management
│   └── config.py               # Loads environment variables (e.g., Groq API key)
└── utils/                      # 🪵 Logging and exception-handling utilities
    ├── custom_exception.py     # Provides consistent, context-rich exception handling
    └── logger.py               # Implements structured, time-stamped logging
```

## ⚙️ `config/` — Configuration Management

The `config` folder contains modules responsible for **managing environment variables and API credentials**.
The existing `config.py` file securely loads values from the `.env` file, such as the **Groq API key**, ensuring that sensitive information is kept outside the codebase and accessed programmatically when required.

## 🪵 `utils/` — Utility Modules

The `utils` folder provides **shared utility components** that support consistent debugging and logging across all parts of the project.
It currently includes:

* **`custom_exception.py`** — Defines a unified `CustomException` class that captures detailed context for any errors raised, including file name, line number, and traceback.
* **`logger.py`** — Configures a centralised logging system that records messages with timestamps and severity levels, supporting transparent monitoring and debugging.

## 🧩 `core/` and `chains/` — Future Expansion Areas

The `core` and `chains` folders are currently placeholders that will later contain the **main itinerary planning logic** and **workflow orchestration** components.
At this stage, their structure has been established as part of the initial setup, ready to be populated with future modules as the project develops.
