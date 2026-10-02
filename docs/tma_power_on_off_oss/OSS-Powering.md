<!-- This page was reviewed and edited by Jacqueline Seron on Oct 2026
Below the descriptions of changes I made
Separate to precondition section clearing the interlocks and oil tank level.
   changed the text in the link to contain the name of the page (instead of 'checked here')
    I added the link to the GIS page in obs-ops
2.1 typo in "the" in "read the message.."
2.2 QUESTION: where should we press reset in the OSS window or the Safety System window or both?
Added the link to the procedure when the OSS fails to turn on due to the chillers.
Added note on startup time

Other minot changes
-->

# OSS Powering ON/OFF

This document explains how and what to check for powering on and off the OSS.
<!-- The process can be followed in the OSS General view, it first ..... 
-->

## Powering on

### Preconditions 

 1. Clear all the interlocks that affect the OSS, these can be [checked in the TMA Safety Matrix](https://ts-tma.lsst.io/docs/tma_tma-is_safety-matrix/index.html)
      1. For clearing these, use the [Safety System window in the TMA EUI](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/034_SafetySystem.html)
      2.And if there is something from the GIS active, clear that on the [GIS](https://obs-ops.lsst.io/Safety/Safety-Systems/GIS.html#troubleshooting) 

 2. Access the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)
    
 3. Oil tank level should be at least 900mm.

> [!NOTE]
> The oil warning and alarm limits are set in the TMA EUI settings and may vary by season.

###Procedure

1. With the interlocks cleared, set the OSS to <code>AUTO</code> mode and <code>REMOTE</code> command by pressing those buttons.
   1. If it fails, read the message, it could be that something was not reseted properly or that something was tripped again. Press <code>RESET</code> and try again.
   2. If the interlock is still triggered contact Electronics Support.
   
2. Press the <code>ON</code> button, on the top of the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)

3. The system should power on.
   1. If the process fails, usually is due to problems in the cooling part, check the chillers and reset them if needed. Refer to [OSS Fails to turn on](https://obs-ops.lsst.io/Simonyi/Troubleshooting/MTCS/TMA/OSS-Fails-to-Turn-On.html).
   2. If the OSS does not power on, contact the electronics support.

 
> [!IMPORTANT] 
> OSS startup typically takes about 15 minutes but may take up to 35 minutes. If startup exceeds 35 minutes, contact Electronics Support.
>
> Startup status is displayed in the EUI OSS General View. The LEDs illuminate in the following sequence: 
> Cooling - Oil Circulation - Accumulator - Pump - Observation

## Powering off

### Precondition
OSS is ON

### Procedure
For powering off, this should be easier than the power on sequence.

1. Go to the [OSS General View window](https://ts-tma.lsst.io/docs/tma_eui-manual-english/02_Monitor%26Control/008_OSSGeneralView.html)
2. Press <code>OFF</code> on the top.
3. The OSS should be OFF after a couple of minutes.
