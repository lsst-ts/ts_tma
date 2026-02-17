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
It uses RDP for remote access and is under the LDAP domain.
It can be accessed on the lsst-wap network or by using the openconnect vpn.
Access can be granted by filing an IHS ticket with IT.
Also, a specific tool to manage the model in the Speedgoat is running here.

**Labview**

* You need your NI account to be granted access by IT to activate a license on the LabVIEW License Server located on nlm-labview-1.lsst.org

Tools needed:

* LabVIEW 2020 - installer zips located on Pavo or on NI's website with NI SSP enabled account
* LabVIEW License manager - Download on NI's website
* JKI LabVIEW VI Package Manager - JKI account needed - Free edition is good enough
* NI MAX - included with LabVIEW
* LabVIEW packages listed in the table in section 4 of 3151_MCS_0036 - All of the packages that the installer comes with except for NI statemachine which is now a VIPM package.
* VI packages listed in section 4 of the deployment document
* QMT database MySQL can be downloaded from the source repo.
* Tekniker made VIs - https://github.com/lsst-ts/ts_tma_vipm_dependency *private repo*

Speedgoat
---------

The Speedgoat is used to simulate the main axis behavior in real time.

- Speedgoat

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
* Speedgoat IO libraries - `Found on speedgoat's website using a speedgoat account <https://www.speedgoat.com/desktopmodules/2sxc/api/app/SpeedgoatExtranet/api/Downloads/DownloadFile?FolderName=Q1ioLpQTXkicnnUD5ML3Sw&fileName=speedgoat_io_blockset_9_4_0_3_R2020a_build_26200.zip>`_

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
The source code and more documentation about configuration can be found in :fab:`github` `forceethercatvars <https://github.com/lsst-ts/ts_tma_hil_force-ethercat-vars>`_.

Follow next steps to deploy this software:

1. Clone the repository :fab:`github` `forceethercatvars <https://github.com/lsst-ts/ts_tma_hil_force-ethercat-vars>`_.
2. Open the project ForceEtherCATVars.lvproj
3. Go to “Build Specifications” and right click in “ForceIOs” to select “Build”
4. Go to “Build Specifications” and right click in “ForceEtherCatVars Installer” to select “Build”
5. When compilation is finished, open location and copy the “Volume” folder to Windows Machine
6. Install the tool using the “install.exe”
7. Run ForceIOs.exe.
    

Read/Write Network Shared Variables Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool allows reading and writing data from network shared variables to other simulators and uses a TCP based custom protocol.
The source code and more documentation about configuration can be found in `readvariables(github) <https://github.com/lsst-ts/ts_tma_hil_read-variables>`_.

Follow next steps to deploy this software:

1. Clone the repository https://github.com/lsst-ts/ts_tma_hil_read-variables
2. Open the project ReadVariables.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder
5. Paste compilation files to desired destination in Windows Machine
6. Open the "data" folder and open "WriteReadVarConfig.xml".
7. Change the path of the field TCP_configuration_file to point to TCP_ServerConfig.xml file in the same data folder.
8. Run ReadWriteNSVs.exe

This tool is used for reading the variables from 3 different hosts the configuration for each of the instances can be found here: https://github.com/lsst-ts/ts_tma_hil_read-variables/tree/develop/Configuration

- ReadWriteAxesPXI_NSVs: the configuration for the instance that reads/writes the variables from the AxesPXI.
- ReadWriteTMAPXI_NSVs: the configuration for the instance that reads/writes the variables from the TMA_PXI.
- ReadWriteLocal_NSVs: the configuration for the instance that reads/writes the variables from the WindowMachine.

BoschPowerSupplySimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the bosch power supply, this simulator manages the digital inputs that tell the TMA PXI the status of the power supply.
The source code and more documentation about configuration can be found in `boschpowersupplysimulator(github) <https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator>`_

Follow next steps to deploy this software:

1. Clone the repository https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator
2. Open the project BoschPowerSupplySimulator.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder 
5. Paste compilation files to desired destination in Windows Machine
6. Run BoschPowerSupplySimulator.exe

motorThermalModelSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the thermal behavior of the phase motors, this simulator manages the analog inputs that tell the TMA PXI the temperatures of the motors and uses this values to control the output signal of the valve to manage the temperature of them.
The source code and more documentation about configuration can be found in `motorthermalmodelsimulator(github) <https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator>`_.

Follow next steps to deploy this software:

1. Clone the repository in the link above https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator
2. Open the project motorThermalModelSimulator.lvproj
3. Go to “Build Specifications” and right click in “Executable” to select “Build”
4. When build finishes go to build folder and copy all files and folder 
5. Paste compilation files to desired destination in Windows Machine
6. Run motorThermalModelSimulator.exe

