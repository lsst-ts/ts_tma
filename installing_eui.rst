**************
Installing EUI
**************

This page contains instructions for installing the EUI from scratch.


.. note::
	Steps from : to : have been completed on a CentOS Docker image here. You must manually complete the image by following steps : to :. Then, on a separate container : to :. 

	This will complete the EUI, you can then using the Windows Virtual Machin here to host your NSV's.


.. _eui-installation-prereqs:

Pre-requisites
==============
1. Obtain Tekniker Install files.

	#. Speak with IT to get acces to the network server called "Pavo"
	#. Copy the folder named "Tekniker Software" onto your local computer. This folder contains Intellection Property from our vendor, remember not to share this software.

#. Install Git. 

	#. Do ``sudo nano /etc/yum.repos.d/wandisco-git.repo``.
	#. Copy the text below and paste into ``wandisco-git.repo``.

		.. code-block:: bash

			[wandisco-git] 
			name=Wandisco GIT Repository
			baseurl=http://opensource.wandisco.com/centos/7/git/$basearch/
			enabled
			gpgcheck=1
			gpgkey=http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco
			Import GPG key for added repository key typing sudo rpm --import http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco

	#. Import the keys with ``sudo rpm --import http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco``.
	#. Install git ``sudo yum install git``.

#. Install the following CentOS7 libraries for development.

	.. code-block:: bash
		
		sudo yum update
		sudo yum groupinstall "Development Tools"
		sudo yum install cmake boost-devel.x86_64
		wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
		sudo rpm -ivh epel-release-latest-7.noarch.rpm
		sudo yum install geany java-1.7.0-openjdk-devel

#. Install the following Linux libraries to run Labview

	.. code-block:: bash

		sudo yum install glibc.i686 libstdc++.so.6 libXinerama.i686
		sudo yum upgrade gnome-packagekit-common
		sudo yum install libglvnd-glx-1.0.1-0.8.git5baa1e5.el7.i686

#. Install the following for use with Docker. 
    ``sudo yum install -y yum-utils device-mapper-persistent-data lvm2``

.. _eui-installation:

EUI Installation
================
#. Install SAL, latest instructions for this can be found here 
	.. todo:: 
		Insert SAL technote installation guide. for ts_xml use commit f9156b8bf300e6381b2d505da058c6b6475aed1f.


Install TMA Operation Manager
------------------------------------------
	
	#. ``git clone https://gitlab.tekniker.es/sai/projects/3151-LSST/lsst.git``
	#. ``cd lsst``
	#. ``git checkout feature-rotator-track`` (As of writinig this is branch to use)
	#. ``cd tma_management/``
	#. ``mkdir build``
	#. ``cd build``
	#. ``cmake ..``
	#. ``make``

Install LabVIEW and dependencies
-----------------------------------------------

	#. Install Labview 2015 32 bit. LabVIEW package manager runs on Labview 2015. This is the only reason we install LV 2015.

		#. Copy LabVIEW2015 from the Tekniker Software folder onto your local computer.
		#. Extract the file.
		#. CD LabVIEW2015/32-bit 
		#. ./INSTALL say yes to everything.

	#. Install Labview 2018 64 bit SP1. Tekniker provided software was developed on LabVIEW 2018.

		#. Copy LabVIEW2018 from the Tekniker Software folder onto your local computer.
		#. Extract the file.
		#. CD LabVIEW2018 
		#. ./INSTALL say yes to everythin3/31/20g.

	#. Install Labview package manager https://vipm.jki.net/download, then install the following libraries. 

		.. note::
			I would like to point out an observation while downloading the libraries. For a reason that is not apparent to me the download may sometimes fail. The following are some tricks that worked for me.
			- right click, install
			- Install the rest of the libraries and come back to it
		 	- Manually find the download online

		.. note::
			 if it is your first time running labVIEW you will need to make sure the port on Labview 2018 is configured and has localhost.

		#. ``OpenG Toolkit``, as of writing this has all but two dependencies installed. The uninstalled dependencies are ``OpenG Port IO`` and ``OpenG Toolkit``. We only need the Toolkit, you can find the link for a manual download here https://sourceforge.net/projects/opengtoolkit/files/lib_openg_toolkit/4.x/openg.org_lib_openg_toolkit-4.0.1.9.vip/download. 
		#. ``GPower All Toolsets``, as of writing this all but two dependencies installed. The uninstalled dependencies are GPower Timing, and GPower Events. We only need Gpower Timing, attempt to install it on VI Package Manager by searching for it just as you would normally search and install any package. 
		#. ``Hidden Gems``
		#. ``NI GOOP Development Suite``
		#. ``NI Event Logger Library``
		#. ``NI GXML``
		#. ``NI LogRotate``
		#. ``NI Syslog Library``

	#. Copy LabVIEW libraries created by Tekniker into the LabVIEW installation directory.

		1. Copy TeknikerLabVIEWLibraries.zip from the Tekniker Software folder onto your local computer.
		#. cd /usr/local/natinst/LabVIEW-2018-64
		#. sudo rsync -ra /path/to/TeknikerLabVIEWLibraries/* . 
		#. sudo chmod -R 777 ./*

#. Install Docker 

	a. Follow these steps https://docs.docker.com/install/linux/docker-ce/centos/
	#.	Install the latest version of Docker CE and containerd.
		``sudo yum install docker-ce docker-ce-cli containerd.io``
	#.	Start docker.
		``sudo systemctl start docker``
	#.	Verify that Docker CE is installed correctly by running the hello-world image.
		``sudo docker run hello-world``

#. Install database		
	
	1.	Add the user to docker users: 
		``$ sudo usermod -aG docker $USER``
	2.	Activate docker to automatically launch
		``$ sudo systemctl start docker``
		``$ sudo systemctl enable docker``
	3.	Reboot machine
		``$ sudo reboot``
	4.	Install docker compose
		``$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose``
		``sudo chmod +x /usr/local/bin/docker-compose``
	5.	Clone the repository here: /home/lsst/LSST
		``cd /home/lsst/LSST``
		``git clone https://gitlab.tekniker.es/aut/projects/3151-LSST/mariadb-docker.git``
	6.	Update repository:
		``cd /home/lsst/LSST/mariadb-docker``
		``git pull``
	7.	Go to /home/lsst/LSST/mariadb-docker 
	8.	Start the docker service:
		``docker-compose up -d``
	9.	Get the last backup database available and copy it to: ./backup
		Copy the three files: 
		a.	lsst_AppData-XXX.sql.gz
		b.	lsst_events-XXX.sql.gz
		c.	lsst_settings-XXX.sql.gz
	10.	Create database
		``sudo ./createdatabases.pl``
	11.	Restore last backup database. The script will choose the most recent backup. 
		``sudo ./restoredatabases.pl``
	12.	Edit contrab file to execute the python code that generates the backups: 
		``sudo crontab -e``
	13.	Add the following lines (Note: that the paths may change for each specific installation.):
		.. code:: bash
		
		5 12 * * * /home/lsst/Documents/Docker/mariadb-docker/createbackup.pl
		.. code:: bash
		
		5 13 * * * docker run --rm -v /home/lsst/Documents/Docker/mariadb-docker/python:/script -v /home/lsst/Documents/Docker/mariadb-docker/backup:/backup python:3.7 python /script/main.py
	14.	Save and exit crontab editor: 
		``:wq``
