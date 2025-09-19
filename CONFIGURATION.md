# Configuration

Ce guide détaille la configuration de l'API ApiJO après installation.

## Configuration Django

### Fichier settings.py

Les principaux paramètres à configurer dans ApiJO_Back/settings.py : les paramètres sont à configurer dans le .env

### Base de données

Modification du moteur de Base de données si nécessaire (PostgreSQL recommandé) :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'apijoback'),
        'USER': os.environ.get('DB_USER', 'apijouser'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### Authentification JWT

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

### CORS (Cross-Origin Resource Sharing)

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend React
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

## Configuration des modèles

### Paramètres par défaut des modèles

#### Événements

Les événements ont des paramètres par défaut configurables :

- Nombre de places par défaut : 1000 places
- Gestion automatique des places restantes

## Configuration des rôles utilisateurs

L'API supporte trois rôles principaux :

### Client

- Permissions : Consultation des événements et offres
- Restrictions : Pas d'accès admin
- Profil : ClientProfile avec informations personnelles

### Employé

- Permissions : Gestion des événements et épreuves
- Restrictions : Pas de création d'utilisateurs
- Profil : EmployeProfile avec matricule
- Utilisation dans les vues : [isEmploye]

### Admin

- Permissions : Accès complet à l'API
- Capacités : Création d'employés, gestion complète
- Accès : API complète
- Utilisation dans les vues : [isAdmin]

## Configuration des validateurs

### Validation des mots de passe

Configuration du StrongPasswordValidator :

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'authentication.validators.StrongPasswordValidator',
        'OPTIONS': {
            'min_length': 12,
            'require_uppercase': True,
            'require_lowercase': True,
            'require_digits': True,
            'require_special': True,
        }
    },
]
```

### Validation des emails

Utilise le EmailValidator intégré avec vérifications anti-spam.

## Configuration de l'API REST

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

## Configuration des médias

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Taille maximale des fichiers (5MB)
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
```

## Configuration de production

```env
# Sécurité
DEBUG=False
SECRET_KEY=votre_clé_très_sécurisée
ALLOWED_HOSTS=votredomaine.com,www.votredomaine.com

# Base de données production
DB_NAME=apijoback_prod
DB_HOST=votre_serveur_db
DB_PASSWORD=mot_de_passe_très_sécurisé

# CORS
CORS_ALLOWED_ORIGINS=https://votredomaine1.com,https://votredomaine2.com
```

## Tests de configuration

```bash
# Test des paramètres Django
python manage.py check

# Test de la base de données
python manage.py dbshell

# Test des migrations
python manage.py showmigrations

# Test de l'API
python manage.py test
```

## Problèmes de configuration courants

- Erreur 500 : Vérifiez DEBUG=True en développement
- CORS : Ajoutez votre frontend aux CORS_ALLOWED_ORIGINS
- JWT : Vérifiez que les tokens ne sont pas expirés
- Permissions : Contrôlez les rôles utilisateurs
