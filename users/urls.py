from django.urls import path, include
from users import views

urlpatterns = [path("home/", views.home, name="home")]
