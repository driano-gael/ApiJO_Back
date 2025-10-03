from django.urls import path

from payment.views import MockPaymentView

urlpatterns = [
    path('check/', MockPaymentView.as_view(), name='checkout-payment'),
]