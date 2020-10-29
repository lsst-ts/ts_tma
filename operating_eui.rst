*************
Operating EUI
*************

Below you will find instructions for operating the EUI.


Operating EUI
=============
	1. Complete :ref:`powering-on-ccw-aux-cabinet`
	#. Log into the CCW Aux PC using the credentials :ref:`ccw-aux-pc-login` 
	#. Open a terminal window.
	#. Execute ``ulimit -s 100000``.
	#. Navigate to Labview 2018 ``cd /usr/local/natinst/LabVIEW-2018-64``.
	#. Start Labview 2018 ``./labview``.
	#. Open the EUI Main project.
	#. Find any missing libraries in the 2018 path.
	#. Close any warning

	.. warning:: If SAL kernel crashes computer must be restarted
