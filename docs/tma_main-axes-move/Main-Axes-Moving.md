<!-- This page was reviewed by Danica, who mentioned missing final periods.
A second revision and edited by Jacqueline Seron
Below the descriptions of changes I made 
Added preconditions and removed what was in the steps (currently it's commented), this is:
"For powering on the axis, the corresponding interlocks must be cleared, this can be done from the [Safety System window in the EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
   2. And if there is something from the GIS active, clear that on the GIS and then come back to the EUI safety window "
Made some sentences shorter, higlighted some words.
Transform the last 2 points into a note. 
-->

# Moving AZ and EL Axes

This document explains how and what to check for moving the AZ and EL axes.

## Preconditions:
* Power supply and Oil Supply System are power On
* NO active interlocks, clear them in:
   *   The TMA IS: verify [Safety System window in the EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
   *   The [GIS Main Control panel](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html) 

## Move TMA AZ and EL

1. **Power on the axes**, this can be done from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
   1. Press <code>RESET ALARM</code>
   2. <code>ON</code> 
3. **Home the axes**, for doing so, use the <code>HOME</code> button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
4. With the axes HOMED, the axes can be moved.
   1. Fill in the desired target position for both AZ and EL.
   2. (Optional) Fill in the desired **speed** for both AZ and EL, if not clear, **leave it to 0 to use the EUI default values**.
   3. (Optional) Fill in the desired **acceleration** for both AZ and EL, if not clear, leave it to 0 to use the EUI default values.
   4. (Optional) Fill in the desired **jerk** for both AZ and EL, if not clear, leave it to 0 to use the EUI default values.
   5. Press the <code>MOVE</code> button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html).
  
> **NOTE:** During motion no more actions can be done other that stopping the motion, for that use any of the STOP buttons from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html). **When the move is completed new moves can be executed**.
