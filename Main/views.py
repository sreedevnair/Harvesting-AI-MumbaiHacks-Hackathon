from django.shortcuts import render
from .forms import FarmingForm
from transformers import AutoModelForCausalLM, AutoTokenizer
from django.conf import settings
import torch
import requests
import os
import re

# Load model and tokenizer
model_name = "meta-llama/Llama-3.2-1B"
local_model_path = os.path.join(settings.MODELS_DIR, "llama3_model")

os.environ["TOKENIZERS_PARALLELISM"] = "false"

if not os.path.exists(local_model_path):
    print("Downloading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=True)
    tokenizer.save_pretrained(local_model_path)
    model.save_pretrained(local_model_path)
else:
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    model = AutoModelForCausalLM.from_pretrained(local_model_path)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
tokenizer.pad_token_id = tokenizer.eos_token_id

# Functions to process input
def generate_llama_response(query):
    inputs = tokenizer(query, return_tensors="pt", padding=True).to(device)
    outputs = model.generate(inputs["input_ids"], attention_mask=inputs["attention_mask"],
        max_length=200, eos_token_id=tokenizer.eos_token_id, num_beams=1, temperature=1.5, 
        top_k=20, top_p=0.9, no_repeat_ngram_size=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def get_weather_data(location):
    api_key = "fd0cd4f2ce26325341d400902d65864b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "temperature": data["main"]["temp"] - 273.15,
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return {"error": "Could not retrieve weather data"}

def trim_incomplete_sentence(text):
    sentences = re.findall(r"([^.?!]*[.?!])", text)
    final_response = ''.join(sentences)
    return final_response

def generate_recommendations(crop, soil_type, location):
    weather_data = get_weather_data(location)
    if "error" in weather_data:
        return {"error": weather_data["error"]}
    
    query = f"How to grow {crop} in {soil_type} in {weather_data['weather_description']} conditions."
    llama_response = generate_llama_response(query)
    trimmed_response = trim_incomplete_sentence(llama_response)

    return {
        "crop": crop,
        "soil_type": soil_type,
        "location": location,
        "weather_data": weather_data,
        "llama_advice": trimmed_response
    }

def index(request):
    return render(request, 'index.html')

# View to handle form submission
def farming_recommendation_view(request):
    if request.method == "POST":
        form = FarmingForm(request.POST)
        if form.is_valid():
            crop = form.cleaned_data["crop"]
            soil_type = form.cleaned_data["soil_type"]
            location = form.cleaned_data["location"]
            
            recommendations = generate_recommendations(crop, soil_type, location)
            print(recommendations)
            return render(request, "result.html", {"recommendations": recommendations})
    else:
        form = FarmingForm()
    return render(request, "forms.html", {"form": form})
