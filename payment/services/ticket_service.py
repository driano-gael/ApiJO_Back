from api.models import Ticket


class TicketService:
    @staticmethod
    def create_tickets_from_items(_client_profile, _items):
        """
        Crée des tickets à partir des items du panier.
        Retourne une liste de tickets créés et une liste d'erreurs.
        """
        tickets_created = []
        tickets_uncreated = []

        for item_data in _items:
            offre = item_data['offre']
            evenement = item_data['evenement']
            quantity = item_data['quantity']

            for _ in range(quantity):
                if evenement.nb_place_restante >= offre.nb_personne:
                    evenement.nb_place_restante -= offre.nb_personne
                    evenement.save()
                    ticket = Ticket(
                        client=_client_profile,
                        evenement=evenement,
                        offre=offre,
                        statut='valide'
                    )
                    ticket.save()
                    tickets_created.append(ticket)
                else:
                    tickets_uncreated.append({
                        "offre": offre.libelle,
                        "evenement": evenement.description,
                        "reason": "Places insuffisantes"
                    })

        return tickets_created, tickets_uncreated