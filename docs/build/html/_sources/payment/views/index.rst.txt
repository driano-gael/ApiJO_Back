Vues Payment
=============

Le module payment contient les vues pour la gestion des transactions de paiement.

.. toctree::
   :maxdepth: 2
   :caption: Vues du module Payment:

   mock_payment

MockPaymentView
---------------

.. autoclass:: payment.views.MockPaymentView
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Vue API pour simuler les transactions de paiement. Cette vue permet de tester
   le processus de paiement sans utiliser de vraie passerelle de paiement.

**Permissions**
   - Utilisateur authentifié requis

**Endpoint**
   - **POST** ``/api/payments/check/`` - Simule une transaction de paiement

**Fonctionnalités**
   - Validation des données de paiement
   - Simulation de transaction avec passerelle fictive
   - Création automatique de tickets en cas de succès
   - Gestion des erreurs et des échecs de paiement
