********************
ATS Deployment Guide
********************

.. contents:: Table of Contents

Introduction
============
This document describes the procedure run the automatic test system.
The document will show the hardware configuration in section 3 and software deployment in section 4.


Reference documents
========================

    +----+----------------------------+----------------------+---------+
    | Nº | Document                   | code                 | Version |
    +====+============================+======================+=========+
    | 1  | Deployment document        | 3151_MCS_0036        | 1.0     | 
    +----+----------------------------+----------------------+---------+
    |    |                            |                      |         |
    +----+----------------------------+----------------------+---------+
    |    |                            |                      |         |
    +----+----------------------------+----------------------+---------+

    .. todo::
    	obtain the table information from the ts_xml table



Hardware configuration
========================

The hardware configuration is explained in a separated file, reference 2.

Software deployment
========================
Each hardware has different software parts, and some hardware had more than one software part. In the following sections each hardware element is explained.
	
Windows Machine
-------------------
		
In the Windows Machine some simulators and some tools are running. 
Start installing the Force EtherCAT Variables installer, that will install the LabVIEW runtime needed in many other tools and simulators.
		
Requirements
^^^^^^^^^^^^^^^^^^

Force EtherCAT Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This tool allows writing data to EtherCAT variables to other simulators using a TCP based custom protocol. The value written using this tool will 
overwrite any set value, so any slave value will be overwritten with the written value.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/forceethercatvars.

Follow next steps to deploy this software:
			
1. If the installer is available continue to step 6
2. Clone the repository in the link above
3. Open the project ForceEtherCATVars.lvproj
4. Go to “Build Specifications” and right click in “ForceIOs” to select “Build”
5. Go to “Build Specifications” and right click in “ForceEtherCatVars Installer” to select “Build”
6. When compilation is finished, open location and copy the “Volume” folder to Windows Machine
7. Install the tool using the “install.exe”
8. Run ForceIOs.exe.
		

Read/Write Network Shared Variables Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool allows reading and writing data from network shared variables to other simulators and back using a TCP based custom protocol.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/readvariables

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project ReadVariables.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Open the "data" folder and open "WriteReadVarConfig.xml".
8. Change the path of the field TCP_configuration_file to point to TCP_ServerConfig.xml file in the same data folder.
9. Run ReadWriteNSVs.exe

This tool is used for reading the variables from 3 different hosts the configuration for each of the instances can be found here: https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/readvariables/-/tree/develop/Configuration

- ReadWriteAxesPXI_NSVs: the configuration for the instance that reads/writes the variables from the AxesPXI.
- ReadWriteTMAPXI_NSVs: the configuration for the instance that reads/writes the variables from the TMA_PXI.
- ReadWriteLocal_NSVs: the configuration for the instance that reads/writes the variables from the WindowMachine.

BoschPowerSupplySimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the bosch power supply, this simulator manages the digital inputs that tell the TMA PXI the status of the power supply.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/boschpowersupply/boschpowersupplysimulator

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project BoschPowerSupplySimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run BoschPowerSupplySimulator.exe

motorThermalModelSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the thermal behaviour of the phase motors, this simulator manages the analog inputs that tell the TMA PXI the temperatures of the motors and uses this values to control the output signal of the valve to manage the temperature of them.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/motorthermalmodel/motorthermalmodelsimulator

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project motorThermalModelSimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run motorThermalModelSimulator.exe

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

This software allows to simulate the behaviour of some subsystem limits switches. Those limits could be part of safety system or EtherCAT distributed IOs.
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
^^^^^^^^^^^^^^^^^^^^^^^^^

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

SpeedgoatManager
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator tool used for the robot framework tests to connect to the Speedgoat.
The source code and more documentation about configuration can be found in https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/speedgoat

Follow next steps to deploy this software:

1. Get the latest version of the compiled code from here: https://gitlab.tekniker.es/aut/projects/3151-LSST/hil/speedgoat/speedgoatmanagerbinaries
2. Paste it to the windows machine

TMA PXI
============

This is the PXI where the control code for all subsystems is running. To be able to configure the TMA PXI, the development PC should be configured as shown in the deployment document 
		
1. Download the PXI repository: https://gitlab.tekniker.es/aut/projects/3151-LSST/LabVIEWCode/PXIController
2. Open the LSST_MainControllerPXI.lvproj.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

	a. Right click in the project an select properties

	.. figure:: /_static/images/TMAPXIpic1.png
	    :name: TMA_PXI_pic1
	    :target: http://target.link/url
	 
	b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

	.. figure:: /_static/images/TMAPXIpic2.png
	    :name: TMA_PXI_pic2
	    :target: http://target.link/url

4. Continue with steps 3.a to 3.c of the point 6.2 in the Deployment document.
5. Open the RT_MCS_Main.vi
6. Run the VI
7. When the vi is deployed to the target, disconnect the target

	a. Right click TMA_PXI target and click Disconnect
 
 	.. figure:: /_static/images/TMAPXIpic3.png
	    :name: TMA_PXI_pic3
	    :target: http://target.link/url


AXES PXI
============

This is the PXI where the control code for the main axes is running. To be able to configure the AXES PXI, the development PC should be configured as shown in the deployment document 

1. Download the PXI repository: https://gitlab.tekniker.es/aut/projects/3151-LSST/LabVIEWCode/PXIController
2. Open the LSST_MainControllerPXI.lvproj.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

	a. Right click in the Axes PXI an select properties

	.. figure:: /_static/images/TMAPXIpic1.png
	    :name: AXES_PXI_pic1
	    :target: http://target.link/url
	 
	b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

	.. figure:: /_static/images/TMAPXIpic2.png
	    :name: AXES_PXI_pic2
	    :target: http://target.link/url

4. Continue with steps 3.a to 3.c of the point 7.2 in the Deployment document.
5. Open the MAIN_AxesPXI.vi
6. Run the VI
7. When the vi is deployed to the target, disconnect the target

	a. Right click AXES_PXI target and click Disconnect
 
 	.. figure:: /_static/images/TMAPXIpic3.png
	    :name: AXES_PXI_pic3
	    :target: http://target.link/url