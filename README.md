# 🎨 **Streamlit Application — LLMOps Travel Itinerary Planner**

This branch introduces the **Streamlit front-end** for the LLMOps Travel Itinerary Planner.
The new `app.py` file provides an interactive web interface that:

* Collects the user’s **city** and **travel interests**
* Uses the `TravelPlanner` core logic and the `itinerary_chain`
* Displays a fully formatted, LLM-generated day-trip itinerary

This is the first stage where the project becomes a **clickable, user-facing travel planner** rather than just a backend pipeline.

<p align="center">
  <img src="img/streamlit/streamlit_app.gif" alt="Streamlit Travel Itinerary Planner Demo" width="100%">
</p>

## 🗂️ **Project Structure (Updated)**

```text
LLMOPS-TRAVEL-ITINERARY-PLANNER/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── img/
│   └── streamlit/
│       └── streamlit_app.gif
├── llmops_travel_itinerary_planner.egg-info/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
├── main.py
├── app.py                           # 🌐 Streamlit UI for interactive itinerary planning
├── src/
│   ├── chains/
│   │   └── itinerary_chain.py
│   ├── core/
│   │   └── planner.py
│   ├── config/
│   │   ├── config.py
│   │   └── README.md
│   └── utils/
│       ├── custom_exception.py
│       ├── logger.py
│       └── README.md
└── README.md
```

> 💡 Only `app.py` is annotated here, as it is the new component introduced in this branch.

## 🧩 **Overview**

The Streamlit application wraps the existing backend logic into a simple, intuitive interface:

* Users select a **city** (text box)
* Users choose **interests** using **checkboxes** (e.g., history, beaches, nightlife)
* The app calls `TravelPlanner`:

  * `set_city(...)`
  * `set_interests(...)`
  * `create_itinerary()`
* The response is rendered as a **Markdown itinerary** inside a styled container

This connects the LCEL itinerary chain to a real user experience for the first time.

## ⚙️ **How the App Works**

1. **Page Setup**
   `st.set_page_config(...)` configures page title and layout, and a centered HTML `<h1>` renders the header banner.

2. **Environment Loading**
   `load_dotenv()` loads API keys and configuration (e.g. Groq key) from `.env`.

3. **Interest Selection**
   A fixed list `INTEREST_OPTIONS` defines common travel interests.
   These are presented as checkboxes in a 3-column layout.

4. **Form Submission**
   The Streamlit `form` collects:

   * `city` (text input)
   * `selected_interests` (checkboxes)

   On submit:

   ```python
   planner = TravelPlanner()
   planner.set_city(city)
   planner.set_interests(", ".join(selected_interests))
   itinerary = planner.create_itinerary()
   ```

5. **Output Rendering**
   The generated itinerary is displayed under **“📄 Your Itinerary”** inside a dark, rounded container using `st.markdown(..., unsafe_allow_html=True)`.

6. **Validation**
   If the user submits without a city or interests, the app shows a warning message instead of calling the planner.

## 🚀 **How to Run the Streamlit App**

From the project root:

```bash
# Activate your virtual environment first, then:
streamlit run app.py
```

This will open the app in your browser (typically at `http://localhost:8501`).

Steps:

1. Enter a city (e.g. `London`, `Barcelona`, `Tokyo`).
2. Tick several interests (e.g. **History**, **Food**, **Nightlife**).
3. Click **“✨ Generate Itinerary”**.
4. View the generated **1-day Markdown itinerary** in the result panel.

## 🧠 **Example Interaction**

Typical user flow:

1. **City:** `London`
2. **Interests selected:** `History`, `Museums`, `Food`
3. **Output:** A structured itinerary such as:

```markdown
### London 1-Day Itinerary

#### Morning
* 9:00 AM: Visit the British Museum to explore world history collections.
* 11:00 AM: Walk to the National Gallery to see classic European paintings.

#### Afternoon
* 1:00 PM: Lunch at Borough Market to try local and international foods.
* 3:00 PM: Explore the Tate Modern on the South Bank.

#### Evening
* 6:30 PM: Enjoy dinner at a traditional pub near Covent Garden.
* 8:00 PM: Stroll along the Thames or catch a West End show.
```

(Exact wording will vary, but the structure remains consistent.)

## 🧰 **Integration Notes**

| Component                       | Role                                                                 |
| ------------------------------- | -------------------------------------------------------------------- |
| `app.py`                        | Streamlit front-end for collecting inputs and displaying itineraries |
| `src/core/planner.py`           | Orchestrates city + interests handling and calls the itinerary chain |
| `src/chains/itinerary_chain.py` | LCEL pipeline that generates the Markdown itinerary                  |
| `src/config/config.py`          | Loads environment variables (e.g. Groq API key from `.env`)          |
| `src/utils/logger.py`           | Logs planner and chain events for debugging                          |
| `src/utils/custom_exception.py` | Provides structured error handling across components                 |

## ✅ **In summary**

This branch elevates the LLMOps Travel Itinerary Planner from a backend workflow to a **fully interactive web application**.
The new `app.py` Streamlit interface connects the planner and itinerary chain to real users, providing a clean, guided experience for generating AI-powered day-trip itineraries.
