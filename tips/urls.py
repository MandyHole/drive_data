from django.urls import path
from tips import views

urlpatterns = [
    path('tips/', views.TipList.as_view()),
]