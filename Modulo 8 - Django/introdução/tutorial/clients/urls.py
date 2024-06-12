from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:client_id>/", views.detail, name="detail"),
    path("cadastro/", views.create, name="create"),
    path("<int:client_id>/update/", views.update, name="update"),
    path("<int:client_id>/delete/", views.delete, name="delete"),
]