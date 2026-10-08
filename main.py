import time
import urllib.request

BASE_URL = "https://raw.githubusercontent.com/owhami/pyqgisAutoMap/main/"


def runScript(nama_file):
    """Unduh file .py dari repo GitHub lalu jalankan di namespace yang sama."""
    url = f"{BASE_URL}{nama_file}?t={int(time.time())}"
    try:
        kode = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
    except Exception as e:
        print(f"Gagal mengunduh {nama_file}: {e}")
        return
    exec(compile(kode, nama_file, "exec"), globals())


runScript("ftth.py")