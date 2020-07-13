*******************
Safety Interlocks
*******************

Below you will find useful instructions when working on the TMA Safety Interlocks.

Clearing Interlocks when Connected to SAL
=========================================
	1. Send clearerror. On a SAL publisher send the command "clearerror"
	#. Sieze Control. Go to main menu and select "GUI"
	#. Override the interlocks, go to the Safety menu and select "override interlocks"
	#. Clear the erros, go to the CCW and select "clear errors"
	#. Release overrides, go to Safety and select "realease ovverride"
	#. Relinquish Control, to to main menu and select "SAL"

Clearing Interlocks when NOT Connected to SAL
=============================================
1. Override the interlocks, go to the Safety menu and select "override interlocks"
2. Clear the erros, go to the CCW and select "clear errors"
3. Release overrides, go to Safety and select "realease ovverride"

Disconnecting the CCW Interlock Systems from Rotator
====================================================
	1. Familiarize yourself with the Safety Interlock Connections. One connection
	leads to the Rotator, the other connection is a standalone connection that is
	tied to the CCW Auxiliary Control Cabinet. Below circled in red are the connections.

	.. figure:: /_static/images/safety_interlock_connections.jpg
	    :name: safety_interlock_connections
	    :target: http://target.link/url

	2. Connect the Standalone Safety Interlock connector into the CCW Auxiliary
	Control Cabinet.

	3. Wire the removed Safety Interlock cable that is now only connected to the
	Rotator cabent as described below

	.. figure:: /_static/images/safety_interlock_standalone_interface.png
	    :name: safety_interlock_standalone_interface
	    :target: http://target.link/url


Connecting the CCW Interlock Systems to Rotator
===================================================