Flash Openwrt in Jio Router JIDU6401, JIDU6201, JIDU6601, JIDU6701, JIDU6111, JIDU6411, JIDU6611, JIDU6811, JIDU6911 using SSH


================================================
Flashing OpenWRT on a Mediatek-based Jio Router (6j01)
Commands for JIDU 6201, 6401, 6601, 6701
================================================

**To get List of partitions

cat /proc/mtd

**Backup the existing stock firmware so you can restore later if you want.
**New Terminal in PC:

ssh root@192.168.31.1 "cat /dev/mtd1" > mtd1_BL2.bin
ssh root@192.168.31.1 "cat /dev/mtd2" > mtd2_uboot_env.bin
ssh root@192.168.31.1 "cat /dev/mtd3" > mtd3_Factory.bin
ssh root@192.168.31.1 "cat /dev/mtd4" > mtd4_FIP.bin
ssh root@192.168.31.1 "cat /dev/mtd5" > mtd5_ubi.bin
ssh root@192.168.31.1 "cat /dev/mtd6" > mtd6_ubi2.bin
ssh root@192.168.31.1 "cat /dev/mtd7" > mtd7_MFG.bin
ssh root@192.168.31.1 "cat /dev/mtd8" > mtd8_Jio_Reserved.bin


**To Flash:

**New Terminal in PC:

scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-initramfs-factory.ubi root@192.168.31.1:/tmp/

**Router ssh Terminal:

ubidetach -m 6
ubiformat /dev/mtd6 -y -f /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-initramfs-factory.ubi
fw_setenv bootcmd 'ubi detach; ubi part ubi2; ubi read 46000000 kernel; fdt addr $(fdtcontroladdr); fdt rm /signature; bootm 0x46000000'
fw_setenv dual_boot.current_slot 1
fw_setenv dual_boot.slot_0_invalid 1
fw_setenv dual_boot.slot_1_invalid 1
fw_setenv ipaddr
reboot

192.168.1.1

**New Terminal in PC:

scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/

**Router ssh Terminal:

sysupgrade /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6j01-squashfs-sysupgrade.bin



===========================================
Flashing OpenWRT on a Qualcomm-based Jio Router (6j11)
Commands for JIDU 6111, 6411, 6611, 6811 and 6911
===========================================
**To get List of partitions

cat /proc/mtd

**Backup the existing stock firmware so you can restore later if you want.

ssh root@192.168.1.1 "cat /dev/mtd23" > mtd23_rootfs.bin
ssh root@192.168.1.1 "cat /dev/mtd24" > mtd24_rootfs1.bin

**To Flash Run:
**New Terminal in PC:

scp -O openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6*11-initramfs-uImage.itb root@192.168.1.1:/tmp/

**Router ssh Terminal:

jioMfgData get all
         **save the real output somewhere safe offline, and never share it publicly
jioMfgData init
      **Default Credentials After Reset
      **Username: jidu6j11
      **Password: TjJRa@pt6D)F3zg1
setenv ipaddr 192.168.1.2
setenv serverip 192.168.1.1
tftpboot openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-initramfs-uImage.itb
 
**New Terminal in PC:

scp -O openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/

 ** upgrade system either through LuCI, or by transferring the file to /tmp/ and running:
sysupgrade /tmp/openwrt-qualcommbe-ipq95xx-jiorouter-ax6000-jidu6j11-squashfs-sysupgrade.bin

 **Fix “No Kernel Found” Error (Some IDU Models)
setenv mtdids nand0=nand0
setenv mtdparts 'mtdparts=nand0:0xE100000@0x1700000(rootfs)'



========================================
4. Restore stock partitions from backup:

mtd -e /dev/mtd23 write /tmp/mtd23_rootfs.bin /dev/mtd23
mtd -e /dev/mtd24 write /tmp/mtd24_rootfs1.bin /dev/mtd24
**To fully revert to stock boot behavior, also fix the boot command:

setenv bootcmd 'bootipq'
**If you lose UART shell access, you may also need to restore the boot args:

setenv bootargs 'console=ttyMSM0,115200n8 cnss2.bdf_pci1=0xb7 cnss2.bdf_integrated=0x30'
