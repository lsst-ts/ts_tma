# Moving AZ and EL Axes

This document explains how and what to check for moving the AZ and EL axes.

## Preconditions

* [Power supply](https://ts-tma.lsst.io/docs/tma_power_on_off_powerSupply/PowerSupply-Powering.html) and [Oil Supply System](https://ts-tma.lsst.io/docs/tma_power_on_off_oss/OSS-Powering.html) are powered On
* NO active interlocks, clear them in:
  * The TMA IS: verify [Safety System window in the EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
  * The [GIS Main Control panel](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html) at Level 2.

## Move TMA AZ and EL

1. **Power on the axes**, this can be done from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
   1. Press <code>RESET ALARM</code>
   2. Press <code>ON</code>
3. **Home the axes**, for doing so, use the <code>HOME</code> button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
4. With the axes HOMED, the axes can be moved.
   1. Fill in the desired target position for both AZ and EL.
   2. (Optional) Fill in the desired **speed** for both AZ and EL, if not clear, **leave it to 0 to use the EUI default values**.
   3. (Optional) Fill in the desired **acceleration** for both AZ and EL, if not clear, leave it to 0 to use the EUI default values.
   4. (Optional) Fill in the desired **jerk** for both AZ and EL, if not clear, leave it to 0 to use the EUI default values.
   5. Press the <code>MOVE</code> button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html).
  
> **NOTE:** During motion no more actions can be done other than stopping the motion, for that use any of the STOP buttons from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html).
> **When the move is completed new moves can be executed**.
