from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from os import listdir, rename
from os.path import dirname, realpath

import shutil
import os
import time
import pandas as pd
import datetime
import xlrd
import os
import getpass


class WhatsappBot:
    
    def __init__(self):
        self.reset = "BOT"
        self.atendente = "ATENDENTE" 
        localdir = os.path.dirname(os.path.realpath(__file__))
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_argument(r"--headless")
        chromeOptions.add_argument('lang=pt-br')
        chromeOptions.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data\Wbot".format(getpass.getuser()))
        exe_path = os.path.join(localdir, 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=exe_path, options=chromeOptions)
        
        self.driver.maximize_window()
        
        self.driver.get('https://web.whatsapp.com')
        
        time.sleep(20)

                                  
    def enviar_texto_validacao(self):
            #Localizando o contato ou grpo
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()
        
            #Localizando o campo para escrever
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(3)
            campo_texto.click()

            self.mensagem = "random22"
        
            #Escrevendo o texto
            campo_texto.send_keys(self.mensagem)

            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()

    def verificador_relatorios(self):
        #Arquivos na pasta do main.py
        local_bot = dirname(realpath(__file__))

        #Local dos relatorios
        local_rel_atrasados = local_bot + "\\relatorios_atrasados"
        local_rel_futuro_venc = local_bot + "\\relatorios_futuro_vencimento"

        #Backup dos relatorios
        backup_rel_atrasados = local_bot + "\\backups\\backup_relatorios_atrasados"
        backup_rel_futuro_venc = local_bot + "\\backups\\backup_relatorios_futuro_vencidos"

        #Data de hoje para renomear os backups
        data_hora = datetime.now()
        data_hoje = data_hora.strftime("%d_%m_%Y")


        if (len(listdir(local_rel_atrasados)) != 0):
            list_rel_atrasados = listdir(local_rel_atrasados)
            old_name_1 = list_rel_atrasados[0].split(".")
            new_name_1 = old_name_1[0]+ "_" + data_hoje + "." + old_name_1[1]
            
            rename(local_rel_atrasados+"\\"+list_rel_atrasados[0],local_rel_atrasados+"\\"+new_name_1)
            shutil.move(local_rel_atrasados+"\\"+new_name_1,backup_rel_atrasados)
        
        if (len(listdir(local_rel_futuro_venc)) != 0):
            list_rel_futuro_venc = listdir(local_rel_futuro_venc)
            old_name_2 = list_rel_futuro_venc[0].split(".")
            new_name_2 = old_name_2[0]+ "_" + data_hoje + "." + old_name_2[1]
            rename(local_rel_futuro_venc+"\\"+list_rel_futuro_venc[0],local_rel_futuro_venc+"\\"+new_name_2)
            shutil.move(local_rel_futuro_venc+"\\"+new_name_2,backup_rel_futuro_venc)
            
    

    def ultimas_notificacoes(self):
        #Buscar notificaçoes não lidas
        campo_busca_notificacao = self.driver.find_elements_by_class_name('VOr2j')

        #Ultima notificacao nao lida
        ultimo = len(campo_busca_notificacao) - 1
        campo_busca_notificacao[ultimo].click()

        #Lendo a mensagem da notificação
        post = self.driver.find_elements_by_class_name('_1VzZY')
        ultimo = len(post) - 1
        msg_recebida = str(post[ultimo].text)


        #Verificando a mensagem
        if msg_recebida == "1":            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_1 = ("Os horários de funcionamento:"
                          "\n*Seg.*  06h30 até 12h00 -- 16h00 até 22h00"
                          "\n*Ter.*   06h30 até 12h00 -- 16h00 até 22h00"
                          "\n*Qua.* 06h30 até 12h00 -- 16h00 até 22h00"
                          "\n*Qui.*  06h30 até 12h00 -- 16h00 até 22h00"
                          "\n*Sex.*  06h30 até 12h00 -- 16h00 até 22h00"
                          "\n*Sab.*  08h00 até 12h00 "
                          "\n"
                          "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_1:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()

            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

                   
        if msg_recebida == "2":            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_2 = ("As academias Revolução se encontram:"
                          "\n Av. Pres. Castelo Branco, 499 - Jardim Zaira, Mauá - SP, 09321-375"
                          "\n R. Rosa Bonini Mariani, 119 - Jardim Guapituba, Mauá - SP, 09360-340"
                          "\n"
                          "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_2:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()


            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

        if msg_recebida == "3":            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_5 = ("Modalidades: "
                          "\n*Musculação* | Segunda - Sábado"
                          "\n*Fitdante* | Terça - Quinta"
                          "\n*Karatê* | Terça - Quinta"
                          "\n*Muay Thai* | Segunda - Quarta - Sexta"
                          "\n*Pilates & Yoga* | Terça - Quinta"
                          "\n*Balé infantil* | Terça - Quinta"
                          "\n*Funcional* | Segunda - Quarta - Sexta"
                          "\n*Jump* | Segunda - Terça - Quinta"
                          "\n*Cross Training* | Segunda - Quarta - Sexta"
                          "\n*Abdômen* | Terça - Quinta"
                          "\n*Jiu Jitsu* | Sábado"
                          "\n Quer saber os horarios das aulas? digite *6*"
                          "\n"
                          "\nCaso queira voltar para o menu, digite *0*"
                          )
            for ch in mensagem_5:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
                    
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()


           
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

                  
        if msg_recebida == "4":            
          
            #Botao anexar
            campo_anexar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/div/span")
            campo_anexar.click()

            #Selecionar imagens
            campo_select_img = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input")
            campo_select_img.send_keys(os.getcwd()+"\imagens_send\planos\planos_pagamentos.jpeg")
            time.sleep(3)


            #Enviando o texto
            campo_texto = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
            campo_texto.click()
            mensagem_4 = ("Segue as imagens com os valores, para mais informações, digite *7* e falará com um atendente."
                          "\n"
                         "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_4:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)

            botao_enviar = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div")
            botao_enviar.click()

            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

            

                    
        if msg_recebida == "5":            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_5 = ("Promoções: "
                          "\n*BLACK* *NOVEMBRO*"
                          "\nTodas as modalidades por *R$89,90*."
                          "\n*Valido até: 03/12/2020"
                          "\n"
                          "\nCaso queira voltar para o menu, digite *0*"
                          )
            for ch in mensagem_5:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
                    
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()
           
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

        if msg_recebida == "6":            
            #Localizando o campo para escrever
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(3)
            campo_texto.click()
            mensagem_6 = ("Por favor, selecionar qual unidade:"
                          "\n*6.1* - Unidade Guapituba"
                          "\n*6.2* - Unidade Zaíra"
                          "\n"
                         "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_6:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)

            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()

            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()


        if msg_recebida == "6.1":
            
            #Botao anexar
            campo_anexar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/div/span")
            campo_anexar.click()

            #Selecionar imagens
            campo_select_img = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input")
            campo_select_img.send_keys(os.getcwd()+"\imagens_send\horarios\\horario_guapituba.jpeg")
            time.sleep(3)


            #Enviando o texto
            campo_texto = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
            campo_texto.click()
            mensagem_61 = ("Segue acima os horários da Unidade Guapituba."
                           "\nPara mais informações, digite *7* e falará com um atendente."
                          "\n"
                         "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_61:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)

            botao_enviar = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div")
            botao_enviar.click()

            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()


        if msg_recebida == "6.2":
            
            #Botao anexar
            campo_anexar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/div/span")
            campo_anexar.click()

            #Selecionar imagens
            campo_select_img = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input")
            campo_select_img.send_keys(os.getcwd()+"\imagens_send\horarios\\horario_zaira.jpeg")
            time.sleep(3)


            #Enviando o texto
            campo_texto = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
            campo_texto.click()
            mensagem_61 = ("Segue acima os horários da Unidade Zaíra."
                           "\nPara mais informações, digite *7* e falará com um atendente."
                          "\n"
                         "\nCaso queira voltar para o menu, digite *0*")
            for ch in mensagem_61:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)

            botao_enviar = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div")
            botao_enviar.click()

            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()
                      
        if msg_recebida == "7":            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_7 = ("Nossa atendente logo enviara mensagem."
                          "\nAgradecemos pela escolha."
                          "\n"
                          "\nCaso queira voltar para o menu, digite *0*")
      
            for ch in mensagem_7:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()

            #Obtendo contato da pessoa
            campo_nome = self.driver.find_element_by_xpath("//*[@id='main']/header/div[2]/div[1]/div/span")
            campo_nome.click()
            time.sleep(4)

            #Numero da pessoa            
            post_cliente = self.driver.find_elements_by_class_name('_3VotX')
            todos_contatos = len(post_cliente)
            contato_cliente = str(post_cliente[4].text)
            time.sleep(2)

            #Horario do atendimento
            data_hora = datetime.datetime.now()
            horario_cliente = data_hora.strftime("%d/%m/%Y %H:%M")
            
            #Enviando para o atendente
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.atendente}']")
            campo_busca_contato.click()
            
            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click()

            #Redirecionar conversa automaticamente
            telefone_bruto = contato_cliente
            telefone_bruto = contato_cliente
            telefone_bruto = telefone_bruto.replace("+","")
            telefone_bruto = telefone_bruto.replace(" ","")
            telefone_bruto = telefone_bruto.replace("-","")
            telefone = telefone_bruto
            
            link_cliente = ('https://api.whatsapp.com/send?phone='+telefone)
            
            mensagem_automatica = ("Cliente solicitou atendimento direto com o atendente."
                                   "\n*Contato:* " + str(contato_cliente)+
                                   "\n*Horário:* " + str(horario_cliente)+
                                   "\n*Acessar conversa:* "+ str(link_cliente))

            for ch in mensagem_automatica:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)

            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()
          
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

        if msg_recebida == "random22":
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()

        if (msg_recebida != "random22" and ( msg_recebida !="1" and msg_recebida !="2" and msg_recebida !="3" and msg_recebida !="4"
                                             and msg_recebida !="5"and msg_recebida !="6"and msg_recebida !="7" and msg_recebida != "0"
                                             and msg_recebida != "6.1"and msg_recebida != "6.2")):
            
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_automatica = ("Bem vindo a Academia Revolução"
                                   "\nComo posso te ajudar?"
                                   "\n *1* - Horário de funcionamento."
                                   "\n *2* - Localização das academias."
                                   "\n *3* - Modalidades."
                                   "\n *4* - Plano de pagamento."
                                   "\n *5* - Promoções."
                                   "\n *6* - Quadro de horários."
                                   "\n *7* - Falar com atendente.")

            for ch in mensagem_automatica:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
                    
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()

            
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()
            
        if msg_recebida == "0":  
            campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            time.sleep(2)
            campo_texto.click() 
            mensagem_automatica = ("Bem vindo a Academia Revolução"
                                   "\nComo posso te ajudar?"
                                   "\n *1* - Horário de funcionamento."
                                   "\n *2* - Localização das academias."
                                   "\n *3* - Modalidades."
                                   "\n *4* - Plano de pagamento."
                                   "\n *5* - Promoções."
                                   "\n *6* - Quadro de horários."
                                   "\n *7* - Falar com atendente.")

            for ch in mensagem_automatica:
                if ch == "\n":
                    ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    campo_texto.send_keys(ch)
                    
            #Enviando o texto
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            botao_enviar.click()

            
            campo_busca_contato = self.driver.find_element_by_xpath(f"//span[@title='{self.reset}']")
            campo_busca_contato.click()
