# ATS Software Design

| Code          | Editor       |
| ------------- | ------------ |
| 3151_MCS_0052 | Julen Garcia |

## Introduction

This document shows the software structure for the ATS.

## Technical description

The simulation software is divided into different elements according to their nature. In this way all similar elements have
a simulation software that can be configured to meet the specific telescope element represented. For example, all drives
for auxiliary axes are simulated by one software that runs with several instances each with a different configuration.
Each simulation software will is explained in [this section](#simulation-software-modules).

Those simulation software modules need some communication tools to exchange data with the real controller. Those
elements are tools that will be explained [here](#tools).

For axes simulators we found two different solutions:

- For main axis, high speed simulation is needed and then a HIL solution with a specific hardware, Speedgoat, is used.
  This is explained [here](#main-axes-simulator).
- For auxiliary axes, the simulation is based on a software simulation with a less demanding timing, running on a Linux
  (Ubuntu) machine, [see](#secondaryaxissil).

Tests are programmed in robot framework and they run on the Linux machine.

In figure below the general overview of all elements is shown. The simulators are running in a windows machine, except
all axes simulators.

```plantuml
@startuml ATS Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
  component secondary_axis_sil <<simulator>>
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node EIB <<realTmaHardware>>
node cRIO <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node speedgoat <<simulationHardware>> {
  component MainAxes_sim <<simulator>>
  component EIB_sim <<simulator>>
  component Drives_sim <<simulator>>

  MainAxes_sim -[#Black]-> EIB_sim
  MainAxes_sim -[#Black]-> Drives_sim
}

node WindowsMachine <<simulationHardware>> {
  interface LocalNSV
  component ReadTMA_PXI_NSV_tool <<tool>>
  ' component ForceEthercat_tool <<tool>> 'no longer in use TODO: remove from limits simulator
  component ReadAXES_PXI_NSV_tool <<tool>>
  component ReadLocal_NSV_tool <<tool>>
  component TekNSV_tool <<tool>>
  component BoschPowerSupply_simulator <<simulator>>
  component MotorThermal_simulators <<simulator>>
  component MainPowerSupply_simulator <<simulator>>
  component Limits_simulator <<simulator>>
  component ModbusTemperature_simulators <<simulator>>
  component DeployableExtensions_simulator <<simulator>>
  component OSS_simulator <<simulator>>
  component SpeedgoatManager <<tool>>
  component TopEndChiller_simulator <<simulator>>

  LocalNSV <-u[#Blue]-> ReadLocal_NSV_tool
  LocalNSV <-u[#Blue]-> BoschPowerSupply_simulator
  LocalNSV <-u[#Blue]-> MotorThermal_simulators
  LocalNSV <-u[#Blue]-> MainPowerSupply_simulator
  LocalNSV <-u[#Blue]-> Limits_simulator
  LocalNSV <-u[#Blue]-> ModbusTemperature_simulators
  LocalNSV <-u[#Blue]-> DeployableExtensions_simulator
  LocalNSV <-u[#Blue]-> OSS_simulator

  ReadTMA_PXI_NSV_tool <-[#Blue]--> BoschPowerSupply_simulator
  ReadTMA_PXI_NSV_tool <-[#Blue]--> ModbusTemperature_simulators
  ReadTMA_PXI_NSV_tool <-[#Blue]--> MotorThermal_simulators
  ReadTMA_PXI_NSV_tool <-[#Blue]--> MainPowerSupply_simulator
  ReadTMA_PXI_NSV_tool <-[#Blue]--> Limits_simulator

  TekNSV_tool <-[#Blue]--> OSS_simulator
  TekNSV_tool <-[#Blue]--> MotorThermal_simulators
  TekNSV_tool <-[#Blue]--> MainPowerSupply_simulator
  TekNSV_tool <-[#Blue]--> DeployableExtensions_simulator
  TekNSV_tool <-[#Blue]--> Limits_simulator

  ReadAXES_PXI_NSV_tool <-[#Blue]-> MotorThermal_simulators

}

' RobotFramework <--> ReadLocal_NSV_tool
' RobotFramework <--> EUI
' RobotFramework <--> SpeedgoatManager
' RobotFramework <--> secondary_axis_sil
' RobotFramework <--> ReadTMA_PXI_NSV_tool

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool

AXES_PXI <-[#Red]-> EIB_sim
AXES_PXI <-[#Red]-> Drives_sim
AXES_PXI <-[#Red]-> cRIO
AXES_PXI <-[#Orange]-> ReadAXES_PXI_NSV_tool

secondary_axis_sil <-[#Green]-> TMA_PXI
Safety_Controller <-[#Green]-> TMA_PXI

AUX_PXI <-[#Green]--> OSS_simulator
AUX_PXI <-[#Green]--> ModbusTemperature_simulators
AUX_PXI <-[#Green]--> TopEndChiller_simulator

SpeedgoatManager <-[#Black]u-> speedgoat

Safety_Controller -[#DarkTurquoise]-> speedgoat
cRIO -[#DarkTurquoise]-> EIB

@enduml
```

### Simulation software modules

In this section all the simulation software modules are explained. This simulation modules are designed to test a
software component in the real controller. A software component can be tested using the full system with the controllers
for both PXIs or just a small VI with only the required software modules. This test vi is indicated in each simulation
software module.

#### Network Shared Variables Simulator (deprecated, no longer in use)

This module generates random data in the NSV that the EUI reads to make it work even without any code in any of the two
PXIs. Data used only for telemetry is generated by this module when the code is running the PXIs. This is the case of
temperature and pressure of ducts for instance. No software test is related with simulation module.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_network-shared-variables-simulation) for the simulation module
more information can be found.

![Network Shared variables simulator interactions](./media/NSV_sim_deprecatedModule.png)

#### Limit simulator (Limits_simulator)

This module simulates the behavior of the hardware limits that are wired to the IOs module. Since there are not
physical limits the limits are simulated reading the position of the elements. The limit simulator reads data directly
from the TMA-PXI using the TekNSV interface and then uses the tool for reading/writing NSV to the TMA PXI
to write the network shared variables, that are used instead of ethercat variables in simulation mode. The safety
variables that are implemented as TekNSV variables are written with the TekNSV interface.

This module is not valid by itself to test any control module. This is used with other simulators to test the complete
behavior of a subsystem. For instance, locking pins needs the auxiliary axes simulators to simulate the position of the
locking pins and this module with the configuration for locking pins to simulate when the limit switches are pressed or
released.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_simulate-limits) for the simulation module more information
can be found.

```plantuml
@startuml Limits_simulator modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
  component secondary_axis_sil <<simulator>>
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component ReadTMA_PXI_NSV_tool <<tool>>
  component TekNSV_tool <<tool>>
  component Limits_simulator <<simulator>>

  ReadTMA_PXI_NSV_tool <-[#Blue]--> Limits_simulator

  TekNSV_tool <-[#Blue]--> Limits_simulator

}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool

secondary_axis_sil <-[#Green]-> TMA_PXI
Safety_Controller <-[#Green]-> TMA_PXI
@enduml
```

#### Temperature simulator over TCP (MotorThermal_simulators)

This module simulates the thermal behavior of the Phase Drives and the TMA_AZ_CS_CBT_0001 cabinet. This module uses the
ReadWrite three instances.

- The instance to read and write NSVs from the Axes PXI allows to simulate the temperature of the motors
- The instance to read and write NSVs from the TMA PXI allows to simulate the temperature of the TMA_AZ_CS_CBT_0001 cabinet.
- The instance to read and write TekNSVs allows to TODO: check

In the [repository](https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator) for the
simulation module more information can be found.

```plantuml
@startuml MotorThermal_simulators Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node speedgoat <<simulationHardware>>

node WindowsMachine <<simulationHardware>> {
  component ReadTMA_PXI_NSV_tool <<tool>>
  component ReadAXES_PXI_NSV_tool <<tool>>
  component TekNSV_tool <<tool>>
  component MotorThermal_simulators <<simulator>>

  ReadTMA_PXI_NSV_tool <-[#Blue]--> MotorThermal_simulators

  TekNSV_tool <-[#Blue]--> MotorThermal_simulators

  ReadAXES_PXI_NSV_tool <-[#Blue]-> MotorThermal_simulators
}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool

AXES_PXI <-[#Red]-> speedgoat
AXES_PXI <-[#Orange]-> ReadAXES_PXI_NSV_tool

@enduml
```

#### Temperature controllers for cabinets (ModbusTemperature_simulators)

This simulator is designed to simulate the temperature behavior in the main cabinet and other cabinets managed by a
temperature controller. This temperature controller is a standalone controller that uses modbus to send/receive data
from the AUX PXI controller.

This module needs the ReadTMA_PXI_NSV_tool module that reads the simulated ethercat variables.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets) for the simulation
module more information can be found.

```plantuml
@startuml ModbusTemperature_simulators Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component ReadTMA_PXI_NSV_tool <<tool>>
  component ModbusTemperature_simulators <<simulator>>

  ReadTMA_PXI_NSV_tool <-[#Blue]--> ModbusTemperature_simulators
}

TMA_PXI <-[#Fuchsia]u-> EUI
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool

AUX_PXI <-[#Green]--> ModbusTemperature_simulators
@enduml
```

#### SecondaryAxisSil (secondary_axis_sil)

This simulator is designed to simulate the behavior of the auxiliary axes (bosch axes). This simulator is implemented
in docker. There is a docker instance of the same docker image for each axis, each of them with the corresponding
configuration.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil) for the simulation
module more information can be found.

