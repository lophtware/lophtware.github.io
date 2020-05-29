# USB HID Interface
The USB Interface is for USB event notifications and device configuration, such as descriptor values.

## Reports
| Report ID               | Direction | Description                                                    |
|-------------------------|-----------|----------------------------------------------------------------|
| [0x01](Reports/0x01.md) | IN        | [Command Acknowledgement](Reports/0x01.md).                    |
| [0x04](Reports/0x04.md) | IN / OUT  | [Configuration Name Descriptor](Reports/0x04.md).              |
| [0x08](Reports/0x08.md) | IN / OUT  | [Power Configuration](Reports/0x08.md).                        |
| [0x10](Reports/0x10.md) | IN        | [I<sup>2</sup>C Message from Master to Host](Reports/0x10.md). |
