Penjelasan Singkat

D4.
Tentukan posisi tengah.
Gambar berukuran 255x255 pixel, dengan indeks di python dimulai dari 0 sehingga titik tengah dari gambar ada di pixel ke (127,127)
Buat loop i dari 0 sampai 128 (dari atas ke bawah)
Buat loop j dari 0 sampai 127 (dari kiri ke kanan)
Buat pixel sesuai jarak dari titik pixel sekarang ke posisi (127,127)
Lalu, gabungkan pixel secara horizontal sehingga terbentuk sebuah image (misal = a) di indeks ke-i sebanyak 126 pixel ke kanan
Tambahkan variabel untuk membalik image yang sudah digabung (misal = balik)
Tambahkan pixel di indeks ke (i,127) (misal = isi)
Gabung a, isi, dan balik secara horizontal sehingga terbentuk sebuah image di indeks ke-i sebanyak 255 pixel
Lakukan hal yang sama untuk membuat image sampai ke bawah

D5b.
Hanya keluarkan rumus t = sqrt(2*h/g)

D5c.
Setelah mendapatkan input dari user, convert semua angka tersebut menjadi radian
Gunakan rumus Haversine untuk mencari jarak antara dua titik tersebut

D6.
Waktu yang diperlukan benda untuk sampai tanah bisa menggunakan rumus t = sqrt(2*h/g)
Kemudian, cari jarak yang ditempuh benda jika benda dijatuhkan dari ketinggian tertentu dan dengan kecepatan tertentu menggunakan dist = v*t
Posisi yang perlu diperlukan pesawat menjatuhkan benda agar benda dapat mengenai target adalah posisi target dikurangi jarak yang ditempuh benda (xPf = xT - dist)
Jarak yang diperlukan pesawat untuk mencapai ke posisi tersebut adalah (jarak = xPf - xPi)
