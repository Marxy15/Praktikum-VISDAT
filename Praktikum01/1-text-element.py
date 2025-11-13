import streamlit as st
st.write("Hello")

import streamlit as st
st.write("Wordl!!!!")

# import liblary
import streamlit as st

# Text element
# header - buat header

st.header("INI HEADER") # MEMBUAT HEADER
st.subheader("INI SUBHEADER") # MEMBUAT SUBHEADER
st.text("INI TEXT BIASA MOTHERFATHER") # MEMBUAT TEXT BIASA
st.markdown("*ini teks bold* dan ini italic") # MEMBUAT MARKDOWN UNTUK FORMAT TEXT
st.caption("ini caption") # MEMBUAT CAPTION(TEXT KECIL DIBAWAH ELEMEN UNTUK PENJELASAN)
st.markdown("""
            - ini baris 1
            - ini menggunakan marcdown multibaris
            - baris 
            - ini menggunakan marcdown multibaris
            - ini baris 3
            * ini memggunakan marcdown multibaris
            """
)

st.header("praktikum1 visualisasi data")
st.subheader("Bagian 1: text element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
#Bagian 2 : menampilkan rumus (LaTex)
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta''') #rumus trigonometri
st.latex(r''' (a+b) ^ 2 = a^2 + n^2 + 2ab ''')# rumus kuardat binominal

#Bagian 3 : menampilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

#simpan ke variabel
code='''def hello():
    print("helo, stream lit!")'''
#st.code()untuk menampilkan potongan kode dengan format rapi dan sytax highlighting
st.code(code, language='python')

st.subheader("java code")
st.code("""public class GFG{
Public static void main(string arg[])
{
system.out.printin(hello world);
}
}""", language='javascript')
#fungsi st.code( ) bisa digunakan untuk bahasa pemograman lain sepert java, java sksrip, c++, HTML, dll
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try{
adddlert("wellcome guest!");
}
Catch(err){
document.getElementById("demo").innerHTML =err.Message;
}
</Script>""")
#kode ini menununjukan contoh bagaimana menangani error(exception) di javascript