# Unlocking SSH Access with `maxshell_daddy.py`

This guide explains how to use [`maxshell_daddy.py`](./maxshell_daddy.py) on Windows to enable root SSH access on JioRouter AX6000 (`6j01` / `6j11`) routers running newer stock firmware versions (**`R3.0` and above**).

---

## How `maxshell_daddy.py` Works

On stock firmware `R3.0` and newer (such as `R3.2`, `R3.2.3`, and `R3.2.6`), earlier password-trick methods may be blocked. `maxshell_daddy.py` authenticates against your router's local web interface (`192.168.31.1`) using the admin login password you configure during initial setup and triggers the `-ssh` unlock workflow so you can log in as `root` over SSH without opening the router enclosure.

---

## Step 1: Connect to the Router & Check Firmware Version

1. Connect your PC to the router via an Ethernet cable (recommended) or Wi-Fi.
2. Open a web browser and go to **`https://192.168.31.1`**.
3. Complete the initial router setup and create a login password (for example: `Admin@07`).
4. Log in to the router's web dashboard and check the **current firmware version**.
5. Confirm that your router is running firmware **`R3.0` or above** (e.g., `R3.2`, `R3.2.3`, or `R3.2.6`) before continuing.

> [!NOTE]
> Remember the exact login password you set here—you will pass it to `maxshell_daddy.py` in Step 4.

---

## Step 2: Download `maxshell_daddy.py` & Open PowerShell

1. Download [`maxshell_daddy.py`](./maxshell_daddy.py) from this repository to your PC (for example, into your `Downloads` folder).
2. Press the **Windows key**, search for **PowerShell**, right-click **Windows PowerShell**, and select **Run as administrator**.
3. Navigate (`cd`) to the folder where you saved `maxshell_daddy.py`:

```powershell
cd "$env:USERPROFILE\Downloads"
```

*(Alternatively, specify the full path manually, e.g., `cd C:\Users\<your_username>\Downloads`.)*

---

## Step 3: Install Python 3 & Required Packages

### Install Python 3

Install Python 3 on Windows using **either** method below:

* **Option A — Microsoft Store:** Open the **Microsoft Store**, search for **Python 3**, and click **Install**.
* **Option B — PowerShell (`winget`):** Run the following command in your Administrator PowerShell window:

```powershell
winget install -e --id Python.Python.3.12
```

> [!IMPORTANT]
> If you installed Python using `winget`, **close and reopen PowerShell (as Administrator)** and `cd` back into your Downloads folder so that `python` and `pip` are recognized in your system `PATH`.

### Install Required Python Packages

Run the following commands in PowerShell to install the required dependencies:

```powershell
pip install requests
pip install pyreadline3
```

---

## Step 4: Run `maxshell_daddy.py` to Enable SSH

In your PowerShell window (inside the folder containing `maxshell_daddy.py`), run the script using the router admin password you set in Step 1.

Using the example password `Admin@07`:

```powershell
python3 maxshell_daddy.py admin:"Admin@07"@192.168.31.1 -ssh
```

> [!TIP]
> * Replace `Admin@07` with your actual router login password.
> * If Windows says `python3` is not recognized (or opens the Microsoft Store), run the same command using `python` instead:
>   ```powershell
>   python maxshell_daddy.py admin:"Admin@07"@192.168.31.1 -ssh
>   ```

Wait for the script to finish enabling SSH on the router.

---

## Step 5: Connect to the Router via SSH

1. Open a **new Command Prompt (`cmd`)** window.
2. Run the following command to clear any old cached SSH host key for `192.168.31.1` and connect as `root`:

```cmd
ssh-keygen -R 192.168.31.1 && ssh root@192.168.31.1
```

3. If prompted with *"Are you sure you want to continue connecting (yes/no/[fingerprint])?"*, type **`yes`** and press **Enter**.

Once connected, you will have a `root` shell on your router!

---

## Next Steps

Now that you have root SSH access, back up your stock partitions and proceed to the flashing guide for your router model:

* **`6j01` Models (`JIDU6201`, `JIDU6401`, `JIDU6601`, `JIDU6701`):** Follow [`6j01_via_ssh.md`](./6j01_via_ssh.md).
* **`6j11` Models (`JIDU6111`, `JIDU6411`, `JIDU6611`, `JIDU6811`, `JIDU6911`):** Follow this video https://youtu.be/7xkd3qDdVFA

---

## License

This project is licensed under a **Custom Personal-Use License** (Commercial use and video creation are strictly prohibited) — see the [LICENSE](LICENSE) file for details.

---

## Credits

* **Mahendra Mali (`for the original python script 'maxshell.py'`):**
* **The_DIY_Daddy (`for modifying the original python script 'maxshel.py' to make it work on latest firmwares`):**
