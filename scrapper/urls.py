from django.urls import path
from .views import *

urlpatterns = [
    path('', scrape, name='site'),
    path('delete/', clear, name='clear'),

]
