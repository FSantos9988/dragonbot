import pandas as pd
import time as tm
import requests as rq
import telegram as tgm
import calendar as cl
from datetime import datetime

TLGchatID = '1883725740'
TLGtoken  = '5741360202:AAFs0wl0mev7Zt4c2RzskUzeHY29Yo2NR6E'

TLGbot = tgm.Bot(token=TLGtoken)

while True:
  symbol = 'ETHUSDT' # Bitcoin em dólares
  timeinterval = 5

  now = datetime.utcnow()
  unixtime = cl.timegm(now.utctimetuple())

  since = unixtime
  start = str(since-60*60*10)

  url = f'https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={str(timeinterval)}m&limit=100'
  data = rq.get(url).json()

  #print(url)

  D = pd.DataFrame(data)
  D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
    'taker_base_vol', 'taker_quote_vol', 'is_best_match']

  period = 14
  df = D
  df['close'] = df['close'].astype(float)
  df2 = df['close'].to_numpy()

  df2 = pd.DataFrame(df2, columns = ['close'])
  delta = df2.diff()

  up, down = delta.copy(), delta.copy()
  up[up < 0] = 0
  down[down > 0] = 0

  _gain = up.ewm(com = (period - 1), min_periods = period).mean()
  _loss = down.abs().ewm(com = (period - 1), min_periods = period).mean()

  RS = _gain / _loss

  rsi = 100 - (1 + RS)
  rsi = rsi['close'].iloc[-1]
  rsi=round(rsi,1)

  msg = f'Binance Futures {symbol} RSI: {str(rsi)}, PERIOD: {str(period)}'

  TLGbot.sendMessage(chat_id=TLGchatID, text=msg)

  tm.sleep(5)