
# 1 - Abrir o sistema de empresa
import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# 2 - Fazer Login
    

# Selecionar campo de e-mail
pyautogui.click(x=762, y=468)
pyautogui.write("gatinhalinda@email.com")
pyautogui.press("tab") # Passa para o próximo campo
pyautogui.click(x=729, y=587)
pyautogui.write("minhasenha")
pyautogui.click(x=938, y=671) # Clique no botão de login

time.sleep(1
           )

# 3 - Importar base de produtos para cadastrar 
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4 - Cadastrar um produto

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=841, y=321)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"] 

    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

