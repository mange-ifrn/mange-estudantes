# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mange para Estudantes'
copyright = '2024, Jurandy Soares'
author = 'Jurandy Soares'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = 'imagens/favicon.ico'
html_favicon = 'imagens/favicon.ico'
html_theme = 'furo'
html_static_path = ['_static']

html_title = html_short_title = project
html_theme_options = {
    'source_repository': 'https://github.com/mange-ifrn/mange-estudantes',
    'source_branch': 'main/docs'
}

