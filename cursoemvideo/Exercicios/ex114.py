import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site Pudim não está acessível no momento!\033[3m')
else:
    print('O site Pudim está acessível!')
    print(site.read())