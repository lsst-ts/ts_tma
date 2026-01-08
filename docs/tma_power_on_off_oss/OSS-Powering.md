# OSS Powering ON/OFF

This document explains how and what to check for powering on and off the OSS.

## Powering on

<!-- This page was reviewed and edited by Jacqueline Seron
Below the descriptions of changes I made 
Step 1 I changed the text in the link to contain the name of the page (instead of here)
Step 1.2 I added the link to the GIS page in obs-ops
2.1 typo in "the" in "read the message.."
2.2 QUESTION: where should we press reset in the OSS window or the Safety System window or both?
I'll talk to electronics so it contains what is the range of how long it can take to power on. also maybe add if we need to check something else like the Oil level...
-->
1. Clear all the interlocks that affect the OSS, these can be [checked in the TMA Safety Matrix](https://ts-tma.lsst.io/docs/tma_tma-is_safety-matrix/index.html)
   1. For clearing these use the [Safety System window in the EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
   2. And if there is something from the GIS active, clear that on the [GIS](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html#troubleshooting) 
2. With the interlocks cleared, try setting the OSS to AUTO mode
   1. If it fails, read the message, it could be that something was not reseted properly or that something was tripped again. Press reset and try again
   2. If this persists contact the electronics team.
3. Once in AUTO press the ON button, the one on the very top of the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)
4. The system should power on
   1. If the process fails, usually due to problems in the cooling part, check the chillers and reset them if needed
   2. If this persists contact the electronics team.

## Powering off

For powering off, this should be easier than the on sequence.

1. Go to the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html) and press OFF on the top
2. The OSS should be OFF
