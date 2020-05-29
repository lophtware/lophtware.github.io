# Quirks
## Microsoft Windows / Number of Device Configurations
In Windows, the USB Generic Parent Driver (usbccgp.sys) does not get loaded for composite devices with more than one configuration.  Instead, the device is given to
the USB HID driver based on the first interface, which cannot handle composite devices.  The magic around this behaviour is hard to find, the price paid being a day of
head scratching and profanities, but it is alluded to [here](https://lore.kernel.org/patchwork/patch/211772/).  To work around this limitation you can:
  1. Supply a custom driver INF file.
  2. Set `NUMBER_OF_CONFIGURATIONS` in [src/Usb/usb_config.h](https://github.com/lophtware/UsbCPic32Breakout/blob/master/src/firmware/src/Usb/usb_config.h) to `1`.
  3. Crank up the configurations and not bother to connect the device to a Windows box.

Each workaround is a compromise, but option _2_ has been chosen as the default.  This reasoning is that the emphasis for the stock firmware is that the device should
just work reliably out of the box with minimal configuration, because we want a quick and easy breadboarding and prototyping solution.  If this wasn't the main design
goal then HID wouldn't have been chosen in the first place.

## NCP367 Current Limiting High / Low Range
Whilst the current can be limited to 500mA (typical), when that limit is exceeded the board will be reset, the intention being that the fault is hopefully cleared.
However, the default reset state limits the current to 1.5A (typical), so after the initial 500mA trip-and-reset cycle, the higher limit again takes hold.  The
default state cannot be set to 500mA without a pull-up, which would necessitate a discrete transistor being squeezed onto the board to protect the microcontroller
from potentially destructive voltages.  The design decision was to forego the transistor, although this might have been a bit of a braindead decision...

The pin is connected but is not actively used by the default firmware as there is little point - if a device, say, enumerates as taking 100mA then even the 500mA trip
would be overly permissive.  So the function of the current limiting is really to ensure that short-circuits are protected against (to a dregree), and firmware glitches
that cause excessive current draw are corrected by a reset, rather than being a substitute for the proper design of the attached circuit to ensure the self-declared
limits are respected.
