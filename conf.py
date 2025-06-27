#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo to update document-specific metadata

from documenteer.conf.guide import *


project = "ts-tma"
html_title = project
html_short_title = project
extensions += ["sphinx.ext.autosectionlabel"]
extensions += ['sphinxcontrib.plantuml']
autosectionlabel_prefix_document = True

# remove sidebars for all pages
html_sidebars["**"] = []
html_theme_options["secondary_sidebar_items"] = []
