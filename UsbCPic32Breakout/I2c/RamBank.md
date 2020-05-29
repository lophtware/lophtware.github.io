# I<sup>2</sup>C RAM Bank
One kilobyte of Random Access Memory (RAM).  This is volatile storage.

Addresses in the range `[0, 1023]` (`[0x000, 0x3ff]`) can be read and written by devices on the I<sup>2</sup>C bus.  On start-up and when a USB _Set
Configuration_ command is sent, the memory will be set to the contents in the RAM Initialisation array.  This in turn was specified by the
[RAM Initialisation Contents](../UsbDeviceModel/I2c/Reports/0x16.md) command on the [USB's I<sup>2</sup>C Interface](../UsbDeviceModel/I2c/Interface.md).
The default firmware sets the contents to all zeroes.

By default all addresses are writable, but an address mask can be configured via the
[Protected RAM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x08.md) command on the
[USB's I<sup>2</sup>C Interface](../UsbDeviceModel/I2c/Interface.md) to change this.

Writes to protected addresses will result in a `NACK`.  This behaviour allows, for example, an area of RAM to be reserved for the USB Host to write
data into that I<sup>2</sup>C Masters can only read.  The address mask does not alter the wrap-around behaviour of the address pointer nor the
initialisation contents of the RAM.  If a Master wishes to determine which addresses are read-only then it can query the `Protected RAM Address Mask`
register in the [I<sup>2</sup>C Interface Bank](I2cInterfaceBank.md).
