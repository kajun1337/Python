import ctypes
import psutil

# Windows API sabitleri
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

# Windows API fonksiyonları
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

OpenProcess = kernel32.OpenProcess
VirtualQueryEx = kernel32.VirtualQueryEx
ReadProcessMemory = kernel32.ReadProcessMemory
CloseHandle = kernel32.CloseHandle

# MEMORY_BASIC_INFORMATION yapısı
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),
        ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_ulong),
        ("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_ulong),
        ("Protect", ctypes.c_ulong),
        ("Type", ctypes.c_ulong),
    ]

def get_process_pid(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return proc.info['pid']
    return None

def read_process_memory(pid):
    # İşlemi aç
    process_handle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not process_handle:
        raise Exception("Process açılamadı")

    # Bellek sorgulama ve okuma
    memory_info = MEMORY_BASIC_INFORMATION()
    address = 0
    while VirtualQueryEx(process_handle, ctypes.c_void_p(address), ctypes.byref(memory_info), ctypes.sizeof(memory_info)):
        base_address = memory_info.BaseAddress
        region_size = memory_info.RegionSize

        # Bellek adresinin None olup olmadığını kontrol et
        if base_address is not None and region_size > 0:
            print(f"Bellek Bölgesi: 0x{base_address:016X} - 0x{(base_address + region_size):016X}")
        else:
            print(f"Geçersiz bellek bölgesi: {base_address}")
        
        # Bir sonraki bellek bölgesine geç
        address += region_size

    # İşlemi kapat
    CloseHandle(process_handle)

if __name__ == '__main__':
    process_name = "Lightshot.exe"  # Hedef işlem
    pid = get_process_pid(process_name)
    if pid:
        print(f"PID: {pid}")
        read_process_memory(pid)
    else:
        print(f"{process_name} bulunamadı.")


