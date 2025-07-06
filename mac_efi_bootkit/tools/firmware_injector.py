import subprocess
import os
import shutil

ROM_DUMP = "rom.bin"
MODIFIED_ROM = "patched.rom"
DXE_DRIVER = "MyDriver.efi"
UEFI_TOOL = "/usr/local/bin/UEFITool"  # or wherever UEFITool is installed

def run(cmd):
    print(f"[>] {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def dump_firmware():
    print("[*] Dumping SPI flash firmware using Chipsec...")
    run("chipsec_util spi dump {}".format(ROM_DUMP))

def backup_original():
    if os.path.exists(ROM_DUMP):
        shutil.copy(ROM_DUMP, "rom_backup.bin")
        print("[+] Backup created: rom_backup.bin")

def inject_dxe_driver():
    print("[*] Injecting DXE driver into ROM...")
    if not os.path.exists(DXE_DRIVER):
        raise FileNotFoundError(f"{DXE_DRIVER} not found")

    # You must use UEFITool or UEFIReplace externally to inject the driver
    print("[!] Manual step required: use UEFITool to inject MyDriver.efi into rom.bin")
    print("    Example (GUI): Add as FFS to DXE volume, then save as patched.rom")
    input("    Press Enter after injection and saving as patched.rom...")

def flash_firmware():
    if not os.path.exists(MODIFIED_ROM):
        raise FileNotFoundError(f"{MODIFIED_ROM} not found")

    print("[*] Flashing modified firmware back to SPI chip...")
    run(f"flashrom -p internal -w {MODIFIED_ROM}")

def main():
    dump_firmware()
    backup_original()
    inject_dxe_driver()
    flash_firmware()
    print("[✓] Firmware implant process completed. Reboot to test.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] Error: {e}")
