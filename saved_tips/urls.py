from django.urls import path
from saved_tips import views

urlpatterns = [
    path('saved_tips/', views.SavedTipList.as_view()),
    path('saved_tips/<int:pk>', views.SavedTipDetail.as_view())
]
