from django.urls import path

from . import views

app_name = 'applications'
urlpatterns = [
    path('', views.Application.as_view(), name='all'),
    path('new', views.NewApplication.as_view(), name='new')
]
