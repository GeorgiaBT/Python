from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()

janela.title("Cotação")

Label(janela, text="Moeda: ",
      font=("Arial 20")).grid(row=0, column=0)

moedaselecionado = ttk.Combobox(janela, font=("Arial 20"))

moedaselecionado["values"] = ('Afegane afegão',
                                'Ariary malgaxe',
                                'Baht tailandês',
                                'Balboa panamenho',
                                'Birr etíope',
                                'Boliviano da Bolívia',
                                'Bolívar soberano',
                                'Cedi ganês',
                                'Colom salvadorenho',
                                'Colón costarriquenho',
                                'Coroa dinamarquesa',
                                'Coroa islandesa',
                                'Coroa norueguesa',
                                'Coroa sueca',
                                'Coroa tcheca',
                                'Córdoba nicaraguense',
                                'Dalasi gambiano',
                                'Dinar argelino',
                                'Dinar bareinita',
                                'Dinar iraquiano',
                                'Dinar jordaniano',
                                'Dinar kuwaitiano',
                                'Dinar líbio',
                                'Dinar macedônio',
                                'Dinar sérvio',
                                'Dinar tunisiano',
                                'Dirham dos Emirados Árabes Unidos',
                                'Dirham marroquino',
                                'Dong vietnamita',
                                'Dram armênio',
                                'Dólar Liberiano',
                                'Dólar americano',
                                'Dólar australiano',
                                'Dólar bahamense',
                                'Dólar barbadense',
                                'Dólar belizenho',
                                'Dólar bermudense',
                                'Dólar bruneano',
                                'Dólar canadense',
                                'Dólar das Ilhas Cayman',
                                'Dólar das Ilhas Salomão',
                                'Dólar de Hong Kong',
                                'Dólar de Trinidad e Tobago',
                                'Dólar do Caribe Oriental',
                                'Dólar fijiano',
                                'Dólar guianense',
                                'Dólar jamaicano',
                                'Dólar namibiano',
                                'Dólar neozelandês',
                                'Dólar singapuriano',
                                'Dólar surinamês',
                                'Escudo cabo-verdiano',
                                'Euro',
                                'Florim arubano',
                                'Florim das Antilhas Holandesas',
                                'Florim húngaro',
                                'Franco CFA Central',
                                'Franco CFA ocidental',
                                'Franco CFP',
                                'Franco burundiano',
                                'Franco comoriano',
                                'Franco congolês',
                                'Franco do Djibouti',
                                'Franco guineano',
                                'Franco ruandês',
                                'Franco suíço',
                                'Gourde haitiano',
                                'Guarani paraguaio',
                                'Hryvnia ucraniano',
                                'Iene japonês',
                                'Kina papuásia',
                                'Kip laosiano',
                                'Kwacha malauiana',
                                'Kwacha zambiano',
                                'Kwanza angolano',
                                'Lari georgiano',
                                'Lek albanês',
                                'Lempira hondurenha',
                                'Leone de Serra Leoa',
                                'Leu moldávio',
                                'Leu romeno',
                                'Lev búlgaro',
                                'Libra Sudanesa',
                                'Libra egípcia',
                                'Libra esterlina',
                                'Libra libanesa',
                                'Lilangeni suazi',
                                'Lira turca',
                                'Loti lesotiano',
                                'Manat azeri',
                                'Manat turcomano',
                                'Marco conversível da Bósnia e Herzegovina',
                                'Metical moçambicano',
                                'Naira nigeriana',
                                'Ngultrum butanês',
                                'Novo dólar taiwanês',
                                'Novo shekel israelense',
                                'Novo sol peruano',
                                'Ouguiya mauritana',
                                'Pataca',
                                'Pa?anga tonganesa',
                                'Peso argentino',
                                'Peso chileno',
                                'Peso colombiano',
                                'Peso cubano',
                                'Peso dominicano',
                                'Peso filipino',
                                'Peso mexicano',
                                'Peso uruguaio',
                                'Pula botsuanesa',
                                'Quetzal guatemalteco',
                                'Quiate',
                                'Rand sul-africano',
                                'Real brasileiro',
                                'Rial catariano',
                                'Rial iemenita',
                                'Rial iraniano',
                                'Rial omanense',
                                'Riel',
                                'Ringgit malaio',
                                'Riyal saudita',
                                'Rublo bielorrusso',
                                'Rublo russo',
                                'Rupia Mauriciana',
                                'Rupia cingalesa',
                                'Rupia das Seychelles',
                                'Rupia indiana',
                                'Rupia indonésia',
                                'Rupia maldívia',
                                'Rupia nepalesa',
                                'Rúpia Paquistanesa',
                                'Som quirguiz',
                                'Som uzbeque',
                                'Somoni',
                                'Taka bengali',
                                'Tenge cazaque',
                                'Unidades de Fomento chilenas',
                                'Won sul-coreano',
                                'Xelim Ugandês',
                                'Xelim queniano',
                                'Xelim somali',
                                'Xelim tanzaniano',
                                'Yuan chinês',
                                'Yuan chinês (offshore)',
                                'Zloty polonês')

moedaselecionado.grid(row=0, column=1)

moedaselecionado.current(0)

def pesquisaritem():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select

    import pyautogui as tempoespera

    # Service verifica a versao do chrome e informa ao selenium para que o chromedrivermanager baixe o arquivo correspondente
    servico = Service(ChromeDriverManager().install())
    meunavegador = webdriver.Chrome(service=servico)

    meunavegador.get("https://www.google.com.br/")

    tempoespera.sleep(3)

    meunavegador.find_element(By.NAME, "q").send_keys("Dólar hoje")

    tempoespera.sleep(2)

    #faz a busca
    meunavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    tempoespera.sleep(4)

    valordolargoogle = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tempoespera.sleep(2)

   # print(valordolargoogle)

    todasmoedas = Select(meunavegador.find_element(By.CLASS_NAME, "l84FKc"))  # zuzy3c

    linha = 0

    for posicaoitem in todasmoedas.options:

        if posicaoitem.text == str(moedaselecionado.get()):

            tempoespera.sleep(2)

            pegadropdrown = meunavegador.find_element(By.CLASS_NAME, "l84FKc") #zuzy3c

            tempoespera.sleep(2)

            itemselecionado = Select(pegadropdrown)

            tempoespera.sleep(2)

            itemselecionado.select_by_index(linha)

            break

        linha = linha + 1

    tempoespera.sleep(4)

    valordolargoogle = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tempoespera.sleep(2)

    valorMoeda.config(text=str(moedaselecionado.get()) + ":" + valordolargoogle)

botaopesquisar = Button(text="Pesquisar",
                        font=("Arial 20"),
                        command=pesquisaritem)
botaopesquisar.grid(row=1, column=0, columnspan=2,sticky="NSEW")

valorMoeda = Label(janela, text="Valor em Reais: 0",
                         font=("Arial 20"))
valorMoeda.grid(row=2, column=0, columnspan=2,sticky="W")

janela.mainloop()