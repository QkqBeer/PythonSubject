__author__ = "那位先生Beer"
#用flask + redis 维护代理池,需要启动proxy_pool，这样会返回一些ip
import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
base_url = 'http://weixin.sogou.com/weixin?'
headers = {
'Cookie': 'SUID=FCAD737C1508990A000000005ACDDF26; SUV=001D53907C73ADFC5ACDDF2BD569E504; CXID=B8E3E1959C8D0EFDCAECB7E5220727AC; sw_uuid=2347722997; dt_ssuid=923719815; ssuid=8605118862; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ad=Ykllllllll2b0SWUlllllVm2ViylllllK4nH@yllll9llllllCxlw@@@@@@@@@@@; IPLOC=CN6101; SNUID=DF74E3ED9195E4BEB2ABA43A9145FBEB; ABTEST=0|1536220205|v1; weixinIndexVisited=1; sct=3; ld=Vyllllllll2z8NDulllllVmyilwlllllK4nH@lllllwlllllxklll5@@@@@@@@@@; JSESSIONID=aaaYD9bPNHj_X-nJCRBvw; ppinf=5|1536223719|1537433319|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozNjolRTklODIlQTMlRTQlQkQlOEQlRTUlODUlODglRTclOTQlOUZ8Y3J0OjEwOjE1MzYyMjM3MTl8cmVmbmljazozNjolRTklODIlQTMlRTQlQkQlOEQlRTUlODUlODglRTclOTQlOUZ8dXNlcmlkOjQ0Om85dDJsdU1NLTh1SjZxT1A3OFdmb2hUVGhlOWNAd2VpeGluLnNvaHUuY29tfA; pprdig=KhMQp6AXKH-DJJD-U9uUNr242YoskX-EUMZx_kyHXOy6geHvBn6_C_eAxxzZeKkPQRbxWWPsZwLb6IMnNLdarC1OQ7nIJSUq4pHi_G11boexb4Qdy3a_c34e9t3NDcO4phcX3Jx6-8ghR8dbH7OoSAr2b6cfuiuUtc7jc3wVc58; sgid=06-34868569-AVuQ6ecL8ia17kKUKqjraOgw; ppmdig=153622371900000070293691dad2fd3ecc2377324a8f4d32; ad=Ykllllllll2b0SWUlllllVm2ViylllllK4nH@yllll9llllllCxlw@@@@@@@@@@@; IPLOC=CN6101; SNUID=DF74E3ED9195E4BEB2ABA43A9145FBEB; ABTEST=0|1536220205|v1; weixinIndexVisited=1; sct=3; ld=Vyllllllll2z8NDulllllVmyilwlllllK4nH@lllllwlllllxklll5@@@@@@@@@@; JSESSIONID=aaaYD9bPNHj_X-nJCRBvw',
'Host': 'weixin.sogou.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
keyword = '风景'
proxy_url = 'http://localhost:5000/get'
proxy = None
max_count = 5
def get_proxy():
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None
def get_html(url,count = 1):
    print('url',url)
    print('count',count)
    global proxy
    if count >= max_count:
        print('Tried too many count')
        return None

    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects = False, headers = headers, proxies = proxies)
        else:
            response = requests.get(url, allow_redirects = False, headers = headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            #need new ip
            print('302')
            proxy = get_proxy()
            if proxy:
                count += 1
                print('Using Proxy', proxy)
                return get_html(url, count)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)

def get_index(keyword,page):
    data = {
        'query' : keyword,
        'type' : 2,
        'page' : page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def main():
    for page in range(1,101):
        html = get_index(keyword,page)
        print(html)
if __name__ == '__main__':
    main()