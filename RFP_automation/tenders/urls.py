from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_tender),
    path('generate-response/<int:tender_id>/', views.generate_response),
]
