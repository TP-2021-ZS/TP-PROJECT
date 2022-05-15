import os

from DatasetUtils.DatasetUnifier import DatasetUnifier
from WebProcessingUtils.WebProcessor import WebProcessor

processor = WebProcessor('./exports/', 'xlsx')

articles = [
    'https://akcie.sk/tesla-predbehla-facebook-a-prekonala-trhovu-hodnotu-1-biliona/',
    'https://www.energie-portal.sk/Dokument/dalsia-biometanova-stanica-by-mohla-vyrast-v-presovskom-kraji-107603.aspx',
    'https://www.energie-portal.sk/Dokument/strategicky-projekt-nabral-polrocny-sklz-ssd-za-to-vini-aj-majitelov-pozemkov-107620.aspx',
    'https://finweb.hnonline.sk/ekonomika/14227130-zistenie-hn-slovenski-zlievari-expanduju-milionove-investicie-smeruju-do-srbska-aj-turecka',
    'https://www.enviroportal.sk/sk/eia/detail/donghee-slovakia-nova-linka-povrchovych-uprav',
    'https://www.enviroportal.sk/sk/eia/detail/zariadenie-na-zber-zhodnocovanie-pripravu-na-opatovne-pouzitie-odpadov-4',
    'https://www.enviroportal.sk/sk/eia/detail/bioplynova-stanica-kolarovo-zariadenie-na-zhodnocovanie-biologicky-roz',
    'https://www.priemyseldnes.sk/strojarstvo/vaillant-dostane-na-prevadzku-v-senici-investicny-stimul-18-milionov-eur-211103',
    'https://www.webnoviny.sk/vpriemysle/trnavsky-stellantis-ohlasil-investiciu-za-miliony-eur-novy-vyrobny-program-sa-spusti-od-roku-2023-video/',
    'https://www.aktuality.sk/clanok/7q6d6rp/velka-investicia-v-rimavskej-sobote-ktoru-nedavno-ohlasil-sulik-je-ohrozena/',
    'https://www.teraz.sk/spravy/eon-investuje-27-miliard-eur-do-pripr/592497-clanok.html',
    'https://www.trend.sk/spravy/budnik-j-t-investuju-kyberbezpecnosti-postavia-unikatne-bezpecnostne-centrum',
    'https://dennikn.sk/2623965/eset-predstavil-navrh-kampusu-od-svetoznamych-architektov-planuje-don-investovat-200-milionov-eur/'
]

files = []

'''
for article in articles:
    files.append(processor.process_url(article))
'''

for f in os.listdir('./exports'):
    name = f.split('.')
    if name[-1] == 'xlsx':
        files.append(f)

unifier = DatasetUnifier('./exports/')
unifier.unify(files)
