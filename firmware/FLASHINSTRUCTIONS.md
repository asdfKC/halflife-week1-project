# Flashing the firmware

The macro pad runs on KMK on CircuitPython on a Raspberry Pi Pico.

1. Download the CircuitPython .uf2 file from circuitpython.org/board/raspberry_pi_pico
2. Before plugging the Pi in, hold the BOOTSEL button, then plug the USB. Continue holding the button while plugging it in. A drive should appear on your computer.
3. Copy the .uf2 file onto that drive; the Pico should reboot and show a new drive called CIRCUITPY.
4. Download KMK from github.com/KMKfw/kmk_firmware and copy its `kmk` folder onto CIRCUITPY.
5. Copy firmware/code.py from this repo onto the CIRCUITPY drive. It should be called code.py
6. The board should restart itself. Press SW1 (switch 1) to test; it should copy.

If a key does the wrong thing, check the keymap in code.py. Switches SW1-SW18 are wired to GP0-GP17 in order. (as mentioned in the readme.me)
