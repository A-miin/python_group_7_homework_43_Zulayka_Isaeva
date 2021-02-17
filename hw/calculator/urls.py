from django.urls import path
from .views import home, calculator



urlpatterns = [
    path('',home),
    path('calculator/', calculator)
]
