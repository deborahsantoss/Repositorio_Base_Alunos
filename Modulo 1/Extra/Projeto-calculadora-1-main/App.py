import streamlit as st 
import Calculadora as calc 

st.image("https://th.bing.com/th/id/OIP.idwuR-qB13QBOb8nz2_rZAHaFW?w=247&h=180&c=7&r=0&o=7&pid=1.7&rm=3")
st.title ("Calculadora 📱")

numero1 = st.number_input("Digite o primeiro numero: ", step=0.1, value=None)
numero2 = st.number_input("Digite o segundo numero: ", step=0.1, value=None)
operaçao = st.selectbox("Selecione a operaçao: ", ("+","-","*","/"))

if st.button("Calcular"):
    resultado = calc.calcular(numero1, numero2 , operaçao)
    st.info(f"O resultado é: {resultado} ")
    if resultado == 67:
        st.info("67")
