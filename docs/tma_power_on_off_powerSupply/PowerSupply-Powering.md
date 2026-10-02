# Power Supply Powering ON/OFF

This document explains how and what to check for powering on and off the Power Supply.

## Precondition

* Clear all the interlocks that affect the Power Supply, [check the TMA Safety Matrix](https://ts-tma.lsst.io/docs/tma_tma-is_safety-matrix/index.html).
For clearing these use the [Safety System window in the TMA EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
* Clear any active interlocks in the [GIS main panel](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html#troubleshooting), on Level 2.



## Powering on
1. With the interlocks cleared, press the <code>ON</code> button, located very top of the [Power Supply window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/018_PowerSupply.html).
2. The system should power on.
   1. If the process fails, usually due to problems in the fuses, check the fuses status in the [Capacitor Banks TMA EUI view](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/019_CapacitorBanks.html), if needed check in situ on Level 7 under the TMA.
   2. If this persists contact the electronics team.

## Powering off

For powering off, this should be easier than the on sequence.

1. Go to the [Power Supply window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/018_PowerSupply.html)
2. Press <code>OFF</code> on the top.
3. The Power Supply should be OFF.


<!-- First review from Paulo L: Good to go, no changes needed
-->
<!-- Second review from Jacqueline S: Good to go
Separated step 1 as precondition
instead of '.. here' to 'Safety Matrix'
Minor changes to the text
Added link to GIS troubleshooting section.
Replaced: check the fuses for any broken ones with 'check the fuses status in [Capacitor bank TMA EUI view](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/019_CapacitorBanks.html), if needed check in situ on Level 7 under the TMA.' 
-->
