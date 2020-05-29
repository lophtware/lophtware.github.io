# I<sup>2</sup>C Behaviour
The [PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf) device allows communication over
I<sup>2</sup>C as both _Master_ and _Slave_, and the default firmware supplied with the USB C / PIC32 Breakout Board allows both modes of operation.

In _Master_ mode the I<sup>2</sup>C bus will be controlled by the device, which in turn will be controlled by the Host interacting with the
[I<sup>2</sup>C Interface of the USB Module](../UsbDeviceModel/I2c/Interface.md).

In _Slave_ mode the I<sup>2</sup>C bus will be controlled by another device on the bus and the MCU can be accessed in a way similar to EEPROMs and sensors,
but will still ultimately be controlled by the Host using the [I<sup>2</sup>C Interface of the USB Module](../UsbDeviceModel/I2c/Interface.md).

## I<sup>2</sup>C Master Mode
In Master mode the device drives the signal lines of the I<sup>2</sup>C bus to communicate with another device, the Slave.  An I<sup>2</sup>C bus uses a
shared data line and so can only transmit in a _half-duplex_ manner, ie. sending _or_ receiving bits rather than sending _and_ receiving simultaneously.  A
typical I<sup>2</sup>C transaction between a Master and Slave follows the sequence:
1. Master claims the bus by sending a 'start' bit.
2. Master sends the Slave's unique address with a 'write' bit, followed by one or more bytes for the address of a register.
3. Master sends another 'start' bit, which allows it to restart communication (in a different direction) without releasing its claim on the bus.
4. Master sends the Slave's unique address, this time with a 'read' bit.
5. Slave sends bits to the bus for the Master to clock them in.
6. Master sends a 'stop' bit to release its claim on the bus and allow other Masters to communicate if they wish.

The Host can initiate such a transaction by sending commands like
[I<sup>2</sup>C - Half-Duplex Transfer; 0-7 Bytes Out, 0+ Bytes In](../UsbDeviceModel/I2c/Reports/0x80.md) via the USB interface.  The firmware takes care of
sending the data to the relevant Slave and forwarding the reply data back to the Host.

## I<sup>2</sup>C Slave Mode
In Slave mode another device on the I<sup>2</sup>C bus acts as a Master to drive the signal lines and communicate with the device.  There does not need to be
an enumerated USB connection or even a data-capable Host attached for this mode of operation, although if there is then it is also possible for the Host to
communicate with Masters by using the device's memory buffers as intermediate storage, ie. the [I<sup>2</sup>C RAM Bank](RamBank.md).  Some details pertinent
to Slave operation are given below.

### Clock Stretching
The [PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf) device has hardware support for
the I<sup>2</sup>C electrical / wire protocol but relies on firmware for interpreting and handling the generated events.  Because of firmware overheads the
device will generally not be able to respond within a single clock period, especially at faster I<sup>2</sup>C clock speeds.  The I<sup>2</sup>C protocol
caters for this scenario by allowing Slave devices to hold the clock line low whilst they are busy.  The Master devices must recognise this condition and not
try to alter the bus state during this time.

Since the factory-supplied firmware leverages clock stretching, any I<sup>2</sup>C Masters on the bus must also support clock stretching otherwise the
integrity of the bus will be compromised.  If Masters on the bus are not able to support clock stretching whilst addressing the PIC32 then the clock speed
will need to be reduced to the point that it does not occur.  This only applies to I<sup>2</sup>C transactions that are addressed to the PIC32 device.

### Addressing
The default I<sup>2</sup>C bus address of the device for slave is `0x31`.  The device maintains an internal 16-bit address pointer which is made up of a
6-bit bank number (`bbbbbb`) and a 10-bit offset into the bank (`aa aaaaaaaa`).  The address is sent in Big Endian order to keep with the established
de-facto conventions of I<sup>2</sup>C EEPROMs:

| Address MSB   | Address LSB |
|---------------|-------------|
| `bbbbbb` `aa` | `aaaaaaaa`  |

All I<sup>2</sup>C writes are preceeded by the 2-byte address, which sets the address pointer.  A write that has no data bytes is allowed and serves the
explicit purpose of setting the address pointer.  Writes of length zero or one byte will be ignored as they have no meaning.

Each byte written to, or read from, the device will cause an increment of the address pointer.  When the offset part of the address pointer reaches `1023`
(`0x03ff`) then the next increment will cause the offset part to wrap around to `0`.  Reads or writes cannot occur across bank bounderies.

The memory banks provided by the slave are:

| Bank Number (Binary)               | Bank Number (Decimal)         | Type | Description                                   |
|:----------------------------------:|:-----------------------------:|------|-----------------------------------------------|
| [000000](RamBank.md)               | [0](RamBank.md)               | R/W  | One kilobyte of Random Access Memory (RAM).   |
| [000001](RomBank.md)               | [1](RomBank.md)               | R/W  | One kilobyte of Flash Read-Only Memory (ROM). |
| [000010](DeviceInformationBank.md) | [2](DeviceInformationBank.md) | R    | Device Information.                           |
| [010011](UsbInterfaceBank.md)      | [19](UsbInterfaceBank.md)     | R/W  | USB Interface Status and Control.             |
| [010100](I2cInterfaceBank.md)      | [20](I2cInterfaceBank.md)     | R/W  | I<sup>2</sup>C Interface Status and Control.  |

### USB Transaction Notifications
It is possible to receive notifications of Slave transactions via USB - see the [Slave Report Configuration](../UsbDeviceModel/I2c/Reports/0x0a.md) command.
The purpose of the transaction notifications is to facilitate using the RAM and ROM banks as a buffer for transferring data between the Host and an
I<sup>2</sup>C Master.
