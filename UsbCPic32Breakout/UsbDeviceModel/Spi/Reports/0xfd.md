
# SPI - Full- / Half-Duplex Transfer; 1000-1007 Bytes Out, 0-1007 Bytes In
Report Type: Interrupt IN / OUT<br />
Report Size: 1010 Bytes

| Report ID | Flags | Flags | Payload |
|-----------|-------|-------|---------|
| 11111101 | `rrr`&nbsp;00000 | `a`&nbsp;`t`&nbsp;000&nbsp;`sss` | 1007 bytes |

## Report ID
HID Report ID.  Always `0xfd`.

This is effectively the seven most significant bits of the payload size (in bytes).  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre>

## Flags

| Bits  | Direction | Meaning |
|-------|-----------|---------|
| `rrr` | IN / OUT  | The number of payload bytes contained in the last packet of the report.  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre> |
| 00000 |          |                                                                       |
| `a`   | OUT      | `1` if the Slave Select line remains asserted after the transfer; `0` if the Slave Select line is reset to its default state. |
| `t`   | OUT      | `1` if the transaction is transmit-only and incoming data on the MISO line is discarded (half-duplex); `0` to transfer the received MISO data back to the host (full-duplex). |
| 000   |          |                                                                       |
| `sss` | IN / OUT | The Slave Select line that is asserted.  The valid range is `[0, 7]`. |

## Payload
A block of 1007 bytes that will be shifted onto the MOSI line for an *OUT* report, or in from the MISO line for an *IN* report.  Bits are shifted MSb-first.  Only the first 1000 + *`rrr`* bytes are meaningful, the rest are ignored or undefined.