PhasePowerSupplySimulator
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the phase power supply, this simulator manages the analog inputs that tell the TMA PXI the status of the power supply.
The source code and more documentation about configuration can be found in `phasepowersupplysimulator(github) <https://github.com/lsst-ts/ts_tma_hil_phase-power-supply_phase-power-supply-simulator>`_.

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

This software allows to simulate the behavior of some subsystem limit switches.
Those limits could be part of safety system or EtherCAT distributed IOs.
The source code and more documentation about configuration can be found in `simulatelimits(github) <https://github.com/lsst-ts/ts_tma_hil_simulate-limits>`_.

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project SimulateLimits.lvproj
4. Go to “Build Specifications” and right click in “SimulateLimits” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compiled files to desired destination in the Windows Machine
7. Open the "data" folder and open "GeneralConfiguration.xml" 
8. Change the first path of the field TCP_senders_configuration_Path to point to ForceECATVars_TCP_SenderConfig.xml file in the same data folder.
9. Change dim='[X]' to dim='[1]' for "TCP_senders_configuration_Path" and for "LimitsDefinition" tags. 
   We are only using the first configured limit because you need the safety full simulator with PILZ hardware to use other limits, when you get this hardware (perhaps you have one on the submit) we can download code to it and use those other limits.
10. Run SimulateLimits.exe

cabinetTemperatureControllerSimulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a simulator for the temperature controller of the cabinets, this simulator contains the simulator of the different temperature controllers available all over the telescope.
The source code and more documentation about configuration can be found in `cabinet-az0001(github) <https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets>`_.
The related configuration file is `TMA_AZ_CS_CBT_0001 <https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets/tree/develop/configFiles/TMA_AZ_CS_CBT_0001>`_.

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
The source code and more documentation about configuration can be found in `dpextensionssimulator(github) <https://github.com/lsst-ts/ts_tma_hil_deployable-platform-extensions-simulator>`_.

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
The source code and more documentation about configuration can be found in `oilsupplysystemsimulator(github) <https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator>`_.

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6 
2. Clone the repository in the link above
3. Open the project OilSupplySystemSimulator.lvproj
4. Go to “Build Specifications” and right click in “Executable” to select “Build”
5. When build finishes go to build folder and copy all files and folder 
6. Paste compilation files to desired destination in Windows Machine
7. Run OilSupplySystemSimulator.exe

Deploy Speedgoat
^^^^^^^^^^^^^^^^
This provides the motion model for the TMA using specialized hardware.
The Speedgoat Manager will handle loading the model and managing the configurations.
Before starting to deploy the model, make sure that the :ref:`docs/developer/ats_deployment_guide:speedgoatmanager` is running.

1. Install matlab 2020a with the following dependencies

  * Simulink
  * Simulink Real Time
  * Simulink coder
  * Matlab Coder

2. `Install Speedgoat IO for Matlab 2020a <https://www.speedgoat.com/help/slrt/page/configuration/refentry_host_software_installation>`_
3. Run the `slrtexplorer` command in matlab
4. Configure it to look for the target's ip address as 192.168.17.1
5. Clone the model repository
6. Build/deploy and run the model

SpeedgoatManager
^^^^^^^^^^^^^^^^

This is a simulator tool used for the robot framework tests to connect to the Speedgoat.
The source code and more documentation about configuration can be found in https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager

Follow next steps to deploy this software:

1. Get the latest version of the compiled code from here: https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager-binaries
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
The source code and more documentation about configuration can be found in https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil

Because of the use of certain internal libaries in the source code, download the compiled binaries from https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondary-axis-sil-binaries

Follow the steps defined in the secondaryAxisSilREADME_.

.. _secondaryAxisSilREADME: https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil/blob/master/README.md

robotFramework
^^^^^^^^^^^^^^

This refers to the automatic test framework the installation steps to setup the environment for robot framework is explained `here: <https://github.com/lsst-ts/ts_tma_test_automatic-test-code/blob/develop/docs/Installation.md>`_

The source code and more documentation can be found in https://github.com/lsst-ts/ts_tma_test_automatic-test-code

.. list-table:: Hostnames for the ATS
  :widths: 50 50
  :header-rows: 1

  * - Name
    - Host Name/IP Address
  * - TMA PXI
    - ats-tma-pxi01.ls.lsst.org (139.229.145.241)
  * - AXES PXI
    - ats-tma-axes-pxi.ls.lsst.org (139.229.145.242)
  * - AUX PXI
    - 139.229.145.238
  * - PILZ
    - tma-windows.ls.lsst.org (139.229.145.101)
  * - HMI/MCC
    - tma-centos.ls.lsst.org (139.229.145.102)


HMI
===

The HMI is installed as a LabVIEW runtime executable on the TMA CentOS machine.
The operation manager is installed as an RPM package which leverages systemd service architecture.


