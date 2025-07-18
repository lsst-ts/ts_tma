# Main Axes Limits

## Limits operation as per specifications (NOT HOW THEY ACTUALLY WORK)

Notice that the proposed behavior for limits, the one that forces the telescope to stop close to the defined limits, is
quite strange and if applied the overall behavior of the system will not be the desired one.

With the proposed limits design, if the CSC commands a position out of moving boundaries, and the system just tries to
go to that position, but a limit is applied as in the specifications, the steps shown below will happen:

1. The command is sent by the CSC
2. The TMA accepts the command
3. The TMA starts moving
4. The TMA stops moving close to the limit, but far from the requested position in step 1
5. The TMA sends and *inPosition* event. But the TMA is not in the desired position. The *inPosition* event compares the
   *rms* error from the trajectory generator and the actual position for the last values. The CSC commanded position is
   not used to send the *inPosition* event, because the *inPosition* is calculated every 1 ms instead of every 50ms.

## Actual limits implementation

Tekniker thought that the behavior explained in the previous section is not wanted for the TMA. So Tekniker implemented
a more classic limit approach, as an implementation like the one proposed by Rubin could be very difficult to implement.
If the idea is just to force the command value coming from the EUI or CSC to valid ones it is quite easy, but the strange
behavior explained in the previous section will occur. On the other hand, if the CSC needs feedback to know that the
command is accepted but the end position is forced (limited) to a valid one, then the communication between TMA and CSC
must be updated.

At this moment, these are the limits available in the system:

- **Command Acceptance Limit:** this is the limit for accepting or rejecting a command, if the TMA gets a position
  command outside this *Command Acceptance Limit*, it will answer with a *Rejected* response, meaning that the movement
  is not going to be executed. So, the CSC easily knows that there is something wrong with the commanded position. On the
  contrary, if the command is accepted, the telescope will "always" stop inside the limits in a controlled way.
  "Always", meaning if nothing goes wrong, this is, most of the cases. The telescope rarely hits any of the limits
  explained later or finishes in another position that is not the commanded one. The values for the maximum and minimum
  allowable positions are settings, that can be managed by the user. In addition, there are limits for these settings,
  to avoid absurd values.
  TODO: poner los nombres de los settings
- **Software Fixed Limit Position:** this is a software limit that will trip if the axis (Az/El) position is exceeds the
  defined limit value. When tripped, the limit will cause the axis (Az/El) to stop in fault mode, but using the motors
  with the defined acceleration (deceleration). These limits (positive and negative) can be managed using the settings.
  TODO: poner los nombres de los settings
- **Limit Switches:** these are electromechanical limit switches, activated when the telescope reaches a fixed position.
  If the telescope presses one of these electromechanical switches, the axis will be stopped in fault mode using the motors.
  The elevation *Operational Limit Switches* work in the same way and have been working reliably. These limits are connected
  to the TMA PXI I/O ethercat modules.
  > The Limit Switches for both axes are physically too close the *Power Off Limit Switches* (about 0.1 deg), this margin
  > is not enough to stop the TMA without overcoming the maximum allowed accelerations, so these limits will work only
  > at very low speeds.
  TODO: poner settings para habilitarlos/deshabilitarlos ??
- **Power Off Limit Switches:** these are electromechanical limit switches, activated when the telescope reaches a
  fixed position. These electromechanical switches are managed by the safety system (TMA IS). When a
  *Power Off Limit Switch* is pressed the safety system disables the torque in the drives (safe torque off or STO is
  applied) and applies the brakes. So, the stopping distance and acceleration depends on the brakes capability at that
  moment.
  > When for an error the TMA reaches one of these limits, an override is needed and teh TMA must be moved back far enough
  > to clear it
- **Hard Stop Limit:** this is a mechanical hard limit for when everything else fails. It is a mechanical stop
  system with a damping device. The telescope should reach the *Hard Stop Limit* without power in the drives, as the
  *Power Off Switches* will be pressed before reaching here. To reach these limits in normal operation several failures
  must occur in the telescope at the same time: the software is not responding to actual position, the brakes must be
  not working properly, and this must happen close to the limit and at full speed.



