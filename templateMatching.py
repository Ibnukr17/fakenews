import cv2

# Load gambar yang ingin dibandingkan
img1 = cv2.imread('alphard.jpg')
img2 = cv2.imread('alphard.jpg')

# Konversi gambar ke grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Menggunakan template matching dengan metode CCORR_NORMED
result = cv2.matchTemplate(gray_img1, gray_img2, cv2.TM_CCOEFF_NORMED)

# Mendapatkan nilai similarity
similarity = cv2.minMaxLoc(result)[1]

# Tampilkan hasil similarity
print(f"Similarity: {similarity}")