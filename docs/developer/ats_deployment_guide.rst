####################
ATS Deployment Guide
####################

Introduction
============
This document describes the procedure to setup and run the automatic test system.
This assumes that the machine is freshly provisioned.


Reference documents
===================

.. list-table::
	:header-rows: 1

	* - N°
	  - Document
	  - code
	  - Version
	* - 1
	  - Deployment document
	  - 3151_MCS_0036
	  - 1.0

Hardware configuration
======================

In this section the needed hardware and its configuration is explained.
	
Development PC
--------------

This is a Windows 10 machine where LabVIEW simulators and tools will run.
It is currently a Virtual Machine located on a hypervisor under the url tma-windows.ls.lsst.org.
It can be accessed on the lsst-wap network or by using the anyconnect or openconnect vpn.
Access can be granted by filing an IHS ticket with IT.
Also, a specific tool to manage to simulator in the Speedgoat is running here.

**Labview**

* Need your NI account to be granted access by IT to activate a license on the LabVIEW License Server located on lsst-pdm

.. warning:: lsst-pdm is being replaced sometime in the future.
	New location is yet to be determined.

Tools needed:

* LabVIEW 2018 SP1 - installer zips located on Pavo
* LabVIEW License manager - location TBD version should be <= 4.0
* JKI LabVIEW VI Package Manager - JKI account needed
* NI MAX - included with LabVIEW
* LabVIEW packages listed in the table in section 4 of 3151_MCS_0036
* VI packages listed in section 4
* Tekniker made VIs - location of the files to be solved eventually

Speedgoat
---------

The Speedgoat is used to simulate the main axis behavior in real time.

- Speedgoat

	- Serial Number: 4539 (ItemID 109200)
	- Options:

		- CPUCorei74200 (ItemID 109211)
		- SSD500GB (ItemID 109048)

- Input/Output modules:
	- Ethercat Slaves, IO750 (x2) (ItemID 2B7506)
	- IO 306

Software configuration will be downloaded using Tekniker made tool.

Tools needed:

* MatLab 2020a
* Simulink
* Speedgoat IO libraries

PILZ CPU
--------

This will be used to simulate and test safety software

- PIlz PSSu 4000 ref 314070 
- PSSu E F 4DI-T 
- PSSu E F 4DO 0.5-T 
	
The configuration of hardware is part of the project where the code is included, some configuration will be explained in section 4.


Software deployment
===================
Each machine has different software running on them.
In the following section, the software is installed on the computers.
	
TMA Windows
-----------
		
In the Windows Machine some simulators and some tools are running.
Start installing the Force EtherCAT Variables installer, that will install the LabVIEW runtime needed in many other tools and simulators.

Force EtherCAT Variables
^^^^^^^^^^^^^^^^^^^^^^^^
This tool allows writing data to EtherCAT variables to other simulators using a TCP based custom protocol.
The value written using this tool will overwrite any set value, so any slave value will be overwritten with the written value.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/forceethercatvars.

Follow next steps to deploy this software:

1. Clone the repository https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/forceethercatvars
2. Open the project ForceEtherCATVars.lvproj
3. Go to “Build Specifications” and right click in “ForceIOs” to select “Build”
4. Go to “Build Specifications” and right click in “ForceEtherCatVars Installer” to select “Build”
5. When compilation is finished, open location and copy the “Volume” folder to Windows Machine
6. Install the tool using the “install.exe”
7. Run ForceIOs.exe.
		

Read/Write Network Shared Variables Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool allows reading and writing data from network shared variables to other simulators and uses a TCP based custom protocol.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/readvariables

Follow next steps to deploy this software:

1. Clone the repository https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/readvariables
2. Open the project ReadVariables.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder
5. Paste compilation files to desired destination in Windows Machine
6. Open the "data" folder and open "WriteReadVarConfig.xml".
7. Change the path of the field TCP_configuration_file to point to TCP_ServerConfig.xml file in the same data folder.
8. Run ReadWriteNSVs.exe

This tool is used for reading the variables from 3 different hosts the configuration for each of the instances can be found here: https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/readvariables/-/tree/develop/Configuration

- ReadWriteAxesPXI_NSVs: the configuration for the instance that reads/writes the variables from the AxesPXI.
- ReadWriteTMAPXI_NSVs: the configuration for the instance that reads/writes the variables from the TMA_PXI.
- ReadWriteLocal_NSVs: the configuration for the instance that reads/writes the variables from the WindowMachine.

BoschPowerSupplySimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the bosch power supply, this simulator manages the digital inputs that tell the TMA PXI the status of the power supply.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/boschpowersupply/boschpowersupplysimulator

Follow next steps to deploy this software:

