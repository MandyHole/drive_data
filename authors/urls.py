from django.urls import path, include
from authors import views

urlpatterns = [
    path('authors/', views.TipAuthorList.as_view()),
    path('authors/<int:pk>/', views.TipAuthorDetail.as_view()),
]
