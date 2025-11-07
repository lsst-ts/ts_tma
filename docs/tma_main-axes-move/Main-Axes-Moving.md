# Moving AZ and EL Axes

This document explains how and what to check for moving the AZ and EL axes.

## Move

1. Power on the axes, this can be done from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
   1. For powering on the axis, the corresponding interlocks must be cleared, this can be done from the [Safety System window in the EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
   2. And if there is something from the GIS active, clear that on the GIS and then come back to the EUI safety window
2. With the axes ON, the next step is to home the axes, for doing so, use the HOME button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
3. With the axes HOMED, the axes can be moved.
   1. Fill in the desired target position for both AZ and EL
   2. (optional) fill in the desired speed for both AZ and EL, if not clear, leave it to 0 to use the EUI default values
   3. (optional) fill in the desired acceleration for both AZ and EL, if not clear, leave it to 0 to use the EUI default values
   4. (optional) fill in the desired jerk for both AZ and EL, if not clear, leave it to 0 to use the EUI default values
   5. Press the MOVE button from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
   6. During motion no more actions can be done other that stopping the motion, for that use any of the STOP buttons from the [Main Axis General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/001_MainAxisGeneralView.html)
4. When the move is completed new moves can be executed.
