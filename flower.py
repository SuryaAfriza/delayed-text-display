import numpy as np
import matplotlib.pyplot as plt

# Membuat data
theta = np.linspace(0, 2 * np.pi, 100)  # Membuat 100 titik dari 0 sampai 2pi
k = 5 # Jumlah kelopak bunga
r = 10 * np.sin(k * theta) # Fungsi sinus untuk membuat kelopak


# Membuat plot polar
plt.subplot(111, projection='polar')  # Mengatur plot ke polar
plt.plot(theta, r, color='magenta')  # Menggambar bunga dengan warna violet
plt.title("bunga mawar dan kelopak")  # Judul plot
plt.show()  # Menampilkan plot
