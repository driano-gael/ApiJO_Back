Vue MockPayment
===============

.. autoclass:: payment.views.MockPaymentView
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

La vue MockPaymentView simule un système de paiement complet pour les tests et le développement.

Fonctionnalités principales
---------------------------

**Simulation de paiement**
   Crée une intention de paiement avec possibilité de forcer un échec pour les tests.

**Gestion transactionnelle**
   Utilise les transactions atomiques Django pour garantir la cohérence.

**Création de tickets**
   Génère automatiquement les tickets après confirmation du paiement.

**Gestion des erreurs**
   Système de remboursement automatique en cas d'erreur de création de tickets.

Endpoint
--------

**URL** : ``POST /api/payments/check/``

**Permissions** : ``IsAuthenticated``

**Paramètres de requête** :

- ``amount`` (decimal) : Montant total du paiement
- ``force_failed`` (boolean, optionnel) : Force l'échec du paiement pour les tests
- ``items`` (array, optionnel) : Liste des items du panier

**Réponse** :

- ``success`` (boolean) : Succès ou échec de l'opération
- ``gateway_response`` (object) : Réponse de la passerelle de paiement
- ``tickets`` (array) : Liste des tickets créés
- ``errors`` (array) : Liste des erreurs éventuelles

Exemple d'utilisation
---------------------

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

Réponse en cas de succès :

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
         "statut": "valide",
         "evenement": {...},
         "offre": {...}
       }
     ],
     "errors": []
   }
