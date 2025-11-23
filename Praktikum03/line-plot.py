import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout streamlit
st.title("Visusalisasi Penjualan Product")
st.sidebar.header("Penjualan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi",(
    "Line Plot", "Kustomisasi Line Plot", "Garis Berbeda untuk Menunjukkan Trend", "Subplot"))

# Identitas Kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 29:
- Santika Sintia Larasati (0110122045)
- Saepulloh  (0110222183)
- Muhammad Ammar (0110122308)
""")

#Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title("Penjualan Produk A Per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penjualan")
    st.pyplot(fig)

#Multiple Line Plot
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color='red', linestyle='-', marker='x')
    ax.set_title("Penjualan Produk Per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penjualan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis Garis untuk Tren
product_C_sales = [18,22,15,28,32,38,42,45,48,52,56,60]
product_D_sales = [23,54,63,68,45,33,23,34,54,20,25,30]
def trend_lines_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label="Product C", color='green', linestyle='-.')
    axs.plot(months, product_D_sales, label="Product D", color='purple', linestyle=':')
    axs.set_title("Trend Penjualan Produk Per Bulan")
    axs.set_xlabel("Bulan")
    axs.set_ylabel("Jumlah Penjualan")
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

# Sobplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # ======================
    # Plot untuk Produk C
    # ======================
    axs[0].plot(
        months,
        product_C_sales,
        label='Product C',
        color='green',
        marker='o'
    )
    axs[0].set_title("Penjualan Produk C Per Bulan")
    axs[0].set_xlabel("Bulan")
    axs[0].set_ylabel("Jumlah Penjualan")
    axs[0].legend()
    axs[0].grid(True)

    # ======================
    # Plot untuk Produk D
    # ======================
    axs[1].plot(
        months,
        product_D_sales,
        label='Product D',
        color='purple',
        marker='x'
    )
    axs[1].set_title("Penjualan Produk D Per Bulan")
    axs[1].set_xlabel("Bulan")
    axs[1].set_ylabel("Jumlah Penjualan")
    axs[1].legend()
    axs[1].grid(True)
    plt.tight_layout()
    st.pyplot(fig)


# Viewer Logic
if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()
