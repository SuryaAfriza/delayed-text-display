import numpy as np
import matplotlib.pyplot as plt

# Membuat data
theta = np.linspace(0, 2 * np.pi, 100)  # Membuat 100 titik dari 0 sampai 2pi
r = np.ones_like(theta)  # Radiusnya tetap 1 (lingkaran)

# Membuat plot polar
plt.subplot(111, projection='polar')  # Mengatur plot ke polar
plt.plot(theta, r)  # Menggambar lingkaran
plt.title("Lingkaran Sederhana")  # Judul plot
plt.show()  # Menampilkan plot
