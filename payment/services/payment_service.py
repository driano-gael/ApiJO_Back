from payment.infrastructure.payement_gateway import PaymentGatewayMock


class PaymentService:
    def create_payment_intent(self, amount, force_failed=False):
        """
        Simule la création d'un Payment
        Le paiement n'est pas encore confirmé (capturé).
        """
        if force_failed:
            return {
                "status": "failed",
                "transaction_id": None,
                "error": "Paiement refusé"
            }
        return {
            "status": "requires_confirmation",
            "transaction_id": "pi_mock_12345",
            "amount": amount
        }

    def confirm_payment(self, transaction_id):
        """
        Simule la confirmation du paiement.
        """
        return {
            "status": "succeeded",
            "transaction_id": transaction_id
        }

    def refund(self, transaction_id):
        """
        Simule un remboursement
        """
        return {
            "status": "refunded",
            "transaction_id": transaction_id
        }