if __name__ == "__main__":
	for reportId in range(129, 256):
		fd = open('0x{reportId:02x}.md'.format(reportId=reportId), 'w+')
		fd.write(
"""
# SPI - Full Duplex Transfer; {minPayloadSize}-{maxPayloadSize} Bytes Out, 0+ Bytes In
Report Type: Interrupt IN / OUT<br />
Report Size: {reportSize} Bytes<br />
Acknowledged By: Transactional reports in the range `[0x80, 0xff]` or [Command Acknowledgement](0x01.md) for USB failures

| Report ID | Flags                                    | Count LSB  | Count MSB  | Address          | Payload  |
|-----------|------------------------------------------|------------|------------|------------------|----------|
| 1{reportId7bits:07b} | `rrr`&nbsp;000&nbsp;`d`&nbsp;`t` | `cccccccc` | `cccccccc` | 00000&nbsp;`aaa` | {maxPayloadSize} bytes  |

## Report ID
HID Report ID.  Always `0x{reportId:02x}`.

This is effectively the seven most significant bits of the *`Payload`* field's size (in bytes).  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre>

## Flags

| Bits  | Direction | Meaning |
|-------|-----------|---------|
| `t`   | IN        | Timeout flag; `1` if the transaction took too long, `0` if not.  For an *OUT* Report this should be `0`. |
| `d`   | IN        | Done flag; `1` if the transaction has completed, `0` if there are more *IN* Reports to follow.  For an *OUT* Report this should be `0`. |
| `rrr` | IN / OUT  | The number of payload bytes contained in the last packet of the report (the 'residual').  The total number of bytes in the payload can be found by: <pre>(*`Report ID`* - 128) * 8 + *`rrr`*</pre>. |

## Count
For an *OUT* Report this is the number of bytes that will be shifted from the MISO line and returned to the Host.  This can be `0` if the transaction is write-only
and the MISO data is to be discarded.

For an *IN* Report this is the number of bytes remaining to be shifted from the MISO line.  If this field is `0` then it does not automatically mean that the
transaction has completed as there might still be data being shifted onto the MOSI line; check the *`Done Flag`* (`d`) to determine when the stream of *IN*
Reports has completed.

This field is *Little Endian*, ie. the Least Significant Byte of the word appears first.  Bit numbering within the constituent bytes is unaffected.

## Address
The Slave Select line that is asserted.  The valid range is `[0, 7]`

## Payload
A block of {maxPayloadSize} bytes that will be shifted onto the MOSI line for an *OUT* report, or in from the MISO line for an *IN* report.  Bits are shifted MSb-first.  Only the first {minPayloadSize} + *`rrr`* bytes are meaningful, the rest are ignored or undefined.
""" \
		.format(
			reportId=reportId,
			reportId7bits=reportId & 0x7f,
			minPayloadSize=(reportId - 0x80) * 8,
			maxPayloadSize=(reportId - 0x80) * 8 + 7,
			reportSize=5 + (reportId - 0x80) * 8 + 7
		))
		fd.close()
