# 🧬 mac_efi_bootkit

An educational EFI bootkit project for macOS that demonstrates the construction, deployment, and testing of UEFI shellcode. The toolkit includes:

- 🧱 A shellcode builder (`builder.py`)
- 🗂 A FAT32 EFI System Partition injector (`injector.py`)
- 💾 Tools to extract and inspect ESP contents
- 🔬 Unit tests and safety guidelines

⚠️ **WARNING: This is for educational use only on authorized systems. Misuse may cause irreversible damage.**

---

## 📁 Directory Structure

```
mac_efi_bootkit/
├── bootkit/
│   ├── builder.py          # Wraps raw shellcode in PE/COFF
│   ├── injector.py         # Mounts and patches ESP
│   ├── fs_utils.py         # FAT32 mount and patch logic
│   ├── uefi_structs.py     # UEFI data structures
│   ├── efi_payload.asm     # NASM x64 shellcode (UEFI entrypoint)
│   └── efi_payload.bin     # Flat binary output
│
├── tools/
│   ├── nasm_compile.py     # Assembles efi_payload.asm
│   ├── esp_extractor.py    # Mounts and copies ESP to folder
│   ├── device_info.py      # Lists EFI volumes and partitions
│   └── firmware_injector.py # Firmware DXE injection & SPI flash automation
│
├── scripts/
│   ├── build_bootkit.sh    # Automates build + injection
│   └── launch_vm.sh        # Boot EFI in QEMU + OVMF
│
├── tests/                  # Unit tests using unittest + mock
├── docs/
│   ├── architecture.md
│   └── safety_guidelines.md
├── requirements.txt
└── setup.py
```

---

## ⚙️ Setup

1. Install dependencies:

```bash
brew install nasm qemu
pip install -r requirements.txt
```

2. Assemble payload:

```bash
python3 tools/nasm_compile.py
```

3. Build EFI binary:

```bash
python3 -c "from bootkit import builder; builder.build_efi_image('bootkit/efi_payload.bin', 'bootkit/BOOTX64.EFI')"
```

4. Inject to ESP:

```bash
sudo python3 -m bootkit.injector
```

---

## 🧪 Test in VM

```bash
bash scripts/launch_vm.sh
```

Requires `OVMF_CODE.fd` and `OVMF_VARS.fd` in `/usr/local/share/OVMF/`.

---

## 🧼 Extract Existing ESP

```bash
python3 tools/esp_extractor.py
```

---

## ✅ Running Tests

```bash
pytest tests/
```

---

## ⚠️ Disclaimer

This toolkit includes low-level firmware interaction tools that can irreversibly alter your hardware. It is for academic use **only** on test machines or virtual environments.

Do not attempt real-world deployment without full understanding of UEFI internals, SPI flash layout, and platform-specific protections.

The authors are not responsible for damage, data loss, or unintended behavior caused by use or misuse. See [docs/safety_guidelines.md](docs/safety_guidelines.md).
