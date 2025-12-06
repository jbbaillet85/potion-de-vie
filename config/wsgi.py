import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Chemin vers le dossier racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Chargement du fichier .env
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Définir le module settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Créer l'application WSGI
application = get_wsgi_application()
