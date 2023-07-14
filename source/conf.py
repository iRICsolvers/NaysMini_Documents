# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NaysMini (Simple version of Nays2dH written in Python code) example manual'
copyright = '2023, Yasuyuki Shimizu'
author = 'Yasuyuki Shimizu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # ... other extensions
    'sphinx_search.extension',
    ]

templates_path = ['_templates']
exclude_patterns = []

numfig = True

numfig_format = {
    'figure': 'Figure %s',
    'table':  'Table %s',
    'code-block':  'List %s',
}

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ['css/custom.css']