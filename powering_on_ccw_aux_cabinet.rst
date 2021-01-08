###########################
Powering On CCW Aux Cabinet
###########################

Below you will find useful instructions when working on CCW Auxiliary Cabinet.
Keep in mind this cabinet is only temporary to allow independent operation of the CCW from the other elements of the TMA.

.. _powering-on-ccw-aux-cabinet:

Turning on the CCW Aux Cabinet
==============================
	1. Plug in the CCW AUX cabinet power. This is a a red plug about 10cm in diameter.
	#. Turn the circular knob on the left of the cabinet to the "on" position.
	#. Wait 2 minutes.
	#. Restart the cRIO by pressing the reset button shown below.

	.. figure:: /_static/images/crio_reset_button.png
	    :name: crio_reset_button

	#. The cabinet is now powered on, which means the PC to operate the EUI is also powered on.

	.. note:: It may take about 2 to 3 minutes for the PC to power on.

Debugging the PILZ box
======================
Sometimes when resetting the interlocks on the CCW, the PILZ box does not reset properly.
You can check this by opening the power cabinet and looking for a row of red LEDs that indicate fault.
You can handle this by turning the pilz box on and off again.

1. Unplug the rightmost power cable in the row of power cables
2. Wait 5 seconds
3. Plug it in again
4. An array of green lights should come up

.. figure:: /_static/images/pilz_power_plug.jpg
	:name: pilz_power_plug

Power Cycling the PILZ box
==========================
If the PILZ box cannot communicate with the controller, the box will remain in fault.
A current work-around is to power cycle the box.

1. Unplug the rightmost power cable in the bottom row of power cables
2. Plug in the cable
3. The array of LEDs should be green

The real solution is to check the wiring.

.. figure:: /_static/images/pilz_power_cycle.jpg
	:name: pilz_power_cycle

Turning off the CCW Aux Cabinet
===============================
When finished with the CCW on the summit for an extended time on the summit, it is summit policy that the cabinet should be turned off.

1. Disable the drives by clicking :guilabel:`Off` under :guilabel:`Control`
#. Hit the e-stop on the side of the CCW auxiliary cabinet.
#. Close down the EUI by clicking in the top of the window manager :menuselection:`labview --> Quit`
#. A window will pop up that asks about saving, click :guilabel:`Don't save all and quit`
#. Turn off the computer in the top right of the window manager click the task bar and then the power icon then select :guilabel:`Shutdown`
#. Turn off the monitor on the back side click the knob and then down to shut off the monitor
#. Turn off the cabinet by throwing the power switch on the left side to ``Off``.
