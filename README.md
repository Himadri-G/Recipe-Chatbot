# Recipe Chatbot Project Collection

This repository contains three implementations of a Recipe Chatbot using LangChain and Ollama:

## 1. Recipe Chatbot Basic (Model.ipynb)
A basic Jupyter notebook implementation demonstrating core functionality.

### Features
- Simple ingredient-to-recipe conversion
- Basic prompt template
- Concise recipe output format
- Uses LangChain with Ollama

### Requirements
```
langchain-ollama
langchain-core
jupyter
```

### Usage
1. Open `Model.ipynb` in Jupyter Notebook
2. Run all cells
3. Input ingredients to get recipe suggestions

---

## 2. Recipe Chatbot (Recipebot.py)
A Streamlit-based web application with chat interface.

### Features
- Chat-based interface
- Detailed recipe format with emojis
- Chat history management
- Enhanced prompt engineering

### Requirements
```
streamlit
langchain-ollama
langchain-core
```

### Usage
```bash
streamlit run Recipebot.py
```

---

## 3. Recipe Chatbot 2.0 (Recipebot2.0.py)
An enhanced version with additional features and UI improvements.

### Features
- Model selection dropdown
- Temperature control
- Chat history with clear function
- Sidebar configuration
- API key input option
- Creator attribution

### Requirements
```
streamlit
langchain-ollama
langchain-core
```

### Usage
```bash
streamlit run Recipebot2.0.py
```

### Configuration
- Select AI model from dropdown
- Adjust temperature (0.0 - 1.0)
- Clear chat history as needed

## Common Setup for All Versions

1. Create virtual environment:
```bash
python -m venv env
.\env\Scripts\activate
```

2. Install dependencies:
```bash
pip install langchain-ollama langchain-core streamlit
```

3. Install Ollama and pull required models:
```bash
ollama pull llama2
```

## System Requirements
- Windows/Linux/MacOS
- Python 3.8+
- 8GB+ RAM recommended
- Ollama installed and running

## Note
Make sure Ollama is running before starting any of the applications.

## Creator
Developed by Himadri Goswami
