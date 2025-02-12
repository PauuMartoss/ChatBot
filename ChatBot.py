import streamlit as st
st.title ("PauGPT")
with st.chat_message("assistant", avatar="🤖"):
    st.write("Hola soy una IA")
with st.chat_message("user", avatar="🧑🏻"):
    st.write("Hola soy un humano")

mensaje_usuario = st.chat_input("Escribe un mensaje")
