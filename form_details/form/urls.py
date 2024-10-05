from django.urls import path
from form.views import *
urlpatterns = [
    path('',submission,name='submission'),
]
