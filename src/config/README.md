# 🧠 **Source Code Overview — LLMOps Travel Itinerary Planner**

The `src/` directory contains the **core source code** for the **LLMOps Travel Itinerary Planner**.
It is designed for **clarity**, **scalability**, and **modularity**, keeping configuration, utilities, and LLM workflow logic cleanly separated for maintainability and future development.

## 📁 Folder Overview

```text
src/
├── chains/                     # 🔄 LLM-driven itinerary generation workflows
│   └── itinerary_chain.py       # Uses Groq-powered model to create city day-trip itineraries
├── core/                       # 🧩 Placeholder for future core orchestration logic
├── config/                     # ⚙️ Configuration management
│   └── config.py               # Loads environment variables and stores API credentials
└── utils/                      # 🪵 Logging and exception-handling utilities
    ├── custom_exception.py     # Provides consistent, context-rich exception handling
    └── logger.py               # Implements structured, time-stamped logging
```

## ⚙️ `config/` — Configuration Management

The `config` folder contains the **environment variable management system** for the project.
The `config.py` file securely loads values such as the **Groq API key** from the `.env` file, ensuring credentials remain outside the source code while staying easily accessible throughout the application.

## 🪵 `utils/` — Utility Modules

The `utils` folder provides shared utility components that enable consistent logging and error handling.

* **`custom_exception.py`** — Defines a unified `CustomException` class that records detailed error context, including the file, line, and traceback information.
* **`logger.py`** — Configures a single logging setup with timestamps and severity levels, promoting transparency and traceability across all modules.

## 🔄 `chains/` — Itinerary Generation Workflows

The `chains` folder contains LLM-based workflow logic for generating travel itineraries.
The implemented **`itinerary_chain.py`** file connects the **Groq API** with **LangChain’s prompt orchestration**, producing concise, structured, day-trip itineraries for a given city and set of user interests.

This file serves as the foundation of the project’s intelligent reasoning layer — combining prompt templates, LLM configuration, and response generation into a reusable function.

## 🧩 `core/` — Future Development Placeholder

The `core` folder has been created to host future modules responsible for **core logic orchestration** and **system-level reasoning**.
At this stage, it remains an empty structural placeholder as part of the project setup.

At present, the **configuration**, **utility**, and **itinerary chain** modules have been fully implemented — forming a functional and modular starting point for the LLMOps Travel Itinerary Planner.
