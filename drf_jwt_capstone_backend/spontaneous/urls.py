from django.urls import path
from spontaneous import views

urlpatterns = [
    path('', views.ExplorerList.as_view())
]