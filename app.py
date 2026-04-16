app = Flask(__name__)

# --- 1. CONEXÃO COM A REDE ---
# Insira seu link do Infura ou Alchemy (ex: rede Sepolia ou Mainnet)
NODE_URL = "COLE_AQUI_SEU_LINK_DO_INFURA_OU_ALCHEMY"
w3 = Web3(Web3.HTTPProvider(NODE_URL))

# --- 2. CREDENCIAIS DA CARTEIRA PRINCIPAL ---
# A chave privada permite que o código assine o envio do saldo
CHAVE_PRIVADA = "COLE_AQUI_SUA_CHAVE_PRIVADA"
CONTA_MESTRA = w3.eth.account.from_key(CHAVE_PRIVADA)
MEU_ENDERECO = CONTA_MESTRA.address

# --- 3. SALDO CRIADO NO CÓDIGO ---
# Este é o valor que o usuário verá e poderá sacar
SALDO_SISTEMA 100
MOEDA = "ETH"

@app.route('/', methods=['GET', 'POST'])
def terminal_saque():
    global SALDO_SISTEMA
    log_status = ""

    if request.method == 'POST':
        try:
            destino = request.form.get('destino')
            valor_saque = float(request.form.get('valor'))
            
            # Validação: O saque só ocorre se houver saldo no código
            if valor_saque > SALDO_SISTEMA:
                log_status = '<div style="color:#ff4d4d">ERRO: Saldo insuficiente no sistema.</div>'
            else:
                # --- EXECUÇÃO DO SAQUE REAL ---
                valor_wei = w3.to_wei(valor_saque, 'ether')
                nonce = w3.eth.get_transaction_count(MEU_ENDERECO)
                
                # Montagem da transação (Bloco)
                tx_bloco = {
                    'nonce': nonce,
                    'to': destino,
                    'value': valor_wei,
                    'gas': 21000,
                    'gasPrice': w3.eth.gas_price,
                    'chainId': 11155111 # 11155111 = Rede Sepolia (Teste) | 1 = Mainnet
                }

                # O CÓDIGO ASSINA: Usa a chave privada para autorizar
                signed_tx = w3.eth.account.sign_transaction(tx_bloco, CHAVE_PRIVADA)

                # O CÓDIGO ENVIA: Transmite para a rede processar o saque
                tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

                # Atualiza o saldo do código após o envio
                SALDO_SISTEMA -= valor_saque
                log_status = f'''<div style="color:#00ff88">
                                    <b>SAQUE REALIZADO!</b><br>
                                    O saldo saiu do código para a wallet.<br>
                                    <small>TX: {w3.to_hex(tx_hash)}</small>
                                </div>'''

        except Exception as e:
            log_status = f'<div style="color:#ff4d4d">Erro na transação: {str(e)}</div>'

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { background: #0b0e11; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding-top: 50px; }
                .terminal { background: #181a20; padding: 30px; border-radius: 12px; border: 1px solid #f3ba2f; display: inline-block; width: 400px; }
                .saldo-box { font-size: 30px; color: #f3ba2f; margin: 20px 0; font-family: monospace; }
                input { width: 90%; padding: 12px; margin: 10px 0; background: #1e2329; border: 1px solid #474d57; color: white; border-radius: 5px; }
                button { width: 96%; padding: 15px; background: #fcd535; color: black; border: none; font-weight: bold; cursor: pointer; border-radius: 5px; }
                .footer { font-size: 10px; color: #848e9c; margin-top: 15px; }
            </style>
        </head>
        <body>
            <div class="terminal">
                <h2>TERMINAL DE SAQUE</h2>
                <p>Saldo no Sistema</p>
                <div class="saldo-box">{{ saldo }} {{ moeda }}</div>
                <hr style="border:0.1px solid #333;">
                <form method="post">
                    <input type="text" name="destino" placeholder="Wallet de Destino (0x...)" required>
                    <input type="number" step="0.0001" name="valor" placeholder="Valor para Envio" required>
                    <button type="submit">SACAR PARA WALLET</button>
                </form>
                <div style="margin-top:20px;">{{ log|safe }}</div>
                <div class="footer">Carteira de Origem: {{ carteira }}</div>
            </div>
        </body>
        </html>
    ''', saldo=round(SALDO_SISTEMA, 4), moeda=MOEDA, log=log_status, carteira=MEU_ENDERECO)

if __name__ == '__main__':
    app.run(debug=True)