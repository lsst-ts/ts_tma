##############
ATS Deployment
##############

This covers deployment of the Rubin ATS software to the Rubin ATS hardware.

TMA PXI
#######

Need to install NI RT Linux system firmware.
Need to add configuration files to the PXI.

1. Clone the https://github.com/lsst-ts/ts_tma_labview_pxi-controller repo and setup any submodules.
#. Open the `TMA` project
#. Open main VI.
#. Save All
#. Save All project
#. Close LabVIEW
#. Clear build cache (Doesn't work in LabVIEW 24q3, need custom VI to do so)
#. Close LabVIEW again.
#. Build target
#. Deploy to target

AXES PXI
########
1. Clone the https://github.com/lsst-ts/ts_tma_labview_pxi-controller repo and setup any submodules.
#. Open the `AXES` project
#. Open main VI.
#. Save All
#. Save All project
#. Close LabVIEW
#. Clear build cache (Doesn't work in LabVIEW 24q3, need custom VI to do so)
#. Close LabVIEW again.
#. Build target
#. Deploy to target

AUX PXI
#######
1. Clone the https://github.com/lsst-ts/ts_tma_labview_pxi-controller repo and setup any submodules.
#. Open the `AUX` project
#. Open main VI.
#. Save All
#. Save All project
#. Close LabVIEW
#. Clear build cache (Doesn't work in LabVIEW 24q3, need custom VI to do so)
#. Close LabVIEW again.
#. Build target
#. Deploy to target

PILZ
####
1. Clone the test dual modbus project via - `https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus <https://github.com/lsst-ts/ts_tma_hil_test-dual-modbus>`_
#. Open the PAS4000 IDE.
#. Open the project via username and password (provided via 1password vault)
#. Create a backup file
#. Open the backup file
#. Build and deploy to the Pilz.

EIB
###

