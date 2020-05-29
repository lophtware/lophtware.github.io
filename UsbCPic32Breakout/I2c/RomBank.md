# I<sup>2</sup>C ROM Bank
One kilobyte of Flash Read-Only Memory (ROM).  This is non-volatile storage.  It will not, however, be preserved if the device firmware is re-flashed.  The
[ROM Contents](../UsbDeviceModel/I2c/Reports/0x1e.md) command on the [USB's I<sup>2</sup>C Interface](../UsbDeviceModel/I2c/Interface.md) can be used to
re-initialise the ROM contents in this scenario.

*Note that this ROM is more akin to _EPROM_ rather than Flash or EEPROM.  Each bit in the array can be programmed from its erased state of `1` to `0`, but any
bits that are `0` cannot be made back into `1` without the ROM array being re-flashed.  Re-flashing can only be done via the USB interface.  This limitation
is necessary because the PIC only allows flash to be erased in 2048 byte pages, and this operation stalls the device for many milliseconds.*

Addresses in the range `[0, 1023]` (`[0x000, 0x3ff]`) can be read and written by devices on the I<sup>2</sup>C bus.  By default, all addresses are read-only as
you'd expect, but an address mask can be configured via the [Protected ROM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x0c.md) command on the
[USB's I<sup>2</sup>C Interface](../UsbDeviceModel/I2c/Interface.md) to change this.

Prior to writing, the write-protect function must be disabled by issuing a [ROM Bank Write-Protect Flag (Slave)](../UsbDeviceModel/I2c/Reports/0x0e.md) command
on the [USB's I<sup>2</sup>C Interface](../UsbDeviceModel/I2c/Interface.md) or by modifying the registers in the [I<sup>2</sup>C Interface Bank](I2cInterfaceBank.md).
If the write-protect flag has not been disabled then any writes into this bank will be ignored and will not be persisted into the non-volatile storage area.
The write-protect flag does not allow writes into addresses protected by the _Protected ROM Address Mask_.  Attempting to convert a bit from a `0` to a `1` will
also be ignored, as mentioned above.

Writing to the Flash is done 8 bytes at a time.  Eight bytes are buffered, and on writing the ninth byte the data is committed to the non-volatile storage
whilst the I<sup>2</sup>C clock is held low (stretched).  The write operation takes about 64us, and when it is completed the ninth byte becomes the first
byte in the buffer for the next write operation.  Since the
[PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf) requires that all flash writes are
aligned to 8-byte boundaries, a write will also occur for writes of less than eight bytes if the addresses being written to straddle a boundary.

To write less than eight bytes of data to ROM, first fill the buffer with the available data and then apply a _Repeated Start_ or _Stop_ condition to the
I<sup>2</sup>C bus.  The data will be written from the buffer into the non-volatile Flash approximately 64us later but the I<sup>2</sup>C bus can be utilised
for other transactions.

Note that Flash endurance for the PIC32MM device is specified as at least 10k erase / write operations with a retention of at least 20 years.  The ROM Bank
is part of the general Flash Program Memory, which will also consume erase / write cycles.  Wear-levelling and error-checking techniques are recommended for
robust designs but are not provided by the default firmware implementation.  It is up to the I<sup>2</sup>C Master performing the writes to verify that the
information has been stored correctly.

It is recommended to re-apply the write-protect flag once there are no more anticipated non-volatile writes.
