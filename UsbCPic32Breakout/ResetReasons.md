# MCU Device Reset Reasons
The Microcontroller's `RCON` register contains details of the most recent reset / power-on event and is exposed via the
[USB](UsbDeviceModel/Core/Reports/0x02.md) and [I<sup>2</sup>C](I2c/DeviceInformationBank.md) interfaces.  See the
[PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf) datasheet for details on how
to interpret this register.

Note that if _bit 15_ is set (`0x00008000`) then the reset reason can be interpreted as a firmware-induced reset rather than a hardware-based fault event.
The reasons the firmware can cause a reset are:

| Code       | Reason                      | Description                                                                                                                   |
|------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 0x8XXX8XXX | Safe Mode Indicator         | The device probably requires re-flashing if you get this.  It's limping along with a default configuration (tri-stated pins). |
| 0xX0008001 | General Exception Handler   | See the _MCU Exception Details_ section below for extra debugging information.                                                |
| 0xX0008041 | Free RTOS Assertion Failure | Basically a firmware bug.  Difficult to track down without a debugger.                                                        |
| 0xX0008042 | Free RTOS Stack Overflow    | Basically a firmware bug.  Difficult to track down without a debugger.                                                        |
| 0xX0008043 | Memory Allocation Error     | Basically a firmware bug.  Difficult to track down without a debugger.                                                        |
| 0xX0008080 | Configuration Updated       | Configuration has been updated successfully and the device reset.                                                             |
| 0xX000808X | Configuration Failure       | Some sort of configuation issue, possibly Flash corruption.  The exact number depends on the assertion in `Configuration.c`.  |

During some resets, snapshots of the Microcontroller's `ERROREPC`, `EPC`, `CAUSE`, `DESAVE` and `RA` registers are also captured and are exposed.

## MCU Exception Details
For MCU general exceptions as well as FreeRTOS assertion, malloc and stack overflow failures, the MCU's `ERROREPC`, `EPC`, `CAUSE`, `DESAVE` and `RA` registers
are persisted through the reset to allow retrieval for debugging.  The values of the registers immediately before the reset can be retrieved via the
[I<sup>2</sup>C Device Information Bank](I2c/DeviceInformationBank.md) or with the [USB Device Status](UsbDeviceModel/Core/Reports/0x02.md) command, presuming
the system manages to boot that far.
