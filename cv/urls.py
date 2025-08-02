from django.urls import path
from .views import cv
urlpatterns = [
    path('mycv/', cv, name='cv'),]