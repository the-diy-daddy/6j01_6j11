
**Flashing OpenWRT on a Qualcomm-based Jio Router (6j11)
Commands for JIDU 6111, 6411, 6611, 6811 and 6911**
===========================================
**To get List of partitions**

    cat /proc/mtd

**Backup the existing stock firmware so you can restore later if you want.**

    ssh root@192.168.1.1 "cat /dev/mtd23" > mtd23_rootfs.bin
    ssh root@192.168.1.1 "cat /dev/mtd24" > mtd24_rootfs1.bin

**To Flash Run:**

**New Terminal in PC:**

    scp -O openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6*11-initramfs-uImage.itb root@192.168.1.1:/tmp/

**Router ssh Terminal:**

    jioMfgData get all
**save the real output somewhere safe offline, and never share it publicly**

    jioMfgData init

 **Default Credentials After Reset, You need to connect your Router's UART pins to any USB-to-TTL Adaptor or ESP32 and use Putty to access Uboot**
 
 **Username: jidu6j11**
 
 **Password: TjJRa@pt6D)F3zg1**

    setenv ipaddr 192.168.1.2
    setenv serverip 192.168.1.1
    tftpboot openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-initramfs-uImage.itb

7. Boot the Initramfs Image

       bootm

 
**New Terminal in PC:**

    scp -O openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/

 ** upgrade system either through LuCI, or by transferring the file to /tmp/ and running:**

    sysupgrade /tmp/openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-squashfs-sysupgrade.bin

 **Fix “No Kernel Found” Error (Some IDU Models)**

    setenv mtdids nand0=nand0
    setenv mtdparts 'mtdparts=nand0:0xE100000@0x1700000(rootfs)'



========================================
**4. Restore stock partitions from backup:**

        mtd -e /dev/mtd23 write /tmp/mtd23_rootfs.bin /dev/mtd23
        mtd -e /dev/mtd24 write /tmp/mtd24_rootfs1.bin /dev/mtd24

**To fully revert to stock boot behavior, also fix the boot command:**

        setenv bootcmd 'bootipq'
        
**If you lose UART shell access, you may also need to restore the boot args:**

setenv bootargs 'console=ttyMSM0,115200n8 cnss2.bdf_pci1=0xb7 cnss2.bdf_integrated=0x30'
