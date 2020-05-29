# Core Interface
The Core Interface allows the Host to control and configure all but one of the twelve non-power pins exposed on the device's GPIO header.
The `/MCLR` pin is a dedicated digital input that resets the device and controls [In-Circuit Serial Programming (ICSP)](../../Icsp.md),
and is thus not available for configuration.

See the [HID Interface](Hid.md) page for a description of the available reports.

## Device Configurations
There can be up to four device configurations, although the default firmware only enables one through the USB interface due to some
[quirks](../../Quirks.md) with the Windows HID drivers.  The device configurations can be manipulated and set through this interface and
are intended to allow different modes of operation under different scenarios.  This facilitates using the device on several projects and
prototypes at once without having to reprogram or reconfigure it each time, or perhaps a different configuration when plugged into a USB
charger vs. a USB Host.

## Pin Configurations
Each pin can be used digitally as a General-Purpose Input / Output (GPIO) or assigned a particular function provided by one of the
USB Interfaces.  Some functions are only available on specific pins, but all pins except `/MCLR` are GPIO-capable.  Of these
GPIO-capable pins, all except the I<sup>2</sup>C-capable `SCL` and `SDA` can have weak pull-ups or pull-downs associated with them.

### Digital GPIO Features
#### Direction

| Direction                       | Description                                                              |
|---------------------------------|--------------------------------------------------------------------------|
| Input                           | The pin is a dedicated input.  Logic levels only, do not allow to float. |
| Output                          | The pin is a dedicated output, either open-drain or push-pull.           |
| Bi-Directional (Default Input)  | The pin direction can be toggled, but defaults to an input at power-on.  |
| Bi-Directional (Default Output) | The pin direction can be toggled, but defaults to an output at power-on. |

#### Suspend Behaviour
Each pin can have a different behaviour when the device enters Suspend Mode, whether it is assigned as GPIO or to one of the device interfaces.
When the device exits Suspend Mode the pre-Suspend settings are restored.

| Suspend Behaviour | Description                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Unchanged         | No action taken on the pin, it will retain the configuration and values prior to entering suspend, including interface / function assignment. |
| Input             | When the device is suspended the pin will become an input.                                                                                    |
| Output Low        | The pin will switch to an output and will be driven low.                                                                                      |
| Output High       | The pin will switch to an output and will be driven high (push-pull) or high-impedance (open-drain).                                          |

#### Default Latch Value

| Default Latch Value | Description                                                                      |
|---------------------|----------------------------------------------------------------------------------|
| 0                   | The output latch will be reset to 0 at power-on.  For inputs this has no effect. |
| 1                   | The output latch will be set to 1 at power-on.  For inputs this has no effect.   |

#### Open-Drain
Outputs can be push-pull, where both high and low states are actively driven, or open-drain where the output is either pulled low or left
high-impedance.  Push-pull should be used only for outputs that are not connected to other outputs.  Open-drain allows more than one output
to be connected together but requires pull-up resistors.  The pull-ups can be either internal or external to the device.

#### Pull-Ups and Pull-Downs
All device pins except the I<sup>2</sup>C `SCL` and `SDA` pins can have on-chip weak pull-ups enabled; the I<sup>2</sup>C pins have discrete
3.3k resistors.  Pull-ups and pull-downs can be useful for pins that are assigned as open-drains or that may float.  Be aware that pull-ups and
pull-downs may violate USB Suspend current limitations.

#### Interrupt-on-Change
Interrupts can be configured for changes in state.  They can also be configured to wake the device from Suspend (ie. USB Remote Wake).

| Interrupt On  | Description                                                               |
|---------------|---------------------------------------------------------------------------|
| None          | An interrupt will not be generated when an input transitions.             |
| Positive Edge | An interrupt can be generated when an input transitions from low-to-high. |
| Negative Edge | An interrupt can be generated when an input transitions from high-to-low. |
| Both          | An interrupt can be generated when an input transitions to high or low.   |

| Interrupt Mode | Description                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------|
| One-Shot       | Only one interrupt will be generated and further transitions will be ignored until a flag is reset. |
| Continuous     | Every transition will generate an interrupt.                                                        |

### Functional Assignment
Each pin can be assigned a specific function from one of the device's available USB Interfaces.  For example, a pin might be assigned to be
a *Slave Select* line on the SPI bus or an input to the ADC.  The available interfaces and functions are pin-specific and are documented on
the pin-specific configuration pages.

Note that when the device enters Suspend Mode, the configuration specified by [Suspend Behaviour](#suspend-behaviour) will be applied,
regardless of the interface / function settings.
