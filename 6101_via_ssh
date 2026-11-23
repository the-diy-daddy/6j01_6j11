## Flashing OpenWrt on `6101` via SSH

> **Applies to:** `JIDU6101` (MediaTek Filogic)  
> **For `6j01` models**, stop here and follow [`6j01_via_ssh.md`](./6j01_via_ssh.md).
> **For `6j11` models**, stop here and follow [`6j11_instructions.md`](./6j11_instructions.md).

### Prerequisites
- Root SSH access to the router at `192.168.31.1`
- OpenSSH client (`ssh` and `scp`) on your PC (Windows PowerShell/Terminal, Linux, or macOS)
- Matching OpenWrt `initramfs-factory.ubi` and `squashfs-sysupgrade.bin` files for your exact board

---

### Step 1: Retrieve & Save the U-Boot Password

> [!IMPORTANT]
> The U-Boot password is required if you ever need to flash via UART or restore stock firmware later. **Save it somewhere safe and do not share it publicly.**

Run these commands inside your **Router SSH Terminal**:

```bash
strings /dev/mtd7 | grep -i pass
```

```bash
/usr/bin/mfg_data get bootpass
```

If needed, inspect all readable strings in `mtd7`:

```bash
strings /dev/mtd7
```

---

### Step 2: Back Up Stock Partitions (Mandatory)

Verify the partition layout first in your **Router SSH Terminal**:

```bash
cat /proc/mtd
```

Then open a **New Terminal on your PC** and run the following commands one by one to back up every stock partition locally:

```bash
ssh root@192.168.31.1 "cat /dev/mtd1" > mtd1_BL2.bin
ssh root@192.168.31.1 "cat /dev/mtd2" > mtd2_uboot_env.bin
ssh root@192.168.31.1 "cat /dev/mtd3" > mtd3_Factory.bin
ssh root@192.168.31.1 "cat /dev/mtd4" > mtd4_FIP.bin
ssh root@192.168.31.1 "cat /dev/mtd5" > mtd5_ubi.bin
ssh root@192.168.31.1 "cat /dev/mtd6" > mtd6_ubi2.bin
ssh root@192.168.31.1 "cat /dev/mtd7" > mtd7_MFG.bin
ssh root@192.168.31.1 "cat /dev/mtd8" > mtd8_Jio_Reserved.bin
```

> [!TIP]
> Confirm all 8 `.bin` files are non-empty on your PC before proceeding to Step 3.

---

### Step 3: Flash OpenWrt `initramfs` Image

Copy the `initramfs-factory.ubi` firmware to the router from a **New Terminal on your PC** *(update the filename if you are flashing `6101`)*:

```bash
scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6101-initramfs-factory.ubi root@192.168.31.1:/tmp/
```

Switch to your **Router SSH Terminal** and run these commands one by one:

```bash
ubidetach -m 6
ubiformat /dev/mtd6 -y -f /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6101-initramfs-factory.ubi
fw_setenv bootcmd 'ubi detach; ubi part ubi2; ubi read 46000000 kernel; fdt addr $(fdtcontroladdr); fdt rm /signature; bootm 0x46000000'
fw_setenv dual_boot.current_slot 1
fw_setenv dual_boot.slot_0_invalid 1
fw_setenv dual_boot.slot_1_invalid 1
fw_setenv ipaddr
reboot
```

Wait for the router to reboot into OpenWrt `initramfs`. Its default IP address will change from `192.168.31.1` to **`192.168.1.1`**.

---

### Step 4: Flash Permanent OpenWrt (`sysupgrade`)

Once the router is reachable at `192.168.1.1`, copy the `sysupgrade` image from a **New Terminal on your PC**:

```bash
scp -O openwrt-mediatek-filogic-jiorouter_ax6000-jidu6101-squashfs-sysupgrade.bin root@192.168.1.1:/tmp/
```

Then run `sysupgrade` inside your **Router SSH Terminal**:

```bash
sysupgrade /tmp/openwrt-mediatek-filogic-jiorouter_ax6000-jidu6101-squashfs-sysupgrade.bin
```

Wait a few minutes for the flash and reboot to complete. You can then access OpenWrt LuCI at `http://192.168.1.1`.

---
