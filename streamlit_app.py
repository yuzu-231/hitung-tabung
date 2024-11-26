import streamlit as st
import math

st.title("MENGHITUNG :blue[Volume Tabung] :smile:")

r = st.number_input("Masukan Jari-jari (cm) :",0)
t = st.number_input("Masukan Tinggi (cm) :",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {v:.2f}')
