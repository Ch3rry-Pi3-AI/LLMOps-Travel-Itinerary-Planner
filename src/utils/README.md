# 🌍 **LLMOps Travel Itinerary Planner — Core Utilities Overview**

This folder provides the **core utility modules** used throughout the **LLMOps Travel Itinerary Planner**.
It contains lightweight, reusable components for **error handling** and **logging**, ensuring that all project scripts and pipelines follow consistent debugging and traceability practices.

## 📁 Folder Overview

```text
utils/
├─ __init__.py          # Marks the directory as a package
├─ custom_exception.py  # Unified and detailed exception handling
└─ logger.py            # Centralised logging configuration
```

## ⚠️ `custom_exception.py` — Unified Error Handling

### Purpose

Defines a `CustomException` class that captures detailed debugging context whenever an error occurs — including the exact **file name**, **line number**, and **traceback**.

### Key Features

* Consistent formatting for all raised exceptions.
* Automatically detects the current exception via `sys.exc_info()` if not provided.
* Useful across any pipeline stage — such as **data ingestion**, **trip recommendation**, or **LLM reasoning** modules.

### Example Usage

```python
from utils.custom_exception import CustomException
import sys

try:
    raise ValueError("Invalid travel query input.")
except Exception as e:
    raise CustomException(e, sys)
```

## 🪵 `logger.py` — Centralised Logging Configuration

### Purpose

Provides a single, reusable logging setup for all components of the **LLMOps Travel Itinerary Planner**.
Logs are stored with timestamps and message severity, ensuring that all processes — from **API calls** to **trip generation** — are consistently traceable.

### Key Features

* Automatically creates a `logs/` directory with time-stamped log files.
* Includes logging levels (`INFO`, `WARNING`, `ERROR`, `CRITICAL`).
* Integrates seamlessly with the `CustomException` module for unified debugging.

### Example Usage

```python
from utils.logger import logging

logging.info("Starting itinerary generation pipeline...")
logging.warning("Destination details missing, using default preferences.")
logging.error("Failed to fetch flight data from API.")
```
