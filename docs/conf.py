# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import subprocess, os, sys

def configureDoxyfile(input_dir, output_dir):

	with open('Doxyfile.in', 'r') as file :
		filedata = file.read()

	filedata = filedata.replace('@DOXYGEN_INPUT_DIR@', input_dir)
	filedata = filedata.replace('@DOXYGEN_OUTPUT_DIR@', output_dir)
	
	with open('Doxyfile', 'w') as file:
		file.write(filedata)

# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

breathe_projects = {}
if read_the_docs_build:
	input_dir = '../src'
	output_dir = 'build'
	output_dox_dir = 'docs/doxygen/build'
	configureDoxyfile(input_dir, output_dir)
	subprocess.call('doxygen', shell=True)
	breathe_projects['pilotifx'] = output_dir + '/xml'


# -- Project information -----------------------------------------------------

project = 'Pilot Library C++'
copyright = '2020, No corporation'
author = 'jaenrig'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#...

extensions = [ "breathe",
			   "recommonmark"]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

#...

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_theme_pd

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
	"head_font_family" : "Source Sans Pro",
	"font_family" : "Source Sans Pro",
	"body_text_align" : "justify",
}

#html_theme_path = [sphinx_theme_pd.get_html_theme_path()]

html_logo = 'img/donquijote_rocinante.jpg'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Breathe Configuration
breathe_default_project = "pilotifx"