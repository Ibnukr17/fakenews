import cv2

# Fungsi untuk menghitung histogram gambar
def compute_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    cv2.normalize(histogram, histogram)
    return histogram

# Fungsi untuk menghitung similarity antara dua gambar berdasarkan histogram
def compute_similarity(histogram1, histogram2):
    similarity = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_CORREL)
    return similarity

# Baca gambar yang ingin dibandingkan
image1 = cv2.imread("alphard.jpg")

# Daftar pembanding
pembanding = ["alphardhitam.jpg", "duapalhard.jpg", "alphard.jpg"]

# Dictionary untuk menyimpan nilai similarity setiap pembanding
similarities = {}

# Loop pada daftar pembanding
for pem in pembanding:
    # Baca gambar pembanding
    image2 = cv2.imread(pem)
    
    # Hitung histogram kedua gambar
    histogram1 = compute_histogram(image1)
    histogram2 = compute_histogram(image2)

    # Hitung similarity antara kedua gambar
    similarity = compute_similarity(histogram1, histogram2)

    # Simpan nilai similarity pada dictionary
    similarities[pem] = similarity

# Tampilkan nilai similarity untuk setiap pembanding
for pem, similarity in similarities.items():
    print("Similarity with", pem, ": ", similarity)

# Cari pembanding dengan nilai similarity tertinggi
most_similar = max(similarities, key=similarities.get)
print("Most similar image is", most_similar, "with similarity", similarities[most_similar])