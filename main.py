import streamlit as st
from convert import pdf_docx , save_uploadedfile

header = st.container()
dataset = st.container()


with header:
    st.title("Bem vindo ao Conversor de Pdf para Doc!")


with dataset:
    st.header("Faça o Upload de Seu arquivo PDF")

    uploaded_file = st.file_uploader("Escolha o Arquivo", type='pdf', accept_multiple_files=False, key=None, help='Somente serão aceitos arquivos com extensão pdf')

    if uploaded_file is not None:
        st.success(save_uploadedfile(uploaded_file))
        name_out = uploaded_file.name.replace(".pdf",".docx")
        with st.spinner('Convertendo...'):
            file_out = pdf_docx(uploaded_file.name,name_out)

        st.text("Arquivo convertido e pronto para Download:")
        with open(file_out, 'rb') as f:
            st.download_button('Download Docx', f, file_name=name_out)







