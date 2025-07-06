
import subprocess
import plistlib

def get_all_disks():
    """
    Returns a list of all disk identifiers and their metadata using diskutil.
    """
    result = subprocess.run(["diskutil", "list", "-plist"], capture_output=True)
    plist = plistlib.loads(result.stdout)
    return plist.get("AllDisksAndPartitions", [])

def find_efi_partitions():
    """
    Returns a list of EFI partitions and their identifiers.
    """
    efi_partitions = []
    for disk in get_all_disks():
        for part in disk.get("Partitions", []):
            if part.get("Content") == "EFI":
                efi_partitions.append({
                    "Disk": disk["DeviceIdentifier"],
                    "Partition": part["DeviceIdentifier"],
                    "MountPoint": part.get("MountPoint", None)
                })
    return efi_partitions

if __name__ == "__main__":
    print("[*] EFI Partitions:")
    for efi in find_efi_partitions():
        print(f"  Disk: {efi['Disk']}  Partition: {efi['Partition']}  Mount: {efi['MountPoint']}")