# I<sup>2</sup>C Device Information Bank
This bank allows I<sup>2</sup>C Masters to interrogate the device and discern device properties.  All registers in this bank are read-only.

## Magic Bytes (Product Identification)
Addresses `[0x000, 0x00f]` form a known sequence so that I<sup>2</sup>C Masters can identify the device.  The sixteen bytes have been generated as a
GUID and should not be taken as encoding any specific information other than being a sufficiently long pattern serving to identify this device from
a possible EEPROM or other device.  In the event of the device being assigned an unknown I<sup>2</sup>C address, Masters should be able to discover
this device on the bus by iterating all possible I<sup>2</sup>C addresses looking for this sequence.

| 0x000 |      |      |      |      |      |      |      |      |      |      |      |      |      |      | 0x00f |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| 0xfb  | 0xb0 | 0x90 | 0x7d | 0xdd | 0x09 | 0x47 | 0x74 | 0x8c | 0x31 | 0x7f | 0x71 | 0xf9 | 0x12 | 0xb9 | 0x2c  |

## Firmware Version
The version of the device firmware resides at `[0x010, 0x013]`:

| 0x010      |            |            | 0x013      |
|------------|------------|------------|------------|
| `rrrrrrrr` | `mmmmmmmm` | `MMMMMMMM` | `ffffffff` |

The version number follows the [Semantic Versioning](https://semver.org/) conventions of `MMMMMMMM`.`mmmmmmmm`.`rrrrrrrr` (_major.minor.revision_).
The `ffffffff` field is for flags.  Currently these flags are all reserved and the byte should equal `0x00`.

## USB API Version
The API that is exposed to the USB Host is versioned separately to the overall firmware version.  The version of the API resides at addresses `[0x014, 0x017]`:

| 0x014      |            |            | 0x017      |
|------------|------------|------------|------------|
| `bbbbbbbb` | `BBBBBBBB` | `mmmmmmmm` | `MMMMMMMM` |

The version number follows the [Semantic Versioning](https://semver.org/) conventions of `MMMMMMMM`.`mmmmmmmm`.`00000000` (_major.minor.revision_) because
the USB Specification only provides two fields, so revision is always zero.  The same version number is encoded as Binary Coded Decimal (BCD) by the fields
`BBBBBBBB`.`bbbbbbbb`, which is the representation used by the _USB Device Descriptor_.

## MCU Device ID
The Microcontroller's `DEVID` register is exposed at addresses `[0x018, 0x01b]`.  According to the
[PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf) datasheet:

| 0x018      |            |            | 0x01b         |
|------------|------------|------------|---------------|
| `iiiiiiii` | `iiiiiiii` | `iiiiiiii` | `vers` `iiii` |

The Device ID bits (`i`) will form the word `0x07718053`, whilst the four `vers` bits specify the silicon revision.

## Unique Device ID
The Microcontroller's five `UDID*` registers are exposed at addresses `[0x01c, 0x02f]`.  These registers do encode die co-ordinate offsets and other
relatively unique parameters but the details are unimportant.  Effectively these bytes provide a serial number, and because of this they are also
exposed via the USB's Device / Serial Number String Descriptor:

| 0x01c      |            |            | 0x01f      | 0x020      |            |            | 0x023      | 0x024      |            |            | 0x027      | 0x028      |            |            | 0x02b      | 0x02c      |            |            | 0x02f      |
|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| `11111111` | `11111111` | `11111111` | `11111111` | `22222222` | `22222222` | `22222222` | `22222222` | `33333333` | `33333333` | `33333333` | `33333333` | `44444444` | `44444444` | `44444444` | `44444444` | `55555555` | `55555555` | `55555555` | `55555555` |

Where `1` is `UDID1`, `2` is `UDID2`, etc.

## MCU Device Reset Reason
The Microcontroller's `RCON` register is exposed at addresses `[0x040, 0x043]`.  See the [Device Reset Reasons](../ResetReasons.md) page for more information.

## MCU Exception Details
During some resets, snapshots of the Microcontroller's `ERROREPC`, `EPC`, `CAUSE`, `DESAVE` and `RA` registers are exposed at addresseses `[0x044, 0x054]`,
respectively.  These values are useful for debugging.
