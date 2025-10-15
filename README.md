# ApiJO_Back

API Django pour la gestion des Jeux Olympiques, servant les applications web client, admin et mobile.

## Table des matières

- [Description](#description)
- [Technologies utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Sécurité](#sécurité)
- [Axes d'évolution future](#axes-dévolution-future)

## Description

Cette API REST fournit une interface complète pour la gestion des Jeux Olympiques, incluant :
- Gestion des lieux sportifs
- Gestion des disciplines sportives
- Gestion des épreuves
- Gestion des événements
- Gestion des offres commerciales
- Système d'authentification avec JWT pour clients et employés

## Technologies utilisées

- Python 3.x
- Django 5.2
- Django REST Framework 3.16
- JWT pour l'authentification
- PostgreSQL
- Sphinx pour la documentation

## Prérequis

- Python 3.x
- PostgreSQL
- Un environnement virtuel Python (recommandé)

## Sécurité

### Authentification et autorisation
- **Authentification JWT** : Utilisation de `djangorestframework-simplejwt` avec tokens d'accès et de rafraîchissement configurables
- **Gestion des rôles** : Système de permissions basé sur 3 rôles (admin, employé, client) avec permissions granulaires
- **Permissions personnalisées** :
  - `IsAdmin` : Accès complet pour les administrateurs
  - `IsAdminOrEmploye` : Accès pour administrateurs et employés
  - `IsAdminOrAuthenticatedReadOnly` : Lecture seule pour utilisateurs authentifiés, accès complet pour admins

### Validation des données
- **Mots de passe renforcés** : Validateur personnalisé `StrongPasswordValidator` imposant :
  - Minimum 10 caractères
  - Au moins une majuscule, une minuscule, un chiffre et un caractère spécial
- **Validation des emails** : Validateur `EmailValidator` vérifiant :
  - Format correct de l'adresse email
  - Rejet des domaines d'emails jetables (tempmail, yopmail, etc.)
  - Unicité des adresses email dans le système

### Configuration sécurisée
- **Variables d'environnement** : Clé secrète et paramètres sensibles gérés via `.env`
- **CORS configuré** : Origines autorisées définies explicitement
- **Middleware de sécurité Django** : Protection contre les attaques courantes (CSRF, Clickjacking, etc.)
- **Base de données** : Configuration PostgreSQL avec paramètres de connexion sécurisés

### Bonnes pratiques implémentées
- Séparation des environnements (DEBUG configurable)
- Algorithme HS256 pour la signature JWT
- Durées de vie configurables pour les tokens JWT
- Modèle utilisateur personnalisé pour une gestion fine des rôles

## Axes d'évolution future

### 1. Système de paiement
**État actuel** : Gateway de paiement simulé (`PaymentGatewayMock`) avec service de paiement basique
**Évolutions possibles** :
- Intégration de véritables passerelles de paiement (Stripe, PayPal, Banque populaire)
- Gestion des remboursements automatisés
- Paiements fractionnés et échelonnés

### 2. Gestion avancée des places et réservations
**État actuel** : Système simple de comptage de places restantes par événement
**Évolutions possibles** :
- Système de réservation temporaire avec timeout
- Gestion des listes d'attente


### 3. Notifications et communication
**Évolutions nécessaires** :
- Notifications par email (confirmations, rappels, annulations)
- SMS pour les informations critiques

### 4. Analytics et reporting
**Évolutions possibles** :
- Tableau de bord administrateur avec métriques en temps réel
- Analyse des ventes par discipline, lieu, période

### 5. Fonctionnalités avancées pour les clients
**Évolutions possibles** :
- Partage social des événements assistés
- Planificateur personnel d'événements avec alertes

### 6. Architecture et performance
**Évolutions techniques** :
- Mise en cache avancée (Redis) pour les données fréquemment consultées

### 7. Sécurité renforcée
**Évolutions possibles** :
- Authentification à deux facteurs (2FA)
- Audit complet des actions utilisateurs
- Chiffrement des données sensibles au repos
