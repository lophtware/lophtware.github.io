
# I<sup>2</sup>C - Half-Duplex Transfer; 744-751 Bytes Out, 0+ Bytes In
Report Type: Interrupt IN / OUT<br />
Report Size: 756 Bytes<br />
Acknowledged By: Transactional reports in the range `[0x80, 0xff]` or [Command Acknowledgement](0x01.md) for USB failures

| Report ID | Flags                                     | Count LSB  | Count MSB  | Address          | Payload  |
|-----------|-------------------------------------------|------------|------------|------------------|----------|
| 11011101  | `rrr`&nbsp;0&nbsp;`R`&nbsp;`c`&nbsp;`ff` | `cccccccc` | `cccccccc` | 0&nbsp;`aaaaaaa` | 751 bytes  |

## Report ID
HID Report ID.  Always `0xdd`.

This is effectively the seven most significant bits of the payload size (in bytes).  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre>

## Flags

| Bits  | Direction | Meaning                                                                                                                       |
|-------|-----------|-------------------------------------------------------------------------------------------------------------------------------|
| `ff`  | IN        | For IN Reports this is the _Fault Code_; `00` is OK, `01` is _Address NACK_, `10` is _Data NACK_, `11` is _Timeout_.  For OUT Reports this is unused so it should be set to `0`. |
| `c`   | IN        | For IN Reports this is the _Collision_ flag; `1` if there was a bus collision and the device lost arbitration, `0` if the transaction was successful.  For OUT Reports this is unused so it should be set to `0`. |
| `R`   | IN        | For IN Reports this is the _Read_ flag; `1` if the Slave Read stage is taking place (or was taking place when an error occurred), `0` if the Slave Write stage was not completed.  For OUT Reports this is unused so it should be set to `0`. |
| `rrr` | IN / OUT  | The number of payload bytes contained in the last packet of the report (the 'residual').  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre> |

## Count
For an *OUT* Report this is the number of bytes that will be shifted from the Slave and returned to the Host after the Master-to-Slave payload has been delivered.  This can be `0` if the transaction is write-only.

For an *IN* Report where the bytes are being shifted from the Master to the Slave (`R` == 0) this is the number of bytes remaining to be shifted from the Master to the Slave.

For an *IN* Report where the bytes are being shifted from the Slave to the Master (`R` == 1) this is the number of bytes remaining to be shifted from the Slave to the Master.

This field is *Little Endian*, ie. the Least Significant Byte of the word appears first.  Bit numbering within the constituent bytes is unaffected.

## Payload
A block of 751 bytes that will be shifted onto the bus for an *OUT* Report, or the Slave's response for an *IN* Report.  Only the first 744 + *`rrr`* bytes are meaningful, the rest are ignored or undefined.

## Notes
The IN Reports (Slave-to-Master-to-Host transfers) will be sent back in chunks to allow a smaller buffer to be used and to reduce latency.  The Host software must
therefore expect any number of reports in the range `[0x80, 0xff]` until the transfer is completed.  Transfers are considered completed once the `Count` field of the
IN Report reaches `0`, the `ff` flag is *not* `00` (indicating a fault) or the `c` flag is `1` (also a fault).

The internal buffer size for I<sup>2</sup>C OUT Reports is limited to 1028 bytes.  It is a circular buffer and OUT Reports are always accepted by the USB stack, which
means that data at the beginning of the buffer can be overwritten without warning if the buffer size is exceeded.  Therefore it is important that the Host software
always waits for the previous I<sup>2</sup>C transfer to complete before sending more data.
