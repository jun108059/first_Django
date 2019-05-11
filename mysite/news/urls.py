from django.urls import path
from . import views

urlpatterns = [
    # path('news/', include('news.urls')),
    path('', views.index),
]
