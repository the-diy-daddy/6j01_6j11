1. Set a static IP on the ethernet interface.

2. Setup TFTP server.

3. Connect the serial port with USB to TTL adapter.

Make sure that the usb-ttl adapter is set to 3.3v (connect jumper plug between vcc and 3.3v)

4. Setup Putty.

5. Start the initial boot.

6. Flash the kernel.bin file into the router.

**Once you are in the U-Boot command prompt, run these commands one by one.**

    setenv ipaddr 192.168.1.1
  
    setenv serverip 192.168.1.2

    tftpboot 0x46000000 openwrt-25.12.5-mediatek-filogic-jiorouter_ax6000-jidu6101-initramfs-kernel.bin

    fdt addr $(fdtcontroladdr)
  
    fdt rm /signature
  
    bootm

7. Flash the sysupgrade.bin File using Luci.

---

## License

This project is licensed under a **Custom Personal-Use License** (Commercial use and video creation are strictly prohibited) — see the [LICENSE](LICENSE) file for details.
