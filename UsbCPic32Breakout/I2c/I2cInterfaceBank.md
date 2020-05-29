# I<sup>2</sup>C Interface Bank
This bank allows I<sup>2</sup>C Masters to query and manipulate the I<sup>2</sup>C properties of the device.

## RAM Write Protect Flag
The Write Protect Flag for the [I<sup>2</sup>C RAM Bank](RamBank.md) resides at address `0x010`.
| 0x010            |
|------------------|
| 0000000&nbsp;`w` |

The `w` flag is `1` if the RAM is write-protected (read-only), or `0` if it is writable.  This register is both readable and writiable by any Master on the bus.

Note that the `Protected RAM Address Mask` (below) takes precedence over this flag and can only be modified by the
[Protected RAM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x10.md) command given over the USB interface.

## RAM Protected Address Mask
The Protected Address Mask for the [I<sup>2</sup>C RAM Bank](RamBank.md) resides at addresses `[0x011, 0x012]` as a 16-bit Little Endian word.
| 0x011 (LSB) | 0x012 (MSB)              |
|-------------|--------------------------|
| `mmmmmmmm`  | `z`&nbsp;00000&nbsp;`mm` |

This register is readable by any Master on the bus.  Writing to the address mask can only be done by issuing a
[Protected RAM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x10.md) command over the USB interface.  See that command for an explanation of the function
and the meanings of the bits.

## ROM Write Protect Flag
The Write Protect Flag for the [I<sup>2</sup>C ROM Bank](RomBank.md) resides at address `0x020`.
| 0x020            |
|------------------|
| 0000000&nbsp;`w` |

The `w` flag is `1` if the ROM is write-protected (read-only), or `0` if it is writable.  This register is both readable and writiable by any Master on the bus.

Note that the `Protected ROM Address Mask` (below) takes precedence over this flag and can only be modified by the
[Protected ROM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x18.md) command given over the USB interface.

## ROM Protected Address Mask
The Protected Address Mask for the [I<sup>2</sup>C ROM Bank](RomBank.md) resides at addresses `[0x021, 0x022]` as a 16-bit Little Endian word.
| 0x021 (LSB) | 0x022 (MSB)              |
|-------------|--------------------------|
| `mmmmmmmm`  | `z`&nbsp;00000&nbsp;`mm` |

This register is readable by any Master on the bus.  Writing to the address mask can only be done by issuing a
[Protected ROM Address Mask (Slave)](../UsbDeviceModel/I2c/Reports/0x18.md) command over the USB interface.  See that command for an explanation of the function
and the meanings of the bits.