TODO: 








First, I would like to notice that the proposed behavior for limits, the one that makes the telescope to stop close to
the limits, is quite strange and if applied the overall behavior of the system will not be the desired one.

If the CSC commands a position out of moving boundaries, and the system just tries to go to that position, but a limit
is applied as in the specifications, the steps shown below will happen:

1.      The command is sent by CSC
2.      The TMA accepts the command
3.      The TMA starts moving
4.      The TMA stops moving close to the limit
5.      The TMA sends and *inPosition* event. But the TMA is not in the desired position. The *inPosition* event compares the rms error from the trajectory generator and the actual position for the last values. The CSC commanded position is not used to send the *inPosition* event, because the *inPosition* is calculated every 1 ms instead of every 50ms.

We, Tekniker, think that this behavior is not wanted in the CSC.
Depending on the implementation you want, it could be very difficult to implement. If the idea is just to force the command value coming from the EUI or CSC to valid ones it is quite easy, but the strange behavior explained before is there. If the CSC needs feedback to know that the command is accepted but the end position is forced to a valid one, then the communication between TMA and CSC must be updated.
At this moment, these are the limits available in the system:
- Command Acceptance Limit. The maximum/minimum allowable position is a setting, that can be managed by the user. Also, there are limits for this setting, to avoid absurd values. These settings limits do not allow to put a setting value outside them. If the TMA gets a position command outside this Command Acceptance Limit, it will answer with a Rejected response meaning that the movement is not going to be executed. So, the CSC easily knows that there is something wrong with the commanded position. If the command is accepted, the telescope will “always” stop inside the limits in a controlled way. Always = if nothing goes wrong, this is, most of the cases. The telescope rarely hits any of the limits explained later or finished in another position that is not the commanded one.
- Software Fixed Limit Position. If this position is exceeded the axis will stop in fault mode but using the motors with the programmed acceleration. These limits can be managed using the settings.
- Limit Switches. If the telescope presses one of these electromechanical switches, the axis will be stopped in fault mode using the motors. The elevation Operational Limit Switches work in the same way and have been working reliably. The Limit Switches of both axes are physically too close the Power Off Limit Switches (about 0.1 deg) and they would work only with a very low speed.
- Power Off Limit Switches. These electromechanical switches are managed by the safety system (TMA IS). When a Power Off Limit Switch is pressed the safety system disables the torque in the drives (safe torque off or STO) and applies the brakes. So, the stopping distance and acceleration depends on the brakes capability at that moment.
- Hard Stop Limit. This is the last mechanical limit. It is a mechanical system with a damping device. The telescope should reach the Hard Stop Limit without power in the drives, as the Power Off Switches will be pressed before reaching here. To reach these limits in normal operation several failures must occur in the telescope at the same time. The software is not responding to actual position, and the brakes must be not working properly, and this must happen close to the limit and at full speed.

So, with these limits available this is the actual behavior of TMA

![alt text](resources/LimitsStateSequence.png)

* Not always sent. The '*inPosition*' status is sent after a slew, but with tracking commands, the telescope remains *inPosition*. The 'Done' response is only sent for point-to-point movements..

The proposed position of the limits for azimuth should be something similar to figure shown bellow. This figure is also valid for elevation when the parking settings are applied, since Operational limit switches are disabled.

![alt text](resources/LimitsDiagramWithoutOperationalLimitSwitch.png)

For elevation limits, the operational limit switch is included in the graph

![alt text](resources/LimitsDiagramWithOpeartionalLimitSwitch.png)

The distance between Software Fixed Limit and the active limit switch can be approached using this formula (it is 10% more than the movement necessary to stop the axis traveling at maximum programmed speed using the maximum programmed acceleration with infinite jerk)
S=1.1*(3/2*Vmax^2/Amax)

The telescope's healthy movement is tracked by various limits and checks, including those for overspeed, following error, and extrapolation time (time without new tracking commands).

Furthermore, limits for speed, acceleration, and jerk, similar to the command acceptance limit, prevent any command with a value exceeding these defined bounds from being accepted.
