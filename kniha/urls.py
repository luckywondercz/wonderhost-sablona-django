from django.urls import path

from . import views

urlpatterns = [path("", views.uvod, name="uvod")]
