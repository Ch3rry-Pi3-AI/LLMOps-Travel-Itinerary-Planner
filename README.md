# 🧭 **Planner Logic — LLMOps Travel Itinerary Planner**

This branch introduces the **core planning controller** of the LLMOps Travel Itinerary Planner — the `TravelPlanner`, which orchestrates user inputs, maintains conversation state, and invokes the itinerary generation chain through a clean, high-level interface.

This component represents the first point where the planner behaves like a real application:
capturing user input and returning a full Markdown itinerary using the underlying LLM workflow.

## 🗂️ **Project Structure (Updated)**

```text
LLMOPS-TRAVEL-ITINERARY-PLANNER/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── llmops_travel_itinerary_planner.egg-info/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
├── main.py
├── src/
│   ├── chains/
│   │   └── itinerary_chain.py
│   ├── core/
│   │   └── planner.py    # 🧩 Controller for user inputs, state, and itinerary generation
│   ├── config/
│   │   ├── config.py
│   │   └── README.md
│   └── utils/
│       ├── custom_exception.py
│       ├── logger.py
│       └── README.md
└── README.md
```

> 💡 Only `src/core/planner.py` is annotated here, as it is the new component introduced in this branch.

## 🧩 **Overview**

The **TravelPlanner** class serves as the main orchestrator for itinerary creation.
It handles:

* User-provided **city**
* User-provided **interests** (comma-separated)
* A growing **conversation history**
* Invocation of the full LCEL itinerary chain
* Logging and exception tracing

This module completes the backend logic needed for an interactive, user-facing itinerary application.

### Key Enhancements in This Branch

* Introduction of `TravelPlanner`
* Clean input handling for city and interests
* Integration with the LCEL itinerary chain
* Fully logged lifecycle (initialisation → input → generation → output)
* Robust exception handling
* Standalone test runner via `if __name__ == "__main__":`

## ⚙️ **How It Works**

1. **City and interest setters** collect and sanitize user input.
2. **Conversation history** is maintained using `HumanMessage` and `AIMessage`.
3. The planner invokes the **LCEL pipeline** from `itinerary_chain.py`.
4. Logging tracks every step of the process.
5. The output is stored and returned as Markdown-formatted text.
6. Running the file directly allows instant verification.

## 🧠 **Example Usage**

```python
from src.core.planner import TravelPlanner

planner = TravelPlanner()
planner.set_city("Barcelona")
planner.set_interests("architecture, beaches, nightlife")

itinerary = planner.create_itinerary()
print(itinerary)
```

## 🗝️ **Example Output (From Standalone Test Runner)**

```
2025-11-14 16:47:30,689 - INFO - Initialized TravelPlanner instance
2025-11-14 16:47:30,689 - INFO - City set successfully
2025-11-14 16:47:30,690 - INFO - Interests set successfully

🧪 Testing TravelPlanner standalone...

2025-11-14 16:47:30,690 - INFO - Generating itinerary for city='Barcelona', interests=['architecture', 'beaches', 'nightlife']
2025-11-14 16:47:31,668 - INFO - Itinerary generated successfully
### Barcelona 1-Day Itinerary
#### Morning
* 9:00 AM: Start at **La Sagrada Familia**, a famous architectural landmark by Antoni Gaudí
* 10:30 AM: Visit **Park Güell**, another iconic Gaudí site with stunning city views
* 12:00 PM: Walk along **Passeig de Gracia**, admiring modernist architecture and shopping

#### Afternoon
* 1:00 PM: Have lunch at a beachside restaurant in **Barceloneta**, trying local seafood
* 2:30 PM: Relax on **Barceloneta Beach**, enjoying the Mediterranean sun and sea
* 4:00 PM: Take a stroll along the **Beach Promenade**, exploring the waterfront

#### Evening
* 8:00 PM: Experience Barcelona's nightlife in the **Gothic Quarter**, exploring bars and clubs
* 10:00 PM: Enjoy live music and cocktails at a rooftop bar with city views, such as **Hotel Arts**
* 12:00 AM: End the night with a visit to **La Rambla**, a famous street filled with street performers and energy

✅ Done.
```

## 🧰 **Integration Notes**

| Component                       | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| `src/core/planner.py`           | Main controller for user inputs and itinerary generation. |
| `src/chains/itinerary_chain.py` | LCEL pipeline producing Markdown itineraries.             |
| `src/config/config.py`          | Loads environment variables (Groq API key).               |
| `src/utils/logger.py`           | Logs planner activity and chain execution.                |
| `src/utils/custom_exception.py` | Provides consistent, traceable error handling.            |

## ✅ **In summary**

This branch delivers a **fully functional planning controller**, completing the bridge between user inputs and the itinerary-generation chain.
It sets the stage for integrating the planner into the upcoming **Streamlit interface** for end-user interaction.
