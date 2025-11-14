# 🧭 **Planner Logic — LLMOps Travel Itinerary Planner**

This branch introduces the **core planning controller** of the LLMOps Travel Itinerary Planner — the **TravelPlanner**, which orchestrates user inputs, maintains conversation history, and invokes the itinerary generation chain through a clean, high-level interface.

This component represents the first point where the planner begins to behave like a real application:
capturing city + interest inputs and returning full Markdown itineraries using the underlying LLM workflow.

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

> 💡 Only `src/core/planner.py` is annotated, as it is the **new component introduced in this stage**.

## 🧩 **Overview**

The **TravelPlanner** class bridges user input and the itinerary-generation chain.
It accepts a **city** and a set of **interests**, records them as structured messages, invokes the LCEL itinerary workflow, and returns a formatted Markdown itinerary.

This stage completes the core backend logic needed for an interactive user-facing application.

### Key Improvements Introduced in This Branch

* A clean planning controller (`TravelPlanner`)
* Integration with the LCEL itinerary chain
* Structured conversation state using `HumanMessage` and `AIMessage`
* Logging for each step (inputs, processing, output)
* Centralised exception handling
* A standalone test runner using `if __name__ == "__main__":`

## ⚙️ **How It Works**

1. **Set City**
   Cleans the input and stores it as a message.

2. **Set Interests**
   Parses a comma-separated string into a list of interests.

3. **Invoke Chain**
   Calls the LCEL pipeline (`itinerary_chain`) to generate Markdown output.

4. **Record AI Response**
   Stores the generated itinerary as an `AIMessage` for history and future context.

5. **Standalone Test Mode**
   You can run:

   ```
   python src/core/planner.py
   ```

   to confirm everything works independently.

## 🧠 **Example Usage**

```python
from src.core.planner import TravelPlanner

planner = TravelPlanner()
planner.set_city("Barcelona")
planner.set_interests("architecture, beaches, nightlife")

itinerary = planner.create_itinerary()
print(itinerary)
```

## 🗝️ **Example Standalone Output**

```
🧪 Testing TravelPlanner standalone...

### Barcelona 1-Day Itinerary
#### Morning
* Scenic viewpoints…
* Local café visit…

#### Afternoon
* Historic district walk…
* Cultural landmark stop…

#### Evening
* Beachfront stroll…
* Dinner with a view…

✅ Done.
```

## 🧰 **Integration Notes**

| Component                       | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| `src/core/planner.py`           | Main controller for user inputs and itinerary generation. |
| `src/chains/itinerary_chain.py` | LCEL pipeline producing Markdown itineraries.             |
| `src/config/config.py`          | Manages environment variables including Groq API key.     |
| `src/utils/logger.py`           | Logs planner activity and chain execution.                |
| `src/utils/custom_exception.py` | Wraps all exceptions for consistent debugging.            |

## ✅ **In summary**

This branch delivers a **fully functional planning controller**, completing the core logic needed to connect user inputs with LLM-powered itinerary generation.
It sets the stage for the upcoming **Streamlit interface**, which will act as the front-end for this planner.
