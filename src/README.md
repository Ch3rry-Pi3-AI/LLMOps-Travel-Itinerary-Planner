# 🧠 **Source Code Overview — LLMOps Travel Itinerary Planner**

The `src/` directory contains the **core implementation** of the LLMOps Travel Itinerary Planner.
It is structured to maintain **clarity, modularity, and scalability**, ensuring that configuration, utilities, workflow chains, and core logic remain cleanly separated and easy to extend.

## 📁 Folder Overview

```text
src/
├── chains/                     
│   └── itinerary_chain.py      # 🔄 LCEL pipeline for generating Markdown-formatted itineraries
├── core/
│   └── planner.py              # 🧩 Controller for user inputs, conversation state, and itinerary creation
├── config/
│   ├── config.py               # ⚙️ Loads environment variables (e.g., Groq API key) via .env
│   └── README.md               # Documentation for configuration module
└── utils/
    ├── custom_exception.py     # 🪵 Unified exception handling with detailed debugging info
    ├── logger.py               # 🪵 Structured logging used across the application
    └── README.md               # Documentation for utility modules
```

## 🔄 `chains/` — LLM Workflow Pipelines

The `chains` folder contains the **LangChain Expression Language (LCEL)** workflows used to generate structured travel itineraries.

Current module:

* **`itinerary_chain.py`**
  Defines the full itinerary-generation pipeline using:

  * A structured chat prompt
  * Groq’s Llama-3.3 model
  * A `StrOutputParser` for clean Markdown output
    Includes a standalone test runner for quick local validation.

## 🧩 `core/` — Core Application Logic

The `core` folder contains the **controller-level logic** that orchestrates how user inputs are processed and how itinerary generation is executed.

Current module:

* **`planner.py`**
  Implements the `TravelPlanner` class responsible for:

  * Capturing city and interest inputs
  * Maintaining conversation history with `HumanMessage` and `AIMessage`
  * Invoking the LCEL itinerary generation chain
  * Logging and error handling
    Includes a fully runnable `__main__` block for standalone testing.

## ⚙️ `config/` — Environment & Credential Management

The `config` folder handles secure loading of all environment variables used by the application.

* **`config.py`**
  Loads API keys (such as the Groq key) from the `.env` file and exposes them to the rest of the system.

This ensures that sensitive values are **not hardcoded**, remain **centralised**, and are **safe to update** without modifying source code.

## 🪵 `utils/` — Logging & Exception Handling

The `utils` folder provides foundational utilities supporting project-wide debugging and traceability.

* **`custom_exception.py`** — Wraps errors with detailed context (file, line number, traceback).
* **`logger.py`** — Provides a central logger with timestamps and severity levels.

These utilities ensure consistent behaviour across all modules.

## 🔍 Current Status

The `src/` directory is now populated with:

✔ A complete itinerary-generation chain
✔ A functional planning controller
✔ Stable configuration loading
✔ Logging and exception foundations

This structure provides a **solid, extensible base** for upcoming features such as multi-day planning, activity filtering, and the Streamlit interface.

