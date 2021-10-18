.. _configurations:

##############
Configurations
##############

The TMA has various softwares which have configuration files.
In this document you will find what these various configuration are for and how to change them. 


.. todo::
   provide more details to 

Humane Machine Interface
========================

.. _hmi-telemetry-variables:

HMITelemetryVariables
---------------------

1) Locate the file ``HMIComputers/Configuration/HMIConfig.xml`` where ``HMIComputers`` is the root directory to the HMI software.
If you are using a virtualmachine this may be inside of ``gitrepos`` or ``gitdir``. 

2) Do a global search and replace on the file.
   You are searching for ``192.168.1.95`` and replacing this IP with the one you want it to be.

.. _hmi-config:

HMIConfig
---------

1) Locate the file ``HMIComputers/Configuration/HMIConfig.xml`` where ``HMIComputers`` is the root directory to the HMI software.
   If you are using a virtualmachine this may be inside of ``gitrepos`` or ``gitdir``. 

2) Do a global search and replace on the file.
   You are searching for ``192.168.1.95`` and replacing this IP with the one you want it to be.


.. todo::
   Consolidate the documentation below as it is repeated in other areas, and does not belong here.

HMI NSV Simulation
==================
The following instructions will help you understand and configure a simulation environment for the TMA Humane Machine Interface, which can be shortened to HMI.
This is the most basic simulation that can be done.
This is called the "HMI NSV Simulation" because we are simulation only the NSV's (Network Shared Variables) on a Windows machine to verify that the HMI is communicating to the NSV's.
Random NSV's will be generated so we will see the HMI behave erratically.
The meat and potatoes of this configuration is to modify a configuration file to have the right IP addresses which point to the NSV hosting Windows machine. 

	1. Install the HMI, if you have not done so you can find the instructions here [TO DO]
	#. Speak with IT to get access to the network server called "Pavo"
	#. Copy the folder named "Tekniker Software" onto your local computer. This folder contains Intellectual Property from our vendor, remember not to share this software.
	#. On a Windows machine copy NSV Simulator from the Tekniker Software folder onto the local computer.
	#. Identify the IP Address of the Windows machine. The IP address that I set my windows machine to is 192.168.1.11. Manually set yours if you need to.
	#. Identify the IP Address of the CentOS machine which is running the HMI. I manually set mine to be 192.168.1.10. Manually set yours if you need to. 
	#. Connect both machines to a switch and verify that the CentOS and Windows machine can ping each other. 

	.. note:: At this point we are confident that both machines can communicate with each other, we continue by editing configuration files of the HMI. The specific repo name is "HMIComputers". This repository contains the LabVIEW GUI which is referred to as the HMI.

	6. Open HMICOmputers/Configuration/HMIConfig.xml. This file contains paths, IP Addresses, and locations to various elements of the HMI. 

	#. Look for a tag named <ErrorTaskDirectoryPath dim='[5]' type='String'>. There will be a series of <String> tags below. These series of tags make a path to the ErrorHistory folder. Modify these strings to the path of your local machine. Don't forget to update the integer value '5' if you change the number of <String> tags.
	#. Look for a tag named <TMA_Management_Linux_Options mems="3">. There will be a nested tag named <Working_Path type="Path">/home/Andrew/gitrepos/lsst/tma_management/build</Working_Path>. Modify this path to the path of your local machine.
	#. Look for a tag named <WindowTelemetryDirectoryPath dim='[5]' type='String'>. There will be a series of <String> tags below. These series of tags make a path to the WindowsLogging folder. Modify these strings to the path of your local machine. Don't forget to update the integer value '5' if you change the number of <String> tags. We are done editing this file, save and close. 

	#. Open HMIComputers/Configuration/HMITelemetryVariablesURLs.ini. This file contains URL's, IP's, and other configuration tags.
	#. Do a global search for 10.1.22.154 and replace these with the IP address of the Windows machine running the NSV Simulator. In my case I will be replacing them with 192.168.1.11. At the time of writing this document there are 1116 occurances when doing a global search and replace. 
	#. Do a global search for 192.168.209.10 and replace these with the IP address of the Windows machine running the NSV Simulator. In my case I will be replacing them with 192.168.1.11. At the time of writing this document there are 282 occurances when doing a global search and replace.

	#. Well done! The EUI is now configured to operate with the NSV Simulator. Open HMI as you normally would [TODO LINK FOR OPENING THE EUI]

Installation for the NSV Force shared 
=====================================

Installing PXI

1) Install a git tool, I use source tree
2) git pull the PXI software onto the windows machine
3) Download Tekniker Labview Libraries by clinging https://gitlab.tekniker.es/aut/libraries/labview/labview
4) Checkout branch LV_2018
5) copy files in the local folder including the .git folder to National Instruments/LabVIEW2019
6) Select the preselected option that Labview asks to load
7) Cancel when labview cannot find the HMI module
8) Cancel when labview cannot find the DatabaseSettingsConfig.ctl
9) Cancel when labview cannot find the Axis Data.ctl
10) When labview asks to find FGV_BasicFGVAction.ctl find it my navigating to Program Files (x86)\National Instruments\LabVIEW 2019\templates\TeknikerTemplates\_controles
