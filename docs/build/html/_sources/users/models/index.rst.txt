Modèles Utilisateurs
====================

Les modèles définissent l'architecture utilisateur personnalisée avec email comme identifiant et profils spécialisés.

Architecture des modèles
========================

**Hiérarchie :**
1. **User** - Modèle de base personnalisé (remplace User Django)
2. **ClientProfile** - Profil client avec clé chiffrée automatique
3. **EmployeProfile** - Profil employé avec matricule professionnel

**Relations :**
- User ↔ ClientProfile (OneToOne)
- User ↔ EmployeProfile (OneToOne)

.. toctree::
   :maxdepth: 2
   :caption: Modèles disponibles

   base_user
   client_profile
   employe_profile
