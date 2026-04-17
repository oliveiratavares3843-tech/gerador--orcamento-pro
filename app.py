import streamlit as st
import streamlit_authenticator as stauth
from fpdf import FPDF
from datetime import datetime
from PIL import Image
import io
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e3a8a;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 1. Configuração da Página (Deve ser a primeira linha)
st.set_page_config(page_title="Gerador Pro", page_icon="💼")

# --- 2. CONFIGURAÇÃO DE ACESSO (Estrutura correta com 'credentials') ---
config = {
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Administrador",
                "password": "123",  # Mude sua senha aqui
                "email": "seu@email.com"
            }
        }
    },
    "cookie": {
        "name": "cookie_gerador_orcamento",
        "key": "chave_secreta_123",
        "expiry_days": 30
    }
}

# Inicializa o autenticador
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- 3. CLASSE DO PDF (Sua lógica original) ---
class OrcamentoPDF(FPDF):
    def __init__(self, logo_img=None):
        super().__init__()
        self.logo_img = logo_img

    def header(self):
        if self.logo_img:
            self.image(self.logo_img, 10, 8, 33)
            self.set_x(50)
        self.set_font("Arial", "B", 15)
        self.cell(0, 10, "ORÇAMENTO DE SERVIÇOS", ln=True, align="R" if self.logo_img else "C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

# --- 4. FUNÇÃO DO SISTEMA PRINCIPAL ---
def meu_sistema_principal():
    st.title("💼 Gerador de Orçamentos Profissional")
    st.info(f"Bem-vindo, {st.session_state['name']}! Personalize seu orçamento abaixo.")

    # Sidebar para configurações de marca
    with st.sidebar:
        st.header("Configurações de Marca")
        logo_upload = st.file_uploader("Upload da sua Logo (PNG/JPG)", type=["png", "jpg", "jpeg"])
        if logo_upload:
            st.image(logo_upload, caption="Prévia da Logo", width=150)

    # Corpo principal
    with st.container():
        cliente = st.text_input("Nome do Cliente:")
        servico = st.text_area("Descrição detalhada do serviço:", placeholder="Ex: Criação de site institucional...")
        
        col1, col2 = st.columns(2)
        with col1:
            valor = st.number_input("Valor Total (R$):", min_value=0.0, format="%.2f")
        with col2:
            data_atual = datetime.now().strftime("%d/%m/%Y")
            st.write(f"**Data de Emissão:** {data_atual}")

    # Lógica de Geração
    if st.button("🚀 Gerar Orçamento"):
        if cliente and servico and valor > 0:
            img_para_pdf = Image.open(logo_upload) if logo_upload else None
            
            pdf = OrcamentoPDF(logo_img=img_para_pdf)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 10, f"Para: {cliente}", ln=True)
            pdf.cell(0, 10, f"Data: {data_atual}", ln=True)
            pdf.ln(10)

            pdf.set_fill_color(240, 240, 240)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(140, 10, "Descrição do Serviço", border=1, fill=True)
            pdf.cell(50, 10, "Total", border=1, fill=True, ln=True)
            
            pdf.set_font("Arial", size=11)
            y_antes = pdf.get_y()
            pdf.multi_cell(140, 10, servico, border=1)
            y_depois = pdf.get_y()
            
            pdf.set_xy(150, y_antes)
            pdf.cell(50, y_depois - y_antes, f"R$ {valor:,.2f}", border=1, ln=True, align="C")

            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            
            st.success("Tudo pronto!")
            st.download_button(
                label="📥 Baixar Orçamento PDF",
                data=pdf_bytes,
                file_name=f"Orcamento_{cliente.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Preencha o Cliente, Serviço e Valor para continuar.")

# --- 5. LÓGICA DE EXIBIÇÃO DO LOGIN ---
# O método login agora atualiza o session_state automaticamente
authenticator.login(location='main')

if st.session_state["authentication_status"]:
    authenticator.logout('Sair', 'sidebar')
    meu_sistema_principal()
elif st.session_state["authentication_status"] is False:
    st.error('Usuário ou senha incorretos')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, insira seu usuário e senha')

