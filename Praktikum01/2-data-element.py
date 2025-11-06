#import liberary
import streamlit as st
import pandas as pd #untuk mengelolah data dalam bentuk frame tabel (dataframe)
import numpy as np # untuk memmbuat data numerik

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1: Data element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)
st.subheader("DataFrame")
df=pd.DataFrame(
    np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10)))
st.dataframe(df)

#highlight nilai minimum 
st.subheader("Highligt Minimum Value di DataFrame")
#highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

#tabel ststis
st.subheader("Tabel Statis")
df= pd.DataFrame(
   np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10)))
st.table(df)

# METRICS : komponen tampilan angka penting
st.subheader("metrics")
st.metric(label= "Temperature", value = "31 C,", delta="1.2 °C")
c1, c2, c3 = st.columns(3)

c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Costumers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456","-1132649")

#The write() Fungticion The write( )as a Superfunction 
import streamlit as st 
import pandas as pd
import numpy as np
df = pd.DataFrame(
np.random.randn(30, 10),
columns= ('col_no %d'% i for i in range (10)))
#mendefinisikan banyak argumen dalam fungsi tulis
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# Membuat data acak
df = pd.DataFrame(
np.random.randn(10, 2),
columns=['a', 'b'])
# Membuat chart batang
chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a', 'b'])
# Menampilkan chart di Streamlit
st.write(chart)

# Magic - perhitungan sederhana
"Adding 5 & 4", 5 + 4
# Memajang variabel 'a'
a = 5
'a', a
# Magic Markdown
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
# DataFrame menggunakan Magic
import pandas as pd
df = pd.DataFrame({'col': [1, 2]})
"DataFrame", df

# Membuat chart menggunakan Magic
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"Chart", chart