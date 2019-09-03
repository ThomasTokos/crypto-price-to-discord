#imports
#create a a webhook on Discord and and put the API URL in the blanks. Make sure you match it with the crypto.
import requests
# ETH Webhook URL
discord_eth_hook = ''
# BTC Webhook URL
discord_btc_hook = ''
# BCH Webhook URL
discord_bch_hook = ''
# LTC Webhook URL
discord_ltc_hook = ''
# XMR Webhook URL
discord_xmr_hook = ''
# XRP Webhook URL
discord_xrp_hook = ''
# XLM Webhook URL
discord_xlm_hook = ''
# Dash Webhook URL
discord_dash_hook = ''
# ZEC Webhook URL
discord_zec_hook = ''
# WAX Webhook URL
discord_wax_hook = ''

#ETH Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
eth_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
price_eth = requests.get(eth_price_url).json()
price_in_usd_eth = price_eth['USD']
#Post to Discord ETH:
price_eth = {
                "content": "ETH price in USD is currently at " +str(price_in_usd_eth)
                        }
requests.post(discord_eth_hook, data=price_eth)

#BTC Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
btc_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
price_btc = requests.get(btc_price_url).json()
price_in_usd_btc = price_btc['bpi']['USD']['rate']

#Post to Discord BTC:
price_btc = {
                "content": "BTC price is currently at $" + price_in_usd_btc + " USD"
                        }
requests.post(discord_btc_hook, data=price_btc)

#BCH Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
bch_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD'
price_bch = requests.get(bch_price_url).json()
price_in_usd_bch = price_bch['USD']
#Post to Discord BCH:
price_bch = {
                "content": "BCH price in USD is currently at " +str(price_in_usd_bch)
                        }
requests.post(discord_bch_hook, data=price_bch)

#LTC Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
ltc_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD'
price_ltc = requests.get(ltc_price_url).json()
price_in_usd_ltc = price_ltc['USD']
#Post to Discord ltc:
price_ltc = {
                "content": "LTC price in USD is currently at " +str(price_in_usd_ltc)
                        }
requests.post(discord_ltc_hook, data=price_ltc)

#XMR Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
xmr_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD'
price_xmr = requests.get(xmr_price_url).json()
price_in_usd_xmr = price_xmr['USD']
#Post to Discord xmr:
price_xmr = {
                "content": "XMR price in USD is currently at " +str(price_in_usd_xmr)
                        }
requests.post(discord_xmr_hook, data=price_xmr)
#XRP Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
xrp_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD'
price_xrp = requests.get(xrp_price_url).json()
price_in_usd_xrp = price_xrp['USD']
#Post to Discord xrp:
price_xrp = {
                "content": "XRP price in USD is currently at " +str(price_in_usd_xrp)
                        }
requests.post(discord_xrp_hook, data=price_xrp)
#XLM Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
xlm_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=USD'
price_xlm = requests.get(xlm_price_url).json()
price_in_usd_xlm = price_xlm['USD']
#Post to Discord xlm:
price_xlm = {
                "content": "XLM price in USD is currently at " +str(price_in_usd_xlm)
                        }
requests.post(discord_xlm_hook, data=price_xlm)
#DASH Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
dash_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD'
price_dash = requests.get(dash_price_url).json()
price_in_usd_dash = price_dash['USD']
#Post to Discord dash:
price_dash = {
                "content": "Dash price in USD is currently at " +str(price_in_usd_dash)
                        }
requests.post(discord_dash_hook, data=price_dash)
#ZEC Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
zec_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD'
price_zec = requests.get(zec_price_url).json()
price_in_usd_zec = price_zec['USD']
#Post to Discord zec:
price_zec = {
                "content": "ZEC price in USD is currently at " +str(price_in_usd_zec)
                        }
requests.post(discord_zec_hook, data=price_zec)

#WAX Pull -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
wax_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=WAX&tsyms=USD'
price_wax = requests.get(wax_price_url).json()
price_in_usd_wax = price_wax['USD']
#Post to Discord wax:
price_wax = {
                "content": "WAX price in USD is currently at " +str(price_in_usd_wax)
                        }
requests.post(discord_wax_hook, data=price_wax)
