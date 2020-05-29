# USB Interfaces
The following USB Interfaces are exposed to the Host, broadly based on the hardware modules provided by
the [PIC32MM0256GPM028](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM0256GPM028.pdf).

| ID  | Name                                             | Description                                                                                        |
|----:|--------------------------------------------------|----------------------------------------------------------------------------------------------------|
|   0 | [Core](Core/Interface.md)                        | Device-, pin- and configuration-related functions, such as GPIO, interrupt-on-change, etc.         |
|   3 | [USB](Usb/Interface.md)                          | USB (Universal Serial Bus) information, such as Debug Accessory Mode detection and general status. |
|   4 | [I2C](I2c/Interface.md)                          | I<sup>2</sup>C (Inter-Integrated Circuit) bus functions.                                           |
<!--
|   1 | [Timer](Timer/Interface.md)                      | Basic timer functions.                                                                             |
|   2 | [CCP](Ccp/Interface.md)                          | CCP (Capture / Compare / Pulse-Width-Modulation) functions.                                        |
|   3 | [USB](Usb/Interface.md)                          | USB (Universal Serial Bus) information, such as Debug Accessory Mode detection and general status. |
|   4 | [I2C](I2c/Interface.md)                          | I<sup>2</sup>C (Inter-Integrated Circuit) bus functions.                                           |
|   5 | [UART](Uart/Interface.md)                        | UART (Universal Asynchronous Receive / Transmit) functions.                                        |
|   6 | [SPI](Spi/Interface.md)                          | SPI (Serial Peripheral Interface) bus functions.                                                   |
|   7 | [ADC](Adc/Interface.md)                          | ADC (Analogue-Digital Converter) functions.                                                        |
|   8 | [DAC](Dac/Interface.md)                          | DAC (Digital-Analogue Converter) functions.                                                        |
|   9 | [Comparator](Comparator/Interface.md)            | Comparator functions.                                                                              |
|  10 | [CLC](Clc/Interface.md)                          | CLC (Configurable Logic Cell) functions.                                                           |
-->

## Reports
Each HID interface has its own set of IN and OUT Reports and the IDs can overlap.  However, there are some generic reports that are consistent across all
interfaces:
| Report ID                    | Direction | Description                                                        |
|------------------------------|-----------|--------------------------------------------------------------------|
| [0x01](Reports/0x01.md)      | IN        | [Command Acknowledgement](Reports/0x01.md)                         |

Reports are categorised as _IN_, _Interrupt IN_ and _OUT_:
| Direction    | Description                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| IN           | The Host can request the report via a standard USB `Get_Report` transaction.                                                               |
| Interrupt IN | The device sends the report to the Host, possibly in response to a previous command or as a notification of an external or periodic event. |
| OUT          | The Host sends the report to the device.                                                                                                   |
