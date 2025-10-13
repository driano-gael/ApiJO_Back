from django.urls import path

from qr_code_service.views import QRCodeCreateByTicket, TicketByKeyView

urlpatterns = [
    path('create_by_ticket/', QRCodeCreateByTicket.as_view(), name='create_by_ticket'),
    path('qrcode/<str:key>/', TicketByKeyView.as_view(), name='ticket-by-key'),

]