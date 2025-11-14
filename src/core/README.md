# ⚙️ **Core Logic — LLMOps Travel Itinerary Planner**

The `core/` folder contains the **high-level application logic** that orchestrates how user inputs are processed and how itinerary generation is executed.
It acts as the bridge between the **frontend/UI layer** (e.g., Streamlit) and the **LLM workflow components** defined in `src/chains/`.

This is where the project begins to take shape as an interactive system rather than a standalone chain.

## 📁 Folder Overview

```text
src/core/
└── planner.py    # Manages user inputs, conversation state, and itinerary generation
```

## 🧭 `planner.py` — Travel Planning Controller

### Purpose

`planner.py` defines the **TravelPlanner** class, which:

* Stores user-provided inputs (city and interests)
* Maintains conversation history with `HumanMessage` and `AIMessage` objects
* Invokes the LCEL itinerary generation pipeline (`itinerary_chain`)
* Wraps all operations with logging and custom exception handling
* Provides a clean, importable interface for the Streamlit front-end or future agents
* Includes a standalone test runner for quick local validation

### Key Features

* Uses the **LCEL runnable pipeline** for consistent itinerary generation
* Clean separation of:

  * Input handling
  * LLM pipeline invocation
  * Error management
  * Logging
* Beginner-friendly comments and NumPy-style documentation
* Fully deterministic behaviour suitable for user-facing apps

### Example Integration

```python
from src.core.planner import TravelPlanner

planner = TravelPlanner()
planner.set_city("Tokyo")
planner.set_interests("sushi, history, anime")

itinerary = planner.create_itinerary()
print(itinerary)
```

## 🔍 Current Status

This folder currently contains the **core orchestration logic** for the system.
Additional modules (e.g., session managers, agent logic, conversation memory) can be added here in future stages, but at this point:

✔ `planner.py` is complete
✔ LLM invocation is stable
✔ The chain-to-core interaction is fully functional

