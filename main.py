import smtplib

import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_Columns', None)  # ele exibe sem o maximo de coluna
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()  # filtra coluna de uma tabela e agrupa e soma , faturamento por loja
print(faturamento)

# quantidade de produtos vendidos por lojas
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('_'* 50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() # to_frame tranforma na tabela
print(ticket_medio)


# enviar um email com relatorio
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jeromie Kirchoff
# Created Date: Mon Aug 02 17:46:00 PDT 2018
# =============================================================================
# Imports
# import smtplib
# import email.message
# =============================================================================


# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = 'luansouza.ti29@gmail.com'
gmail_app_password = 'souza1991'

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================
sent_from = gmail_user
sent_to = ['luansouza88@gmail.com', 'luansouza.ti29@gmail.com']
sent_subject = "teste envio email?"
sent_body = ("E ai, como vai? amigo!\n\n"
             "Espero que esteja bem!\n"
             "\n"
             "Atenciosamente,\n"
             "Luan\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# =============================================================================
# SEND EMAIL OR DIE TRYING!!!
# Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email enviado')
except Exception as exception:
    print("Error: %s!\n\n" % exception)




# ======================================== dicas =======================================

# tabela_vendas[['ID Loja', 'Valor Final']] #// filtra colubna de uma tabela

# tabela_vendas.groupby('ID Loja').sum() #// e agrupa e soma o restos das tabelas
