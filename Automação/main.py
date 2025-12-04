import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#importar a base de dados

tabela_vendas = pd.read_excel("Vendas.xlsx")

#visualizar a base de dados

pd.set_option('display.max_columns', None)

#faturamento por loja

#print('-' * 50)
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)
#print('-' * 50)

#quantidade vendida no total

vendas = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(vendas)
#print('-' * 50)

#ticket medio por produto em cada loja

ticket = (faturamento['Valor Final'] / vendas['Quantidade']).to_frame()
ticket = ticket.rename(columns={0:'Ticket Médio'})
#print(ticket)
#print('-' * 50)

# enviar um relatorio no email 

# configurar credenciais (altere com suas informações)
remetente = 'gustavobusiness7612@gmail.com'
senha = '32374774gu'  # Use senha de app do Gmail se tiver 2FA
destinatario = 'gustavomoney7612@gmail.com'

# criar mensagem
msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = 'Relatório de vendas por loja.'

corpo_html = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas de cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
<p>Quantidade:</p>
{vendas.to_html()}
<p>Ticket Médio dos produtos:</p>
{ticket.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}
<p>Qualquer dúvida estou à disposição.</p>
<p>Att.,</p>
<p>Marques</p>
'''

msg.attach(MIMEText(corpo_html, 'html'))

# enviar email
try:
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(remetente, senha)
    smtp.send_message(msg)
    smtp.quit()
    print('Email enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar email: {e}')
