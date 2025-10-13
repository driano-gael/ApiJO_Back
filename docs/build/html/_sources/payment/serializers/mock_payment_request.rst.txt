Sérialiseur MockPaymentRequest
==============================

.. autoclass:: payment.serializers.MockPaymentRequestSerializer
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Ce sérialiseur gère la validation des données de requête pour les paiements mock.

Champs du sérialiseur
---------------------

**amount** (DecimalField)
   Montant total du paiement avec précision décimale (10 digits, 2 décimales).

**force_failed** (BooleanField, optionnel)
   Paramètre pour forcer l'échec du paiement lors des tests. Par défaut : False.

**items** (PanierItemSerializer, liste, optionnel)
   Liste des éléments du panier contenant offre, événement et quantité.

Validation
----------

Le sérialiseur valide automatiquement :

- Format décimal correct pour le montant
- Type booléen pour force_failed
- Structure valide des items du panier via PanierItemSerializer

Exemple de données valides
--------------------------

.. code-block:: json

   {
     "amount": "150.00",
     "force_failed": false,
     "items": [
       {
         "offre": 1,
         "evenement": 1,
         "quantity": 2
       }
     ]
   }
