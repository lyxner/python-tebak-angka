import random

def main():
    print("=== Selamat datang di permainan Tebak Angka ===")
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    batas_percobaan = 10              # ← ini baris baru: menetapkan batas percobaan

    while percobaan < batas_percobaan:
        try:
            tebakan = int(input(f"Percobaan ke-{percobaan+1}/{batas_percobaan}. Masukkan tebakan (1–100): "))
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Tebakan Anda benar setelah {percobaan} kali percobaan.")
                return
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat antara 1–100.")

    # Jika loop selesai tanpa return, artinya batas percobaan habis
    print(f"Maaf, kesempatan Anda sudah habis. Angka rahasia: {angka_rahasia}")

if __name__ == "__main__":
    main()
