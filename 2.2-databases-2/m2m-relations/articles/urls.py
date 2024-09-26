from django.urls import path
from .views import articles_list

urlpatterns = [
    path('news/', articles_list, name='news'),
]

