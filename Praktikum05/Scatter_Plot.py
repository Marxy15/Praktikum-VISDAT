# Scatter Plot
import streamlit as st
import matplotlib.pyplot as plt

# Layout utama
st.title('Visualisasi Scatter PlotPenjualan Es Krim')
st.sidebar.header("Pengaturan Visualisais")

# Menu di Sidebar
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# Identitas Kelompok
st.caption("Praktikum 5 - Matplotlib Scatter PLot")
st.write("Kelompok 9:")
st.markdown("""
- Santika Sintia Larasati (0110122045)
- Saepulloh  (0110222183)
- Muhammad Ammar (0110122308)
""")

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

# 1. Basic Scatter Plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='blue')
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)


# ===============================
# 2. Kustomisasi scatter plot
def custom_scatter():
    st.subheader("2. Kustomisasi scatter plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)


# ===============================
# Data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 120, 140, 160, 180, 200]

# 3. Multiple scatter plot
def multiple_scatter():
    st.subheader("3. Multiple scatter plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Penjualan Es Krim Berdasarkan Hari')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.legend()
    st.pyplot(fig)


# ----------------------------------------------------------------------------
# 4. Analisa dengan Scatter  Plot
import pandas as pd

# Data dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 90, 100, 110, 130, 150, 180],
    'Penjualan_Vanila': [45, 55, 65, 80, 95, 105, 120, 140, 160],
    'Penjualan_Stroberi': [40, 50, 60, 75, 90, 100, 115, 130, 150],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

def scatter_3_variabel():
    st.subheader("4. Analisa dengan Scatter Plot")

    # Pilih jenis es krim
    jenis_eskrim = st.selectbox(
        'Pilih Jenis Es Krim:',
        ['Cokelat', 'Vanila', 'Stroberi']
    )

    # Tentukan kolom sesuai pilihan
    if jenis_eskrim == 'Cokelat':
        kolom_penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        kolom_penjualan = df['Penjualan_Vanila']
    else:
        kolom_penjualan = df['Penjualan_Stroberi']

    # Tampilkan data
    st.subheader('Data Penjualan dan Suhu')
    st.dataframe(df)

    # Scatter plot (DIPINDAHKAN KE DALAM FUNGSI)
    fig, ax = plt.subplots()
    scatter = ax.scatter(
        df['Suhu'],
        kolom_penjualan,
        c=df['Kelembapan'],
        s=150,
        cmap='coolwarm',
        alpha=0.7
    )

    ax.set_title(f'Hubungan Suhu, Kelembapan, dan Penjualan Es Krim ({jenis_eskrim})')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    
    plt.colorbar(scatter, label='Kelembapan (%)')

    # Tampilkan grafik
    st.pyplot(fig)

    # Analisis
    st.subheader('Analisis Hubungan')
    st.write(
        f"Grafik menunjukkan hubungan antara suhu, kelembapan, "
        f"dan penjualan es krim jenis **{jenis_eskrim}**."
    )

#---------------------------------------------------------------------------------------------

# Judul aplikasi
st.title("Visualisasi 3D Penjualan Es Krim Berdasarkan Suhu")

# Data suhu
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]

# Data tambahan untuk kategori hari
penjualan_kerja = [40, 50, 60, 78, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Membuat 3D Scatter Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    suhu,
    penjualan_kerja,
    penjualan_akhir_pekan,
    color='orange',
    s=80,
    label='Data Penjualan'
)

# Pengaturan judul dan label sumbu
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (3D Version)')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Hari Kerja')
ax.set_zlabel('Penjualan Akhir Pekan')
ax.legend()

# Tampilkan grafik di Streamlit
st.pyplot(fig)


# Rounting berdasarkan menu sidebar
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variabel()