from django.urls import path
from .views import farming_recommendation_view, index

urlpatterns = [
    path('', index, name="index"),
    path('farming-form', farming_recommendation_view, name='farming_form'),
]
