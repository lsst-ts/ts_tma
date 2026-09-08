# ATS Deployment

| Code          | Editor       |
| ------------- | ------------ |
| 3151_MCS_0051 | Julen Garcia |

## Introduction

This document describes the procedure to setup the different systems for running the automatic test system.

## Software Deployment

Each hardware has different software parts, and some hardware had more than one software part. In the following sections
each hardware element is explained.

### Windows Machine

In the Windows Machine some simulators and some tools are running.

#### Force EtherCAT Variables DEPRECATED

This tool allows writing data to EtherCAT variables to other simulators using a TCP based custom protocol. The value
written using this tool will overwrite any set value, so any slave value will be overwritten with the written value. The
source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_force-ethercat-vars)

Follow next steps to deploy this software:

1. If the installer is available continue to step 6
2. Clone the repository in the link above
3. Open the project `ForceEtherCATVars.lvproj`
4. Go to *Build Specifications* and right click in *ForceIOs* to select *Build*
5. Go to *Build Specifications* and right click in *ForceEtherCatVars Installer* to select *Build*
6. When compilation is finished, open location and copy the `Volume` folder to Windows Machine
7. Install the tool using the *install.exe*
8. Run *ForceIOs.exe*.

#### Read/Write Network Shared Variables Tool

This tool allows reading and writing data from network shared variables to other simulators and back using a TCP based
custom protocol. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_read-variables)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `ReadVariables.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Open the `data` folder and open "WriteReadVarConfig.xml".
8. Change the path of the field *TCP_configuration_file* to point to *TCP_ServerConfig.xml* file in the same data folder.
9. Run *ReadWriteNSVs.exe*

This tool is used for reading the variables from 3 different hosts the configuration for each of the instances can be
found [here](https://github.com/lsst-ts/ts_tma_hil_read-variables/tree/develop/Configuration):

- ReadWriteAxesPXI_NSVs: the configuration for the instance that reads/writes the variables from the AxesPXI.
- ReadWriteTMAPXI_NSVs: the configuration for the instance that reads/writes the variables from the TMA_PXI.
- ReadWriteLocal_NSVs: the configuration for the instance that reads/writes the variables from the WindowMachine.

#### BoschPowerSupplySimulator

This is a simulator for the bosch power supply, this simulator manages the digital inputs that tell the TMA PXI the
status of the power supply. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `BoschPowerSupplySimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *BoschPowerSupplySimulator.exe*

#### motorThermalModelSimulator

This is a simulator for the thermal behavior of the phase motors, this simulator manages the analog inputs that tell
the TMA PXI the temperatures of the motors and uses this values to control the output signal of the valve to manage the
temperature of them. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `motorThermalModelSimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *motorThermalModelSimulator.exe*

#### PhasePowerSupplySimulator

This is a simulator for the phase power supply, this simulator manages the analog inputs that tell the TMA PXI the
status of the power supply. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_phase-power-supply_phase-power-supply-simulator)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `PhasePowerSupplySimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *PhasePowerSupplySimulator.exe*

#### Simulate limits

This software allows to simulate the behavior of some subsystem limits switches. Those limits could be part of safety
system or EtherCAT distributed IOs. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_simulate-limits)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `SimulateLimits.lvproj`
4. Go to *Build Specifications* and right click in "SimulateLimits" to select *Build*
5. When build finishes go to build folder and copy all files and folders
6. Paste compiled files to desired destination in the Windows Machine
7. Open the `data` folder and open `GeneralConfiguration.xml`
8. Check the IPs for the limits variables
9. Run *SimulateLimits.exe*

#### cabinetTemperatureControllerSimulator

This is a simulator for the temperature controller of the cabinets, this simulator contains the simulator of the
different temperature controllers available all over the telescope. The source code and more documentation about
configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `cabinetTemperatureControllerSimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *cabinetTemperatureControllerSimulator.exe*

The cabinets included in this simulator are:

- *TMA_AX_DZ_CBT_0001* (Phase Main Power Cabinet)
- *TMA_AZ_CS_CBT_0001* (TEK Mount Control System cabinet - MCS)
- *TMA_AZ_PD_CBT_0001* (Azimuth Power Distribution)
- *TMA_AZ_PD_TRM_0001* (Isolation transformer)
- *TMA_EL_PD_CBT_0001* (Elevation Power Distribution 1)
- *TMA_EL_PD_CBT_0002* (Elevation Power Distribution 2)

#### extensionSimulatorForDP

This is a simulator for the extensions of the deployable platforms, this simulator manages the digital inputs that tell
the Safety system the status of the extensions of the deployable platforms. The source code and more documentation about
configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_deployable-platform-extensions-simulator)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `DPextensionsSimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *extensionSimulatorForDP.exe*

