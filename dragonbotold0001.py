import requests
import telegram
import time
import math

# Seta o token e o chat_id do telegram
botToken = '5741360202:AAFs0wl0mev7Zt4c2RzskUzeHY29Yo2NR6E'
chatID = '1883725740'

# Cria o bot do telegram e passa o token
bot = telegram.Bot(botToken)

"""
Função para processar e enviar mensagens para o telegram - Double
"""
def double():
    url = 'https://blaze.com/api/roulette_games/recent' # Guarda URL da fonte de dados da Blaze - Double

    response = requests.get(url) # Pega URL 
    r = response.json() # Transforma dados em array

    rayColor = [] # Cria array para cores
    rayNumber = [] # Cria array para números

    rollID = r[0]['id'] # Pega o id da rolagem

    # Laço para ler os dados capturados do site da Blaze
    for x in range(len(r)):
        color = r[x]['color'] # Pega a cor da rolagem

        # Seta o indicador da cor: B = Branco(0), V = Vermelho(1), P = Preto(2)
        if color == 0:
            color = 'B'
        
        if color == 1:
            color = 'V'
        
        if color == 2:
            color = 'P'

        number = r[x]['roll'] # Pega o número da rolagem

        rayColor.append(color) # Adiciona ao array a cor capturada
        rayNumber.append(number) # Adiciona ao array o número capturado

    if rayColor[0:1] == ['B']:
        msg =  f'''::: DRAGONBOT.RF.GD :::\n'''
        msg += f'''::: --  DOUBLE  -- :::\n'''
        msg += f'''✅ ROLAGEM DE ⚪ ... RECALCULANDO!\n'''
        msg += f'''✅ ID DA ROLAGEM: {rollID}\n'''
        msg += f''':::MAIOR BOT DE BLAZE DO BRAZIL:::'''
        bot.send_message(chat_id=chatID, text=msg)
        time.sleep(5)

    elif rayColor[1] == 'B':
        icnclr = ''

        if rayColor[0] == 'V':
            icnclr = '🔴'
        else:
            icnclr = '⚫'

        msg = '''::: DRAGONBOT.RF.GD :::\n'''
        msg += ''':::  --  DOUBLE  -- :::\n'''
        msg += f'''✅ POSSÍVEL ROLAGEM DE {icnclr} DAQUI A {rayNumber[0]} ROLAGENS!\n'''
        msg += f'''✅ ID DA ROLAGEM: {rollID}\n'''
        msg += ''':::MAIOR BOT DE BLAZE DO BRAZIL:::'''
        bot.send_message(chat_id=chatID, text=msg)
        time.sleep(5)

    elif rayColor[0:4] == ['V', 'V', 'V', 'V']:
        msg = ''' ::: DRAGONBOT.RF.GD :::\n'''
        msg += ''':::  --  DOUBLE  -- :::\n'''
        msg += '''✅ POSSÍVEL ENTRADA NO 🔴 BUSCAR APOIO NO ⚪\n'''
        msg += f'''✅ ID DA ROLAGEM: {rollID}\n'''
        msg += ''':::MAIOR BOT DE BLAZE DO BRAZIL:::'''
        bot.send_message(chat_id=chatID, text=msg)
        time.sleep(5)

    elif rayColor[0:4] == ['P', 'P', 'P', 'P']:
        msg = ''' ::: DRAGONBOT.RF.GD :::\n'''
        msg += ''':::  --  DOUBLE  -- :::\n'''
        msg += '''✅ POSSÍVEL ENTRADA NO ⚫ BUSCAR APOIO NO ⚪\n'''
        msg += f'''✅ ID DA ROLAGEM: {rollID}\n'''
        msg += ''':::MAIOR BOT DE BLAZE DO BRAZIL:::'''
        bot.send_message(chat_id=chatID, text=msg)
        time.sleep(5)
        
"""
Função para processar e enviar mensagens para o telegram - Crash
"""
def crash():
    url = 'https://blaze.com/api/crash_games/recent' # Guarda URL da fonte de dados da Blaze - Crash
    
    response = requests.get(url)
    r = response.json()

    rayCrash = []

    crashID = r[0]['id']

    for x in range(len(r)):
        crash = r[x]['crash_point']

        rayCrash.append(crash)

    media = (float(rayCrash[0]) + float(rayCrash[1]) + float(rayCrash[2]) + float(rayCrash[3]) + float(rayCrash[4])) / 5.0

    if media <= 2.0:
        msg =  f'''::: DRAGONBOT.RF.GD :::\n'''
        msg += f'''::: --  CRASH  -- :::\n'''
        msg += f'''✅ POSSÍVEL 4x DETECTADO\n'''
        msg += f'''✅ ID DO ÚLTIMO CRASH: {crashID}\n'''
        msg += f''':::MAIOR BOT DE BLAZE DO BRAZIL:::'''
        bot.send_message(chat_id=chatID, text=msg)
        time.sleep(5)

# Execução principal do programa
while True:
    double()
    crash()

    time.sleep(30)