# Information Retrieval: Recipe Analysis

Analisis kemiripan resep masakan Indonesia menggunakan teknik Information Retrieval dan text vectorization dengan Python.

## Deskripsi Project

Project ini mengimplementasikan sistem analisis resep yang dapat:

- Membandingkan kemiripan antar resep berdasarkan bahan-bahan
- Mengidentifikasi bahan unik dan umum dalam dataset resep
- Melakukan pencarian resep berdasarkan query bahan tertentu
- Menganalisis pola penggunaan bahan dalam masakan Indonesia

## Dataset

Dataset terdiri dari 4 resep masakan Indonesia tradisional:

1. **Soto** - Sup ayam dengan bumbu tradisional
2. **Rendang** - Masakan daging dengan santan dan rempah
3. **Gado-gado** - Salad sayuran dengan bumbu kacang
4. **Opor** - Ayam dengan kuah santan

## Teknologi yang Digunakan

- **Python 3.x**
- **Scikit-learn** - CountVectorizer untuk text vectorization
- **Pandas** - Data manipulation dan analisis
- **NumPy** - Operasi matematika dan array

## Fitur Utama

### 1. Term-Document Matrix

Membuat representasi vektor dari setiap resep berdasarkan bahan-bahannya.

### 2. Analisis Kemiripan

Menghitung kemiripan antar resep menggunakan dot product dari vektor bahan.

### 3. Identifikasi Bahan Unik

Menemukan bahan yang hanya digunakan dalam satu resep tertentu.

### 4. Analisis Bahan Umum

Mengidentifikasi bumbu atau bahan yang paling sering digunakan.

### 5. Query Search

Sistem pencarian yang dapat menemukan resep paling cocok berdasarkan bahan yang diberikan.

## Cara Menjalankan

1. **Install dependencies:**

   ```bash
   pip install scikit-learn pandas numpy
   ```

2. **Jalankan program:**
   ```bash
   python 2208107010064_Muhammad_Ridho.py
   ```

## Output Program

Program akan menampilkan:

### Informasi Dataset

- Daftar semua resep dan bahan-bahannya
- Jumlah total bahan unik dalam dataset

### Term-Document Matrix

- Representasi numerik dari setiap resep
- Matriks yang menunjukkan kehadiran setiap bahan di setiap resep

### Analisis Kemiripan

- Perbandingan kemiripan antar resep
- Identifikasi resep yang paling mirip dengan Soto

### Bahan Unik dan Umum

- Daftar bahan yang hanya muncul di satu resep
- Ranking bahan berdasarkan frekuensi penggunaan

### Query Analysis

- Hasil pencarian berdasarkan query bahan tertentu
- Rekomendasi resep yang paling sesuai

## Struktur File

```
├── 2208107010064_Muhammad_Ridho.py    # File utama program
├── README.md                          # Dokumentasi project
└── tugas2.pdf                        # Spesifikasi tugas
```

## Contoh Output

```
=== TERM-DOCUMENT MATRIX ===
           asam  ayam  bawang  ...  tempe  tofu  kunyit
Soto          0     1       2  ...      0     0       1
Rendang       1     0       2  ...      0     0       2
Gado-gado     1     0       1  ...      1     1       0
Opor          0     1       2  ...      0     0       0

Resep paling mirip dengan Soto: Opor
Bahan yang sama: ayam, bawang merah, bawang putih, kemiri, serai
```

## Metodologi

1. **Text Preprocessing**: Tokenisasi bahan-bahan resep
2. **Vectorization**: Konversi teks ke representasi numerik menggunakan CountVectorizer
3. **Similarity Calculation**: Perhitungan kemiripan menggunakan dot product
4. **Analysis**: Interpretasi hasil untuk mendapatkan insights

## Insights yang Didapat

- **Bahan Paling Umum**: Analisis menunjukkan bumbu yang paling sering digunakan
- **Karakteristik Resep**: Setiap resep memiliki signature ingredients yang unik
- **Similaritas**: Soto dan Opor memiliki kemiripan tinggi karena sama-sama berbasis ayam

## Pengembangan Selanjutnya

- Implementasi TF-IDF untuk weighting yang lebih sophisticated
- Penambahan lebih banyak resep dalam dataset
- Implementasi cosine similarity untuk perbandingan yang lebih akurat
- Integrasi dengan database resep yang lebih besar

## Author

Muhammad Ridho - 2208107010064
