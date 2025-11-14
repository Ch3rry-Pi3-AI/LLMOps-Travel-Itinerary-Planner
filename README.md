# 🧭 **Itinerary Generation Chain — LLMOps Travel Itinerary Planner**

This branch introduces the **first functional workflow component** of the **LLMOps Travel Itinerary Planner** — the **Itinerary Generation Chain**.
It connects the **Groq large language model** to a structured **LangChain prompt template**, allowing the application to dynamically generate personalised, bulleted day-trip itineraries based on a user’s **city** and **interests**.

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
│   │   └── itinerary_chain.py    # 🧭 Groq + LangChain workflow for generating day-trip itineraries
│   ├── core/
│   ├── config/
│   │   ├── config.py
│   │   └── README.md
│   └── utils/
│       ├── custom_exception.py
│       ├── logger.py
│       └── README.md
└── README.md
```

> 💡 **Note:** Only the new file `src/chains/itinerary_chain.py` is annotated in this structure, as it represents the newly added component for this development stage.

## 🧩 **Overview**

The **Itinerary Generation Chain** is responsible for turning simple user input into a structured day-trip plan.
It combines:

* The **Groq model** (`llama-3.3-70b-versatile`) for reasoning and text generation.
* A **LangChain prompt template** that ensures consistent and context-aware itinerary outputs.
* A **clean, single-function interface** (`generate_itinerary`) that can later integrate with APIs or front-end layers.

This marks the first point at which the system begins producing **intelligent travel recommendations**.

## ⚙️ **How It Works**

1. **API Key Management**
   The Groq API key is securely loaded from `.env` using the existing `src/config/config.py` module.

2. **Prompt Creation**
   A `ChatPromptTemplate` defines a clear system and human instruction structure, guiding the model to create bulleted, easy-to-read itineraries.

3. **Model Invocation**
   The chain initialises a `ChatGroq` model and uses the `invoke()` method to generate responses for any given city and list of interests.

4. **Result Return**
   The `generate_itinerary()` function returns the formatted itinerary text ready for display or downstream use.

### 🧠 Example Usage

```python
from src.chains.itinerary_chain import generate_itinerary

plan = generate_itinerary(
    city="Lisbon",
    interests=["history", "coffee", "viewpoints"]
)

print(plan)
```

### 🗝️ Example Output

```
**Day Trip in Lisbon**
- **Morning:** Explore the Alfama district for historic views and coffee spots.
- **Afternoon:** Visit Castelo de S. Jorge for panoramic views of the city.
- **Evening:** Sunset at Miradouro da Senhora do Monte followed by dinner in Bairro Alto.
```

## 🧰 **Integration Notes**

| Component                       | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| `src/chains/itinerary_chain.py` | Defines the main LangChain–Groq pipeline for itinerary generation. |
| `src/config/config.py`          | Handles secure environment variable loading (Groq API key).        |
| `src/utils/logger.py`           | Logs runtime activity and debugging output.                        |
| `src/utils/custom_exception.py` | Handles exceptions and error tracing across the workflow.          |

✅ **In summary:**
This branch introduces the **first intelligent workflow** of the LLMOps Travel Itinerary Planner — a modular, reusable chain that combines Groq inference with LangChain templates to produce personalised, structured travel itineraries ready for future integration into the user-facing interface.
