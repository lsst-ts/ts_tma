############
ATS Software
############

The ATS software ecosystem is primarily implemented in LabVIEW and C++.
It includes TMA control and HMI applications, real-time simulation models, subsystem simulators, communications tools, safety software, and Robot Framework automated tests.

.. list-table:: lsst-ts ATS repositories
   :header-rows: 1

   * - Title
     - Summary
     - Repository location
   * - ts_tma_gis_modbus-comm-only
     - This project has the code necessary to test GIS modbus communication using the ATS hardware
     - `https://github.com/lsst-ts/ts_tma_gis_modbus-comm-only <https://github.com/lsst-ts/ts_tma_gis_modbus-comm-only>`_
   * - ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator
     - This repo contains the simulator for the Phase Power Supply.
     - `https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator <https://github.com/lsst-ts/ts_tma_hil_bosch-power-supply_bosch-power-supply-simulator>`_
   * - ts_tma_hil_cabinet-temperature-controller_cabinets
     - This repo contains the simulator for the Temperature Controlled Cabinets.
     - `https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets <https://github.com/lsst-ts/ts_tma_hil_cabinet-temperature-controller_cabinets>`_
   * - ts_tma_hil_deployable-platform-extensions-simulator
     - This repo contains the simulator for the safety locks that lock into place the Deployable Platforms extensions.
     - `https://github.com/lsst-ts/ts_tma_hil_deployable-platform-extensions-simulator <https://github.com/lsst-ts/ts_tma_hil_deployable-platform-extensions-simulator>`_
   * - ts_tma_hil_force-ethercat-vars
     - This repo contains the tool developed to force the ethercat variables from the ATS.
     - `https://github.com/lsst-ts/ts_tma_hil_force-ethercat-vars <https://github.com/lsst-ts/ts_tma_hil_force-ethercat-vars>`_
   * - ts_tma_hil_main-axes_lsst-hil
     - This repository contains the simulink code that simulates the main axes of the LSST telescope. The code has been developed to run in a speedgoat system
     - `https://github.com/lsst-ts/ts_tma_hil_main-axes_lsst-hil <https://github.com/lsst-ts/ts_tma_hil_main-axes_lsst-hil>`_
   * - ts_tma_hil_main-axes_main-axis-model-manager-python
     - This project contains a python interface to manage the speedgoat using a custom made tool instead of Matlab.
     - `https://github.com/lsst-ts/ts_tma_hil_main-axes_main-axis-model-manager-python <https://github.com/lsst-ts/ts_tma_hil_main-axes_main-axis-model-manager-python>`_
   * - ts_tma_hil_main-axes_slrt-binaries-for-speedgoat
     - This repo contains the binaries generated for the speedgoat.
     - `https://github.com/lsst-ts/ts_tma_hil_main-axes_slrt-binaries-for-speedgoat <https://github.com/lsst-ts/ts_tma_hil_main-axes_slrt-binaries-for-speedgoat>`_
   * - ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator
     - This repo contains the simulator for the thermal control of the Azimuth and Elevation motors.
     - `https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator <https://github.com/lsst-ts/ts_tma_hil_motor-thermal-model_motor-thermal-model-simulator>`_
   * - ts_tma_hil_network-shared-variables-simulation
     - The cde at this repository is used to deploy the network shared variables (NSVs) needed for entering the simulation mode at the EUI.
     - `https://github.com/lsst-ts/ts_tma_hil_network-shared-variables-simulation <https://github.com/lsst-ts/ts_tma_hil_network-shared-variables-simulation>`_
   * - ts_tma_hil_oil-supply-system_oil-supply-system-simulator
     - This repo contains the simulator for the Oil Supply System (OSS).
     - `https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator <https://github.com/lsst-ts/ts_tma_hil_oil-supply-system_oil-supply-system-simulator>`_
   * - ts_tma_hil_phase-power-supply_phase-power-supply-simulator
     - This repo contains the simulator for the Phase Power Supply.
     - `https://github.com/lsst-ts/ts_tma_hil_phase-power-supply_phase-power-supply-simulator <https://github.com/lsst-ts/ts_tma_hil_phase-power-supply_phase-power-supply-simulator>`_
   * - ts_tma_hil_read-variables
     - This repo contains the tool developed to read/write Network Shared Variables using TCP.
     - `https://github.com/lsst-ts/ts_tma_hil_read-variables <https://github.com/lsst-ts/ts_tma_hil_read-variables>`_
   * - ts_tma_hil_read-variables-tek-nsv
     - This repo contains the tool developed to read/write TekNSV (Network shared Variables equivalent developed by Tekniker) using TCP.
     - `https://github.com/lsst-ts/ts_tma_hil_read-variables-tek-nsv <https://github.com/lsst-ts/ts_tma_hil_read-variables-tek-nsv>`_
   * - ts_tma_hil_secondary-axis_generatedsecnodaryaxismodel
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_secondary-axis_generatedsecnodaryaxismodel <https://github.com/lsst-ts/ts_tma_hil_secondary-axis_generatedsecnodaryaxismodel>`_
   * - ts_tma_hil_secondary-axis_secondary-axis-sil-binaries
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondary-axis-sil-binaries <https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondary-axis-sil-binaries>`_
   * - ts_tma_hil_secondary-axis_secondary-axis-sil-python-interface
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondary-axis-sil-python-interface <https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondary-axis-sil-python-interface>`_
   * - ts_tma_hil_secondary-axis_secondaryaxissil
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil <https://github.com/lsst-ts/ts_tma_hil_secondary-axis_secondaryaxissil>`_
   * - ts_tma_hil_silinterface
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_silinterface <https://github.com/lsst-ts/ts_tma_hil_silinterface>`_
   * - ts_tma_hil_simulate-limits
     - This repo contains the tool developed to simulate the hardware limits of the telescope.
     - `https://github.com/lsst-ts/ts_tma_hil_simulate-limits <https://github.com/lsst-ts/ts_tma_hil_simulate-limits>`_
   * - ts_tma_hil_simulator_top-end-chiller
     - This is a very simple simulator for the TMA top end chiller.
     - `https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller <https://github.com/lsst-ts/ts_tma_hil_simulator_top-end-chiller>`_
   * - ts_tma_hil_simulators-start-stop-scripts
     - This repo contains the scripts for starting/stopping the ATS simulators.
     - `https://github.com/lsst-ts/ts_tma_hil_simulators-start-stop-scripts <https://github.com/lsst-ts/ts_tma_hil_simulators-start-stop-scripts>`_
   * - ts_tma_hil_speedgoat_speedgoat-manager
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager <https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager>`_
   * - ts_tma_hil_speedgoat_speedgoat-manager-binaries
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager-binaries <https://github.com/lsst-ts/ts_tma_hil_speedgoat_speedgoat-manager-binaries>`_
   * - ts_tma_hil_tcp-modbus-bridge
     - This repo contains a project that makes a bridge from TCP to modbus.
     - `https://github.com/lsst-ts/ts_tma_hil_tcp-modbus-bridge <https://github.com/lsst-ts/ts_tma_hil_tcp-modbus-bridge>`_
   * - ts_tma_hil_test-dual-modbus
     - This repo contains the safety code for the ATS safety system running on the PILZ.
     - `https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus <https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus>`_
   * - ts_tma_hil_thermal-model_generated-thermal-model
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_thermal-model_generated-thermal-model <https://github.com/lsst-ts/ts_tma_hil_thermal-model_generated-thermal-model>`_
   * - ts_tma_hil_thermal-model_thermal-model
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model <https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model>`_
   * - ts_tma_hil_thermal-model_thermal-model-dll
     - —
     - `https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model-dll <https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model-dll>`_
   * - ts_tma_hil_thermal-model_thermal-model-in-labview
     - Labview library to simulate a thermal model based on a heat exchanger
     - `https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model-in-labview <https://github.com/lsst-ts/ts_tma_hil_thermal-model_thermal-model-in-labview>`_
   * - ts_tma_hil_tools_tcp-communication-tool
     - LabVIEW library which contains code to interact with ReadVariables and ForceEtherCAT tools
     - `https://github.com/lsst-ts/ts_tma_hil_tools_tcp-communication-tool <https://github.com/lsst-ts/ts_tma_hil_tools_tcp-communication-tool>`_
   * - ts_tma_test_automatic-test-code
     - Code for TMA automatic tests. The test framework used is Robot Framework
     - `https://github.com/lsst-ts/ts_tma_test_automatic-test-code <https://github.com/lsst-ts/ts_tma_test_automatic-test-code>`_
   * - ts_tma_test_lsst-bridge
     - —
     - `https://github.com/lsst-ts/ts_tma_test_lsst-bridge <https://github.com/lsst-ts/ts_tma_test_lsst-bridge>`_
   * - ts_tma_test_testing-procedures
     - This repo contains the testing software procedures files in docx.
     - `https://github.com/lsst-ts/ts_tma_test_testing-procedures <https://github.com/lsst-ts/ts_tma_test_testing-procedures>`_

.. list-table:: Repos related to ATS
   * - Title
     - Summary
     - Repository location
   * - ts_tma_labview_hmi-computers
     - This repo contains the code for the HMI, both the EUI and the HHD.
     - https://github.com/lsst-ts/ts_tma_labview_hmi-computers
   * - ts_tma_labview_pxi-controller
     - This repo contains the code for the PXI real-time controller.
     - https://github.com/lsst-ts/ts_tma_labview_pxi-controller
     