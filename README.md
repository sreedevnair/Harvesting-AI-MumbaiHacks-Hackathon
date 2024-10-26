# Harvesting AI 🌾

## Overview
**Harvesting AI** is an AI-powered application designed to assist farmers with personalized, data-driven farming recommendations, enabling more effective and sustainable crop growth across diverse environmental conditions. Using AI, weather data, and agricultural insights, this tool aims to support farmers in maximizing crop yield while promoting environmentally friendly practices.

## Project Purpose
Agriculture is a key sector in the global efforts to address climate change, hunger, and food security. **Harvesting AI** tackles these challenges by offering actionable insights to farmers, helping them make informed decisions that foster both agricultural success and climate resilience. This project aligns with the social good track by contributing to sustainable agriculture, promoting food security, and advancing environmental stewardship.

## Key Features
- **Crop-Specific Guidance**: Tailored recommendations based on crop type.
- **Location-Based Weather Integration**: Fetches current weather data using the OpenWeatherMap API.
- **AI-Driven Suggestions**: Employs the powerful Llama 3.2-1B language model to generate insightful and relevant farming tips.
- **User-Friendly Interface**: Accessible web interface designed for ease of use.

## How It Works
1. **User Input**: The user provides information about the crop type, soil type, and location.
2. **Weather Data Retrieval**: Using the OpenWeatherMap API, the app gathers real-time weather data for the specified location.
3. **AI-Generated Advice**: The Llama 3.2 model processes the crop, soil, and weather data to deliver tailored farming recommendations.
4. **Output Display**: Recommendations are displayed in a clear, easy-to-understand format.

## Project Structure
The project is built with Django as the backend framework and leverages Hugging Face’s transformers library to integrate and interact with the Llama 3.2-1B model locally.

### Key Components
- **Backend**: Django application to handle data flow and form submissions.
- **Model**: Llama 3.2-1B, a language model from Hugging Face, used for generating recommendations.
- **Weather API**: OpenWeatherMap API for real-time weather conditions.
- **Frontend**: Simple HTML/CSS forms and results page for input and output display.

## Tech Stack
- **Python**: Programming language for logic and data processing.
- **Django**: Web framework for backend handling and routing.
- **Transformers (Hugging Face)**: NLP library to load and interact with the Llama 3.2-1B model.
- **OpenWeatherMap API**: Service for real-time weather data.
- **HTML/CSS**: Frontend interface for user input and displaying results.

## Model Usage and Local Setup
Due to the large size of the Llama 3.2-1B model, we loaded it locally but couldn't push it to GitHub. To work around this, we set up a dedicated directory in the local environment to hold the model files:

1. **Model Download and Storage**: Upon the first run, the model and tokenizer are downloaded via Hugging Face's `AutoModelForCausalLM` and `AutoTokenizer` using an authentication token.
2. **Local Directory**: The model files are saved in a directory (`./llama3_model`) within the project structure.
3. **Local Loading**: If the model directory exists, the application loads it directly from the local environment, skipping the re-download.

## Project Snapshots

### Home Page
![Home Page](https://github.com/sreedevnair/Harvesting-AI-MumbaiHacks-Hackathon/blob/main/Output-Images/Homepage.png?raw=true)

<br>

### Farming Recommendation Page
![Farming Recommendation Page](https://github.com/sreedevnair/Harvesting-AI-MumbaiHacks-Hackathon/blob/main/Output-Images/Farming-Recommendation-Page.png?raw=true)

<br>

#### Farming Recommendation Page With Input
![Farming Recommendation Page With Input](https://github.com/sreedevnair/Harvesting-AI-MumbaiHacks-Hackathon/blob/main/Output-Images/Farming-Recommendation-Page.png?raw=true)

<br>

### Farming Recommendation Output Page
![Farming Recommendation Page](https://github.com/sreedevnair/Harvesting-AI-MumbaiHacks-Hackathon/blob/main/Output-Images/Farming-Recommendation-Output.png?raw=true)



