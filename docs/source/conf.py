from recommonmark.parser import CommonMarkParser  # <----- ADDED BY JB
import os  # <----- ADDED BY JB
import sys  # <----- ADDED BY JB

sys.path.insert(
    0, os.path.abspath("../..")
)  # <----- ADDED BY JB - pick up modules on root

source_parsers = {".md": CommonMarkParser}
source_suffix = [".rst", ".md"]  # <----- ADDED BY JB - can pick up markdown as well.

# -- Project information -----------------------------------------------------

project = "tester"
copyright = "2020, JB"
author = "JB"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
]  # <----- ADDED BY JB

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

