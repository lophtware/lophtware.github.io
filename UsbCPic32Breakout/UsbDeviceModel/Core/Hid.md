# Core HID Interface
The Core Interface handles microcontroller, pin and device configuration.  It allows pins to be assigned to other interfaces, configured as inputs or outputs or
one of a number of other functions.  As well as configuration this interface can be used to change the values of the pins or query their current values, and also
allows the Host to be notified of certain events.

## Reports
| Report ID               | Direction | Description                                                  |
|-------------------------|-----------|--------------------------------------------------------------|
| [0x01](Reports/0x01.md) | IN        | [Command Acknowledgement](Reports/0x01.md).                  |
| [0x02](Reports/0x02.md) | IN        | [Device Status](Reports/0x02.md).                            |
| [0x04](Reports/0x04.md) | OUT       | [Set Unlock Key](Reports/0x04.md).                           |
| [0x08](Reports/0x08.md) | OUT       | [Store Current Configuration](Reports/0x08.md).              |
| [0x14](Reports/0x14.md) | OUT       | [Pin Parallel Load / Set / Reset / Toggle](Reports/0x14.md). |
| [0x16](Reports/0x16.md) | IN        | [Pin Parallel Status](Reports/0x16.md).                      |
| [0x18](Reports/0x18.md) | IN        | [Pins Changed](Reports/0x18.md).                             |
| [0x42](Reports/0x42.md) | IN / OUT  | [Pin Configuration (A2)](Reports/0x42.md).                   |
| [0x43](Reports/0x43.md) | IN / OUT  | [Pin Configuration (A3)](Reports/0x43.md).                   |
| [0x44](Reports/0x44.md) | IN / OUT  | [Pin Configuration (A4)](Reports/0x44.md).                   |
| [0x50](Reports/0x50.md) | IN / OUT  | [Pin Configuration (B0)](Reports/0x50.md).                   |
| [0x51](Reports/0x51.md) | IN / OUT  | [Pin Configuration (B1)](Reports/0x51.md).                   |
| [0x52](Reports/0x52.md) | IN / OUT  | [Pin Configuration (B2)](Reports/0x52.md).                   |
| [0x53](Reports/0x53.md) | IN / OUT  | [Pin Configuration (B3)](Reports/0x53.md).                   |
| [0x54](Reports/0x54.md) | IN / OUT  | [Pin Configuration (B4)](Reports/0x54.md).                   |
| [0x55](Reports/0x55.md) | IN / OUT  | [Pin Configuration (B5)](Reports/0x55.md).                   |
| [0x57](Reports/0x57.md) | IN / OUT  | [Pin Configuration (B7)](Reports/0x57.md).                   |
| [0x69](Reports/0x69.md) | IN / OUT  | [Pin Configuration (C9)](Reports/0x69.md).                   |
