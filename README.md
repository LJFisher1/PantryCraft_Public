# PantryCraft

## Introduction
**PantryCraft** is a desktop application designed to help users organize and manage the ingredients in their pantry. By tracking available ingredients, it suggests recipes to reduce food waste and inspire new meal ideas.

## Problem Statement
Many people struggle with deciding what to cook based on the ingredients they have. **PantryCraft** solves this by offering an easy way to input pantry items and receive recipe suggestions based on what’s available. This helps reduce food waste, save time, and discover new recipes.

## Features
- **Ingredient Tracking**: Easily add and manage pantry items.
- **Recipe Suggestions**: Get recipes based on the ingredients you currently have.
- **Pantry Overview**: View all pantry items at a glance and keep track of expiration dates.
- **Recipe Database**: A growing collection of recipes that utilize common pantry items.

## Technologies
**PantryCraft** is built using the following technologies:
- **Language**: Python
- **GUI Framework**: Tkinter (for the user interface)
- **Database**: A simple `.txt` file that stores pantry items and updates automatically at regular intervals.
- **API**: Spoonacular API for recipe suggestions based on available ingredients.

## Installation

### Prerequisites
Before you can run **PantryCraft**, you'll need the following:
- Python 3.x
- Tkinter (usually pre-installed with Python, or can be installed via `pip install tk`)
- **Spoonacular API Key**: Sign up at [Spoonacular](https://spoonacular.com/food-api) to obtain an API key.

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/LJFisher1/pantrycraft_public.git
    ```
2. **Install Dependencies**:
    If you don’t have Tkinter, install it with:
    ```bash
    pip install tk
    ```
    Install the `requests` library for API interaction:
    ```bash
    pip install requests
    ```
3. **Set Up the Spoonacular API Key**:
    - Sign up for an API key at [Spoonacular](https://spoonacular.com/food-api).
    - Save your API key in a configuration file or as an environment variable:
    ```bash
    SPOONACULAR_API_KEY=your-api-key-here
    ```
4. **Run the Project**:
    - Navigate to the project directory and run:
    ```bash
    python pantrycraft.py
    ```

> **Note**: The first time you run the program, a `.txt` file will be created to store your pantry data. This file will update automatically as you add or remove items.

## Development Setup

### Required Software
- **Python 3.x**
- **Tkinter** (usually pre-installed with Python)
- **requests** (for API interaction)

## License
This project is licensed under the MIT License.

## Contributors
- **Joseph Fisher**

## Project Status
**PantryCraft** is in **Beta**. The core features for ingredient management and recipe suggestions are complete, but development is currently on hold.
