from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_view, name="list"),
    # path("api/products/", views.create_view, name="create"),
]
