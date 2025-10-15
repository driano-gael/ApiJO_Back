Passerelle de Paiement
======================

.. autoclass:: payment.infrastructure.payement_gateway.PaymentGatewayMock
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Classe de simulation pour les passerelles de paiement externes.
   Cette classe mock permet de tester les transactions de paiement sans
   utiliser de vraie passerelle de paiement.

**Méthodes principales**

create_payment_intent()
-----------------------
   Simule la création d'une intention de paiement :

   - Génère un ID unique pour la transaction
   - Simule le succès ou l'échec selon le paramètre force_fail
   - Retourne une réponse formatée comme une vraie passerelle

**Paramètres**
   - **_amount** : Montant de la transaction
   - **_force_fail** : Booléen pour forcer l'échec du paiement

**Réponses simulées**

**Succès** :
   - status: "succeeded"
   - id: UUID généré automatiquement
   - charges: Liste avec détails de la transaction

**Échec** :
   - status: "failed"
   - error: Message d'erreur explicatif

**Utilisation**
   Cette classe mock est utilisée dans l'environnement de développement
   et de test pour simuler les comportements des vraies passerelles
   de paiement sans frais réels.
