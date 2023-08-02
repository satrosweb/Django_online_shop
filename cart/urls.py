from django.urls import path
from . import views


urlpatterns = [
    path("detail/", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:pk>", views.AddCartView.as_view(), name="cart_add"),
    path("remove/<int:pk>", views.RemoveCartView.as_view(), name="cart_remove")
]