#### OilSupplySystemSimulator

This is a simulator for the Oil Supply System (OSS), this simulator contains a modbus server that connects to the AUX
PXI to transmit the status of the OSS. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator)

Follow next steps to deploy this software:

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `OilSupplySystemSimulator.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *OilSupplySystemSimulator.exe*

#### SpeedgoatManager

This is a simulator tool used for the robot framework tests to connect to the Speedgoat. The source code and more
documentation can be found in [this repo](https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager).

Follow next steps to deploy this software:

1. Get the latest version of the compiled code from
   [built app repo](https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager-binaries) in a folder called
   `SpeedgoatManager`
2. Get the latest version of the compiled models for the speedgoat and clone the repo in a folder named
   `slrtbinariesforspeedgoat` next to the `SpeedgoatManager` folder. The result should look like the image below:

   ![Two folders with the corresponding files](media/slrtBinariesFolder.png)

#### Top End Chiller simulator

This is a simulator for the Top End Chiller (TEC), this simulator contains a modbus server that connects to the AUX
PXI to transmit the status of the TEC. The source code and more documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller/)

Follow the steps defined in the repo [README](https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller/blob/develop/README.md)

#### WriteTekNsvVariables

This is a tool to update the required TekNSV variables in the TMA-PXI with a default value or by manually providing one.
This is used for setting the status of the deployable extensions as well as the AZ and EL brakes pressures, but more
variables can be written by updating the config file of the tool. The source code and more documentation about
configuration can be found in [this repo](https://github.com/lsst-ts/ts_tma_hil_write-TekNSV-variables).

1. If the installer or executable is available continue to step 6
2. Clone the repository in the link above
3. Open the project `Write TekNSV Variables.lvproj`
4. Go to *Build Specifications* and right click in *Executable* to select *Build*
5. When build finishes go to build folder and copy all files and folder
6. Paste compilation files to desired destination in Windows Machine
7. Run *WriteTekNsvVariables.exe*

#### Start/Stop the Simulators and Tools in Windows

You can use the scripts in [ts_tma_hil_simulators-start-stop-scripts](https://github.com/lsst-ts/ts_tma_hil_simulators-start-stop-scripts) to start or stop all ATS related applications in a once.
You need to modify the paths of applications in scripts.

#### Firewall Rules in Windows

You need to add the firewall Inbound Rules for the ATS ports (5002, 50050-50099):

![firewall rule 1](media/windows_firewall_rule_1.png)
![firewall rule 2](media/windows_firewall_rule_2.png)
![firewall rule 3](media/windows_firewall_rule_3.png)

### Linux Machine

In the Linux Machine the secondary axis simulators and the robot framework tests are running.

#### secondaryAxisSil

This is a simulator for the secondary axes (bosch axes), this simulator contains a modbus server that connects to the
TMA PXI to transmit the status of each of the axes. The source code and more documentation about configuration can be
found in [this repo](https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil)

Follow the steps defined in the repo [README](https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil/blob/master/README.md)

#### robotFramework

This refers to the automatic test framework the installation steps to setup the environment for robot framework is
explained [here](https://github.com/lsst-ts/ts_tma_test_automatic-test-code/blob/develop/docs/Installation.md)

The source code and more documentation can be found in
[this repo](https://github.com/lsst-ts/ts_tma_test_automatic-test-code/)

### TMA PXI

This is the PXI where the control code for all subsystems is running. To be able to configure the TMA PXI, the
development PC should be configured as shown in the
[deployment document](https://ts-tma.lsst.io/docs/tma_maintenance_deployment/deployment.html#development-pc)

1. Download the [PXI repository](https://github.com/lsst-ts/ts_tma_labview_pxi-controller)
2. Open the `ATS_Projects/ATS_LSST_MainControllerPXI.lvproj`

   > This project is only meant to be used for building the TMA PXI code for the ATS

3. Ensure that in the project properties the *Conditional Disable Symbol* `HIL` is set to `True`

    1. Right click in the project an select properties

    ![Project properties](./media/proyectProperties.png)

    2. In the opened window go to *Conditional Disable Symbols* page and set the value for `HIL` symbol to `True`.

    ![Conditional Disable Symbols for TMA PXI](./media/conditionaldisableSymbols.png)

4. Open the main `RT_MCS_Main.vi`
   1. Solve the requested dependencies if they appear.
   2. Close the main.
   3. Save all the request files.
5. Build the `rtexe`
   1. Open the *Build Specifications* section
   2. Right click and build

    ![alt text](media/BuildRtexe.png)

6. Once built, deploy the rtexe to the target. This can be done using SSH (scp) or with the LabVIEW project.
7. Before rebooting the PXI, deploy the Network Shared Variables (NSVs) for the ATS.
   1. Open the `ATS_Projects/ATS_TMA_PXI.lvproj`
   2. Connect the project to the PXI
   3. Deploy the `ATS_ECATSlave_NSV.lvlib`. This lib contains the NSVs for the ATS simulation mode.

    ![DeployAtsEthercatSlave](media/DeployAtsEthercatSlave.png)

    > Note that these NSV variables are meant to replace the need for an ethercat master in the TMA PXI for the ATS.
    > Therefore, deploying the ethercat config in this project is not necessary.

   4. Disconnect from the project
8. Reboot the PXI -> check the boot of the PXI with the *labviewmessages* alias command

  > To test just one subsystem some specific test VIs can be found inside the corresponding subsystem folder. For
  > example the Balancing specific test VI shown bellow:
  >
  > ![Balancing test code](./media/balancingTestCode.png)
  >
  > These are not built, but could be run and deployed from the project directly if needed

You need to copy the required `.so` libraries, setup NTP/PTP, set the `cron` job, add the configruraion files in `/c/Configuration`, modify the IPs in the configuration file, and more.
This step applies to the Axes PXI and AUX PXI as well.
See [tma-pxi deployment](https://ts-tma.lsst.io/docs/tma_maintenance_deployment/deployment.html#tma-pxi),  [tma-pxi target](https://ts-tma.lsst.io/docs/tma_pxi-controller_documentation/80%20DeployOnTargets/01%20TMA%20PXI.html#tma-pxi), and [Deploy On Targets introduction](https://ts-tma.lsst.io/docs/tma_pxi-controller_documentation/80%20DeployOnTargets/00%20Introduction.html) for more details.
For the EIB configuration file (`multi_ext.txt`), use the [multi_extForATS.txt](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/EIB/multi_ext_forATS.txt) instead and rename it to `multi_ext.txt`.
You might need to get or update the related EIB IP, port, gateway, and UDP destination (IP, MAC, and port) as well (see [changing-eib-ip](https://ts-tma.lsst.io/docs/tma_maintenance_eib_eib-change-ip/Change-IP.html#changing-eib-ip)).
For the UDP destination, it would be the ATS AXES PXI.
For example, see:

```text
EIB8;network_user:ip_address;139.229.145.242;
EIB8;network_user:netmask;255.255.255.0;
EIB8;network_user:gateway;139.229.145.254;
EIB8;network_user:tcp_port;1050;
EIB8;network_user:dhcp_enabled;0;

