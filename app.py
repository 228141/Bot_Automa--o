'''
1 - Entrar na planilha e extrair o processo.

2 - Entro no Site do Prodigi (https://prodigi.saobernardo.sp.gov.br/solar/), e pesquiso o status do processo informado pelo usuário

3 - Verificar se o processo está em andamento ou arquivado

4 - Se estiver arquivado, inserir na planilha a informação de "Processo Arquivado"

5 - Caso constrario (Se estiver em andamento) inserir na planilha a informação de "Em Andamento"

6 - Inserir essas informações em uma nova Planilha

7 - Repetir isso até finalizar ultimo processo da planilha.

'''

import openpyxl 

#1 - Entrar na planilha e extrair o processo.

planilha_clientes = openpyxl.load_workbook('proc_arquivados') 
