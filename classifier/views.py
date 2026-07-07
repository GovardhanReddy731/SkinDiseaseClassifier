import os
import json
import torch
import torch.nn as nn
from PIL import Image
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from torchvision.models import efficientnet_b4
import torchvision.transforms as transforms

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load model
num_classes = 9
model = efficientnet_b4(weights=None)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
model_path = os.path.join(settings.BASE_DIR, 'best_model_b4_optimized.pth')
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

# Class and disease mapping
class_names = [
    'Vascular lesion',
    'Tinea Ringworm Candidiasis',
    'Squamous cell carcinoma',
    'Melanoma',
    'Melanocytic nevus',
    'Dermatofibroma',
    'Benign keratosis',
    'Atopic Dermatitis',
    'Actinic keratosis'
]

# Precautions mapping
precaution_map = {
    "Vascular lesion": [
        "Apply pressure if bleeding",
        "Avoid trauma to the area",
        "Consult a dermatologist for laser options"
    ],
    "Tinea Ringworm Candidiasis": [
        "Keep skin dry and clean",
        "Use antifungal creams",
        "Avoid sharing towels/clothing"
    ],
    "Squamous cell carcinoma": [
        "Avoid sun exposure",
        "Use SPF 30+ sunscreen",
        "Schedule a biopsy and follow-up"
    ],
    "Melanoma": [
        "Immediate dermatological evaluation",
        "Avoid UV exposure",
        "Check for moles and irregular spots"
    ],
    "Melanocytic nevus": [
        "Regular monitoring for changes",
        "Avoid picking or irritation",
        "Apply sunscreen to prevent darkening"
    ],
    "Dermatofibroma": [
        "Avoid scratching or injury",
        "Use moisturizer",
        "Seek removal if it causes discomfort"
    ],
    "Benign keratosis": [
        "Moisturize skin regularly",
        "Avoid picking",
        "Monitor changes and consult doctor"
    ],
    "Atopic Dermatitis": [
        "Use prescribed emollients",
        "Avoid harsh soaps and irritants",
        "Manage stress to reduce flares"
    ],
    "Actinic keratosis": [
        "Regular skin exams",
        "Use SPF daily",
        "Consult doctor for cryotherapy or creams"
    ]
}

# Image transformation
transform = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# Home page
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ImageUploadForm()
    return render(request, 'classifier/home.html', {'form': form})

# Predict skin disease
@login_required(login_url='login')
def predict(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image']).convert('RGB')
            img_tensor = transform(image).unsqueeze(0).to(device)

            with torch.no_grad():
                outputs = model(img_tensor)
                _, pred = torch.max(outputs, 1)
                prediction = class_names[pred.item()]

            request.session['prediction'] = prediction
            return redirect('result')
    else:
        form = ImageUploadForm()
    return render(request, 'classifier/home.html', {'form': form})

# Display result and precautions
@login_required(login_url='login')
def result(request):
    prediction = request.session.get('prediction')
    if not prediction:
        return redirect('home')

    precautions = precaution_map.get(prediction, [])
    google_link = f"https://www.google.com/search?q={prediction.replace(' ', '+')}+treatment"

    # Example chart data (can be made dynamic)
    chart_data = {
        "labels": ["Mild", "Moderate", "Severe"],
        "values": [30, 45, 25]
    }
    chart_data_serialized = {
        "labels": json.dumps(chart_data["labels"]),
        "values": json.dumps(chart_data["values"])
    }

    context = {
        "prediction": prediction,
        "precautions": precautions,
        "google_link": google_link,
        "chart_data": chart_data_serialized,
    }

    return render(request, 'classifier/result.html', context)

# Unified login view
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    login_form = AuthenticationForm()
    signup_form = UserCreationForm()

    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'classifier/auth.html', {
        'form': login_form,
        'signup_form': signup_form,
        'tab': 'login'
    })

# Signup view
def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    signup_form = UserCreationForm(request.POST or None)
    login_form = AuthenticationForm()

    if request.method == "POST":
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            messages.success(request, "Signup successful!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'classifier/auth.html', {
        'form': login_form,
        'signup_form': signup_form,
        'tab': 'signup'
    })

# Logout view
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')