# Setup UDP destination: Setup later in program
EIB8;udp_transfer:udp_dest_mac;00.80.2f.23.eb.99;        ;Set MAC address, where UDP packets of the EIB8 are sent to (set programmatically)
EIB8;udp_transfer:udp_dest_ip;139.229.145.238;            ;Set IP address, where UDP packets of the EIB8 are sent to (set programmatically)
EIB8;udp_transfer:udp_dest_port;3051;                    ;Set Port, where UDP packets of the EIB8 are sent to
```

You need to modify the **Logging IP** of **ENCODERSYSTEM** by the ATS TMA EUI to point to the ATS TMA PXI address.
You might need to use the administor account instead of the operator account to do so.

![EIB settings logging ip](media/eib_settings_logging_ip.png)

To test the EIB connection, you can go to the Encoder system window in the EUI and press power on for AZ or EL, if it comes on, then you are OK, if not, something is wrong.

The use of EIB is to be close to the real system.

> Note that we are not using the values coming from the EIB to control AZ and EL when using the ATS.

For the safety configuration files (`Safety_ModBusMapping_ForReadWriteDefinition.txt` and `Safety_ModBusMapping.txt`) in `/c/Configuration/Safety`, use the [Safety_ModBusMapping_ForReadWriteDefinition_ForATS.txt](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/Safety/Safety_ModBusMapping_ForReadWriteDefinition_ForATS.txt) and [Safety_ModBusMapping_ForATS.txt](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/Safety/Safety_ModBusMapping_ForATS.txt) instead and rename them to `Safety_ModBusMapping_ForReadWriteDefinition.txt` and `Safety_ModBusMapping.txt`.
Since the control system will do the ModBus connection to the safety system, you need to make sure the safety systems allows this peer connection.
Open the PAS4000 IDE and use the **IP Connections Editer** and **Online Network Editor** to check or modify the **Remote IP Address** under the **Modbus/TCP** protocol to have the ATS TMA PXI IP in the allowed list.
See the **Network settings** in **IP Connections Editer** to do the related modification.
If you do the change, you need to redeploy the change to the safety system.

For the Bosch system configuration file, copy the [BoschSILConfig.ini](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/RT%20Code/BoschMotor/HIL/Configuration/BoschSILConfig.ini) file to `/c/Configuration` directory and modify the IPs inside to point to the VM that runs the [ts_tma_hil_secondary-axis_secondaryaxissil](https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil).

For the axis management communication, make sure the `Remote_Adress` in `/c/Configuration/axisManagementComm/SenderConfig.xml` points to the ATS AXES PXI.

Since there are many IPs in the configuration files in `/c/Configuration` directory, it would be good to check the current values on summit or ATS before any modification.
You can do `grep -nr "139" /c/Configuration` or `grep -nr "192" /c/Configuration` to check each IP address based on the case that the PXIs are on the summit or ATS.
`139.x.x.x` belongs to the Rubin IP domain in Chile and `192.x.x.x` belongs to the Tekniker IP domain (in case you copy the configuration file from the [ts_tma_labview_pxi-controller](https://github.com/lsst-ts/ts_tma_labview_pxi-controller)).
You can use the `host` command to check each IP address if it has an assigned hostname.
You can also check the current TMA setup here: [Ethernet-Connections](https://ts-tma.lsst.io/docs/tma_ethernet-conexions/Ethernet-Connections.html).

The control system will generate the log file in the `/home/lvuser/log` directory.
Make sure you create this directory in advance.
The ownership of log directory should be `lvuser:ni`.
This ownership appies to the `/c/Configuration` as well.
You can do a soft link of `/home/admin/logs` to this log directory.
This step applies to the Axes PXI and AUX PXI.

To make the TCP/IP socket reusable immediately, add the following line to `/etc/natinst/share/lvrt.conf`:

```text
SocketSetReuseAddr=True
```

You can see the related reference here: [LabVIEW Returns Error 60 When Opening TCP Connection on Local Port](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P9ZQSA0&l=en-US).
This step applies to the Axes PXI and AUX PXI.

### Axes PXI

Same as TMA-PXI, but instead of opening the TMA project, open the `ATS_Projects/ATS_MainAxes.lvproj` and the
`MAIN_AxesPXI.vi`. And instead of deploying the NSVs library, deploy the ethercat master, see image below.

![Deploy ethercat master](media/DeployEthercatMaster.png)

You might need to download the build cRIO-9145 FPGA bitfile.
See [ethercat-crio-9145](https://ts-tma.lsst.io/docs/tma_maintenance_deployment/deployment.html#ethercat-crio-9145).
See [note of NI-9145](#note-of-ni-9145), [electrical-connections](https://ts-tma.lsst.io/docs/ats_tekniker/ATS_HardwareDesign.html#electrical-connections), and [ATS_ElectricalSchematics.pdf](https://github.com/lsst-ts/ts_tma/blob/main/docs/ats_tekniker/ATS_ElectricalSchematics.pdf) for more details.

> Note the `MainFPGA.vi` might be broken in `ATS_Projects/ATS_MainAxes.lvproj`.
> To fix it, re-select each network shared variable with the same name under the **Device2**.

In addition, you need to change the mode of NI-9401 module to be the **output** mode (you can do so for DIO0-3 and DIO4-7, it will not hurt).
See [Configuring NI 9401’s Bidirectional Pins As Inputs and Outputs](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P7ZESA0&l=en-US).
After the fix, you can build the bitfile and download it to the cRIO-9145.

The reason that we need to fix this FPGA code at each time is because this is the same code for the non-ATS and ATS, so one has to be broken (because of the confliction) and we prefer to break the ATS one rather than the non-ATS one.

Copy the [MainAxisConfig_forATS.ini](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/MainAxes/AxesPXI/Configuration/MainAxisConfig_forATS.ini) to the `/c/Configuration` in PXI and rename it to be the `/c/Configuration/MainAxisConfig.ini`.

You may want to check the EtherCAT slaves can be put into the **Operational** state or not.
Connect the **ATS_MainAxes.lvproj** project to the ATS AXES PXI.
Right click the **MainDrives EtherCAT Master** to see the **Online Master State** option.
Click it and the LabVIEW should pop up a window to show the current 3 slave states:

- x2 are the speedgoat modules.
- x1 is the cRIO that triggers the EIB signal, note that the EIB is NOT connected to the ethercat line directly.
See the details in [ATS_HardwareDesign](https://ts-tma.lsst.io/docs/ats_tekniker/ATS_HardwareDesign.html).

If the ATS AXES PXI does not detect the slaves using the **Online Master State**, check the following:

1. The speedgoat is up and running.
2. The ethercat connections are in place and right order, see [ethercat-line-device-order](https://ts-tma.lsst.io/docs/ats_tekniker/ATS_HardwareDesign.html#ethercat-line-device-order).

#### Note of NI-9145

The cRIO-9145 regularly sends a synchronous signal to the EIB by the NI-9401 module (Mod1/DIO0 and Mod1/DIO1).
If the FPGA code in the cRIO-9145 runs correctly, you should be able to see:

1. The cRIO "FPGA LED" flashs in the running.
2. In the NI distribution system (you need to add the ATS AXES PXI to it), the **CyclesCounter** (how many times that the EIB has been triggered) increases overtime.
This counts the FPGA executions, so as long as it’s increasing everything should be OK.
3. The flashing of **FPGACodeRunningClock** in the NI distribution system.
This is a true/false clock that will be constantly switching if the FPGA is running.

If you check the **MainFPGA.vi** in **MainAxesPXI.lvproj**, you will see [Input Virtual Point](https://www.ni.com/docs/en-US/bundle/ni-industrial-communications-ethercat/page/ni-9145-fpga-i-o.html) is used to trigger a state machine to send the signal to EIB.
This is synced to the Ethercat scan engine, and that’s why it is used to trigger the EIB.
See more details in [ni-9145-timing-diagram](https://www.ni.com/docs/en-US/bundle/ni-industrial-communications-ethercat/page/ni-9145-timing-diagram.html).
This FPGA code is running while the Ethercat is in **Active** mode, therefore this signal (Input Virtual Point) is automatically generated by the cRIO.
You cannot check it from outside the FPGA code, as it is not exposed to the outside by anything at the moment.

If you check the NI distribution system, you can see the **InputVirtualPointTiming** to be 1000.
This allows people to check the "Input Virtual Point" sampling time, which is in fact an indirect way of measuring the "Input Virtual Point" and see that it is working fine.
As a value of 1000 usec = 1ms, the sampling rate of Ethercat.

You can measure the pulse duration from the cRIO to the EIB as well.
From the NI distribution system, you can see

- WaitTime_ticks = 14600
- OnTime_ticks = 6400
- FPGA clock = 40 MHz

Digital output ON time in seconds 1/40MHz * 6400 = 0.00016 seconds (0.16 ms).
Therefore, it is recommended to use the oscilloscope to check this synchronous signal when needed.

If there are problems with the EIB trigger, the **OnTime_ticks** variable might have a `0`value when testing, set it to
65535 with the NI distribution manager to make sure there is the signal in oscilloscope.

For example, the following is the figure of difference between the sync+ and sync- signals, using a value of 65535:

![oscilloscope diff plus and minus](media/oscilloscope_diff_plus_and_minus.png)

### AUX PXI

Same as TMA-PXI, but instead of opening the TMA project, open the `ATS_Projects/ATS_AuxSystemsController.lvproj` and the
`AuxSystemsMain.vi`. For this PXI there are no libraries to be deployed

For the CPU temperature monitor task to work, the ssh key generation is required.
See [ssh-keys-for-cpu-temperatures](https://ts-tma.lsst.io/docs/tma_pxi-controller_documentation/80%20DeployOnTargets/02%20AUX%20PXI.html#ssh-keys-for-cpu-temperatures).
Make sure you have tested the `lvuser` in AUX PXI can `ssh` to the TMA PXI and AXES PXI (`admin` account in these two PXIs).
When doing the test, note that you need to use the same IP assigned in `/c/Configuration/CpuTempMonitoring/PxiCpuMonitoringConfiguration.json`.
That means if you use the numbered IP in `/c/Configuration/CpuTempMonitoring/PxiCpuMonitoringConfiguration.json`, test the `ssh` with this numbered IP.
If you are using the hostname in `/c/Configuration/CpuTempMonitoring/PxiCpuMonitoringConfiguration.json`, test the `ssh` with this hostname.
You need to put the public key to the `/home/admin/.ssh/authorized_keys` for the above two PXIs.
You might need to modify `/c/Configuration/CpuTempMonitoring/PxiCpuMonitoringConfiguration.json` for the path of `temp1_input` file.
It could be `/sys/devices/platform/coretemp.0/hwmon/hwmon0/temp1_input`, `/sys/devices/platform/coretemp.0/hwmon/hwmon1/temp1_input`, or others, which depends on your PXI controller.

For the Modbus temperature controller configuration files, copy the [ModbusTemperatureControllers](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/tree/develop/ESIFiles/ModbusTemperatureControllers) directory to `/c/Configuration` directory and modify the IPs and ports in `ini` files to point to the VM that runs the [ts_tma_hil_cabinet-temperature-controller_cabinets](https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets).
You also need to remove the `_forATS` word in the file name.
For example, rename the `TMA_AX_DZ_CBT_0001_mapping_forATS.txt` to `TMA_AX_DZ_CBT_0001_mapping.txt`.
Note that you need to modify the **IP address** and **port** in **MainCabinet** section in the database by the TMA EUI as well.
Point the IP to the main cabinet simulator such as the numbered IP of `tma-windows.ls.lsst.org`.
Point the port to [TMA_AZ_CS_CBT_0001/ServerConfig.ini](https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets/blob/develop/configFiles/TMA_AZ_CS_CBT_0001/ServerConfig.ini).
After this, you need to reboot the ATS AUX PXI to read this new setting in the database.

![main cabinet ip and port](media/main_cabinet_settings_ip_and_port.png)

For the top-end chiller, the configuration files are in the [TEC](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/tree/develop/ESIFiles/TEC).
Note that for the ATS, you need to modify the `Address` and `Port` in [ServerConfig.ini](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/TEC/ServerConfig.ini).
The `Port` value is assigned in [main.py](https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller/blob/develop/src/topEndChillerSimulator/main.py) of [ts_tma_hil_simulator_top-end-chiller](https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller).

For the oil supply system (OSS), the configuration files are in the [OSS](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/tree/develop/ESIFiles/OSS).
Note that for the ATS, you need to modify the `Address` and `Port` in [ServerConfig.ini](https://github.com/lsst-ts/ts_tma_labview_pxi-controller/blob/develop/ESIFiles/OSS/ServerConfig.ini).
The `Port` value is assigned in [OSS_ServerConfig.ini](https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator/blob/develop/configFiles/OSS_ServerConfig.ini) of [ts_tma_hil_oil-supply-system_oil-supply-system-simulator](https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator).
When you try to power on the OSS, you might get the following error:

![OSS error](media/oss_error.png)

This is because the level variable is not published by the simulator, so you need to change the setting to be able to power on the OSS.
To do the OSS level warning/alarm deactivation, do:

![OSS error deactivation](media/oss_error_deactivation.png)

For the ATS AUX PXI, if it is a Beckhoff device as [aux-pxi](https://ts-tma.lsst.io/docs/tma_pxi-controller_documentation/80%20DeployOnTargets/02%20AUX%20PXI.html#aux-pxi), you can configure it to be a PXI by following: [after-installation-to-set-as-pxi](https://ts-tma.lsst.io/docs/tma_maintenance_ni-linux-rt-installation/NI-Linux-RT-Installation.html#after-installation-to-set-as-pxi).
Note you might need to use the following two commands instead for the instructions on the above link:

```bash
grub-editenv - set DeviceDesc=PXIe-8880_Beckhoff
grub-editenv - set hostname=ats_AUX-PXI
```

### Main Axes Interlocks

The main axes might be locked by interlocks, a very common one after a reboot is the Locking Pins (LP).

To fix the interlock for the Locking pins, extend and retract the deployable platforms to update the limits.

The initial condition is:

![Deployable platform initial condition](media/deployable_platform_initial.png)

Issue when trying to extend the deployable platforms:

![Deployable platform try to extend](media/deployable_platform_try_to_extend.png)

To fix it, you need to change the settings for the deployables or a better idea, fix the value of the inclinometer, currently set to -33 deg:

![Inclinometer -33 deg](media/inclinometer_neg_33.png)

Inclinometer value changed to 4.5 deg from the NI distribution manager:

![Inclinometer 4.5 deg](media/inclinometer_4_point_5.png)
![Inclinometer 4.5 deg view](media/inclinometer_4_point_5_view.png)

Resetting EL several times to get the value from the inclinometer:

![Resetting EL](media/resetting_EL.png)

Extending deployable platforms:

![Deployable platform extend](media/deployable_platform_extend.png)

Retracting the deployable platforms:

![Deployable platform retract](media/deployable_platform_retract.png)

The platforms does not reach the retracted limits, so you have to change the settings to reach them.

![Modify setting of deployable platform plus](media/modify_setting_deployable_platform_plus.png)
![Modify setting of deployable platform minus](media/modify_setting_deployable_platform_minus.png)

Then retract again until reaching the retracted limits.

![Deployable platform retract limit](media/deployable_platform_retract_limit.png)

Then power off the deployable platforms.
Then reset locking pins and retract them, send to free, they are already at free, but the limits are not updated, so you need to insert them and retract them, for doing this the fastest way is to disable the check that verifies the EL position.

Set the **disableElevationPositionCheck** to **TRUE**:

![Locking pins setting](media/locking_pins_setting.png)

Then, power on LPs, send them to Lock, then to free, then power Off LPs.

![Locking pins lock](media/locking_pins_lock.png)
![Locking pins clear](media/locking_pins_clear.png)

The locking pin interlocks were cleared, but there were still interlocks from the limits for AZ and EL

- AZ limit -
- EL limit -

![Safety system error 0](media/safety_system_error_0.png)

To clear these several things must happen:

1. The axis must be moved back, to a higher position, as this is a negative limit, for EL this was done to set it in a position suitable for the deployable platforms.
2. Make sure that the simulator stops setting the value to limit pressed, this means the axis must be within the limits for the axis, see settings.
3. The value for the safety encoder, in this case simulated with a variable, must be higher than the previously registered value, the value that had when the limit was tripped. To force this, there is a tool in the windows machine.
4. Finally reset from the safety window.

![Safety system error 1](media/safety_system_error_1.png)
![Safety system error 2](media/safety_system_error_2.png)
![Safety system error 3](media/safety_system_error_3.png)

### Deployable Platform and Locking Pins interlock relation

The *locking pin retracted* and *platform NO total extended* interlocks are not stored (this means that they will go away
automatically when the cause is no longer active), this is represented by *orange* color in the safety matrix window.

Here is how to remove the interlocks from the deployment platforms (DPs) by moving the locking pins (LPs):

1. Interlock active for the Deployable Platforms

   ![LP retracted and DP interlock 1](./media/lp_retracted_dp_interlock_1.png)

2. Power ON LPs
3. Move LPs to LOCK
4. Power OFF LPs

   ![LP retracted and DP interlock 2](./media/lp_retracted_dp_interlock_2.png)
   ![LP retracted and DP interlock 3](./media/lp_retracted_dp_interlock_3.png)

5. Reset DPs
6. Power ON DPs
7. Move DPs

   ![LP retracted and DP interlock 4](./media/lp_retracted_dp_interlock_4.png)

### Note of the Safety Matrix

You can see the details of safety matrix in [TMA IS Matrix](https://ts-tma.lsst.io/docs/tma_tma-is_safety-matrix/index.html).
You need to know that it's impossible to have a 100% clean interlock table (aka. no triggered interlock), as there are causes that are opposite, for example:

1. LPs, only have 3 options, all are covered by the table:

   - Inserted (LOCK)
   - Test intermediate position for balancing
   - Retracted (FREE)

2. DPs, have two options, and when one is not active the other will:

   - Platform NO parking, this is active when the platforms are not completely retracted
   - Platform NO total extended, this is active  until the platforms are completely extended

### Safety code deployment

The code that runs on the PILZ controller to simulate the behavior of the TMA IS. The source code and more
documentation about configuration can be found in
[this repo](https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus)

1. Open the *TestDualModbus* project with *PAS4000* version 1.18.0
2. Activate the *TestDualModbus*

  ![Activate project](./media/PasActivateProject.png)

3. Open the online network editor.

  ![Open network editor](./media/PasOpenNetworkEditor.png)

4. Scan project to scan the network to verify that the PILZ CPU is connected.

  ![Scan project](./media/ScanProject.png)

5. Close the online network editor
6. Download the project
    1. Open the Project downloader:

    ![Open project downloader](./media/PasOpenProjectDownloader.png)

    > If asked to build changes say YES
    >
    > ![Build changes](./media/PasBuildChanges.png)

    2. Start download:

    ![Start download](./media/PasStartDownload.png)

    3. Confirm download:

    ![Confirm download](./media/PasConfirmDownload.png)

    4. Download completed:

    ![Download complete](./media/PasDownloadComplete.png)

7. Logout:

  ![Logout](./media/PasLogOut.jpg)

8. Close the PAS4000

## Relevant considerations and miscellaneous

### Database

When setting up the ATS is important to have a separated database instance just for the ATS system, the backups for these
can be found [**here**](https://github.com/lsst-ts/ts_tma_ats_database-backup).

### Cabinet modbus temperature controllers

For the auxiliary cabinets temperature controllers the `Send reset` and `Reset value` settings are updated to *TRUE* and
*1* respectively, to act as a power on when sending the reset command. This means that each time the cabinets simulators
is booted, the cabinets temperature controllers would be off, until a reset command is sent to each of them.

> This is done with the `ManualReset` variable from the PXI which for the ATS is pointing to the `1016` register of the
> simulators, the power register.

![Auxiliary boxes settings](media/AuxiliaryBoxesSettings.png)

![Auxiliary boxes after sending a reset command](media/AuxiliaryBoxesEnabled.png)

After this, you need to do the followings to persist the change:

1. Stop all the Windows tools and simulators.
2. Reboot the ATS AUX PXI.
3. Reboot the ATS TMA PXI.
4. Reboot the ATS AUX PXI.

After each reboot before the step 4, if you run the Windows tools and simulators, you will see the connection issues of the auxiliary boxes and main cabinet.
Only after the step 4, you will not see the communication issues anymore and you should be good to enable (or reset) the auxiliary boxes from the EUI.

### Elevation inclinometer

The default value for the elevation inclinometer variable `TMA-EL-CS-CBT-0101-220A30_ElevationInclinometer` is set to
`10430` which means a position of `45.22500002` deg. This is done to have a valid EL position when powering on the EL
axis, this variable is not updated by any simulator, but it can be manually updated.

### EUI

The executable of the EUI for the ATS and the TMA are the same, the only difference is that the database, the PXIs and
the operation manager it targets must be different. This is why the ATS must use a different instance of the EUI than
the real TMA, for this we recommend using a different machine. The EUI can be installed from a RPM package found
[here](https://repo-nexus.lsst.org/nexus/#browse/search=keyword%3Dtma_eui)
