import subprocess
import pyautogui
import time
import pandas as pd

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

def preencher_login():
    try:
        subprocess.Popen(['google-chrome', LINK])
        
        time.sleep(3)

        pyautogui.press('tab')
        pyautogui.write("pythonimpressionador@gmail.com")
        time.sleep(0.5)

        pyautogui.press('tab')
        pyautogui.write("superSenha")
        time.sleep(0.5)
        
        pyautogui.press('enter')        

        cadastrar_produtos()

        return True
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def cadastrar_produtos(): 
    time.sleep(0.3)

    tabela = ler_dados_csv("produtos.csv")

    for linha in tabela.index:
        pyautogui.press('tab')
        codigo = str(tabela.loc[linha, "codigo"])
        pyautogui.write(codigo)
        time.sleep(0.3)

        pyautogui.press('tab')
        marca = str(tabela.loc[linha, "marca"])
        pyautogui.write(marca)
        time.sleep(0.3)

        pyautogui.press('tab')
        tipo = str(tabela.loc[linha, "tipo"])
        pyautogui.write(str(tipo))
        time.sleep(0.3)

        pyautogui.press('tab')
        categoria = str(tabela.loc[linha, "categoria"])
        pyautogui.write(str(categoria))
        time.sleep(0.3)

        pyautogui.press('tab')
        preco_unitario = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.write(str(preco_unitario))
        time.sleep(0.3)

        pyautogui.press('tab')
        custo = str(tabela.loc[linha, "custo"])
        pyautogui.write(str(custo))
        time.sleep(0.3)

        pyautogui.press('tab')        
        
        obs = str(tabela.loc[linha, "obs"])

        if obs != 'nan':
            pyautogui.write(obs)
        pyautogui.press('tab')

        '''if not pd.isna(obs):            
            pyautogui.write(obs)
            time.sleep(0.3)
            pyautogui.press('tab')
            #continue'''

        pyautogui.press('enter')

        pyautogui.press('f5')
        time.sleep(1)
        #pyautogui.scroll(5000)        

    return True


def ler_dados_csv(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo CSV: {e}")
        return None

if __name__ == "__main__":
    preencher_login()
    time.sleep(3)