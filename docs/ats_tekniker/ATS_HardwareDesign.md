# ATS Hardware Design

| Code          | Editor       |
| ------------- | ------------ |
| 3151_MCS_0050 | Julen Garcia |

## Introduction

This document explains the hardware configuration used for the automatic test system (ATS).

## Hardware configuration

In this section the needed hardware and its configuration is explained.

### Windows Machine

This is a Windows 10 machine where LabVIEW simulators and tools run.

The configuration of the hardware is:

- CPU: Intel i5-7500 @ 3.40GHz
- RAM: 8 GB
- Hard Drive: SSD 250 GB
- OS: Windows 10 Pro version 1909
- x2 Ethernet gigabit connection ports

### Speedgoat

The Speedgoat is a real time target machine used to simulate the main axes behavior.

The configuration of the hardware is:

- CPU: Intel i7-7700K @ 4.20GHz
- RAM: 4 GB
- Hard Drive: SSD 500 GB
- Input/Output modules:
  - Ethercat Slave module IO750 (x2)
  - Digital IOs module IO306
  - Analog IOs module IO131

### PILZ CPU

This is used to simulate and test the safety software.

The configuration of the hardware is:

- PILZ PSSu 4000 ref 314070
- PSSu E F 4DI-T
- PSSu E F 4DO 0.5-T

### Linux Machine

This is an Ubuntu 18.04 machine used to run the secondary axes simulators and execute the robot framework tests.

The configuration of the hardware is:

- CPU: Intel i5-750 @ 2.67GHz
- RAM: 4 GB
- Hard Drive: HHD 500GB
- x2 Ethernet gigabit connection ports

### Mount Control Computer (MCC)

This is a CentOS 7 machine which replicates the one in the server room at the summit in Chile. It runs the EUI
(Engineering User Interface), the database for the settings and events and the
[mtmount_operation_manager](https://github.com/lsst-ts/ts_tma_operation-manager_mt-mount-operation-manager).

The configuration of the hardware is:

- CPU: Intel i7-3770 @ 3.40 GHz
- RAM: 16 GB
- Hard Drive: HHD 500 GB
- OS: CentOS 7
- x2 Ethernet gigabit connection ports
  - Tekniker local and internet network
  - PXIs subnet

The configuration of the hardware for a newer OS version is:

- Non-NI hardware: DELL Precision 3660
- CPU: Intel i7-12700
- RAM: 16 GB
- Hard Drive: NVME 250 GB

### TMA PXI

The PXI that contains the state machines for all the main systems and the communication with the MCC and AXES PXI.

The configuration of the hardware is:

- Non-NI hardware: DELL Precision 3660
- CPU: Intel i7-12700
- RAM: 16 GB
- Hard Drive: NVME 250 GB

### AXES PXI

The PXI that contains the code for controlling the main axes, azimuth and elevation.

The configuration of the hardware is:

- Non-NI hardware: DELL Precision 3660
- CPU: Intel i7-12700
- RAM: 16 GB
- Hard Drive: NVME 250 GB

### AUX PXI

The PXI that contains the code for the temperature controllers and the OSS state machines.

The configuration of the hardware is:

- Non-NI hardware: DELL Precision 3660
- CPU: Intel i7-12700
- RAM: 16 GB
- Hard Drive: NVME 250 GB

### EIB 8791

The EIB is the encoder system used to monitor the heads of azimuth and elevation, same as in the summit, more info
[here](https://ts-tma.lsst.io/docs/tma_mcs-equipment-general-description/MCS_Equipment_General_Description.html#encoder-heidenhain-eib-8791)

### cRIO NI 9144

This *cRIO + 8 DIO Module NI 9401* are used to trigger the EIB, same as in the summit, more info
[here](https://ts-tma.lsst.io/docs/tma_mcs-equipment-general-description/MCS_Equipment_General_Description.html#crio-system)

### Ethernet Switches

TODO: review

#### Managed Switch

Netgear GS724Tv4 ProSafe 24-port Gigabit Ethernet Smart Switch.

##### Managed switch port configuration

| Ports   | VLAN |
|---------|------|
| 1 - 6   | 209  |
| 7 - 8   | 213  |
| 9 - 12  | 211  |
| 13 - 14 | 180  |

This is the main switch where the following items are connected:

- MCC (VLAN 209: for HMI data communication)
- TMA PXI (VLAN 209: for HMI data communication)
- TMA PXI (VLAN 213: for communication between the two PXIs)
- TMA PXI (VLAN 211: for communication with the EIB)
- AXES PXI (VLAN 213: for communication between the two PXIs)
- AXES PXI (VLAN 211: for communication with the EIB)
- EIB (VLAN 211: for communication with the EIB)

#### Unmanaged Switch

TODO: check and add

## Hardware connections diagram

TODO: update

Here the connections between the different hardware devices explained in this document are represented.

![ATS connections schematic](./media/ATS_ConnectionsSchematic.png)
