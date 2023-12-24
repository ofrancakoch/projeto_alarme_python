#------------------------------------------------------------------------------------------------------
#Libraries part

import schedule
import re
import webbrowser         
import time

#-------------------------------------------------------------------------------------------------------
#File operation part

def AbrirArquivo(nomeArq): 

  #  Nesse código, a função vai abrir um arquivo e vai procurar somente palavras no texto
  #  (A expressão regular 'r"\S+"' faz isso).
  #  A expressão 'utf-8' é utilizada para ler caracteres diferentes da ANSI.
  with open(nomeArq,"r",encoding='utf-8') as arquivo:
    procurarMed = re.findall(r"\S+",arquivo.read()) 
  arquivo.close()                                  
  return procurarMed


def EscreverArquivo(nomeArq,mensagem): 

  # Código abaixo irá escrever em um arquivo para não perder as informações iniciais do usuário.

  with open(nomeArq,"w",encoding='utf-8') as arquivo:
    arquivo.write(mensagem)                         
  arquivo.close()

#-------------------------------------------------------------------------------------------------------
#Notification part (Website)

def HTML():

  # HTML/CSS foi utilizado com objetivo igual a uma notificação.
  # A espressão "AbrirArquivo('exemplo.txt')[1]" diz respeito a função AbrirArquivo que 
  # abre o texto 'exemplo.txt' e escolhe a segunda palavra.
  # Já AbrirArquivo('exemplo.txt')[-3] fala para pegar a terceira palavra da direita para a esquerda.

  fileHTML = f''' 
    <!DOCTYPE html>
    <html>
    <head>
      <title>ALERTA</title>
    </head>
    <body style="display: flex;
                 align-items: center;
                 justify-content: center;
                 height: 100vh;">
      <div class="mensagem" style="text-align: center;
                                   padding: 100px;
                                   font-size: 25px;
                                   border: 1px solid #ccc;
                                   background-color: #f8f8f8;">
        <h1>{AbrirArquivo('exemplo.txt')[1]}</h1>
        <p>É necessário tomar {AbrirArquivo('exemplo.txt')[-3]}</p>
      </div>
    </body>
    </html>
    '''
  #Escreve no arquivo 'arqHTML.html'.
  EscreverArquivo('arqHTML.html', fileHTML) 

#-------------------------------------------------------------------------------------------------------
#Core part

class Projeto():
        
    def introDados(self):

      print("____________________________________________________________________________________")
      print("\n\t\tAlarme de Medicação\n")

      Nome = input("\n\tColoque seu nome:\n\t") 
      Med = input("\n\tColoque o remédio:\n\t") 
      Tempo = input("\n\tColoque o horário (horas:minutos):\n\t")
      
      dados = f"Nome: {Nome}\nMedicação: {Med}\nHorário: {Tempo}"
        
      EscreverArquivo('exemplo.txt',dados)
        
      print("\n\n\n\tDados foram armazenados com sucesso!\n") 
      print(f"\tO programa lhe avisará assim que o horário for {Tempo}.\n")
      print("____________________________________________________________________________________")

    
    def Alarme(self):

      HTML()
      webbrowser.open(f"https://www.google.com/search?q={AbrirArquivo('exemplo.txt')[-3]}")
      webbrowser.open('arqHTML.html') 
      webbrowser.open(f"https://www.youtube.com/watch?v=yEDVI-HtfdE&list=RDyEDVI-HtfdE&start_radio=1")

#-------------------------------------------------------------------------------------------------------
#Execution part

projeto = Projeto()

x = True

def Exec():
  global x

  if x:

    projeto.introDados()
    x = False           
    Exec()

  else:

    schedule.every().day.at(f"{AbrirArquivo('exemplo.txt')[-1]}").do(projeto.Alarme) 

    while True:
        schedule.run_pending()
        time.sleep(1)

Exec()

#Colocar no maximo dois remedios sob agenda.
