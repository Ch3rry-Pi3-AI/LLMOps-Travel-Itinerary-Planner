# 🧭 **Itinerary Generation Chain — LLMOps Travel Itinerary Planner**

This branch introduces the **first fully functional workflow component** of the **LLMOps Travel Itinerary Planner** — the **Itinerary Generation Chain**, upgraded using **LangChain Expression Language (LCEL)** and a **string output parser** for clean, Markdown-ready itineraries.

The chain combines:

* A structured **LangChain prompt template**
* A **Groq Llama-3.3 model**
* A **StrOutputParser()** for clean, display-ready output
* A full **runnable pipeline** (`prompt | llm | parser`)
* A built-in **standalone test runner** via `if __name__ == "__main__":`

This stage marks the moment when the system can generate polished, human-readable itineraries directly from user preferences.

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
│   │   └── itinerary_chain.py    # 🧭 LCEL pipeline: Prompt → Model → Output Parser (+ standalone runner)
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

> 💡 Only the newly added/updated file (`itinerary_chain.py`) is annotated.

## 🧩 **Overview**

The **Itinerary Generation Chain** transforms basic user input into a structured, Markdown-formatted day-trip itinerary.
Enhancements in this branch include:

* **LCEL runnable pipeline** (`prompt | llm | StrOutputParser()`)
* A **Markdown-directive system prompt** ensuring consistent formatting
* A **standalone test runner** for quick execution

This is the first stage where the project produces **intelligent travel recommendations**.

## ⚙️ **How It Works (Updated)**

1. **API Key Management**
   The Groq API key is loaded securely via `src/config/config.py`.

2. **Prompt Template**
   A `ChatPromptTemplate` provides the system and human messages guiding the model.

3. **Runnable Pipeline**
   The itinerary chain is composed using LCEL:
   **Prompt → Groq Model → StrOutputParser**

4. **Output Handling**
   `StrOutputParser()` ensures that the final output is plain, clean Markdown.

5. **Public Interface**
   `generate_itinerary(city, interests)` prepares the inputs and invokes the runnable.

6. **Standalone Runner**
   Running the file directly triggers a built-in test to confirm everything works.

## 🧠 **Example Usage (LCEL Version)**

```python
from src.chains.itinerary_chain import generate_itinerary

plan = generate_itinerary(
    city="Lisbon",
    interests=["history", "coffee", "viewpoints"]
)

print(plan)
```

## 🗝️ **Example Output (From Standalone Test Runner)**

```
🧪 Testing itinerary generation...

### Lisbon 1-Day Itinerary
#### Morning
* 9:00 AM: Start at the **Miradouro de São Pedro de Alcântara** for a panoramic view of the city
* 10:00 AM: Visit the **National Pantheon** to explore Lisbon's historical heritage
* 11:30 AM: Stop by a traditional café, **Café Nicola**, for a coffee break

#### Afternoon
* 1:00 PM: Have lunch at a local restaurant in the **Baixa neighborhood**
* 2:30 PM: Explore the **Castle of São Jorge** for a glimpse into Lisbon's medieval past
* 4:00 PM: Enjoy the views from **Miradouro das Portas do Sol**

#### Evening
* 6:00 PM: Take a stroll through the **Alfama neighborhood** and admire its Fado music culture
* 8:00 PM: End the day with dinner and a view at a rooftop restaurant, such as **Park Bar**

✅ Done.
```

## 🧰 **Integration Notes**

| Component                       | Description                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| `src/chains/itinerary_chain.py` | LCEL runnable (Prompt → Model → Parser) with standalone runner. |
| `src/config/config.py`          | API key and environment variable loading.                       |
| `src/utils/logger.py`           | Logs chain execution and errors.                                |
| `src/utils/custom_exception.py` | Wraps errors in a consistent, traceable format.                 |

## ✅ **In summary**

This branch delivers a **modern, modular, LCEL-driven itinerary generation system**, producing clean Markdown output with a fully testable standalone runner.
It forms the foundation for integrating itinerary logic into planners, agents, and Streamlit interfaces in future stages.
