.. image:: https://img.shields.io/badge/ts--tma-lsst.io-brightgreen.svg
   :target: https://ts-tma.lsst.io
.. image:: https://github.com/lsst-ts/ts_tma/workflows/CI/badge.svg
   :target: https://github.com/lsst-ts/ts_tma/actions?query=workflow%3ACI

#################
TMA Documentation
#################

ts-tma
======

The vendor for the TMA is `Tekniker`_.

The documentation generated by Tekniker is gathered in this repo, using submodules, as originally these files were stored
in gitlab and the migrated to github.

**Links:**

- Publication URL: https://ts-tma.lsst.io
- Alternative editions: https://ts-tma.lsst.io/v
- GitHub repository: https://github.com/lsst-tstn/ts-tma
- Build system: https://github.com/lsst-ts/ts_tma/actions


Build this technical note
=========================

You can clone this repository and build the html locally with `Sphinx`_:

.. code-block:: bash

   git clone https://github.com/lsst-tstn/ts-tma
   cd ts-tma
   pip install -r requirements.txt
   make html

.. note::

   In a Conda_ environment, ``pip install -r requirements.txt`` doesn't work as expected.
   Instead, ``pip`` install the packages listed in ``requirements.txt`` individually.

The built html is located at ``_build/html/index.html``.

Editing this technical note
===========================

You can edit the ``index.rst`` file, which is a reStructuredText document.
The `DM reStructuredText Style Guide`_ is a good resource for how we write reStructuredText.

Remember that images and other types of assets should be stored in the ``_static/`` directory of this repository.
See ``_static/README.rst`` for more information.

The published html is located at https://ts-tma.lsst.io and will be automatically rebuilt whenever you push your changes
to the ``master`` branch on `GitHub <https://github.com/lsst-tstn/ts-tma>`_.

Updating metadata
=================

This html's metadata is maintained in ``metadata.yaml``.

Using the bibliographies
========================

The bibliography files in ``lsstbib/`` are copies from `lsst-texmf`_.
You can update them to the current `lsst-texmf`_ versions with::

   make refresh-bib

Add new bibliography items to the ``local.bib`` file in the root directory (and later add them to `lsst-texmf`_).

.. _Sphinx: http://sphinx-doc.org
.. _DM reStructuredText Style Guide: https://developer.lsst.io/restructuredtext/style.html
.. _this repo: ./index.rst
.. _Conda: http://conda.pydata.org/docs/
.. _lsst-texmf: https://lsst-texmf.lsst.io
.. _Tekniker: https://www.tekniker.es/
