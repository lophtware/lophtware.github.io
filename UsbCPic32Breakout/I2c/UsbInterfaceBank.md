# USB Interface Bank
This bank allows I<sup>2</sup>C Masters to query the state of the USB module and connection, and even send small payloads directly to a connected Host.

## Status Flags `[0x010, 0x013]`
Flags indicating the status of the USB cable, connection and stack:

| 0x010      | 0x011            | 0x012           | 0x013           |
|------------|------------------|-----------------|-----------------|
| `hgfedcba` | 00&nbsp;`rqpkji` | Reserved (zero) | Reserved (zero) |

| Bits    | Direction | Meaning                                                                                                                                                                                 |
|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `a`     | IN / OUT  | Attached to a device (ie. a Source (Host) will be on the other end of the cable).                                                                                                       |
| `b`     | IN / OUT  | Attached as a Debug (Sink) Accessory.                                                                                                                                                   |
| `c`     | IN / OUT  | Attached to an Audio (Sink / Source) Accessory - *THE ELECTRICAL SPECIFICATIONS FOR AUDIO ACCESSORIES ARE NOT SUPPORTED AND WILL DAMAGE THE DEVICE; THIS FLAG IS FOR INFORMATION ONLY*. |
| `d`     | IN / OUT  | The cable is an active cable.                                                                                                                                                           |
| `e`     | IN / OUT  | The VBUS (+5V) voltage is within USB specifications.                                                                                                                                    |
| `f`     | IN / OUT  | The voltage on the CC pins is within USB specifications.                                                                                                                                |
| `g`     | IN / OUT  | The CC1 pin (USB connector pin A5) is connected.                                                                                                                                        |
| `h`     | IN / OUT  | The CC2 pin (USB connector pin B5) is connected.                                                                                                                                        |
| `i`     | IN / OUT  | No faults have occurred when examining the CC pin(s).                                                                                                                                   |
| `j`     | IN / OUT  | The D+ / D- lines were checked for short on power-up.                                                                                                                                   |
| `k`     | IN / OUT  | The D+ / D- lines were shorted on power-up, a crude indication of being connected to a dedicated charger.                                                                               |
| `p`     | IN / OUT  | Source has suspended the device.                                                                                                                                                        |
| `q`     | IN / OUT  | USB enumeration has completed.                                                                                                                                                          |
| `r`     | IN / OUT  | USB protocol error has occurred (one or more endpoints are in the HALTED state).                                                                                                        |

## Current Limit `[0x014, 0x015]`
A 16-bit Little Endian word indicating the current limit, in milliamps, that has been agreed with the Host or assumed of the charger.  Note that this may change
during the lifetime of the connection, for example if the Host decides to re-enumerate the device under a different configuration:

| 0x014      | 0x015            |
|------------|------------------|
| `cccccccc` | 00000&nbsp;`ccc` |

## Configuration Number `[0x016]`
The currently selected USB configuration.  This is the value from the standard USB `Set_Configuration` request that is sent during enumeration.  If the device
has not enumerated (for example, it is attached to a charger or the Host cannot satisfy the requested current limits) then this value will be `0x00`.

| 0x016            |
|------------------|
| 0000&nbsp;`cccc` |

## Send Message to Host `[0x200, 0x206]`
An arbitrary message can be sent to the Host at the other end of the USB cable by writing to register `[0x206]`, with the payload being the previous 6 bytes
(registers in the range `[0x200, 0x205]`):

| 0x200-0x205      | 0x206                    |
|------------------|--------------------------|
| 6 bytes          | 000000&nbsp;`b`&nbsp;`w` |

The `w` flag is `1` if the payload in registers `[0x200, 0x205]` is to be sent (written) as an
[I<sup>2</sup>C Message from Master to Host](../UsbDeviceModel/Usb/Reports/0x10.md), or `0` if no message is to be sent.

The `b` flag is `1` if the I<sup>2</sup>C transaction should be blocked until the message is sent (the clock will be stretched as long as is necessary), or
`0` if a _NACK_ is preferable should the outgoing message queue be full.

Note that if a Host is not connected then these messages will just drip out of the unconnected end of the cable in a puddle of ignored bits, so the Status Flags
registers in `[0x010, 0x016]` should be interrogated first if it is important to you that something is actually connected, enumerated and listening for your
messages.