```plantuml
@startuml secondary_axis_sil Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
  component secondary_axis_sil <<simulator>>
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

TMA_PXI <-[#Fuchsia]u-> EUI
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI

secondary_axis_sil <-[#Green]-> TMA_PXI
@enduml
```

#### Safety simulator (Safety_Controller)

This simulator is designed to simulate the behavior of the TMA IS. The simulator is implemented in PILZ code, as well
as the TMA IS, the difference with the real TMA IS is that the simulator instead of using real IOs wired to the
controller, the value for this IOs comes over Modbus from the TMA PXI. There are only a couple of digital outputs to
send the STO and brakes to the Speedgoat.

This module needs the TekNSV_tool module that read the safety variables hosted in the TMA PXI to simulate inputs for
the Safety simulator, such us limits or ETPBs. This allows the tests to force limits or simulate ETPB being pressed.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus) for the simulation
module more information can be found.

```plantuml
@startuml Safety_Controller Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node speedgoat <<simulationHardware>>

node WindowsMachine <<simulationHardware>> {
  component TekNSV_tool <<tool>>
}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI

Safety_Controller <-[#Green]-> TMA_PXI
Safety_Controller -[#DarkTurquoise]-> speedgoat
@enduml
```

#### OSS simulator (OSS_simulator)

This simulator is designed to simulate the behavior of the Oil Supply system. The simulator is implemented in LabVIEW
code. This simulator, as the real OSS, implements a modbus server to send/receive data from the AUX PXI controller.