1. Clone the repository https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/boschpowersupply/boschpowersupplysimulator
2. Open the project BoschPowerSupplySimulator.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder 
5. Paste compilation files to desired destination in Windows Machine
6. Run BoschPowerSupplySimulator.exe

motorThermalModelSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the thermal behaviour of the phase motors, this simulator manages the analog inputs that tell the TMA PXI the temperatures of the motors and uses this values to control the output signal of the valve to manage the temperature of them.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/motorthermalmodel/motorthermalmodelsimulator

Follow next steps to deploy this software:

1. Clone the repository in the link above https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/motorthermalmodel/motorthermalmodelsimulator
2. Open the project motorThermalModelSimulator.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder 
5. Paste compilation files to desired destination in Windows Machine
6. Run motorThermalModelSimulator.exe

PhasePowerSupplySimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the phase power supply, this simulator manages the analog inputs that tell the TMA PXI the status of the power supply.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/phasepowersupply/phasepowersupplysimulator

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project PhasePowerSupplySimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run PhasePowerSupplySimulator.exe

Simulate limits
^^^^^^^^^^^^^^^

This software allows to simulate the behavior of some subsystem limits switches. Those limits could be part of safety system or EtherCAT distributed IOs.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/simulatelimits

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project SimulateLimits.lvproj
4. Go to “Build Specifications” and right click in “SimulateLimits” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compiled files to desired destination in the Windows Machine
7. Open the "data" folder and open "GeneralConfiguration.xml" 
8. Change the first path of the field TCP_senders_configuration_Path to point to ForceECATVars_TCP_SenderConfig.xml file in the same data folder.
9. Change dim='[X]' to dim='[1]' for "TCP_senders_configuration_Path" and for "LimitsDefinition" tags. We are only using the first configured limit becauseyou need the safety full simulator with PILZ hardware to use other limits, When you get this hardware (perhaps you have one on the submit) we can download code to it and use those other limits.
10. Run SimulateLimits.exe

cabinetTemperatureControllerSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the temperature controller of the cabinets, this simulator contains the simulator of the different temperature controllers available all over the telescope.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/cabinettemperaturecontroller/cabinet-az0001

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project cabinetTemperatureControllerSimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run cabinetTemperatureControllerSimulator.exe

The cabinets included in this simulator are:

- TMA_AX_DZ_CBT_0001 (Phase Main Power Cabinet)
- TMA_AZ_CS_CBT_0001 (TEK Mount Control System cabinet - MCS)
- TMA_AZ_PD_CBT_0001 (Azimuth Power Distribution)
- TMA_AZ_PD_TRM_0001 (Isolation transformer)
- TMA_EL_PD_CBT_0001 (Elevation Power Distribution 1)
- TMA_EL_PD_CBT_0002 (Elevation Power Distribution 2)

extensionSimulatorForDP
^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the extensions of the deployable platforms, this simulator manages the digital inputs that tell the Safety system the status of the extensions of the deployable platforms.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/dpextensionssimulator

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project DPextensionsSimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run extensionSimulatorForDP.exe

OilSupplySystemSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the Oil Supply System (OSS), this simulator contains a modbus server that connects to the TMA PXI to transmit the status of the OSS.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/oilsupplysystem/oilsupplysystemsimulator

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project OilSupplySystemSimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run OilSupplySystemSimulator.exe

.. _deploy-speedgoat:

Speedgoat
^^^^^^^^^
This provides the motion model for the TMA using specialized hardware.
The Speedgoat Manager will handle loading the model and managing the configurations.

1. Install matlab 2020a with the following dependencies

	* Simulink
	* Simulink Real Time
	* Simulink coder
	* Matlab Coder

2. `Install Speedgoat IO for Matlab 2020a <https://www.speedgoat.com/help/slrt/page/configuration/refentry_host_software_installation>`_
3. Run the `slrtexplorer` command in matlab
4. Configure it to look for the target's ip address as 192.168.17.1
5. Clone the model repository
6. Run the model

SpeedgoatManager
^^^^^^^^^^^^^^^^^

This is a simulator tool used for the robot framework tests to connect to the Speedgoat.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/speedgoat

Follow next steps to deploy this software:

1. Get the latest version of the compiled code from here: https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/speedgoat/speedgoatmanagerbinaries
2. Change the ip address setting to become the windows machine's ip address
3. Paste it to the windows machine

TMA Centos
----------
		
In the Linux Machine the secondary axis simulators and the robot framework tests are running.
This is a Virtual Machine running on a hypervisor that is located under tma-centos.ls.lsst.org.
It can be accessed either on the lsst-wap network or by using the anyconnect vpn.
Access can be granted by filing an IHS ticket with Vera C. Rubin Observatory IT.

secondaryAxisSil
^^^^^^^^^^^^^^^^