TMA PXI
=======

The PXI is a model 1086.

Use NI-MAX to install NI Linux RT system image along with Variable Engine and Ethercat driver.

Then create configuration directories and files using `this document <https://github.com/lsst-ts/ts_tma_tma-documentation_pxi-controller_documentation/blob/master/80%20DeployOnTargets/01%20TMA%20PXI.md>`_.

.. prompt:: bash

  mkdir -p /c/Configuration/CAR_TCP /c/Configuration/DiscreteStateReporting /c/Configuration/EIB /c/Configuration/Safety /c/Configuration/TekNSVs /c/Configuration/axisManagementComm

Find the files under the `ESIfiles` directory of the PXIController repo.
Most of the folders match the names on the cRIO.
Some of the files have the suffix ForATS and those are the ones that you want to copy.

This is the PXI where the control code for all subsystems is running.
To be able to configure the TMA PXI, the development PC should be configured as shown in the deployment document.
    
1. Download the PXI repository: https://github.com/lsst-ts/ts_tma_labview_pxi-controller
2. Open the `ATS_Projects/ATS_LSST_MainControllerPXI.lvproj`.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

  a. Right click in the project an select properties

  .. figure:: ../../_static/images/TMAPXIpic1.png
      :name: TMA_PXI_pic1
   
  b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

  .. figure:: ../../_static/images/TMAPXIpic2.png
     :name: TMA_PXI_pic2
#. Update target address to use `ats-tma-pxi01.ls.lsst.org`
#. Save project.

#. Save the project.
#. Close the project.
#. Under tools, clear build cache
#. Close labview
#. Open labview
#. Open project.
#. Open main.vi
#. Close main.vi
#. Configure ethercat project to match hardware connection order and change ID to 0.
#. Build target
#. Deploy target


AXES PXI
========

The PXI is a model 1086.

Start by adding the necessary configuration files from `ESIfiles` using `this document <https://github.com/lsst-ts/ts_tma_tma-documentation_pxi-controller_documentation/blob/master/80%20DeployOnTargets/03%20AXES%20PXI.md>`_.

.. prompt:: bash

  mkdir -p /c/Configuration/axisManagementComm

This is the PXI where the control code for the main axes is running.
To be able to configure the AXES PXI, the development PC should be configured as shown in the deployment document

1. Download the PXI repository: https://github.com/lsst-ts/ts_tma_labview_pxi-controller
2. Open the `ATS_Projects/ATS_MainAxes.lvproj`.
3. Ensure that in the project properties the Conditional Disable Symbol “HIL” is set to “True”

  a. Right click in the Axes PXI an select properties

  .. figure:: ../../_static/images/TMAPXIpic1.png
      :name: AXES_PXI_pic1
   
  b. In the opened window go to Conditional Disable Symbols page and set the value for HIL symbol to “True”.

  .. figure:: ../../_static/images/TMAPXIpic2.png
     :name: AXES_PXI_pic2

#. Update project target to ats-tma-axes-pxi.ls.lsst.org
#. Save project.
#. Close project.
#. Clean build cache
#. Close LabVIEW
#. Open LabVIEW
#. Open project
#. Open main.vi
#. Close main.vi
#. Configure ethercat with ethercat project to match connection order
#. Build target
#. Deploy to target

FGPA Deployment
^^^^^^^^^^^^^^^
The AXES cRIO runs FPGA code that needs to be deployed.
Use the NI Package Manager to install the FPGA package and its dependencies.
Otherwise find a FPGA compile server that's located on the network.

.. todo:: Find a list of working FPGA compile servers.

1. Open the AXES (not for ATS) project.
#. Change the AXES target IP address to the AXES ATS IP address.
#. Open the FPGA target under the cRIO folder.
#. Build the FPGA target locally or with a FPGA compile server.
#. Download to the target.

.. note:: The simulink model needs to be deployed on the speedgoat before the fpga code will work.

AUX PXI
=======
The PXI is a virtual machine running NI RT linux.

Start by setting up the configuration directory using `this document <https://github.com/lsst-ts/ts_tma_tma-documentation_pxi-controller_documentation/blob/master/80%20DeployOnTargets/02%20AUX%20PXI.md>`_.
You can find the files in the `ESIFiles` directory inside of the `PXIController` repo.

#. Open `ATS_Projects/ATS_AuxSystemsController.lvproj`.
#. Save project.
#. Close project
#. Clear cache
#. Close labview
#. open labview
#. Open project
#. Open main.vi
#. Close main.vi
#. Build target
#. Deploy network variables
#. Deploy target

Safety code deployment
======================

The code that runs on the PILZ controller to simulate the behavior of the TMA Interlock System.
The source code and more documentation about configuration can be found in `testdualmodbus(github) <https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus>`_

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
