from django.urls import path
from payment.views import MockStripePaymentView


urlpatterns = [
    path('check/', MockStripePaymentView.as_view(), name='checkout-payment'),
]