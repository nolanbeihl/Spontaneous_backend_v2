from django.urls import path
from spontaneous import views

urlpatterns = [
    path('all/', views.get_all),
    path('', views.explorers),
]