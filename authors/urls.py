from django.urls import path, include
from authors import views

urlpatterns = [
    path('authors/', views.TipAuthorList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('authors/<int:pk>/', views.TipAuthorDetail.as_view()),
]
