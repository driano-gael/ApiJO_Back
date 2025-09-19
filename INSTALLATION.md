# Guide d'installation de l'API ApiJO

Ce guide vous accompagne dans l'installation complète de l'API ApiJO.

## Prérequis

- Python 3.x
- PostgreSQL
- Un environnement virtuel Python (recommandé)

## Installation de l'environnement

### 1. Cloner le dépôt
```bash
git clone [url-du-repo]
cd ApiJO_Back
```

### 2. Créer l'environnement virtuel
```bash
# Sur Windows
python -m venv .venv
.venv\Scripts\activate

# Sur Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Configuration de la base de données

### 1. Créer une base de données PostgreSQL
```sql
CREATE DATABASE apijoback;
CREATE USER apijouser WITH PASSWORD 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE apijoback TO apijouser;
```

### 2. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet a l'image du fichier `.env.exemple` et modifiez les valeurs selon votre configuration :
```env
# Configuration de la base de données
DB_NAME=apijoback
DB_USER=apijouser
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432

# Configuration Django
SECRET_KEY=votre_clé_secrète
DEBUG=True

# Configuration CORS
CORS_ALLOWED_ORIGINS=http:ip_du_frontEnt
CORS_ALLOW_CREDENTIALS=True

# Configuration Admin par défaut
ADMIN_EMAIL=mail@admin.com
ADMIN_PASSWORD=@DminPass123
ADMIN_NOM=Admin
ADMIN_PRENOM=admin
ADMIN_MATRICULE=ADM001
```

## Configuration de Django

### 1. Appliquer les migrations
```bash
python manage.py migrate
```

### 2. Créer un administrateur
Pour les tests, un admin par défaut peut être créé avec la commande suivante :
```bash
python manage.py createAdmin
```
Note : Les identifiants de l'administrateur peuvent être personnalisés en modifiant les variables ADMIN_* dans le fichier .env

### 3. Collecter les fichiers statiques
```bash
python manage.py collectstatic
```

### 4. Peupler la base de donnée
```bash
python manage.py populate_jo_2
```

## Vérification de l'installation

### 1. Tests de base
```bash
python manage.py check
python manage.py test
```

### 2. Lancer le serveur
```bash
python manage.py runserver
```
L'API devrait être accessible à http://localhost:8000/

### 3. Vérifier l'acces aux Endpoint
Accédez à http://localhost:8000/api/evenement/

### 4. Acces Swagger
une fois le serveur lancé:
Accédez à http://localhost:8000/api/docs/swagger/

## Dépannage

Problèmes courants :

- **Erreur de connexion à la base de données** : Vérifiez les paramètres dans `.env`
- **Erreur CORS** : Vérifiez CORS_ALLOWED_ORIGINS dans `.env`
- **Erreur de dépendances** : Réinstallez avec `pip install -r requirements.txt`
- **Erreur de migrations** : Essayez `python manage.py migrate --run-syncdb`
- **Variables d'environnement non chargées** : Vérifiez que le fichier `.env` est bien à la racine du projet
