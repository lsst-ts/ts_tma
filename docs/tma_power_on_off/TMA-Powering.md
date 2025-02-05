# TMA Powering ON/OFF

This document explains how and what to check for powering off and on the TMA.

## Powering on

The system is designed to be always on. When power is restored after a power outage or manually turned off, all the systems
will power on automatically. Even though, there are components/elements that need to be checked after such event, as
things don't always reach the desired state on their own when this kind of events occur.

1. Ensure that all the elements in the main cabinets are ON, if these cabinets are ON, it can be assumed that the rest
   of the auxiliary cabinets for each system are ON too.
   1. Level 8
      1. Azimuth Main Cabinet TMA-AZ-CS-CBT-0001
      2. Phase Main Cabinet TMA-AZ-DR-CBT-0001
   2. Level 1
      1. OSS Main Cabinet
2. Check the PXIs state
   1. Log into the 3 PXIs (TMA, AUX and AXES) and check that all the software modules started properly, use command `labviewmessages`. For
      more details about these logs check the [training from September - 2024](https://ts-tma.lsst.io/docs/tma_training/2024%20-%20Training%20September.html)
   2. If there is anything wrong with any of the PXIs during powering, a reboot should fix it, but check the error
      description and do the checks from next step before rebooting anything.
3. Check the ethercat lines IOs and Drives, follow the guide to check
   [EtherCAT lines IOs and Drives are working properly](https://ts-tma.lsst.io/docs/tma_maintenance_ethercat_manage-ethercat-line-status/Manage-EtherCAT-Line-Status.html).
   If the ethercat lines are giving problems, refer to
   [this guide for recovering it](https://ts-tma.lsst.io/docs/tma_maintenance_ethercat_ethercat-line-diagnostic/EtherCAT-Line-Diagnostic.html)

   > Remember that the TMA has 2 ethercat lines, one for the drives and one for the IO signals and the power supply

> At this point if there are no errors in the PXIs using the `labviewmessages` command in each of them, and the ethercat
> lines are OK, the system should be ready.

4. Check each system
   individually using the EUI.

   - Ensure that the **safety system** is working, reset the active causes in the TMA IS using the EUI
   - Ensure that the **thermal systems** are working, by setting them to tracking ambient (drives, cabinets, top end chiller)
   - Ensure that the **auxiliary bosch systems** are working, a power on and off without errors should be enough
     - Locking Pins
     - Deployable Platforms
     - Cable Wraps (CCW, ACW)
     - Fine Balancing
     - Mirror Covers (with locks)
   - Ensure that the **power supply** can be powered on
   - Ensure that the **OSS** can be powered on
   - Ensure that **AZ** and **EL** can be powered on and off
   - Ensure that the **power supply** and **OSS** can be powered off

## Powering off

For powering off, this should be easier than the on sequence.

1. Make sure that all the state machines in the TMA are in *Idle* state, off (except the main cabinet temperature controller)
   1. Power supply
   2. OSS
   3. CCW
   4. Locking Pins
   5. Deployable Platforms
   6. Balancing
   7. Mirror Cover and cover locks
   8. AZ
   9. EL
   10. AZ drives thermal control
   11. EL drives thermal control
2. Power off the PXIs, this is not mandatory, but is a good idea. This can be done by press and holding the power button
   on the PXIs.
3. Remove power from the main cabinet (TMA-AZ-CS-CBT-0001)

> With this procedure, the control part of the MCS for the TMA would be off, but not the OSS, main power supply or other
> systems, that are not covered by this guide
