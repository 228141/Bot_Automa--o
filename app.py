''' REALIZAR BACKUP DE FORMULÁRIOS DO MÓDULO DO BPM

1 - Entrar no Site do Prodigi (https://prodigi.saobernardo.sp.gov.br/solar/)

2 - Clicar no módulo do BPM / BPM - fomulário Dinâmico

3 - Clicar no "Formulário"

4 - Clicar em "Exportar"

5 - Clicar em "Salvar Como"

6 - Abrir a pasta da Rede (\\fileserver-01\pmsbc\SA3\SA-32\PRODIGI\Formularios)

7 - "Salvar" o documento na pasta da rede

8 - O processo irá se repetir até todos os formulários sejam salvos


'''

import openpyxl 

#1 - Entrar na planilha e extrair o processo.

planilha_clientes = openpyxl.load_workbook('proc_arquivados') 
