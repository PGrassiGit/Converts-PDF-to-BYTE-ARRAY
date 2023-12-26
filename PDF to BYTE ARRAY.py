import os
import pandas as pd     #criar o banco
import base64   #pro bytearray do pdf
from tkinter import Tk, filedialog  # Import tkinter

def seleciona_dir():
    root = Tk()
    root.withdraw()  
    folder_selected = filedialog.askdirectory(title="Selecione a Pasta com os arquivos")  # abre a box pra selecionar a pasta
    return folder_selected

pasta_selecionada = seleciona_dir()

if pasta_selecionada:
    # lista todos arquivos do dir
    files = os.listdir(pasta_selecionada)
    print(f'arquivos listados{files}')  
    for file in files:          
        pdf_path = os.path.join(pasta_selecionada, file)                 
    with open(pdf_path, 'rb') as pdf_file:  #abre o pdf
        pdf_bytes = pdf_file.read()     #lê o pdf
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')        #faz o malabarismo/converte em bytes
        print (pdf_base64)