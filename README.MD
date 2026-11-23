<div align="center">

# JioRouter AX6000 (`6101` / `6j01` / `6j11`) — OpenWrt Flashing Guide

[![Models](https://img.shields.io/badge/Models-6101%20%7C%206j01%20%7C%206j11-0078D4?style=flat-square)](#supported-models)
[![Platform](https://img.shields.io/badge/Platform-MediaTek%20Filogic%20%2F%20OpenWrt-00B5E2?style=flat-square)](#supported-models)
[![License](https://img.shields.io/badge/License-Custom%20Personal--Use-orange?style=flat-square)](./LICENSE)
[![YouTube](https://img.shields.io/badge/YouTube-%40the__diy__daddy-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@the_diy_daddy)

Commands, unlock guides, helper scripts, and UART pinout references for unlocking SSH and flashing **OpenWrt** on Jio AirFiber / JioRouter AX6000 (`6101`, `6j01`, and `6j11`) routers.

[Interactive Flashing Master-Chart](https://the-diy-daddy.github.io/jidu-openwrt-flashing-guide/) · [6j11 Guide](./6j11_instructions.md) · [6101 UART Commands](./6101_commands.md) · [Password Trick](./6j01_6j11_password_trick.md) · [UART Pinouts](./uart_pins/uart_read.md)

</div>

---

## Quick Navigation

| Resource | Description |
| :--- | :--- |
| **[Interactive Master-Chart](https://the-diy-daddy.github.io/jidu-openwrt-flashing-guide/)** | Visual step-by-step decision chart for choosing the right method per model & stock firmware |
| **[`6101_via_ssh.md`](./6101_via_ssh.md)** | Complete backup and SSH flashing commands for **`6101`** |
| **[`6j01_via_ssh.md`](./6j01_via_ssh.md)** | Complete backup and SSH flashing commands for **`6j01`** models (below) |
| **[`6j11_instructions.md`](./6j11_instructions.md)** | Full UART flashing instructions and partition backup steps for **`6j11`** models |
| **[`6101_commands.md`](./6101_commands.md)** | U-Boot / TFTP & UART serial flashing commands for **`JIDU6101`** (also works as UART fallback for `6j01`) |
| **[`6j01_6j11_password_trick.md`](./6j01_6j11_password_trick.md)** | Stock firmware password trick for unlocking root SSH access |
| **[`uart_pins/uart_read.md`](./uart_pins/uart_read.md)** | Visual UART pinout index (`TX`, `RX`, `GND`) for supported boards |


---

## Supported Models

> [!CAUTION]
> Always verify your exact router model from the rear hardware label before flashing. Flashing a firmware image meant for the wrong family (`6101` vs. `6j01` vs. `6j11`) can permanently brick the bootloader.

| Family | Supported Models | Guide | Notes |
| :--- | :--- | :--- | :--- |
| **`6101`** | `JIDU6101` | [`6101_commands.md`](./6101_commands.md) | MediaTek Filogic — supports SSH (where available) and UART/TFTP flashing across stock firmwares |
| **`6j01`** | `JIDU6201`, `JIDU6401`, `JIDU6601`, `JIDU6701` | [Below](#flashing-openwrt-on-6j01-via-ssh) | MediaTek Filogic — flash via SSH on supported stock firmware, or fall back to UART (`6101` method) |
| **`6j11`** | `JIDU6111`, `JIDU6411`, `JIDU6611`, `JIDU6811`, `JIDU6911` | [`6j11_instructions.md`](./6j11_instructions.md) | Follow the dedicated `6j11` guide for SSH unlock, full partition backups, and flashing |

---

## Repository Structure

```text
6j01_6j11/
├── README.md                       # Overview and 6j01 SSH flashing commands
├── 6101_commands.md                # U-Boot / TFTP UART commands for JIDU6101
├── 6j01_6j11_password_trick.md     # Administrative password trick for SSH access
├── 6j11_instructions.md            # Dedicated backup & flashing guide for 6j11 series
├── custom_breeze.sh                # Shell helper script (breeze.sh unlock workflow)
├── maxshell_daddy.py               # Python helper script for shell/unlock workflow
├── LICENSE                         # Custom Personal-Use License terms
└── uart_pins/
    ├── uart_read.md                # UART pinout gallery & connection notes
    ├── JIDU6111.jpg
    ├── JIDU6201.jpg
    ├── JIDU6401.jpg
    ├── JIDU6411.jpg
    ├── JIDU6601.jpg
    ├── JIDU6611.jpg
    ├── JIDU6811.jpg
    └── JIDU6911.jpg
```

---

## Unlock Workflow Overview

Depending on your model and installed stock firmware version, follow this escalation order (detailed in the [Master-Chart](https://the-diy-daddy.github.io/jidu-openwrt-flashing-guide/)):

1. **Attempt the maxshell_daddy.py** — Start with [`maxshell_daddy.md`](./maxshell_daddy.md) to obtain root SSH access without opening the router.
2. **Attempt the Password Trick** — Use [`6j01_6j11_password_trick.md`](./6j01_6j11_password_trick.md) to obtain root SSH access without opening the router if maxshell_daddy.py fails.
3. **Use Helper Scripts (If Password Trick Fails)** — Use [`custom_breeze.sh`](./custom_breeze.sh)
4. **Downgrade Stock Firmware (If Blocked)** — On newer patched stock firmwares where software SSH unlock is blocked, downgrade via WebUI (if signature upload is available) or via UART.
5. **UART / TFTP Fallback** — Connect a **3.3V** USB-to-TTL adapter using the board photos in [`uart_pins/`](./uart_pins/uart_read.md) and follow [`6101_commands.md`](./6101_commands.md) (for `6101`/`6j01`) or [`6j11_instructions.md`](./6j11_instructions.md) (for `6j11`).

---


## UART Pinouts

> [!WARNING]
> Always set your USB-to-TTL adapter to **3.3V** (never 5V) and **do not connect VCC** unless specifically required—connect only **TX**, **RX**, and **GND**.

See [`uart_pins/uart_read.md`](./uart_pins/uart_read.md) for the full visual gallery, or jump directly to your board photo:

| `6j01` Models | `6j11` Models |
| :--- | :--- |
| [JIDU6201](./uart_pins/JIDU6201.jpg) | [JIDU6111](./uart_pins/JIDU6111.jpg) |
| [JIDU6401](./uart_pins/JIDU6401.jpg) | [JIDU6411](./uart_pins/JIDU6411.jpg) |
| [JIDU6601](./uart_pins/JIDU6601.jpg) | [JIDU6611](./uart_pins/JIDU6611.jpg) |
| — | [JIDU6811](./uart_pins/JIDU6811.jpg) |
| — | [JIDU6911](./uart_pins/JIDU6911.jpg) |

---

## Video Guides & Resources

- **YouTube Channel:** [THE DIY DADDY (`@the_diy_daddy`)](https://www.youtube.com/@the_diy_daddy) — Full step-by-step SSH, UART, and OpenWrt setup tutorials
- **Flashing Compatibility Master-Chart:** [the-diy-daddy.github.io/jidu-openwrt-flashing-guide](https://the-diy-daddy.github.io/jidu-openwrt-flashing-guide/)

---

## Disclaimer

Flashing third-party firmware and modifying bootloader environment variables (`fw_setenv`) carries an inherent risk of bricking your hardware and may void your warranty. All scripts, commands, and documentation in this repository are provided as-is for educational and personal use on hardware you own. Always create and verify full partition backups before making changes—you proceed at your own risk.

---

## License

This project is licensed under a **Custom Personal-Use License** (commercial use and video creation are strictly prohibited) — see the [`LICENSE`](./LICENSE) file for full details.
