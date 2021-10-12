#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo to update document-specific metadata

from documenteer.conf.pipelinespkg import *


project = "ts-tma"
html_theme_options["logotext"] = project
html_title = project
html_short_title = project