This module needs an instance of the TekNSV_tool module to read the safety variables hosted in the TMA PXI to
simulate inputs from the Safety simulator. The local variables at the windows machine are specific of this simulator and
are used to simulate faults.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator) for the simulation
module more information can be found.

```plantuml
@startuml OSS_simulator Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component TekNSV_tool <<tool>>
  component OSS_simulator <<simulator>>

  TekNSV_tool <-[#Blue]--> OSS_simulator
}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI

AUX_PXI <-[#Green]--> OSS_simulator

Safety_Controller <-[#Green]-> TMA_PXI
@enduml
```

#### Phase Power Supply simulator (MainPowerSupply_simulator)

This simulator is designed to simulate the behavior of the Phase Power Supply. The simulator is implemented in LabVIEW
code. This simulator manages the variables that correspond to the power supply to simulate its behavior.

This module needs an instance of the TekNSV_tool module and the ReadTMA_PXI_NSV_tool module to read the ethercat variables
hosted in the TMA PXI to simulate inputs from the power supply. The local variables at the windows machine are specific
of this simulator and are used to simulate faults.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_phase-power-supply_phase-power-supply-simulator) for the simulation
module more information can be found.

```plantuml
@startuml MainPowerSupply_simulator Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component ReadTMA_PXI_NSV_tool <<tool>>
  component TekNSV_tool <<tool>>
  component MainPowerSupply_simulator <<simulator>>

  ReadTMA_PXI_NSV_tool <-[#Blue]--> MainPowerSupply_simulator
  TekNSV_tool <-[#Blue]--> MainPowerSupply_simulator
}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool

@enduml
```

#### Bosch Power Supply simulator (BoschPowerSupply_simulator)

This simulator is designed to simulate the behavior of the Bosch Power Supply. The simulator is implemented in LabVIEW
code. This simulator manages the variables that correspond to the power supply to simulate its behavior.

This module needs an instance of the ReadTMA_PXI_NSV_tool module that read the simulated ethercat variables hosted in the
TMA PXI to simulate inputs from the power supply. The local variables at the windows machine are specific of this
simulator and are used to simulate faults.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator) for the simulation
module more information can be found.

```plantuml
@startuml BoschPowerSupply_simulator Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component ReadTMA_PXI_NSV_tool <<tool>>
  component BoschPowerSupply_simulator <<simulator>>

  ReadTMA_PXI_NSV_tool <-[#Blue]--> BoschPowerSupply_simulator
}

TMA_PXI <-[#Fuchsia]u-> EUI
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI
TMA_PXI <-[#Orange]-> ReadTMA_PXI_NSV_tool
@enduml
```

#### Deployable Extensions simulator (DeployableExtensions_simulator)

