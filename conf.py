#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo to update document-specific metadata

from documenteer.conf.guide import *


project = "ts-tma"
html_theme_options["logotext"] = project
html_title = project
html_short_title = project
extensions += ["sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True
