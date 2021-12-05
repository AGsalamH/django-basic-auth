from django.urls import path
from .views import (
    ProtectedTemplateView,
    RegisterView,
    MyLoginView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('', ProtectedTemplateView.as_view(), name='index'),
]
