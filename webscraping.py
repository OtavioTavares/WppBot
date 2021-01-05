class Webscraping:

    def dados__futuro_vencimento(self):
        localdir = os.path.dirname(os.path.realpath(__file__))
        chromeOptions = webdriver.ChromeOptions()
        diretorio_download = localdir + "\\relatorios_futuro_vencimento"
        prefs = { "download.default_directory" : diretorio_download }
        chromeOptions.add_experimental_option("prefs", prefs)
        chromeOptions.add_argument('lang=pt-br')
        exe_path = os.path.join(localdir, 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=exe_path, options=chromeOptions)

        self.driver.get('https://app.tecnofit.com.br/ng/login')
        time.sleep(10)

        #Login no tecnofit
        campo_login = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[1]/div[1]/input")
        campo_login.click()
        email = "EMAIL_TECNOFIT"
        campo_login.send_keys(email)

        campo_senha =self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[1]/div[2]/input")
        campo_senha.click()      
        senha = "SENHA_TECNOFIT"
        campo_senha.send_keys(senha)

        campo_acessar = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[2]/div/div/button[2]")
        campo_acessar.click()
        time.sleep(7)

        #Acessando planilha de clientes ativos
        campo_relatorios = self.driver.find_element_by_link_text('Relatórios')
        campo_relatorios.click()
        time.sleep(3)           

        #Clientes ativos
        campo_clientes_ativos = self.driver.find_element_by_link_text('Clientes Ativos')
        campo_clientes_ativos.click()
        time.sleep(3)
        #Todos os dados do cliente
        campo_contato_cliente = self.driver.find_element_by_xpath("//*[@id='frmPesquisa'/div/div[2]/div/div/div[2]/div/div/div/label/div/ins")
        campo_contato_cliente.click()
        time.sleep(3)

        campo_pesquisa = self.driver.find_element_by_xpath("//*[@id='btnPesquisa']")
        campo_pesquisa.click()
        time.sleep(3)
        try:  
            campo_excel_download = self.driver.find_element_by_xpath("//*[@id='btnExporar']")
            campo_excel_download.click()
        except:
            print("Nenhum usuário atrasado")


    def dados_atrasados(self):
        localdir = os.path.dirname(os.path.realpath(__file__))
        diretorio_download = localdir + "\\relatorios_atrasados"
        prefs = { "download.default_directory" : diretorio_download }
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", prefs)
        chromeOptions.add_argument('lang=pt-br')
        exe_path = os.path.join(localdir, 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=exe_path, options=chromeOptions)

        
        #Acessando o site tecnofit
        
        self.driver.get('https://app.tecnofit.com.br/ng/login')
        time.sleep(8)

        #Login no tecnofit
        campo_login = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[1]/div[1]/input")
        campo_login.click()
        email = "EMAIL_TECNOFIT"
        campo_login.send_keys(email)

        campo_senha =self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[1]/div[2]/input")
        campo_senha.click()      
        senha = "SENHA_TECNOFIT"
        campo_senha.send_keys(senha)

        campo_acessar = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[1]/div/div[2]/div/form/div[2]/div/div/button[2]")
        campo_acessar.click()
        time.sleep(5)
        
        #Obter pagina sobre os contratos
        self.driver.get('https://app.tecnofit.com.br/relatorio/clienteContrato')
        time.sleep(5)

      
        #Selecionado o campo de datas
        campo_data = self.driver.find_element_by_xpath("//*[@id='date_range']")
        campo_data.click()
        time.sleep(3)

        #Análise dos atrasados hoje
        campo_data_hoje = self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/ul/li[1]")
        campo_data_hoje.click()
        time.sleep(3)

        #Selecionando o campo de status cliente
        campo_status_cliente = self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[1]/div/div/button/span[1]")
        campo_status_cliente.click()
        time.sleep(3)

        #Clientes bloqueados
        campo_status_bloqueado = self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[1]/div/div/div/ul/li[2]")
        campo_status_bloqueado.click()
        time.sleep(3)

        #Clientes sem contratos
        campo_status_sem_contrato = self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[1]/div/div/div/ul/li[6]")
        campo_status_sem_contrato.click()
        time.sleep(3)

        #Saindo do campo de status cliente
        campo_status_cliente = self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[1]/div/div/button/span[1]")
        campo_status_cliente.click()
        time.sleep(3)

        #Selecionando o campo de contratos
        campo_status_contrato = self.driver.find_element_by_xpath( "//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[2]/div/div/button")
        campo_status_contrato.click()
        time.sleep(3)


        #Contratos em atraso
        campo_contratos_em_atraso =self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/a/span")
        campo_contratos_em_atraso.click()
        time.sleep(3)

        #Sair do campo de contratos
        campo_status_contrato = self.driver.find_element_by_xpath( "//*[@id='frmPesquisa']/div/div[2]/div[1]/div/div[2]/div/div/button")
        campo_status_contrato.click()
        time.sleep(3)

        #Selecionando o contato completo do cliente
        campo_detalhes_contato = self.driver.find_element_by_xpath("//*[@id='frmPesquisa']/div/div[2]/div[3]/div[2]/div/div/div/label/div/ins")
        campo_detalhes_contato.click()
        time.sleep(3)

        #Confirmando a pesquisa
        campo_pesquisar = self.driver.find_element_by_xpath("//*[@id='btnPesquisa']")
        campo_pesquisar.click()
        time.sleep(3)

        try:    
            #Baixando arquivo excel
            campo_excel_download_pendentes = self.driver.find_element_by_xpath("//*[@id='btnExporar']")
            campo_excel_download_pendentes.click()
        except:
            print("Nenhum usuário pendente")
            
        
    def notificar_futuro_vencimento(self):
        localdir = os.path.dirname(os.path.realpath(__file__))
        diretorio_download = localdir + "\\relatorios_futuro_vencimento\\relatorio.xls"

        df = pd.read_html(diretorio_download)
        
        df_cad = df[0]
        
        localdir = os.path.dirname(os.path.realpath(__file__))
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('lang=pt-br')
        exe_path = os.path.join(localdir, 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=exe_path, options=chromeOptions)
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)

        #Data de hoje
        data_hora = datetime.datetime.now()
        data_hoje = data_hora.strftime("%d/%m/%Y")

        data_hoje_convertido = datetime.datetime.strptime(data_hoje,"%d/%m/%Y")
        ven_mensal = 3
        data_notificacao = data_hoje_convertido  + datetime.timedelta(ven_mensal)

        y = str(data_notificacao.year)
        m = str(data_notificacao.month)
        d = str(data_notificacao.day)
        data = d+"/"+m+"/"+y

        #DATA DE VENCIMENTO ATUALIZAR ***
        nomes_clientes = list(df_cad[df_cad["Vencimento"] <= data]["Cliente"])
        telefones_clientes = list(df_cad[df_cad["Vencimento"] <= data]["Contato"])

        nomes_telefones = zip(nomes_clientes,telefones_clientes)
                
        for nome,telefone in nomes_telefones:
            
            mensagem_vencimento = ("Boa tarde " + str(nome)+".\nNós da equipe Revolução estamos informando que seu plano vence em 3 dias."
                                "\nVenha renovar essa experiência novamente!")
            telefone_bruto = str(telefone)
            telefone_bruto = telefone_bruto.replace(" ","")
            telefone_bruto = telefone_bruto.replace("(","")
            telefone_bruto = telefone_bruto.replace(")","")
            telefone_bruto = telefone_bruto.replace("-","")
            telefone_cliente = telefone_bruto[0:11]


            #Enviar mensagem para o contato
            try:
                link_de_acesso = ('https://api.whatsapp.com/send?phone=55'+telefone_cliente)
                self.driver.get(link_de_acesso)
                            
                time.sleep(5)
                campo_iniciar_conversa = self.driver.find_element_by_xpath("//*[@id='action-button']")
                campo_iniciar_conversa.click()
                            

                campo_wpp_web = self.driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a")
                time.sleep(3)
                campo_wpp_web.click()
                time.sleep(10)
                
                campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                time.sleep(2)
                campo_texto.click()
                        
                for ch in mensagem_vencimento:
                    if ch == "\n":
                        ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                    else:
                        campo_texto.send_keys(ch)
                #Enviando o texto
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)
                botao_enviar.click()
                time.sleep(10)
            except:
                pass

    def notificar_atrasados(self):
        localdir = os.path.dirname(os.path.realpath(__file__))
        diretorio_download = localdir + "\\relatorios_atrasados\\relatorio.xls"

        df = pd.read_html(diretorio_download)
        
        df_cad = df[0]
        
        localdir = os.path.dirname(os.path.realpath(__file__))
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('lang=pt-br')
        exe_path = os.path.join(localdir, 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=exe_path, options=chromeOptions)
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)

        #Data de hoje
        data_hora = datetime.datetime.now()
        data_hoje = data_hora.strftime("%d/%m/%Y")

        data_hoje_convertido = datetime.datetime.strptime(data_hoje,"%d/%m/%Y")
        ven_mensal = 0
        data_notificacao = data_hoje_convertido  + datetime.timedelta(ven_mensal)

        y = str(data_notificacao.year)
        m = str(data_notificacao.month)
        d = str(data_notificacao.day)
        data = d+"/"+m+"/"+y
        #DATA DE VENCIMENTO ATUALIZAR ***
        nomes_clientes = list(df_cad[df_cad["Vencimento"] <= data]["Cliente"])
        telefones_clientes = list(df_cad[df_cad["Vencimento"] <= data]["Contato"])

        nomes_telefones = zip(nomes_clientes,telefones_clientes)
                
        for nome,telefone in nomes_telefones:
            
            mensagem_vencimento = ("Boa tarde " + str(nome)+".\nNós da equipe Revolução estamos informando que seu plano venceu hoje."
                                "\nVenha renovar essa experiência novamente!")
            telefone_bruto = str(telefone)
            telefone_bruto = telefone_bruto.replace(" ","")
            telefone_bruto = telefone_bruto.replace("(","")
            telefone_bruto = telefone_bruto.replace(")","")
            telefone_bruto = telefone_bruto.replace("-","")
            telefone_cliente = telefone_bruto[0:11]


            #Enviar mensagem para o contato
            try:
                link_de_acesso = ('https://api.whatsapp.com/send?phone=55'+telefone_cliente)
                self.driver.get(link_de_acesso)
                            
                time.sleep(5)
                campo_iniciar_conversa = self.driver.find_element_by_xpath("//*[@id='action-button']")
                campo_iniciar_conversa.click()
                            

                campo_wpp_web = self.driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a")
                time.sleep(3)
                campo_wpp_web.click()
                time.sleep(10)
                
                campo_texto = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                time.sleep(2)
                campo_texto.click()
                        
                for ch in mensagem_vencimento:
                    if ch == "\n":
                        ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                    else:
                        campo_texto.send_keys(ch)
                #Enviando o texto
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)
                botao_enviar.click()
                time.sleep(10)
            except:
                pass
