def tower_of_hanoi(n, asal, tujuan, bantuan):
    """
    n       : Jumlah piringan
    asal    : Tiang awal (Variabel A)
    tujuan  : Tiang akhir (Variabel C)
    bantuan : Tiang sementara (Variabel B)
    """
    
    # KONDISI BERHENTI (Base Case)
    # Jika hanya ada 1 piringan, langsung pindahkan dari tiang asal ke tujuan
    if n == 1:
        print(f"Pindahkan piringan 1 dari {asal} ke {tujuan}")
        return
    
    # LANGKAH 1: Pindahkan (n-1) piringan di atas ke tiang bantuan (B)
    # Tiang tujuan (C) sementara bertugas sebagai tiang bantuan
    tower_of_hanoi(n-1, asal, bantuan, tujuan)
    
    # LANGKAH 2: Pindahkan piringan paling besar (bawah) ke tiang tujuan (C)
    print(f"Pindahkan piringan {n} dari {asal} ke {tujuan}")
    
    # LANGKAH 3: Pindahkan (n-1) piringan dari tiang bantuan (B) ke tiang tujuan (C)
    # Tiang asal (A) sekarang bertugas sebagai tiang bantuan
    tower_of_hanoi(n-1, bantuan, tujuan, asal)

# --- BAGIAN EKSEKUSI ---
# Kita mainkan dengan 3 piringan
# A = Tiang Asal, C = Tiang Tujuan, B = Tiang Bantuan
print("Urutan langkah penyelesaian Tower of Hanoi:")
tower_of_hanoi(3, 'A', 'C', 'B')