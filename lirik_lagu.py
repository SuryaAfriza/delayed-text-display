import time
import sys

def kalkulator_talk_bagian(teks_berdelay):
    for bagian, delay in teks_berdelay:
        for huruf in bagian:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(delay)
    print()

semua_teks = [
    [("sudah terbiasa terjadi ", 0.10), ("tante", 0.15)],
    [("teman datang ketika lagi butuh ", 0.08), ("saja", 0.12)],
    [("coba kalau lagi ", 0.1), ("susah", 0.12)],
    [("mereka semua ", 0.09), ("menghilaaangggg..........", 0.18)]
]

for kalimat in semua_teks:
    kalkulator_talk_bagian(kalimat)
    time.sleep(0.09)
