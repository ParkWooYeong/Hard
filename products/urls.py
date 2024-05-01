from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_view.as_view(), name="list"),
    path("<int:pk>/", views.detail_view.as_view(), name="detail"),
]
