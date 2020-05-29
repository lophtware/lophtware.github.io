# I<sup>2</sup>C HID Interface
The I<sup>2</sup>C Interface allows configuration of the device's I<sup>2</sup>C peripherals and provides a mechanism for the Host to communicate
with Master and Slave devices on the I<sup>2</sup>C bus.

## Reports

| Report ID                    | Direction | Description                                                        |
|------------------------------|-----------|--------------------------------------------------------------------|
| [0x01](Reports/0x01.md)      | IN        | [Command Acknowledgement](Reports/0x01.md)                         |
| [0x04](Reports/0x04.md)      | IN / OUT  | [Bus Configuration](Reports/0x04.md)                               |
| [0x06](Reports/0x06-0x07.md) | IN / OUT  | [Master Configuration (Stored)](Reports/0x06-0x07.md)              |
| [0x07](Reports/0x06-0x07.md) | IN        | [Master Configuration (Immediate)](Reports/0x06-0x07.md)           |
| [0x08](Reports/0x08-0x09.md) | IN / OUT  | [Slave Configuration (Stored)](Reports/0x08-0x09.md)               |
| [0x09](Reports/0x08-0x09.md) | IN        | [Slave Configuration (Immediate)](Reports/0x08-0x09.md)            |
| [0x11](Reports/0x11.md) | IN / OUT  | [RAM Transaction](Reports/0x11.md)                                      |
| [0x0a](Reports/0x0a.md) | IN / OUT  | [Slave Report Configuration](Reports/0x0a.md)                           |
| [0x0c](Reports/0x0c.md) | IN        | [Slave Transaction Done](Reports/0x0c.md)                               |
| [0x10](Reports/0x10.md) | IN / OUT  | [Protected RAM Address Mask (Slave)](Reports/0x10.md)                   |
| [0x16](Reports/0x16.md) | IN / OUT  | [RAM Initialisation Contents](Reports/0x16.md)                          |
| [0x18](Reports/0x18.md) | IN / OUT  | [Protected ROM Address Mask (Slave)](Reports/0x18.md)                   |
| [0x19](Reports/0x19.md) | IN / OUT  | [ROM Transaction](Reports/0x19.md)                                      |
| [0x1c](Reports/0x1c.md) | IN / OUT  | [ROM Bank Write-Protect Flag (Slave)](Reports/0x1c.md)                  |
| [0x1e](Reports/0x1e.md) | IN / OUT  | [ROM Contents](Reports/0x1e.md)                                         |
| [0x80](Reports/0x80.md) | IN / OUT  | [Half-Duplex Transfer; 0-7 Bytes Out, 0+ Bytes In](Reports/0x80.md)     |
| [0x81](Reports/0x81.md) | IN / OUT  | [Half-Duplex Transfer; 8-15 Bytes Out, 0+ Bytes In](Reports/0x81.md)    |
| [0x82](Reports/0x82.md) | IN / OUT  | [Half-Duplex Transfer; 16-23 Bytes Out, 0+ Bytes In](Reports/0x82.md)   |
| [0x83](Reports/0x83.md) | IN / OUT  | [Half-Duplex Transfer; 24-31 Bytes Out, 0+ Bytes In](Reports/0x83.md)   |
| [0x84](Reports/0x84.md) | IN / OUT  | [Half-Duplex Transfer; 32-39 Bytes Out, 0+ Bytes In](Reports/0x84.md)   |
| [0x85](Reports/0x85.md) | IN / OUT  | [Half-Duplex Transfer; 40-47 Bytes Out, 0+ Bytes In](Reports/0x85.md)   |
| [0x86](Reports/0x86.md) | IN / OUT  | [Half-Duplex Transfer; 48-55 Bytes Out, 0+ Bytes In](Reports/0x86.md)   |
| [0x87](Reports/0x87.md) | IN / OUT  | [Half-Duplex Transfer; 56-63 Bytes Out, 0+ Bytes In](Reports/0x87.md)   |
| [0x88](Reports/0x88.md) | IN / OUT  | [Half-Duplex Transfer; 64-71 Bytes Out, 0+ Bytes In](Reports/0x88.md)   |
| [0x89](Reports/0x89.md) | IN / OUT  | [Half-Duplex Transfer; 72-79 Bytes Out, 0+ Bytes In](Reports/0x89.md)   |
| [0x8a](Reports/0x8a.md) | IN / OUT  | [Half-Duplex Transfer; 80-87 Bytes Out, 0+ Bytes In](Reports/0x8a.md)   |
| [0x8b](Reports/0x8b.md) | IN / OUT  | [Half-Duplex Transfer; 88-95 Bytes Out, 0+ Bytes In](Reports/0x8b.md)   |
| [0x8c](Reports/0x8c.md) | IN / OUT  | [Half-Duplex Transfer; 96-103 Bytes Out, 0+ Bytes In](Reports/0x8c.md)  |
| [0x8d](Reports/0x8d.md) | IN / OUT  | [Half-Duplex Transfer; 104-111 Bytes Out, 0+ Bytes In](Reports/0x8d.md) |
| [0x8e](Reports/0x8e.md) | IN / OUT  | [Half-Duplex Transfer; 112-119 Bytes Out, 0+ Bytes In](Reports/0x8e.md) |
| [0x8f](Reports/0x8f.md) | IN / OUT  | [Half-Duplex Transfer; 120-127 Bytes Out, 0+ Bytes In](Reports/0x8f.md) |
| [0x90](Reports/0x90.md) | IN / OUT  | [Half-Duplex Transfer; 128-135 Bytes Out, 0+ Bytes In](Reports/0x90.md) |
| [0x91](Reports/0x91.md) | IN / OUT  | [Half-Duplex Transfer; 136-143 Bytes Out, 0+ Bytes In](Reports/0x91.md) |
| [0x92](Reports/0x92.md) | IN / OUT  | [Half-Duplex Transfer; 144-151 Bytes Out, 0+ Bytes In](Reports/0x92.md) |
| [0x93](Reports/0x93.md) | IN / OUT  | [Half-Duplex Transfer; 152-159 Bytes Out, 0+ Bytes In](Reports/0x93.md) |
| [0x94](Reports/0x94.md) | IN / OUT  | [Half-Duplex Transfer; 160-167 Bytes Out, 0+ Bytes In](Reports/0x94.md) |
| [0x95](Reports/0x95.md) | IN / OUT  | [Half-Duplex Transfer; 168-175 Bytes Out, 0+ Bytes In](Reports/0x95.md) |
| [0x96](Reports/0x96.md) | IN / OUT  | [Half-Duplex Transfer; 176-183 Bytes Out, 0+ Bytes In](Reports/0x96.md) |
| [0x97](Reports/0x97.md) | IN / OUT  | [Half-Duplex Transfer; 184-191 Bytes Out, 0+ Bytes In](Reports/0x97.md) |
| [0x98](Reports/0x98.md) | IN / OUT  | [Half-Duplex Transfer; 192-199 Bytes Out, 0+ Bytes In](Reports/0x98.md) |
| [0x99](Reports/0x99.md) | IN / OUT  | [Half-Duplex Transfer; 200-207 Bytes Out, 0+ Bytes In](Reports/0x99.md) |
| [0x9a](Reports/0x9a.md) | IN / OUT  | [Half-Duplex Transfer; 208-215 Bytes Out, 0+ Bytes In](Reports/0x9a.md) |
| [0x9b](Reports/0x9b.md) | IN / OUT  | [Half-Duplex Transfer; 216-223 Bytes Out, 0+ Bytes In](Reports/0x9b.md) |
| [0x9c](Reports/0x9c.md) | IN / OUT  | [Half-Duplex Transfer; 224-231 Bytes Out, 0+ Bytes In](Reports/0x9c.md) |
| [0x9d](Reports/0x9d.md) | IN / OUT  | [Half-Duplex Transfer; 232-239 Bytes Out, 0+ Bytes In](Reports/0x9d.md) |
| [0x9e](Reports/0x9e.md) | IN / OUT  | [Half-Duplex Transfer; 240-247 Bytes Out, 0+ Bytes In](Reports/0x9e.md) |
| [0x9f](Reports/0x9f.md) | IN / OUT  | [Half-Duplex Transfer; 248-255 Bytes Out, 0+ Bytes In](Reports/0x9f.md) |
| [0xa0](Reports/0xa0.md) | IN / OUT  | [Half-Duplex Transfer; 256-263 Bytes Out, 0+ Bytes In](Reports/0xa0.md) |
| [0xa1](Reports/0xa1.md) | IN / OUT  | [Half-Duplex Transfer; 264-271 Bytes Out, 0+ Bytes In](Reports/0xa1.md) |
| [0xa2](Reports/0xa2.md) | IN / OUT  | [Half-Duplex Transfer; 272-279 Bytes Out, 0+ Bytes In](Reports/0xa2.md) |
| [0xa3](Reports/0xa3.md) | IN / OUT  | [Half-Duplex Transfer; 280-287 Bytes Out, 0+ Bytes In](Reports/0xa3.md) |
| [0xa4](Reports/0xa4.md) | IN / OUT  | [Half-Duplex Transfer; 288-295 Bytes Out, 0+ Bytes In](Reports/0xa4.md) |
| [0xa5](Reports/0xa5.md) | IN / OUT  | [Half-Duplex Transfer; 296-303 Bytes Out, 0+ Bytes In](Reports/0xa5.md) |
| [0xa6](Reports/0xa6.md) | IN / OUT  | [Half-Duplex Transfer; 304-311 Bytes Out, 0+ Bytes In](Reports/0xa6.md) |
| [0xa7](Reports/0xa7.md) | IN / OUT  | [Half-Duplex Transfer; 312-319 Bytes Out, 0+ Bytes In](Reports/0xa7.md) |
| [0xa8](Reports/0xa8.md) | IN / OUT  | [Half-Duplex Transfer; 320-327 Bytes Out, 0+ Bytes In](Reports/0xa8.md) |
| [0xa9](Reports/0xa9.md) | IN / OUT  | [Half-Duplex Transfer; 328-335 Bytes Out, 0+ Bytes In](Reports/0xa9.md) |
| [0xaa](Reports/0xaa.md) | IN / OUT  | [Half-Duplex Transfer; 336-343 Bytes Out, 0+ Bytes In](Reports/0xaa.md) |
| [0xab](Reports/0xab.md) | IN / OUT  | [Half-Duplex Transfer; 344-351 Bytes Out, 0+ Bytes In](Reports/0xab.md) |
| [0xac](Reports/0xac.md) | IN / OUT  | [Half-Duplex Transfer; 352-359 Bytes Out, 0+ Bytes In](Reports/0xac.md) |
| [0xad](Reports/0xad.md) | IN / OUT  | [Half-Duplex Transfer; 360-367 Bytes Out, 0+ Bytes In](Reports/0xad.md) |
| [0xae](Reports/0xae.md) | IN / OUT  | [Half-Duplex Transfer; 368-375 Bytes Out, 0+ Bytes In](Reports/0xae.md) |
| [0xaf](Reports/0xaf.md) | IN / OUT  | [Half-Duplex Transfer; 376-383 Bytes Out, 0+ Bytes In](Reports/0xaf.md) |
| [0xb0](Reports/0xb0.md) | IN / OUT  | [Half-Duplex Transfer; 384-391 Bytes Out, 0+ Bytes In](Reports/0xb0.md) |
| [0xb1](Reports/0xb1.md) | IN / OUT  | [Half-Duplex Transfer; 392-399 Bytes Out, 0+ Bytes In](Reports/0xb1.md) |
| [0xb2](Reports/0xb2.md) | IN / OUT  | [Half-Duplex Transfer; 400-407 Bytes Out, 0+ Bytes In](Reports/0xb2.md) |
| [0xb3](Reports/0xb3.md) | IN / OUT  | [Half-Duplex Transfer; 408-415 Bytes Out, 0+ Bytes In](Reports/0xb3.md) |
| [0xb4](Reports/0xb4.md) | IN / OUT  | [Half-Duplex Transfer; 416-423 Bytes Out, 0+ Bytes In](Reports/0xb4.md) |
| [0xb5](Reports/0xb5.md) | IN / OUT  | [Half-Duplex Transfer; 424-431 Bytes Out, 0+ Bytes In](Reports/0xb5.md) |
| [0xb6](Reports/0xb6.md) | IN / OUT  | [Half-Duplex Transfer; 432-439 Bytes Out, 0+ Bytes In](Reports/0xb6.md) |
| [0xb7](Reports/0xb7.md) | IN / OUT  | [Half-Duplex Transfer; 440-447 Bytes Out, 0+ Bytes In](Reports/0xb7.md) |
| [0xb8](Reports/0xb8.md) | IN / OUT  | [Half-Duplex Transfer; 448-455 Bytes Out, 0+ Bytes In](Reports/0xb8.md) |
| [0xb9](Reports/0xb9.md) | IN / OUT  | [Half-Duplex Transfer; 456-463 Bytes Out, 0+ Bytes In](Reports/0xb9.md) |
| [0xba](Reports/0xba.md) | IN / OUT  | [Half-Duplex Transfer; 464-471 Bytes Out, 0+ Bytes In](Reports/0xba.md) |
| [0xbb](Reports/0xbb.md) | IN / OUT  | [Half-Duplex Transfer; 472-479 Bytes Out, 0+ Bytes In](Reports/0xbb.md) |
| [0xbc](Reports/0xbc.md) | IN / OUT  | [Half-Duplex Transfer; 480-487 Bytes Out, 0+ Bytes In](Reports/0xbc.md) |
| [0xbd](Reports/0xbd.md) | IN / OUT  | [Half-Duplex Transfer; 488-495 Bytes Out, 0+ Bytes In](Reports/0xbd.md) |
| [0xbe](Reports/0xbe.md) | IN / OUT  | [Half-Duplex Transfer; 496-503 Bytes Out, 0+ Bytes In](Reports/0xbe.md) |
| [0xbf](Reports/0xbf.md) | IN / OUT  | [Half-Duplex Transfer; 504-511 Bytes Out, 0+ Bytes In](Reports/0xbf.md) |
| [0xc0](Reports/0xc0.md) | IN / OUT  | [Half-Duplex Transfer; 512-519 Bytes Out, 0+ Bytes In](Reports/0xc0.md) |
| [0xc1](Reports/0xc1.md) | IN / OUT  | [Half-Duplex Transfer; 520-527 Bytes Out, 0+ Bytes In](Reports/0xc1.md) |
| [0xc2](Reports/0xc2.md) | IN / OUT  | [Half-Duplex Transfer; 528-535 Bytes Out, 0+ Bytes In](Reports/0xc2.md) |
| [0xc3](Reports/0xc3.md) | IN / OUT  | [Half-Duplex Transfer; 536-543 Bytes Out, 0+ Bytes In](Reports/0xc3.md) |
| [0xc4](Reports/0xc4.md) | IN / OUT  | [Half-Duplex Transfer; 544-551 Bytes Out, 0+ Bytes In](Reports/0xc4.md) |
| [0xc5](Reports/0xc5.md) | IN / OUT  | [Half-Duplex Transfer; 552-559 Bytes Out, 0+ Bytes In](Reports/0xc5.md) |
| [0xc6](Reports/0xc6.md) | IN / OUT  | [Half-Duplex Transfer; 560-567 Bytes Out, 0+ Bytes In](Reports/0xc6.md) |
| [0xc7](Reports/0xc7.md) | IN / OUT  | [Half-Duplex Transfer; 568-575 Bytes Out, 0+ Bytes In](Reports/0xc7.md) |
| [0xc8](Reports/0xc8.md) | IN / OUT  | [Half-Duplex Transfer; 576-583 Bytes Out, 0+ Bytes In](Reports/0xc8.md) |
| [0xc9](Reports/0xc9.md) | IN / OUT  | [Half-Duplex Transfer; 584-591 Bytes Out, 0+ Bytes In](Reports/0xc9.md) |
| [0xca](Reports/0xca.md) | IN / OUT  | [Half-Duplex Transfer; 592-599 Bytes Out, 0+ Bytes In](Reports/0xca.md) |
| [0xcb](Reports/0xcb.md) | IN / OUT  | [Half-Duplex Transfer; 600-607 Bytes Out, 0+ Bytes In](Reports/0xcb.md) |
| [0xcc](Reports/0xcc.md) | IN / OUT  | [Half-Duplex Transfer; 608-615 Bytes Out, 0+ Bytes In](Reports/0xcc.md) |
| [0xcd](Reports/0xcd.md) | IN / OUT  | [Half-Duplex Transfer; 616-623 Bytes Out, 0+ Bytes In](Reports/0xcd.md) |
| [0xce](Reports/0xce.md) | IN / OUT  | [Half-Duplex Transfer; 624-631 Bytes Out, 0+ Bytes In](Reports/0xce.md) |
| [0xcf](Reports/0xcf.md) | IN / OUT  | [Half-Duplex Transfer; 632-639 Bytes Out, 0+ Bytes In](Reports/0xcf.md) |
| [0xd0](Reports/0xd0.md) | IN / OUT  | [Half-Duplex Transfer; 640-647 Bytes Out, 0+ Bytes In](Reports/0xd0.md) |
| [0xd1](Reports/0xd1.md) | IN / OUT  | [Half-Duplex Transfer; 648-655 Bytes Out, 0+ Bytes In](Reports/0xd1.md) |
| [0xd2](Reports/0xd2.md) | IN / OUT  | [Half-Duplex Transfer; 656-663 Bytes Out, 0+ Bytes In](Reports/0xd2.md) |
| [0xd3](Reports/0xd3.md) | IN / OUT  | [Half-Duplex Transfer; 664-671 Bytes Out, 0+ Bytes In](Reports/0xd3.md) |
| [0xd4](Reports/0xd4.md) | IN / OUT  | [Half-Duplex Transfer; 672-679 Bytes Out, 0+ Bytes In](Reports/0xd4.md) |
| [0xd5](Reports/0xd5.md) | IN / OUT  | [Half-Duplex Transfer; 680-687 Bytes Out, 0+ Bytes In](Reports/0xd5.md) |
| [0xd6](Reports/0xd6.md) | IN / OUT  | [Half-Duplex Transfer; 688-695 Bytes Out, 0+ Bytes In](Reports/0xd6.md) |
| [0xd7](Reports/0xd7.md) | IN / OUT  | [Half-Duplex Transfer; 696-703 Bytes Out, 0+ Bytes In](Reports/0xd7.md) |
| [0xd8](Reports/0xd8.md) | IN / OUT  | [Half-Duplex Transfer; 704-711 Bytes Out, 0+ Bytes In](Reports/0xd8.md) |
| [0xd9](Reports/0xd9.md) | IN / OUT  | [Half-Duplex Transfer; 712-719 Bytes Out, 0+ Bytes In](Reports/0xd9.md) |
| [0xda](Reports/0xda.md) | IN / OUT  | [Half-Duplex Transfer; 720-727 Bytes Out, 0+ Bytes In](Reports/0xda.md) |
| [0xdb](Reports/0xdb.md) | IN / OUT  | [Half-Duplex Transfer; 728-735 Bytes Out, 0+ Bytes In](Reports/0xdb.md) |
| [0xdc](Reports/0xdc.md) | IN / OUT  | [Half-Duplex Transfer; 736-743 Bytes Out, 0+ Bytes In](Reports/0xdc.md) |
| [0xdd](Reports/0xdd.md) | IN / OUT  | [Half-Duplex Transfer; 744-751 Bytes Out, 0+ Bytes In](Reports/0xdd.md) |
| [0xde](Reports/0xde.md) | IN / OUT  | [Half-Duplex Transfer; 752-759 Bytes Out, 0+ Bytes In](Reports/0xde.md) |
| [0xdf](Reports/0xdf.md) | IN / OUT  | [Half-Duplex Transfer; 760-767 Bytes Out, 0+ Bytes In](Reports/0xdf.md) |
| [0xe0](Reports/0xe0.md) | IN / OUT  | [Half-Duplex Transfer; 768-775 Bytes Out, 0+ Bytes In](Reports/0xe0.md) |
| [0xe1](Reports/0xe1.md) | IN / OUT  | [Half-Duplex Transfer; 776-783 Bytes Out, 0+ Bytes In](Reports/0xe1.md) |
| [0xe2](Reports/0xe2.md) | IN / OUT  | [Half-Duplex Transfer; 784-791 Bytes Out, 0+ Bytes In](Reports/0xe2.md) |
| [0xe3](Reports/0xe3.md) | IN / OUT  | [Half-Duplex Transfer; 792-799 Bytes Out, 0+ Bytes In](Reports/0xe3.md) |
| [0xe4](Reports/0xe4.md) | IN / OUT  | [Half-Duplex Transfer; 800-807 Bytes Out, 0+ Bytes In](Reports/0xe4.md) |
| [0xe5](Reports/0xe5.md) | IN / OUT  | [Half-Duplex Transfer; 808-815 Bytes Out, 0+ Bytes In](Reports/0xe5.md) |
| [0xe6](Reports/0xe6.md) | IN / OUT  | [Half-Duplex Transfer; 816-823 Bytes Out, 0+ Bytes In](Reports/0xe6.md) |
| [0xe7](Reports/0xe7.md) | IN / OUT  | [Half-Duplex Transfer; 824-831 Bytes Out, 0+ Bytes In](Reports/0xe7.md) |
| [0xe8](Reports/0xe8.md) | IN / OUT  | [Half-Duplex Transfer; 832-839 Bytes Out, 0+ Bytes In](Reports/0xe8.md) |
| [0xe9](Reports/0xe9.md) | IN / OUT  | [Half-Duplex Transfer; 840-847 Bytes Out, 0+ Bytes In](Reports/0xe9.md) |
| [0xea](Reports/0xea.md) | IN / OUT  | [Half-Duplex Transfer; 848-855 Bytes Out, 0+ Bytes In](Reports/0xea.md) |
| [0xeb](Reports/0xeb.md) | IN / OUT  | [Half-Duplex Transfer; 856-863 Bytes Out, 0+ Bytes In](Reports/0xeb.md) |
| [0xec](Reports/0xec.md) | IN / OUT  | [Half-Duplex Transfer; 864-871 Bytes Out, 0+ Bytes In](Reports/0xec.md) |
| [0xed](Reports/0xed.md) | IN / OUT  | [Half-Duplex Transfer; 872-879 Bytes Out, 0+ Bytes In](Reports/0xed.md) |
| [0xee](Reports/0xee.md) | IN / OUT  | [Half-Duplex Transfer; 880-887 Bytes Out, 0+ Bytes In](Reports/0xee.md) |
| [0xef](Reports/0xef.md) | IN / OUT  | [Half-Duplex Transfer; 888-895 Bytes Out, 0+ Bytes In](Reports/0xef.md) |
| [0xf0](Reports/0xf0.md) | IN / OUT  | [Half-Duplex Transfer; 896-903 Bytes Out, 0+ Bytes In](Reports/0xf0.md) |
| [0xf1](Reports/0xf1.md) | IN / OUT  | [Half-Duplex Transfer; 904-911 Bytes Out, 0+ Bytes In](Reports/0xf1.md) |
| [0xf2](Reports/0xf2.md) | IN / OUT  | [Half-Duplex Transfer; 912-919 Bytes Out, 0+ Bytes In](Reports/0xf2.md) |
| [0xf3](Reports/0xf3.md) | IN / OUT  | [Half-Duplex Transfer; 920-927 Bytes Out, 0+ Bytes In](Reports/0xf3.md) |
| [0xf4](Reports/0xf4.md) | IN / OUT  | [Half-Duplex Transfer; 928-935 Bytes Out, 0+ Bytes In](Reports/0xf4.md) |
| [0xf5](Reports/0xf5.md) | IN / OUT  | [Half-Duplex Transfer; 936-943 Bytes Out, 0+ Bytes In](Reports/0xf5.md) |
| [0xf6](Reports/0xf6.md) | IN / OUT  | [Half-Duplex Transfer; 944-951 Bytes Out, 0+ Bytes In](Reports/0xf6.md) |
| [0xf7](Reports/0xf7.md) | IN / OUT  | [Half-Duplex Transfer; 952-959 Bytes Out, 0+ Bytes In](Reports/0xf7.md) |
| [0xf8](Reports/0xf8.md) | IN / OUT  | [Half-Duplex Transfer; 960-967 Bytes Out, 0+ Bytes In](Reports/0xf8.md) |
| [0xf9](Reports/0xf9.md) | IN / OUT  | [Half-Duplex Transfer; 968-975 Bytes Out, 0+ Bytes In](Reports/0xf9.md) |
| [0xfa](Reports/0xfa.md) | IN / OUT  | [Half-Duplex Transfer; 976-983 Bytes Out, 0+ Bytes In](Reports/0xfa.md) |
| [0xfb](Reports/0xfb.md) | IN / OUT  | [Half-Duplex Transfer; 984-991 Bytes Out, 0+ Bytes In](Reports/0xfb.md) |
| [0xfc](Reports/0xfc.md) | IN / OUT  | [Half-Duplex Transfer; 992-999 Bytes Out, 0+ Bytes In](Reports/0xfc.md) |
| [0xfd](Reports/0xfd.md) | IN / OUT  | [Half-Duplex Transfer; 1000-1007 Bytes Out, 0+ Bytes In](Reports/0xfd.md) |
| [0xfe](Reports/0xfe.md) | IN / OUT  | [Half-Duplex Transfer; 1008-1015 Bytes Out, 0+ Bytes In](Reports/0xfe.md) |
| [0xff](Reports/0xff.md) | IN / OUT  | [Half-Duplex Transfer; 1016-1023 Bytes Out, 0+ Bytes In](Reports/0xff.md) |
