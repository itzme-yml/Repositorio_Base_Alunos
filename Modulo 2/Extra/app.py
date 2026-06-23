import streamlit as st 
st.title("Yas TI bleh")
nome = st.text_input("Digite o nome do funcionário")
idade= st.text_input("Digite a idade do funcionário")
email= st.text_input("Digite o email do funcionário")
salario= st.text_input("Digite o salario do funcionário")
cargo= st.text_input("Digite cargo do funcionário")

if st.button("Cadastrar"):
    st.success(f"O funcinário {nome}, foi cadastrado com sucesso!!")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')
if st.button("Novo Cadastro"):
        st.rerun()