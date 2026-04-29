<!-- This page was reviewed and edited by Jacqueline Seron
Below the descriptions of changes I made
Separate to precondition section clearing the interlocks 
   changed the text in the link to contain the name of the page (instead of 'checked here')
    I added the link to the GIS page in obs-ops
2.1 typo in "the" in "read the message.."
2.2 QUESTION: where should we press reset in the OSS window or the Safety System window or both?
Added the link to the procedure when the OSS fails to turn on due to the chillers.
I'll talk to electronics so it contains what is the range of how long it can take to power on. also maybe add if we need to check something else like the Oil level...

-->
# OSS Powering ON/OFF

This document explains how and what to check for powering on and off the OSS.
<!-- The process can be followed in the OSS General view, it first ..... 
-->

## Preconditions 
 Clear all the interlocks that affect the OSS, these can be [checked in the TMA Safety Matrix](https://ts-tma.lsst.io/docs/tma_tma-is_safety-matrix/index.html)
   1. For clearing these use the [Safety System window in the TMA EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
   2. And if there is something from the GIS active, clear that on the [GIS](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html#troubleshooting) 

## Powering on

1. With the interlocks cleared, try setting the OSS to by pressing <code>AUTO</code> mode.
   1. If it fails, read the message, it could be that something was not reseted properly or that something was tripped again. Press <code>RESET</code> and try again.
   2. If this persists contact the electronics team.
2. Once in AUTO mode press the <code>ON</code> button, the one on the very top of the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)
3. . The system should power on.
   1. If the process fails, usually due to problems in the cooling part, check the chillers and reset them if needed. Refer to [OSS Fails to turn on](https://obs-ops.lsst.io/Simonyi/Troubleshooting/MTCS/TMA/OSS-Fails-to-Turn-On.html).
   2. If the issue persists contact the electronics team.

<!--  
> [!NOTE] 
> The time it takes to power ON the OSS varies according to ambient temperature. Normally when temperatures are not moderate it takes about 15 minutes, if it takes longer it means there could be an issue. 
-->

## Powering off

For powering off, this should be easier than the on sequence.

1. Go to the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)
2. Press <code>OFF</code> on the top.
3. The OSS should be OFF after a couple of minutes.
