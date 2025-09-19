# Configuration file for the Sphinx documentation builder.
#
# Pour la doc Sphinx complète : https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# -- Chemins du projet Django -----------------------------------------------
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'ApiJO_Back.settings'
django.setup()

# -- Informations sur le projet ---------------------------------------------
project = 'ApiJO'
copyright = '2025, Gael Driano'
author = 'Gael Driano'
release = '0.1'

# -- Extensions Sphinx ------------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # Documentation automatique des modules
    'sphinx.ext.napoleon',         # Support Google & NumPy style
    'sphinx_autodoc_typehints',    # Prend en charge les annotations de type
]

# -- Templates et fichiers à exclure ---------------------------------------
templates_path = ['_templates']
exclude_patterns = []

# -- Langue ---------------------------------------------------------------
language = 'fr'

# -- Options autodoc --------------------------------------------------------
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# -- Thème HTML -------------------------------------------------------------
html_theme = 'furo'
