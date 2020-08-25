#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo to update document-specific metadata

import os
from documenteer.sphinxconfig.stackconf import build_package_configs

# Ingest settings from metadata.yaml and use documenteer's configure_technote()
# to build a Sphinx configuration that is injected into this script's global
# namespace.

_g = globals()
_g.update(build_package_configs(
    project_name='TSSW Developer Guide',version="current"))
# Add intersphinx inventories as needed
# http://www.sphinx-doc.org/en/stable/ext/intersphinx.html
# Example:
#
#     intersphinx_mapping['python'] = ('https://docs.python.org/3', None)
