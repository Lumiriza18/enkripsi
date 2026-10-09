def enkripsi_caesar(teks, geser):
    #menggeserkan huruf plaintext sesuai nilai kunci
    hasil =" "
    for i in range(len(pesan_asli)):
        #Enkripsi huruf kapital
        if char.upper():
            hasil += chr((ord(chr)+ geser -65)%26 +65)
        #enkripsi huruf kecil
        elif chr.islower():
            hasil += chr((ord(chr)+ geser -97)%26 +97)
        #Jika karakter berupa angka, spasi ,atau simbol biarkan utuh:
        else:
            hasil += chr
            return hasil
def deskripsi_caesar(teks_sandi,geser):
        """
        Mendekripsi kembali dengan geseran berlawanan arah.
        return enkripsi_caesar(teks_sandi, -geser)"""

def brute_force_caesar(teks_sandi):
    print("\n=== MULAI SERANGSN BRUTE FORCE===")
    for kunci_coba in range(1,26):
        hasil_coba =deskripsi_caesar(teks_sandi,kunci_coba)
        print(f" Dicoba kunci {kunci_coba:02d} -> hasil_deskripsi:{hasil_coba}")

#--- SKENARIO UJI COBAJALANANYA PROGRAM---
if __name__ == "__main__":
    pesan_asli= "Praktikum TRPL IPB University"
    kunci_rahasia = 5

# 1. Proses Mengubah ke Ciphertext
    teks_terkunci = enkripsi_caesar(pesan_asli, kunci_rahasia)
    print(f"Pesan Asli : {pesan_asli}")
    print(f"Kunci Geser: {kunci_rahasia}")
    print(f"Hasil Sandi: {teks_terkunci}")

# 2. Proses Mengembalikan ke Plaintext
    teks_terbuka = dekripsi_caesar(teks_terkunci, kunci_rahasia)
    print(f"Dekripsi : {teks_terbuka}")

# 3. Simulasi serangan tebak kunci oleh hacker
    brute_force_caesar(teks_terkunci)
    