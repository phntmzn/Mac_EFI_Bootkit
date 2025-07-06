; efi_payload.asm — UEFI x64 Hello World
; Assemble: nasm -f win64 efi_payload.asm -o efi_payload.obj

BITS 64
GLOBAL efi_main

section .text
efi_main:
    ; rcx = ImageHandle
    ; rdx = *SystemTable
    mov     rsi, rdx
    mov     rdi, [rsi + 64]         ; SystemTable->ConOut
    mov     rax, [rdi + 8]          ; ConOut->OutputString
    mov     rcx, rdi
    lea     rdx, [rel message]
    call    rax
    ret

section .data
    message:    dw "Hello from UEFI payload!", 13, 10, 0