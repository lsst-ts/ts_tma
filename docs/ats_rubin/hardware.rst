############
ATS Hardware
############

The ATS hardware closely matches the production equipment at the summit.
It combines real-time TMA, axes, and auxiliary controllers with a Speedgoat axis simulation target, encoder and safety interfaces, and an ESXi host for its supporting virtual machines.

.. list-table:: Hardware

   * - Name
     - Model
     - Description
     - Host Name
     - Operating System
   * - ATS TMA PXI
     - NI PXI-8880
     - Provides real time control over the various TMA subsystems.
     - ats-tma-pxi.ls.lsst.org
     - NI RT Linux 24
   * - ATS AXES PXI
     - NI PXI-8881
     - Provides real time control over the TMA AXES subsystem.
     - ats-axes-pxi.ls.lsst.org
     - NI RT Linux 24
   * - ATS AUX PXI
     - Beckhoff industrial slide in PC
     - Provides auxiliary subsystems to reduce load on TMA PXI
     - ats-aux-pxi.ls.lsst.org
     - NI RT Linux 24
   * - Speedgoat
     - Speedgoat Performance Target Machine
     - Provides AXES simulation model to PXI.
     - 
     - Matlab 2026
   * - EIB Tape Encoder
     - Heidenhain EIB 8791
     - Provides encoder data to the AXES PXI
     - 
     - 
   * - PILZ Safety System
     -
     - Provides safety signal to system.
     - 
     -
   * - ESXI VM host
     - 
     - Provides hypervisor based Virtual Machines
     -
     - VMWare ESXI
