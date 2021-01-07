*************
Operating EUI
*************

Below you will find instructions for operating the EUI.


Operating EUI
=============
	#. Open a terminal window.
	
	.. prompt:: bash

		ulimit -s 100000
		cd /usr/local/natinst/LabVIEW-2018-64
		./labview

	#. Open the ``LSST_HMIs.lvproj`` under ``Recent Projects``.
	#. Go to :menuselection:`Main --> HMIMain_EUI.vi`
	#. Double click ``HMIMain_EUI.vi``
	#. Find any missing libraries in the 2018 path.
	#. Close any warning
	#. Log in using :ref:`HMI Credentials <hmi-login>`

	.. warning:: If SAL kernel crashes computer must be restarted


Resetting Interlocks
====================

1. Go to :menuselection:`Main Interface --> Safety System`
#. On the right-most top-most column of the interface underneath :guilabel:`Negative Pullcord` click :guilabel:`Reset`
#. Go to :menuselection:`Camera Cable Wrap`
#. On the right-most top-most column of the interface under :guilabel:`Control` click :guilabel:`Reset Alarm`
#. On the row below in the same column underneath :guilabel:`Cable Wrap Drive Selector` click :guilabel:`2`
#. You may see an error and timeout, this is fine repeat the step above
#. Then in the row above in :guilabel:`Control` click :guilabel:`On`

In the left-most column, underneath :guilabel:`Drive 2` it should say :guilabel:`Standstill` with a box :guilabel:`run/alarm` with the color green above it.

Changing Settings
=================

1. Go to :menuselection:`Settings --> Camera Cable Wrap Settings`
#. Locate the settings under the :guilabel:`Monitoring` column in the left-most top-most section.
#. Find the name of the setting you want to change under the :guilabel:`Name` column
#. Change the value in the :guilabel:`Value` column
#. In the column next to :guilabel:`Value` it should change to the color red for modified.
#. In the right-most top-most column under :guilabel:`Control` click :guilabel:`Write` under :guilabel:`Apply Changes temporarily`
#. In the column that changed to red it should become orange for written.
