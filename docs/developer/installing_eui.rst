
.. _human-machine-interface:

##############
Installing HMI
##############

This page contains instructions for building/installing the HMI from a docker image.

This will complete the installation of the HMI, you can then use the Windows Virtual Machine to host your NSV's.


.. _HMI-installation-prereqs:

Pre-requisites
==============

* Access to Tekniker software
* The mtmount dockerfile


Dockerfile Setup
================

The dockerfile will install most of the dependencies needed to run the HMI as well as for building the Operations Manager.
It sets up the XML as well as the SAl package.

.. note:: If you want to run different versions, you'll need to adjust the versions that are checked out in the dockerfile.

.. _HMI-installation:

HMI Installation
================

Install LabVIEW and dependencies
--------------------------------

#. Install the following libraries using the VIPM. 

	.. note::
		An observation while downloading the libraries. For a reason that is not apparent to me the download may sometimes fail. The following are some tricks that worked for me.
		- right click, install
		- Install the rest of the libraries and come back to it
		- Manually find the download online

	.. note::
			if it is your first time running labVIEW you will need to make sure the port on Labview 2018 is configured and has localhost.
			Activating the remote port on Labview is under the tool menu

.. list-table:: 
	:header-rows: 1

	* - Package Name
	* - OpenG Toolkit
	* - Gpower All Toolsets
	* - Gpower Timing
	* - Hidden Gems
	* - NI GOOP Development Suite
	* - NI Event Logger Library
	* - NI GXML
	* - NI LogRotate
	* - NI Syslog Library


#. ``OpenG Toolkit``, as of writing this has all but two dependencies installed.
	The uninstalled dependencies are ``OpenG Port IO`` and ``OpenG Toolkit``.
	We only need the `OpenG Toolkit <https://sourceforge.net/projects/opengtoolkit/files/lib_openg_toolkit/4.x/openg.org_lib_openg_toolkit-4.0.1.9.vip/download>`_.

#. Copy LabVIEW libraries created by Tekniker into the LabVIEW installation directory.

	1. Copy TeknikerLabVIEWLibraries.zip from the Tekniker Software folder onto your local computer.
	#. cd /usr/local/natinst/LabVIEW-2018-64
	#. sudo rsync -ra /path/to/TeknikerLabVIEWLibraries/* . 
	#. sudo chmod -R 777 ./*

Setup Maria DB image
--------------------

#. Install database		
	1.	Clone the repository here: /home/lsst/LSST
		
		.. prompt:: bash
			
			cd /home/lsst/LSST
			git clone https://gitlab.tekniker.es/aut/projects/3151-LSST/mariadb-docker.git
	#.	Update repository:
		
		.. prompt:: bash
			
			cd /home/lsst/LSST/mariadb-docker
			git pull
	#.	Start the docker service:
		
		.. prompt:: bash 
			
			docker-compose up -d
	#.	Get the last backup database available and copy it to: ./backup

		.. prompt:: bash

			cp lsst_AppData-*.sql.gz lsst_events-*.sql.gz lsst_settings-*.sql.gz ./backup

	#.	Create database
		
		.. prompt:: bash

			sudo ./createdatabases.pl
	#.	Restore last backup database. The script will choose the most recent backup. 
		
		.. prompt:: bash
			
			sudo ./restoredatabases.pl
	#.	Edit contrab file to execute the python code that generates the backups: 
		
		.. prompt:: bash
			
			sudo crontab -e
	#.	Add the following lines (Note: that the paths may change for each specific installation.):
		
		.. code:: bash
		
			5 12 * * * /home/lsst/Documents/Docker/mariadb-docker/createbackup.pl
			5 13 * * * docker run --rm -v /home/lsst/Documents/Docker/mariadb-docker/python:/script -v /home/lsst/Documents/Docker/mariadb-docker/backup:/backup python:3.7 python /script/main.py
	
	#.	Save and exit crontab editor: 
		``:wq``
