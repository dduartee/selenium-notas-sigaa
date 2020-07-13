from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys
from getpass import getpass

logininput = input("Usuario: ")
senhainput = str(getpass(prompt="Senha: ", stream=None))

# Criar instância do navegador
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')

browser.get('https://sig.ifsc.edu.br/sigaa/verTelaLogin.do')

# Seleciono todos os elementos que possuem a class post
login = browser.find_elements_by_name("user.login")[0]
senha = browser.find_elements_by_name("user.senha")[0]

login.send_keys(logininput)
senha.send_keys(senhainput)

print("\nlogando...\n")
browser.find_elements_by_xpath('//*[@id="conteudo"]/div[3]/form/table/tfoot/tr/td/input')[0].click()#submit
time.sleep(0.5)
#descomente estas linhas caso tenha outro curso vinculado
#browser.find_elements_by_xpath('/html/body/div[4]/div[2]/form/table/tbody/tr/td/table/tbody/tr[2]/td[5]/a')[0].click()#seleciona curso
#time.sleep(1)

materias_array = [
  'sociologia',
  'qualidade',
  'metrologia',
  'matematica',
  'portugues',
  'cts',
  'artes',
  'biologia',
  'desenho',
  'edf',
  'eletrica',
  'filosofia',
  'fisica',
  'geografia',
  'historia',
  'ingles',
  'quimica',
  'usinagem'
]

for i in materias_array:
  time.sleep(1)
  print(i)
  print("clicando...")
  if i == 'artes':
    time.sleep(1)
    try:
      artes = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[1]/td[1]/form/a')[0]
      artes.click()
    except:
      print("error123")
  elif i == 'biologia':
    time.sleep(1)
    try:
      biologia = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[3]/td[1]/form/a')[0]
      biologia.click()
    except:
      print("error123")
  elif i == 'cts':
    time.sleep(1)
    try:
      cts = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[5]/td[1]/form/a')[0]
      cts.click()
    except:
      print("error123")
  elif i == 'desenho':
    time.sleep(1)
    try:
      desenho = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr[7]/td[1]/form/a')[0]
      desenho.click()
    except:
      print("error123")
  elif i == 'edf':
    time.sleep(1)
    try:
      edf = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[9]/td[1]/form/a')[0]
      edf.click()
    except:
      print("error123")
  elif i == 'eletrica':
    time.sleep(1)
    try:
      eletrica = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[11]/td[1]/form/a')[0]
      eletrica.click()
    except:
      print("error123")
  elif i == 'filosofia':
    time.sleep(1)
    try:
      filosofia =browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[13]/td[1]/form/a')[0]
      filosofia.click()
    except:
      print("error123")
  elif i == 'fisica':
    time.sleep(1)
    try:
      fisica = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[15]/td[1]/form/a')[0]
      fisica.click()
    except:
      print("error123")
  elif i == 'geografia':
    time.sleep(1)
    try:
      geografia = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[17]/td[1]/form/a')[0]
      geografia.click()
    except:
      print("error123")
  elif i == 'historia':
    time.sleep(1)
    try:
      historia = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[19]/td[1]/form/a')[0]
      historia.click()
    except:
      print("error123")
  elif i == 'ingles':
    time.sleep(1)
    try:
      ingles = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[21]/td[1]/form/a')[0]
      ingles.click()
    except:
      print("error123")
  elif i == 'portugues':
    time.sleep(1)
    try:
      portugues = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[23]/td[1]/form/a')[0]
      portugues.click()
    except:
      print("error123")
  elif i == 'matematica':
    time.sleep(1)
    try:
      matematica = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[25]/td[1]/form/a')[0]
      matematica.click()
    except:
      print("error123")
  elif i == 'metrologia':
    time.sleep(1)
    try:
      metrologia = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[27]/td[1]/form/a')[0]
      metrologia.click()
    except:
      print("error123")
  elif i == 'qualidade':
    time.sleep(1)
    try:
      qualidade = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[29]/td[1]/form/a')[0]
      qualidade.click()
      time.sleep(1)
    except:
      print("error123")
  elif i == 'quimica':
    time.sleep(1)
    try:
      quimica = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[31]/td[1]/form/a')[0]
      quimica.click()
    except:
      print("error123")
  elif i == 'sociologia':
    time.sleep(1)
    try:
      sociologia = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[33]/td[1]/form/a')[0]
      sociologia.click()
    except:
      print("error123")
  elif i == 'usinagem':
    time.sleep(1)
    try:
      usinagem = browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/table[2]/tbody/tr[35]/td[1]/form/a')[0]
      usinagem.click()
    except:
      print("error123")
  else:
    print("error")
  try:
    browser.find_elements_by_xpath('/html/body/div[1]/form/div/div/div[2]/div[1]')[0].click()
  except:
    print("secao aberta")
  try:
    browser.find_elements_by_xpath('/html/body/div[1]/form/div/div/div[2]/div[3]/table/tbody/tr/td/a[3]')[0].click()
  except:
    print("178")
  print("ver notas")
  
  time.sleep(3)
  f = open("notas.txt", "a")
  f.write("\n"+i+' '+browser.find_elements_by_tag_name('tbody')[0].text+"\n")
  print("escrevendo")
  f.close()
  #browser.find_elements_by_xpath('/html/body/div[1]/div[1]/div[1]/a')[0].click()
  print("voltando para a pagina inicial")
  browser.get("https://sig.ifsc.edu.br/sigaa/portais/discente/discente.jsf")
  #browser.find_elements_by_xpath('/html/body/div[1]/div[5]/div[2]/div[4]/form[2]/button[1]')[0].click()
  time.sleep(1)
f = open("notas.txt", "r")
print("LIDO "+f.read())
browser.quit()
#print(browser.find_elements_by_class_name('notas')[0].text)
