Sérialiseur MockPaymentResponse
==============================

.. autoclass:: payment.serializers.MockPaymentResponseSerializer
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Ce sérialiseur structure la réponse des opérations de paiement mock.

Champs du sérialiseur
--------------------

**success** (BooleanField)
   Indique si l'opération de paiement a réussi ou échoué.

**gateway_response** (DictField)
   Contient la réponse brute de la passerelle de paiement simulée.

**tickets** (TicketSerializer, liste, optionnel)
   Liste des tickets créés suite au paiement réussi.

**errors** (ListField, optionnel)
   Liste des erreurs rencontrées pendant le processus de paiement.

Structure de la réponse
-----------------------

**En cas de succès** :

.. code-block:: json

   {
     "success": true,
     "gateway_response": {
       "status": "succeeded",
       "transaction_id": "pi_mock_12345"
     },
     "tickets": [
       {
         "id": 1,
         "key": "TKT_ABC123",
         "statut": "valide"
       }
     ],
     "errors": []
   }

**En cas d'échec** :

.. code-block:: json

   {
     "success": false,
     "gateway_response": {
       "status": "failed",
       "error": "Paiement refusé"
     },
     "tickets": [],
     "errors": [
       {
         "reason": "Places insuffisantes"
       }
     ]
   }
