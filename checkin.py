import requests

bot_token = "98964309:AAHMRuqeOe7lOySG2k3n0MwktQzXMLkn6ik"
chat_id = "86415403"
text = "action test"
requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
