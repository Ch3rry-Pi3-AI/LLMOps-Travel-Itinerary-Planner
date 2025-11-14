# 🔄 **Chains Module — LLMOps Travel Itinerary Planner**

The `chains/` folder contains the **LLM workflow components** used to generate structured travel itineraries.
This is where prompt templates, LLM configurations, and runnable pipelines are defined using **LangChain Expression Language (LCEL)**.

These chains represent the **intelligent reasoning layer** of the system and are designed to be modular, testable, and easily extendable.

## 📁 Folder Overview

```text
src/chains/
└── itinerary_chain.py    # LCEL pipeline for generating Markdown-formatted day-trip itineraries
```

## 🧭 `itinerary_chain.py` — Itinerary Generation Workflow

### Purpose

This module defines the complete runnable pipeline responsible for generating travel itineraries.
It combines:

* A **structured LangChain chat prompt**
* The **Groq Llama-3.3 model** for reasoning and text synthesis
* A **StrOutputParser** to ensure clean, Markdown-ready output

It is the first component of the system that produces useful, user-facing content.

### Key Features

* LCEL pipeline:
  **Prompt → Model → StrOutputParser**
* Markdown-directed output for clean rendering in front-end applications
* Secure API key usage via the `src/config/config.py` module
* Can be imported directly by any component requiring itinerary generation
* Includes a **standalone test runner** for quick local verification
  (`python src/chains/itinerary_chain.py`)

### Example Usage

```python
from src.chains.itinerary_chain import generate_itinerary

plan = generate_itinerary("Lisbon", ["history", "coffee", "viewpoints"])
print(plan)
```

### Output Format

The chain produces clear, consistent Markdown with headings such as:

```
### City 1-Day Itinerary
#### Morning
* ...
#### Afternoon
* ...
#### Evening
* ...
```

Ideal for rendering directly in:

* Streamlit
* Web apps
* Chatbot interfaces
* PDFs or formatted reports

## 🔍 Current Status

This folder currently contains the **first complete LLM workflow** of the project.
Future chains (multi-day planning, budget optimisation, activity filtering, etc.) can be added here following the same structure.