This simulator is designed to simulate the behavior of the deployable platforms extensions locks. To do so, this
simulator manages the digital inputs that tell the Safety system the status of the extensions of the deployable
platforms locks.

This module needs the TekNSV_tool module that reads/writes the Safety variables hosted in the TMA PXI to simulate
inputs from the hardware that locks/unlocks the deployable extensions.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_deployable-platform-extensions-simulator) for the simulation
module more information can be found.

```plantuml
@startuml DeployableExtensions_simulator Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node WindowsMachine <<simulationHardware>> {
  component TekNSV_tool <<tool>>
  component DeployableExtensions_simulator <<simulator>>

  TekNSV_tool <-[#Blue]--> DeployableExtensions_simulator
}

TMA_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Fuchsia]-> TekNSV_tool
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI

Safety_Controller <-[#Green]-> TMA_PXI
@enduml
```

#### Main axes simulator (MainAxes_sim)

This simulator is designed to simulate the mechanical behavior of Azimuth and Elevation. The simulator is implemented in
matlab code and runs in the speedgoat. This simulator uses the Encoder and Drives simulators.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_main-axes_lsst-hil) for the simulation module more information
can be found.

```plantuml
@startuml MainAxes_sim Modules
skinparam component {
  BackgroundColor<<simulator>> White
  BackgroundColor<<tool>> Pink
  BackgroundColor<<realTmaSoftware>> AliceBlue
}

skinparam node {
  BackgroundColor<<simulationHardware>> NavajoWhite
  BackgroundColor<<realTmaHardware>> SkyBlue
}

skinparam legend {
  BackgroundColor #GhostWhite
}

legend right
    | Color | Communication type |
    | <#Green> | Modbus |
    | <#Red> | Ethercat |
    | <#Blue> | Custom TCP |
    | <#Orange> | Network Shared Variables (NSV) |
    | <#Purple> | Network Streams |
    | <#DarkTurquoise> | Digital IOs |
    | <#Black> | Unknown (HW Specific) |
    | <#Fuchsia> | TekNSV |
endlegend

node MCC <<realTmaHardware>> {
  component EUI <<realTmaSoftware>>
  component MtMount_OperationManager <<realTmaSoftware>>

  EUI <-l[#Blue]-> MtMount_OperationManager
}

node LinuxMachine <<simulationHardware>> {
  component RobotFramework
}

node TMA_PXI <<realTmaHardware>>
node AUX_PXI <<realTmaHardware>>
node AXES_PXI <<realTmaHardware>>

node EIB <<realTmaHardware>>
node cRIO <<realTmaHardware>>

node Safety_Controller <<realTmaHardware>>

node speedgoat <<simulationHardware>> {
  component MainAxes_sim <<simulator>>
  component EIB_sim <<simulator>>
  component Drives_sim <<simulator>>

  MainAxes_sim -[#Black]-> EIB_sim
  MainAxes_sim -[#Black]-> Drives_sim
}

node WindowsMachine <<simulationHardware>> {
  component SpeedgoatManager <<tool>>
}

TMA_PXI <-[#Fuchsia]u-> EUI
AUX_PXI <-[#Fuchsia]u-> EUI
TMA_PXI <-[#Purple]-> AXES_PXI

AXES_PXI <-[#Red]-> EIB_sim
AXES_PXI <-[#Red]-> Drives_sim
AXES_PXI <-[#Red]-> cRIO

Safety_Controller <-[#Green]-> TMA_PXI

SpeedgoatManager <-[#Black]u-> speedgoat

Safety_Controller -[#DarkTurquoise]-> speedgoat
cRIO -[#DarkTurquoise]-> EIB
@enduml
```

##### Phase Drives simulator (Drives_sim)

This simulator is designed to simulate the behavior of the Phase Drives for Azimuth and Elevation. The simulator is
implemented in matlab code and runs in the speedgoat. This simulator manages the variables that correspond to the drives
to simulate their behavior.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_main-axes_lsst-hil) for the simulation
module more information can be found.

##### Encoder simulator (EIB_sim)

This simulator is designed to simulate the behavior of the Encoder system for Azimuth and Elevation. The simulator is
implemented in matlab code and runs in the speedgoat. This simulator is different from the real EIB, here instead of
publishing the position over UDP it is done over ethercat to tell the axes pxi the actual position of the Azimuth and
Elevation axes, as implementing the simulated communication in ethercat was easier than recreating the UDP communication
from the real EIB.

In the [repository](https://github.com/lsst-ts/ts_tma_hil_main-axes_lsst-hil) for the simulation
module more information can be found.

