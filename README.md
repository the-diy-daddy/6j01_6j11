Flash Openwrt in Jio Router JIDU6401, JIDU6201, JIDU6601, JIDU6701, JIDU6111, JIDU6411, JIDU6611, JIDU6811, JIDU6911 using SSH
=====================

*For 6J11 visit:*

https://github.com/the-diy-daddy/6j01_6j11/blob/main/6j11_instructions.md



****Flashing OpenWRT on a Mediatek-based Jio Router (6j01)
Commands for JIDU 6201, 6401, 6601, 6701****
==========================================================

***To get List of partitions***

    cat /proc/mtd

*Backup the existing stock firmware so you can restore later if you want.*
**Run these commands one by one**

**New Terminal in PC:**

    ssh root@192.168.31.1 "cat /dev/mtd1" > mtd1_BL2.bin
    ssh root@192.168.31.1 "cat /dev/mtd2" > mtd2_uboot_env.bin
    ssh root@192.168.31.1 "cat /dev/mtd3" > mtd3_Factory.bin
    ssh root@192.168.31.1 "cat /dev/mtd4" > mtd4_FIP.bin
    ssh root@192.168.31.1 "cat /dev/mtd5" > mtd5_ubi.bin
    ssh root@192.168.31.1 "cat /dev/mtd6" > mtd6_ubi2.bin
    ssh root@192.168.31.1 "cat /dev/mtd7" > mtd7_MFG.bin
    ssh root@192.168.31.1 "cat /dev/mtd8" > mtd8_Jio_Reserved.bin


*To Flash:*

**New Terminal in PC:**

    scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-initramfs-factory.ubi root@192.168.31.1:/tmp/

**Router ssh Terminal:**

    ubidetach -m 6
    
    ubiformat /dev/mtd6 -y -f /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-initramfs-factory.ubi
    
    fw_setenv bootcmd 'ubi detach; ubi part ubi2; ubi read 46000000 kernel; fdt addr $(fdtcontroladdr); fdt rm /signature; bootm 0x46000000'
    
    fw_setenv dual_boot.current_slot 1
    
    fw_setenv dual_boot.slot_0_invalid 1
    
    fw_setenv dual_boot.slot_1_invalid 1
    
    fw_setenv ipaddr
    
    reboot

**New Terminal in PC:**

    scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/

**Router ssh Terminal:**

    sysupgrade /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-squashfs-sysupgrade.bin





