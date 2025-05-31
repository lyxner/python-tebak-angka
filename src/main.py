import random

def main():
    print("=== Selamat datang di permainan Tebak Angka ===")
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input("Masukkan tebakan (1–100): "))
            percobaan += 1
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Tebakan Anda benar setelah {percobaan} kali percobaan.")
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat antara 1–100.")

if __name__ == "__main__":
    main()
