from django.urls import path

from qr_code_service.views import QRCodeCreateByTicket

urlpatterns = [
    path('clientGet/', QRCodeCreateByTicket.as_view(), name='client-get-qr_code_service'),
]