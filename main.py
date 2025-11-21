import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data_Penjualan_Toko_Online.csv")
print(df.head())

print(df.info())
print(df.isnull().sum())

df.dropna()
print("Statistik Deskriptif: ")
print(df.describe())

print("\nProduk Terlaris: ")
print(df.groupby("Produk")["Jumlah"].sum().sort_values(ascending=False))

plt.figure(figsize = (8, 5))
sns.barplot(data = df, x = "Produk", y = "Pendapatan", estimator=sum, ci=None)
plt.title("Total Pendapatan per Produk")
plt.show()

plt.figure(figsize = (10, 5))
sns.lineplot(data = df, x = "Tanggal", y = "Pendapatan", marker = "o")
plt.title("Tren Pendapatan Mingguan")
plt.show()

df.to_csv("hasil_analisis_penjualan.csv", index = False)
print("Data hasil analisis telah disimpan sebagai hasil_analisis_penjualan.csv")


df["Discount"] = "10%"

p_bersih = []

for p in df["Pendapatan"]:
    p_bersih.append(int(p - (p * 0.1)))

df["Pendapatan Bersih"] = p_bersih

plt.figure(figsize = (8, 5))
sns.barplot(data = df, x = "Produk", y = "Pendapatan Bersih", estimator=sum, ci=None)
plt.title("Total Pendapatan Bersih per Produk")
plt.show()

plt.figure(figsize = (10, 5))
sns.lineplot(data = df, x = "Tanggal", y = "Pendapatan Bersih", marker = "o")
plt.title("Tren Pendapatan Bersih Mingguan")
plt.show()

print(df.head())

df.to_csv("hasil_analisis_diskon.csv", index = False)
print("Data hasil analisis telah disimpan sebagai hasil_analisis_diskon.csv")
