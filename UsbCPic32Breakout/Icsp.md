# In-Circuit Serial Programming (ICSP)
The device can be programmed with Microchip's PICKit, a Raspberry Pi running [Pickle](https://wiki.kewl.org/dokuwiki/projects:pickle) or by using a custom
USB Type-C connector / dongle to connect as a Debug Accessory.

Note that the +5V and +3.3V pins broken out by the header _should NOT_ be driven from off the board.  The _ONLY_ way to power the board is via the USB connector.
All ICSP signals are +3.3V CMOS.

The ICSP details are in the [PIC32 Family Programming and Diagnostics](https://github.com/lophtware/UsbCPic32Breakout/blob/master/doc/datasheets/mcu/PIC32MM-33-ProgrammingAndDiagnostics-61129F.pdf)
datasheet but PIC ICSP can get a bit complicated so it's best to use a PICKit, Pickle or some other programmer and just map the signals accordingly.

## PICKit
The PICKit is straightforward.  Make sure that power is applied to the board (ie. the USB cable is attached) and connect the following pins:

| Board Pin | PICKit Name | Notes                                                                                       |
|-----------|-------------|---------------------------------------------------------------------------------------------|
| EN        | /MCLR       |                                                                                             |
| +3.3V     | VDD         | Provides the sense voltage for the PICKit so that it drives the right voltage on PGC / PGD. |
| 0V        | VSS         |                                                                                             |
| B0        | PGD         | This is called *PGED1* in the PIC's datasheet.                                              |
| B1        | PGC         | This is caled *PGEC1* in the PIC's datasheet.                                               |

You can either wire the pins up on a breadboard or make a simple Dupont-style cable, but note that due to the routing constraints the board header _does not
map 1:1_ with the PICKit's header.  The order of the board pins is *+3.3V*, *0V*, *EN*, *PGD*, *PGC*.

## Pickle
A Raspberry Pi running [Pickle](https://wiki.kewl.org/dokuwiki/projects:pickle) is another way of programming the device.  The ICSP pin mapping is:

| Board Pin | Name        | Notes                                          |
|-----------|-------------|------------------------------------------------|
| EN        | /MCLR       |                                                |
| B0        | PGD         | This is called *PGED1* in the PIC's datasheet. |
| B1        | PGC         | This is caled *PGEC1* in the PIC's datasheet.  |

## Debug Accessory Mode
Debug Accessory Mode can be used to program the PIC via the USB connector but the details will depend upon the circuitry connected to the board.  This section is
a bit vague since doing this properly would involve a mux for the _SBU1_ routing and cable orientation detection, but it is possible to hack together something
simpler if you can guarantee correct connector orientation.  I have done this with a Raspberry Pi, Pickle, a USB Type-C connector breakout board and a 3D printed
enclosure - a PICKit won't work unless you provide an external power source for the +5V (the ICSP signals are +3.3V, and the *Rp* pull-ups need to be tied to a
+5V VBUS).

Programming the device as a Debug Accessory utilises the following USB pins:

| USB Pin  | Name | ICSP Pin | Description                                                                                                                       |
|----------|------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| Various  | VBUS |          | A +5V supply capable of providing current to whatever circuitry is attached.                                                      |
| Various  | GND  |          | Ground reference voltage, 0V.                                                                                                     |
| A8       | SBU1 | /MCLR    | Master Clear (active-low) - holds the PIC in reset, with all pins tri-stated.                                                     |
| B8       | SBU2 | USB Mux  | Can be left floating or pulled low for programming.  If high then _D+_ / _D-_ are routed as USB signals rather than ICSP signals. |
| A6 or B6 | D+   | PGD      | ICSP data - *when SBU2 is low or floating then this is a +3.3V CMOS signal, _NOT_ USB voltage levels*.                            |
| A7 or B7 | D-   | PGC      | ICSP clock - *when SBU2 is low or floating then this is a +3.3V CMOS signal, _NOT_ USB voltage levels*.                           |
| A5       | CC1  |          | Tied to the +5V VBUS via a pull-up resistor (*Rp*, see the USB Type-C Specifications) - typically 22k.                            |
| B5       | CC2  |          | Tied to the +5V VBUS via a pull-up resistor (*Rp*, see the USB Type-C Specifications) - typically 10k.                            |

Debug Accessory Mode requires a connector-to-connector mating because a USB Type-C cable only carries a single CC line.  This is why a custom widget needs to be
created if you wish to use this method of programming.
