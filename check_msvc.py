import ctypes

for dll in ("vcruntime140.dll", "vcruntime140_1.dll", "msvcp140.dll"):
    try:
        ctypes.WinDLL(dll)
        print(f"{dll} loaded OK")
    except Exception as e:
        print(f"{dll} failed: {e}")
