from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.ProductView.as_view(), name="product-op"),
    path("<int:id>", views.ProductView.as_view(), name="product-op-with-id"),
]