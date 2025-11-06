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
- Required Input/Output modules:
  - Ethercat Slave module IO750 (x2)
  - Digital IOs module IO306

### PILZ CPU

This is used to simulate and test the safety software.

The configuration of the hardware is:

- PILZ PSSu 4000 ref 314070
- PSSu E F 4DI-T (not really in use at the moment)
- PSSu E F 4DO 0.5-T

### Linux VMs

There are two Debian 12 VMs for the ATS.

#### ATS Bosch Dockers

For running the secondary axis (bosch axis) simulators in docker containers, no graphical interface installed.

This has the following software installed:

- xe-guest-utilities -> for status reporting to the hypervisor
- git
- docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
- vim

VM hardware config:

- x4 cores
- 4 GB RAM
- 80 GB ROM

#### ATS Run Tests

For running the robot framework tests.

This has the following software installed:

- xe-guest-utilities -> for status reporting to the hypervisor
- git
- vim
- Python 3.11.2
- requirements from [here](https://github.com/lsst-ts/ts_tma_test_automatic-test-code/blob/develop/docs/Installation.md)
- KDE Plasma for graphical interface
- Remote desktop for running the tests

VM hardware config:

- x12 cores
- 16 GB RAM
- 80 GB ROM

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

The configuration of the hardware for a ALMA9 OS version is:

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

### cRIO NI 9145

This *cRIO + 8 DIO Module NI 9401* are used to trigger the EIB, same as in the summit, more info
[here](https://ts-tma.lsst.io/docs/tma_mcs-equipment-general-description/MCS_Equipment_General_Description.html#crio-system)

### Ethernet Switches and Connections

The setup in Tekniker uses 2 switches, a managed one and an unmanaged one.

```plantuml
@startuml network connections
nwdiag {
    tekniker_network [ shape = cloud, description = "Tekniker network"];
    tekniker_network -- wall_port
    network d_link {
      address = "10.1.22.0/24"
      description = "Unmanaged Switch"

      wall_port
      router [description = "WiFi router"]
      ats_mcc [description = "MCC CentOS 7"]
      alma [description = "MCC ALMA 9"]
      ats_win [description = "ATS Windows"]
      speedgoat [description = "Speedgoat config port"]
      csc [description = "CSC running PC"]
    }

    network netgear_209 {
        address = "192.168.209.0/24"
        description = "Managed Switch\nVLAN 209"
        
        ats_linux [ description = "Linux Machine"]
        ats_win [ description = "Windows Machine"]
        ats_mcc [ description = "MCC CentOS 7"]
        ats_tma [ description = "TMA PXI"]
        ats_aux [ description = "AUX PXI"]
    }

    network netgear_213 {
        address = "192.168.213.0/24"
        description = "Managed Switch\nVLAN 213"
        
        ats_tma [ description = "TMA PXI"]
        ats_axes [ description = "AXES PXI"]
    }

    network netgear_211 {
        address = "192.168.211.0/24"
        description = "Managed Switch\nVLAN 211"
        
        ats_tma [ description = "TMA PXI"]
        ats_eib [ description = "EIB"]
        ats_axes [ description = "AXES PXI"]
    }

    network netgear_180 {
        address = "192.168.180.0/24"
        description = "Managed Switch\nVLAN 180"
        
        ats_tma [ description = "TMA PXI"]
        ats_pilz [ description = "PILZ PSS 4000"]
    }

    network netgear_config {
        address = "192.168.0.0/24"
        description = "Managed Switch\nConfig"

        ats_win [ description = "Windows Machine"]
    }
}
@enduml
```

#### Managed Switch

Netgear GS724Tv4 ProSafe 24-port Gigabit Ethernet Smart Switch. Managed switch ports and VLAN configuration:

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

##### VLAN 209

```plantuml
@startuml vlan 209
nwdiag {
    network netgear_209 {
        address = "192.168.209.0/24"
        description = "Managed Switch\nVLAN 209"
        
        ats_linux [address = "port 1\n192.168.209.131" description = "Linux Machine"]
        ats_win [address = "port 2\n192.168.209.130" description = "Windows Machine"]
        ats_mcc [address = "port 3\n192.168.209.200" description = "MCC CentOS 7"]
        ats_tma [address = "port 4\n192.168.209.10" description = "TMA PXI"]
        ats_aux [address = "port 5\n192.168.209.11" description = "AUX PXI"]
    }
}
@enduml
```

##### VLAN 213

```plantuml
@startuml vlan 213
nwdiag {
    network netgear_213 {
        address = "192.168.213.0/24"
        description = "Managed Switch\nVLAN 213"
        
        ats_tma [address = "port 7\n192.168.213.10" description = "TMA PXI"]
        ats_axes [address = "port 8\n192.168.213.11" description = "AXES PXI"]
    }
}
@enduml
```

##### VLAN 211

```plantuml
@startuml vlan 211
nwdiag {
    network netgear_211 {
        address = "192.168.211.0/24"
        description = "Managed Switch\nVLAN 211"
        
        ats_tma [address = "port 9\n192.168.211.10" description = "TMA PXI"]
        ats_eib [address = "port 10\n192.168.211.1" description = "EIB"]
        ats_axes [address = "port 11\n192.168.211.11" description = "AXES PXI"]
    }
}
@enduml
```

##### VLAN 180

```plantuml
@startuml vlan 180
nwdiag {
    network netgear_180 {
        address = "192.168.180.0/24"
        description = "Managed Switch\nVLAN 180"
        
        ats_tma [address = "port 13\n192.168.180.100" description = "TMA PXI"]
        ats_pilz [address = "port 14\n192.168.180.10" description = "PILZ PSS 4000"]
    }
}
@enduml
```

##### Switch config

```plantuml
@startuml switch config
nwdiag {
    network netgear_config {
        address = "192.168.0.0/24"
        description = "Managed Switch\nConfig"

        ats_win [address = "port 23\n192.168.0.50" description = "Windows Machine"]
    }
}
@enduml
```

#### Unmanaged Switch

D-Link DGS-1024D 24 ports Gigabit Ethernet Switch for local network access, this connects to the local network in Tekniker.

```plantuml
@startuml network connections
nwdiag {
    tekniker_network [ shape = cloud, description = "Tekniker network"];
    tekniker_network -- wall_port
    network d_link {
      address = "10.1.22.0/24"
      description = "Unmanaged Switch"

      wall_port [address = "port 1"]
      router [address = "port 3" description = "WiFi router"]
      ats_mcc [address = "port 9\n10.1.22.39" description = "MCC CentOS 7"]
      alma [address = "port 10\n10.1.22.67" description = "MCC ALMA 9"]
      ats_win [address = "port 11\n10.1.22.158" description = "ATS Windows"]
      speedgoat [address = "port 12\n10.1.22.211" description = "Speedgoat config port"]
      csc [address = "port 13" description = "CSC running PC"]
    }
}
@enduml
```

## Electrical connections

The setup for the ATS is very simple compared to the real one, but there are a couple of connections anyway.

```plantuml
@startuml
rectangle axes_pxi as "AXES PXI"
rectangle crio as "cRIO NI 9145"
rectangle Speedgoat
rectangle EIB
rectangle PILZ as "PILZ PSS 4000"

axes_pxi <--> crio #red
crio <-> Speedgoat #red

crio --> EIB #blue :trigger eib\nreadings
PILZ --> Speedgoat #blue : manage model\nbrakes from PILZ

' set legend to have a white background
skinparam legendBackgroundColor #FFFFFF
' remove box around legend
skinparam legendBorderColor #FFFFFF
' remove the lines between the legend items
skinparam legendEntrySeparator #FFFFFF

legend right
'   the <#FFFFFF,#FFFFFF> sets the background color of the legend to white
    <#FFFFFF,#FFFFFF>|<#red>| ethernet connection, for ethercat communication |
    ' the space between the | and <#blue> is important to make the color column wider
    |<#blue>     | 24v connection, for digital signals |
endlegend
@enduml
```

### Ethercat line device order

AXES PXI -> cRIO 9145 -> Speedgoat IO750 -> Speedgoat IO750(2)

### Digital signals

Speedgoat IO306 card -> module with the 24V signals from the PILZ

[**More details see images here**](#pilz-and-speedgoat-connections)

## Hardware configuration at Tekniker

### Speedgoat modules

![SpeedgoatCards](./media/SpeedgoatCards.jpg)

### Pilz And Speedgoat Connections

![PilzAndSpeedgoatConnections](./media/PilzAndSpeedgoatConnections.jpg)

![PilzAndSpeedgoatConnectionsDetail_1](./media/PilzAndSpeedgoatConnectionsDetail_1.jpg)

![PilzAndSpeedgoatConnectionsDetail_2](media/PilzAndSpeedgoatConnectionsDetail_2.jpg)

![PilzAndSpeedgoatConnectionsDetail_3](media/PilzAndSpeedgoatConnectionsDetail_3.jpg)

![PilzAndSpeedgoatConnectionsDetail_4](media/PilzAndSpeedgoatConnectionsDetail_4.jpg)

![PilzAndSpeedgoatConnectionsDetail_5](media/PilzAndSpeedgoatConnectionsDetail_5.jpg)
