Service de Paiement
==================

.. autoclass:: payment.services.payment_service.PaymentService
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Service principal pour la gestion des transactions de paiement. Ce service
   coordonne les opérations de paiement et l'intégration avec les passerelles externes.

**Méthodes principales**

process_payment()
-----------------
   Traite une transaction de paiement complète incluant :

   - Validation des données de paiement
   - Communication avec la passerelle de paiement
   - Gestion des réponses et erreurs
   - Création des tickets en cas de succès

validate_payment_data()
-----------------------
   Valide les données de paiement avant traitement :

   - Vérification des informations de carte
   - Validation du montant et de la devise
   - Contrôle de cohérence des données

**Intégration**
   Ce service est utilisé par les vues de paiement pour centraliser
   la logique métier des transactions.
