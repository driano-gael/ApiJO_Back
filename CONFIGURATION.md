# Guide de Configuration de l'API ApiJO

Ce guide détaille toutes les options de configuration disponibles pour l'API ApiJO.

## Configuration de l'Environnement

### Variables d'Environnement (.env)

Toutes les configurations sensibles sont gérées via le fichier `.env`. Copiez `.env.example` en `.env` et personnalisez les valeurs.

#### Configuration Django
```env
DEBUG=True/False
SECRET_KEY=votre-clé-secrète
ALLOWED_HOSTS=127.0.0.1,localhost,votre-domaine.com
```

- `DEBUG` : Active/désactive le mode debug
- `SECRET_KEY` : Clé de sécurité Django (à changer en production)
- `ALLOWED_HOSTS` : Liste des hôtes autorisés, séparés par des virgules

#### Configuration Base de données
```env
DATABASE_NAME=nom_base_de_données
DATABASE_USER=utilisateur_base_de_données
DATABASE_PASSWORD=mot_de_passe_base_de_données
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

- Supporte PostgreSQL par défaut
- Configurez les accès selon votre environnement

#### Configuration CORS
```env
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CORS_ALLOW_CREDENTIALS=True
```

- Liste des origines autorisées pour les requêtes CORS
- Important pour l'interaction avec le frontend

#### Configuration JWT
```env
ACCESS_TOKEN_LIFETIME=00:00:30
REFRESH_TOKEN_LIFETIME=08:00:00
```

- Durées de vie des tokens d'authentification
- Format : HH:MM:SS

#### Configuration Admin
```env
ADMIN_EMAIL=admin@exemple.com
ADMIN_PASSWORD=mot_de_passe_securise
ADMIN_NOM=Nom
ADMIN_PRENOM=Prénom
ADMIN_MATRICULE=MAT001
```

- Informations pour le compte administrateur par défaut
- Utilisées par la commande `python manage.py createAdmin`

## Sécurité

### En Production

1. Désactivez le mode DEBUG :
```env
DEBUG=False
```

2. Configurez une SECRET_KEY sécurisée :
```env
SECRET_KEY=votre-clé-très-secrète-et-très-longue
```

3. Limitez les ALLOWED_HOSTS :
```env
ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com
```

4. Configurez CORS strictement :
```env
CORS_ALLOWED_ORIGINS=https://votre-frontend.com
```

5. Ajustez les durées des tokens JWT :
```env
ACCESS_TOKEN_LIFETIME=00:15:00
REFRESH_TOKEN_LIFETIME=24:00:00
```

## Scripts de Gestion

### Population de la Base de Données
```bash
python manage.py populate_jo_2
```
- Crée des données de test pour les JO
- Utilisez uniquement en développement

### Nettoyage de la Base de Données
```bash
python manage.py flush
```
- Supprime toutes les données
- À utiliser avec précaution

## Configuration du Serveur Web

### Développement
```bash
python manage.py runserver
```

### Production
Recommandations :
- Utilisez Gunicorn comme serveur WSGI
- Configurez Nginx comme proxy inverse
- Activez HTTPS avec Let's Encrypt

## Configuration des Settings Django

### Structure des Settings

Le projet utilise une configuration modulaire des settings :
- `settings.py` : Configuration de base
- Variables d'environnement : Configurations sensibles

### Paramètres Principaux

#### Applications Installées
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
    'users',
    'authentication',
]
```

#### Middleware
```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Important pour CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

#### Configuration REST Framework
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

#### Configuration JWT
```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('ACCESS_TOKEN_LIFETIME', 30))),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=int(os.getenv('REFRESH_TOKEN_LIFETIME', 24))),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

#### Configuration des Fichiers Statiques et Media
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Paramètres de Sécurité

#### Protection contre les attaques
```python
# Protection CSRF
CSRF_COOKIE_SECURE = True  # En production
CSRF_COOKIE_HTTPONLY = True

# Protection XSS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Protection SSL/HTTPS
SECURE_SSL_REDIRECT = True  # En production
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### Internationalisation
```python
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```

### Configuration des Templates
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Configuration des Logs
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Customisation du Modèle Utilisateur
```python
AUTH_USER_MODEL = 'users.User'
```

### Validation des Mots de Passe
```python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```
