def enkripsi_caesar(teks, geser):
    # Menggunakan string kosong, bukan spasi, agar hasil awalnya bersih
    hasil = "" 
    
    # Membaca per karakter dari 'teks' yang dimasukkan
    for char in teks:
        # Cek apakah huruf kapital
        if char.isupper():
            hasil += chr((ord(char) + geser - 65) % 26 + 65)
        # Cek apakah huruf kecil
        elif char.islower():
            hasil += chr((ord(char) + geser - 97) % 26 + 97)
        # Jika karakter berupa angka, spasi, atau simbol biarkan utuh
        else:
            hasil += char
            
    # Posisi return HARUS sejajar dengan 'for', di luar perulangan
    return hasil

def dekripsi_caesar(teks_sandi, geser): # Typo diperbaiki menjadi 'dekripsi'
    # Keluarkan rumus dari tanda kutip agar mesin mau mengerjakannya
    return enkripsi_caesar(teks_sandi, -geser)

def brute_force_caesar(teks_sandi):
    print("\n=== MULAI SERANGAN BRUTE FORCE ===")
    for kunci_coba in range(1, 26):
        hasil_coba = dekripsi_caesar(teks_sandi, kunci_coba)
        print(f"Dicoba kunci {kunci_coba:02d} -> hasil_dekripsi: {hasil_coba}")

# --- SKENARIO UJI COBA JALANNYA PROGRAM ---
if __name__ == "__main__":
    pesan_asli = "Praktikum TRPL IPB University"
    kunci_rahasia = 5

    # 1. Proses Mengubah ke Ciphertext
    teks_terkunci = enkripsi_caesar(pesan_asli, kunci_rahasia)
    print(f"Pesan Asli : {pesan_asli}")
    print(f"Kunci Geser: {kunci_rahasia}")
    print(f"Hasil Sandi: {teks_terkunci}")

    # 2. Proses Mengembalikan ke Plaintext
    teks_terbuka = dekripsi_caesar(teks_terkunci, kunci_rahasia)
    print(f"Dekripsi   : {teks_terbuka}")

    # 3. Simulasi serangan tebak kunci oleh hacker
    brute_force_caesar(teks_terkunci)