import random
import time

daftar_perasaan = ["sedih"," bahagia"," rindu"," kesepian"," bete"," malas"," lapar"]
perasaan_rahasia = random.choice(daftar_perasaan)
percobaan = 0
batas_percobaan = 3

print("=== GAME: Tebak Perasaan Uyu ==="); time.sleep(0.8)
print("Apa yang sedang Uyu rasakan saat ini?")
print("Mari menebak bersama!")
print(f"Pilihan: {','.join(daftar_perasaan)}")
print(f"Kamu punya {batas_percobaan} kesempatan, gunakan sebaik mungkin. Semoga berhasil!")

while True:
    tebakan = input("Tebakanmu: ").lower().strip()
    percobaan += 1
    if tebakan == "":
        print("Ups! Kamu belum mengetik apapun, coba isi dulu ya!")
        continue

    if tebakan == perasaan_rahasia:
        print(f"Selamat tebakanmu benar! Uyu sedang merasa {perasaan_rahasia}.")
        print(f"Wow keren! Kamu menebak dengan benar dalam {percobaan} percobaan!")
        break
    elif tebakan not in ["sedih","bahagia","rindu","kesepian","bete","malas"]:
        print("Masukkan jawaban yang valid. Coba lagi!")
    else:
        print("O-oh! Sayang sekali tebakanmu belum tepat... coba tebak lagi ya~")

    if percobaan >= batas_percobaan:
        print(f"Yah... Kesempatanmu habis! Uyu sebenarnya sedang merasa {perasaan_rahasia}.")
        break

print("Terima kasih sudah bermain!")