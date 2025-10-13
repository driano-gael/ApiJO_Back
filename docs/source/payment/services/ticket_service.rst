Service de Tickets
==================

.. autoclass:: payment.services.ticket_service.TicketService
   :members:
   :undoc-members:
   :show-inheritance:

**Description**
   Service responsable de la création et gestion des tickets après un paiement réussi.
   Ce service coordonne la génération des billets avec les informations d'événement et d'offre.

**Méthodes principales**

create_tickets()
----------------
   Crée les tickets après validation du paiement :

   - Génération des clés uniques pour chaque ticket
   - Association avec le client, l'événement et l'offre
   - Définition du statut initial du ticket
   - Sauvegarde en base de données

validate_ticket_creation()
--------------------------
   Valide les conditions de création de tickets :

   - Vérification de la disponibilité des places
   - Contrôle des limites par client
   - Validation de la cohérence offre/événement

generate_ticket_key()
---------------------
   Génère une clé unique pour chaque ticket :

   - Utilisation d'algorithmes de hachage sécurisés
   - Garantie d'unicité dans le système
   - Format compatible avec les QR codes

**Intégration**
   Ce service est appelé automatiquement par le PaymentService
   lors du succès d'une transaction pour créer les tickets correspondants.
