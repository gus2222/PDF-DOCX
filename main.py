import streamlit as st
from convert import pdf_docx , save_uploadedfile

st.set_page_config(page_title="PDF-DOCX",page_icon="./pdf_icon.png")
header = st.container()
body = st.container()
footer = st.container()
st.markdown(""" <footer class="css-1q1n0ol egzxvld0">"Criado por"<a href="dossantosgss@gmail.com" class="css-1vbd788 egzxvld1">Gustavo</a> </footer><style>
#MainMenu {visibility: hidden;}

</style> """, unsafe_allow_html=True)

with header:
    st.title("Bem vindo ao Conversor de Pdf para Doc!")


with body:
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

with footer:
    st.caption("Criado por Gustavo: dossantosgss@gmail.com")





