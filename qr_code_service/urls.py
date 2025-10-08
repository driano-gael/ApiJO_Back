from django.urls import path

from qr_code_service.views import QRCodeCreateByTicket

urlpatterns = [
    path('create_by_ticket/', QRCodeCreateByTicket.as_view(), name='create_by_ticket'),
]