This is a simulator for the secondary axes (bosch axes), this simulator contains a modbus server that connects to the TMA PXI to transmit the status of each of the axes.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/secondaryaxis/secondaryaxissil

Because of the use of certain internal libaries in the source code, download the compiled binaries from https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/secondaryaxis/secondaryaxissilbinaries

Follow the steps defined in the secondaryAxisSilREADME_.

.. _secondaryAxisSilREADME: https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/secondaryaxis/secondaryaxissil/-/blob/master/README.md

robotFramework
^^^^^^^^^^^^^^

This refers to the automatic test framework the installation steps to setup the environment for robot framework is explained `here: <https://gitlab.tekniker.es/aut/projects/3151-LSST/test/robotframework/-/wikis/Installation>`_

The source code and more documentation can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/test/robotframework

HMI
===

See :ref:`hmi-virtual-machine` for running the HMI and operation manager docker container.


TMA PXI
=======

This is the PXI where the control code for all subsystems is running. To be able to configure the TMA PXI, the development PC should be configured as shown in the deployment document.
		
1. Download the PXI repository: https://gitlab.tekniker.es/aut/projects/3151-LSST/LabVIEWCode/PXIController
2. Open the LSST_MainControllerPXI.lvproj.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

	a. Right click in the project an select properties

	.. figure:: ../../_static/images/TMAPXIpic1.png
	    :name: TMA_PXI_pic1
	 
	b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

	.. figure:: ../../_static/images/TMAPXIpic2.png
	    :name: TMA_PXI_pic2

4. Continue with steps 3.a to 3.c of the point 6.2 in the Deployment document.
5. Open the RT_MCS_Main.vi (for testing the hole project)

  a. To test just one subsystem some specific test VIs can be found inside the corresponding subsystem folder. For example the Balancing specific test VI shown bellow:

	.. figure:: ../../_static/images/TmaPxi_Test_BAL_TaskVI.png
	    :name: Test VI for the balancing subsystem


6. Run the VI
7. When the vi is deployed to the target, disconnect the target

	a. Right click TMA_PXI target and click Disconnect
 
 	.. figure:: ../../_static/images/TMAPXIpic3.png
	    :name: TMA_PXI_pic3


AXES PXI
========

This is the PXI where the control code for the main axes is running.
To be able to configure the AXES PXI, the development PC should be configured as shown in the deployment document

1. Download the PXI repository: https://gitlab.tekniker.es/aut/projects/3151-LSST/LabVIEWCode/PXIController
2. Open the LSST_MainControllerPXI.lvproj.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

	a. Right click in the Axes PXI an select properties

	.. figure:: ../../_static/images/TMAPXIpic1.png
	    :name: AXES_PXI_pic1
	 
	b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

	.. figure:: ../../_static/images/TMAPXIpic2.png
	    :name: AXES_PXI_pic2

4. Continue with steps 3.a to 3.c of the point 7.2 in the Deployment document.
5. Open the MAIN_AxesPXI.vi
6. Run the VI
7. When the vi is deployed to the target, disconnect the target

	a. Right click AXES_PXI target and click Disconnect
 
 	.. figure:: ../../_static/images/TMAPXIpic3.png
	    :name: AXES_PXI_pic3

Safety code deployment
======================

The code that runs on the PILZ controller to simulate the behaviour of the TMA Interlock System.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/testdualmodbus

1. Open the "TestDualModbus" project with PAS4000 version 1.18.0
2. Activate the "TestDualModbus"

	.. figure:: ../../_static/images/PASS4000activateProject.png
	    :name: PASS4000activateProject

3. Open the online network editor

	.. figure:: ../../_static/images/PASS4000onlineNetworkEditor.png
	    :name: PASS4000onlineNetworkEditor

4. Scan project to scan the network to verify that the PILZ CPU is connected

	.. figure:: ../../_static/images/PASS4000scan.png
	    :name: PASS4000scan

5. Close the online network editor
6. Download the project

  a. Open the Project downloader:

	.. figure:: ../../_static/images/PASS4000downloadCode.png
	    :name: PASS4000downloadCode

  If asked to build changes say YES

	.. figure:: ../../_static/images/PASS4000buildChanges.png
	    :name: PASS4000buildChanges

  b. Start download:

	.. figure:: ../../_static/images/PASS4000startDownload.png
	    :name: PASS4000startDownload

  c. Confirm download:

	.. figure:: ../../_static/images/PASS4000confirmDownload.png
	    :name: PASS4000confirmDownload

  d. Download completed:

	.. figure:: ../../_static/images/PASS4000downloadCompleted.png
	    :name: PASS4000downloadCompleted

7. Logout:

	.. figure:: ../../_static/images/PASS4000logout.jpg
	    :name: PASS4000logout

8. Close the PAS4000
