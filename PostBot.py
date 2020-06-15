from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

class postBotFacebook:

    def __init__(self):

        # Caso queira executar no windowns, precisa ajutar o local da path do webdriver
        self.driver = webdriver.Firefox()
        self.groupList = ['https://www.facebook.com/groups/3190866357637973/']
        ''',
                          'https://www.facebook.com/groups/547101548649889/',
                          'https://www.facebook.com/groups/127554540780625/',
                          'https://www.facebook.com/groups/1401113143461223/',
                          'https://www.facebook.com/groups/1089174344430456/',
                          'https://www.facebook.com/groups/456501161401329/',
                          'https://www.facebook.com/groups/114513845416203/',
                          'https://www.facebook.com/groups/131601414118211/',
                          'https://www.facebook.com/groups/1464038113861362/',
                          'https://www.facebook.com/groups/358910174220684/',
                          'https://www.facebook.com/groups/1700715133531822/',
                          'https://www.facebook.com/groups/486404922105015/',
                          'https://www.facebook.com/groups/354636257987545/',
                          'https://www.facebook.com/groups/456943084342938/',
                          'https://www.facebook.com/groups/173128086190318/',
                          'https://www.facebook.com/groups/645817649524518/',
                          'https://www.facebook.com/groups/233091337537454/',
                          'https://www.facebook.com/groups/435929026453698/',
                          'https://www.facebook.com/groups/662891787202884/'
                          ]
                          '''


    def login(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(3)
        # escrever nome de usuário no input
        print("Digite o nome de usuário:")
        userName = str(input())
        print("Digite a senha:")
        userPass = str(input())

        userLabel = driver.find_element_by_xpath('//*[@id="email"]')
        userLabel.click()
        userLabel.clear()
        userLabel.send_keys(userName)

        # escrever senha no input
        passWordLabel = driver.find_element_by_xpath('//*[@id="pass"]')
        passWordLabel.click()
        passWordLabel.clear()
        passWordLabel.send_keys(userPass)

        # apertar o botão 'entrar'
        buttonLogin = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        buttonLogin.click()
        time.sleep(1)

    def postText(self, mensagem):
        driver = self.driver

        for groupLink in self.groupList:
            driver.get(groupLink)

            # ação: clicar no box 'Escrever algo' e digitar a mensagem
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'xhpc_message_text'))
            )

            escreverAlgo = driver.find_element_by_name('xhpc_message_text')
            escreverAlgo.clear()
            escreverAlgo.click()
            escreverAlgo.send_keys(mensagem)
            time.sleep(5)
            postar = driver.find_element(By.XPATH, '//span[text()="Publicar"]')
            postar.click()
            time.sleep(5)

    def postImage(self, endereco, mensagem):

        driver = self.driver

        for groupLink in self.groupList:
            try:
                driver.get(groupLink)

                # ação: clicar no box 'Inserir Imagem' e adicionar doc
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, 'xhpc_message_text'))
                )

                escreverAlgo = driver.find_element_by_name('xhpc_message_text')
                escreverAlgo.clear()
                escreverAlgo.click()
                escreverAlgo.send_keys(mensagem)
                time.sleep(2)

                enviarArquivo = driver.find_element(By.XPATH, '//span[text()="Foto/vídeo"]')
                time.sleep(1)
                enviarArquivo.click()
                time.sleep(5)
                enviarArquivo = driver.find_element_by_name('composer_photo')
                enviarArquivo.send_keys('/home/diogo/Downloads/questao2.jpg')
                time.sleep(5)

                postar = driver.find_element(By.XPATH, '//span[text()="Publicar"]')
                postar.click()
                time.sleep(5)

            except:
                continue

    def postFanPageToGrupo(self):

        urlPublic = 'https://www.facebook.com/AkasaConcursos/photos/a.118824473198931/118824449865600/?type=3&av=110427400705305&eav=AfaaWMXHtgUGwI8AdwPs1CLlyEcpebZ4oLcO3AtAvYjWoxkP3I5FV5ykjKPngkeZZIk&theater'
        listaNomeGrupo = ['akasa concursos']

        driver = self.driver
        driver.get(urlPublic)
        time.sleep(5)
        compartilhar = driver.find_elements_by_xpath("//*[contains(text(), 'Compartilhar')]")
        compartilhar[-1].click()
        time.sleep(3)
        select = driver.find_element(By.XPATH, '//span[text()="Select an option"]')
        select.click()
        time.sleep(0.5)

        emGrupo = driver.find_element(By.XPATH, '//span[text()="Compartilhar em um grupo"]')
        emGrupo.click()

        nomeGrupo = driver.find_element(By.XPATH, "//input[@placeholder='Nome do grupo']")
        nomeGrupo.click()
        time.sleep(0.5)
        nomeGrupo.send_keys('Akasa concursos')
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys('Postagem da Page para Grupo')
        actions.perform()

        time.sleep(1)

        postar = driver.find_element(By.XPATH, '//span[text()="Publicar"]')
        postar.click()
        time.sleep(5)


bot = postBotFacebook()
bot.login()
#bot.postImage('enderecooo', 'Galera, Certo ou Errado? \n Veja o Gabarito no vídeo: https://youtu.be/erYuyiqFqHk')
bot.postFanPageToGrupo()
