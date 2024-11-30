from django.urls import path
from .views import CartListView, AddToCartView, OrderCreateView, OrderStatusView, PaymentView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('orders/', OrderCreateView.as_view(), name='create-order'),
    path('orders/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
    path('payment/<int:order_id>/', PaymentView.as_view(), name='payment'),
]
