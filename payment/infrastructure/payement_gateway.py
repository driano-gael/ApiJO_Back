import uuid
class StripeGatewayMock:
    """
    Simule un appel à un service de paiement
    """

    def create_payment_intent(self, _amount, _force_fail):
        if _force_fail:
            return {
                "id": "pi_" + str(uuid.uuid4()),
                "status": "failed",
                "error": {"message": "Simulation volontairement en echec"}
            }
        else:
            return {
                "id": "pi_" + str(uuid.uuid4()),
                "status": "succeeded",
                "charges": [{"id": "ch_" + str(uuid.uuid4()), "montant": _amount}]
            }
