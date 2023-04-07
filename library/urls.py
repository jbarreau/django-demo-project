from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'library'
urlpatterns = [
    path('/comics', csrf_exempt(views.ComicsView.as_view()), name='comic'),
    path('/comics/<int:pk>', csrf_exempt(views.ComicsDetailView.as_view()), name='comic'),
]