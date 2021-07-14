#Foi preciso diminuir o arquivo ficando apenas com os candidatos autista para facilitar o processamento
#Ao utilizar o script coloque o path do arquivo na variável arquivo

#ENEM 2019

#importando as bibliotecas para trabalho

import pandas as pd
import pandera as pa

#Estabelecendo variáveis das colunas que vamos excluir e o caminho do arquivo

arquivo = r"PATH"

colunas_excluir = ['NU_INSCRICAO', 'NU_ANO', 'CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO',
                   'CO_UF_NASCIMENTO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'CO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'CO_PROVA_CN',
                   'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',
                   'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
                   'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3',
                   'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24',
                   'IN_AMPLIADA_18', 'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS', 'IN_TEMPO_ADICIONAL',
                   'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS', 'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA',
                   'IN_GUIA_INTERPRETE', 'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO', 'IN_CADEIRA_ACOLCHOADA',
                   'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO', 'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
                   'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA', 'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL',
                   'IN_SALA_ESPECIAL', 'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO', 'IN_MATERIAL_ESPECIFICO',
                   'IN_NOME_SOCIAL'
                  ]

#Abrindo o arquivo no pandas para limpeza e tratamento
#O separado dos dados do arquivo é ";" e foi preciso usar "encoding" pelo não reconhecimento dos caracteres especiais PT-BR

df = pd.read_csv(arquivo, sep = ";", encoding = 'latin-1')
df.sample(5)

#Excluindo as colunas que serão desnecessárias à nossa análise

df = df.drop([i for i in colunas_excluir], axis=1)
df.sample(5)

#Restringindo os dados aos candidatos com TEA (Transtorno do Espectro Autista)
df_tea = df.loc[df.IN_AUTISMO == 1]

#Salvando o arquivo referente ao ano
df_tea.to_csv("c:/enem_2019_tea.csv")

#ENEM 2018

#Estabelecendo variáveis das colunas que vamos excluir e o caminho do arquivo

arquivo = r"PATH"

colunas_excluir = ['NU_INSCRICAO', 'CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO',
                   'CO_UF_NASCIMENTO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'CO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'CO_PROVA_CN',
                   'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',
                   'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
                   'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3',
                   'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24',
                   'IN_AMPLIADA_18', 'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',
                   'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS', 'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA',
                   'IN_GUIA_INTERPRETE', 'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO', 'IN_CADEIRA_ACOLCHOADA',
                   'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO', 'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
                   'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA', 'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL',
                   'IN_SALA_ESPECIAL', 'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO', 'IN_MATERIAL_ESPECIFICO',
                   'IN_NOME_SOCIAL'
                  ]

#Abrindo o arquivo no pandas para limpeza e tratamento
#O separado dos dados do arquivo é ";" e foi preciso usar "encoding" pelo não reconhecimento dos caracteres especiais PT-BR

df = pd.read_csv(arquivo, sep = ";", encoding = 'latin-1')
df.sample(5)

#Excluindo as colunas que serão desnecessárias à nossa análise

df = df.drop([i for i in colunas_excluir], axis=1)
df.sample(5)

#Restringindo os dados aos candidatos com TEA (Transtorno do Espectro Autista)
df_tea = df.loc[df.IN_AUTISMO == 1]

df_tea.to_csv("c:/enem_2018_tea.csv")

#ENEM 2017


#Estabelecendo variáveis das colunas que vamos excluir e o caminho do arquivo

arquivo = r"C:\Users\azureuser\Documents\ProjetoDIO\microdados_enem2018\DADOS\MICRODADOS_ENEM_2018.csv"

colunas_excluir = ['NU_INSCRICAO', 'CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO',
                   'CO_UF_NASCIMENTO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'CO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'CO_PROVA_CN',
                   'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',
                   'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
                   'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3',
                   'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24',
                   'IN_AMPLIADA_18', 'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',
                   'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS', 'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA',
                   'IN_GUIA_INTERPRETE', 'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO', 'IN_CADEIRA_ACOLCHOADA',
                   'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO', 'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
                   'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA', 'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL',
                   'IN_SALA_ESPECIAL', 'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO', 'IN_MATERIAL_ESPECIFICO',
                   'IN_NOME_SOCIAL'
                  ]

#Abrindo o arquivo no pandas para limpeza e tratamento
#O separado dos dados do arquivo é ";" e foi preciso usar "encoding" pelo não reconhecimento dos caracteres especiais PT-BR

df = pd.read_csv(arquivo, sep = ";", encoding = 'latin-1')
df.sample(5)

#Excluindo as colunas que serão desnecessárias à nossa análise

df = df.drop([i for i in colunas_excluir], axis=1)
df.sample(5)

#Restringindo os dados aos candidatos com TEA (Transtorno do Espectro Autista)
df_tea = df.loc[df.IN_AUTISMO == 1]

#Salvando o arquivo csv referente ao ano 2017
df_tea.to_csv("c:/enem_2017_tea.csv")

#ENEM 2016


#Estabelecendo variáveis das colunas que vamos excluir e o caminho do arquivo

arquivo = r"C:\Users\azureuser\Documents\ProjetoDIO\microdados_enem2018\DADOS\MICRODADOS_ENEM_2018.csv"

colunas_excluir = ['NU_INSCRICAO', 'CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO',
                   'CO_UF_NASCIMENTO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'CO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'CO_PROVA_CN',
                   'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',
                   'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
                   'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3',
                   'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24',
                   'IN_AMPLIADA_18', 'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',
                   'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS', 'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA',
                   'IN_GUIA_INTERPRETE', 'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO', 'IN_CADEIRA_ACOLCHOADA',
                   'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO', 'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
                   'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA', 'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL',
                   'IN_SALA_ESPECIAL', 'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO', 'IN_MATERIAL_ESPECIFICO',
                   'IN_NOME_SOCIAL'
                  ]

#Abrindo o arquivo no pandas para limpeza e tratamento
#O separado dos dados do arquivo é ";" e foi preciso usar "encoding" pelo não reconhecimento dos caracteres especiais PT-BR

df = pd.read_csv(arquivo, sep = ";", encoding = 'latin-1')
df.sample(5)

#Excluindo as colunas que serão desnecessárias à nossa análise

df = df.drop([i for i in colunas_excluir], axis=1)
df.sample(5)

#Restringindo os dados aos candidatos com TEA (Transtorno do Espectro Autista)
df_tea = df.loc[df.IN_AUTISMO == 1]

#Salvando o arquivo csv referente ao ano 2017
df_tea.to_csv("c:/enem_2016_tea.csv")
