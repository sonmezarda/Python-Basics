import requests
from bs4 import BeautifulSoup

haftaNo = int(input("Hafta No: "))

macNo = int(input("Maç No: "))

if macNo < 10:
    macNo = f"0{macNo}"
else:
    macNo = str(macNo)

url = f"https://www.tff.org/Default.aspx?pageID=198&hafta={haftaNo}"

response = requests.get(url)

document = BeautifulSoup(response.content, 'html.parser')

mac = {
    'tarih': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_lblTarih').text,
    'saat': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_lblSaat').text,
    'icSaha': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_Label4').text,
    'deplasman': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_Label1').text,
    'icSahaSkor': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_Label5').text,
    'deplasmanSkor': document.find(id=f'ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari_ctl{macNo}_Label6').text
}

if int(mac['icSahaSkor'])>int(mac['deplasmanSkor']):
    kazanan = mac['icSaha']
else:
    kazanan = mac['deplasman']

print(f"""
------ {haftaNo}. HAFTA {macNo}. MAÇ ------
TARİH: {mac['tarih']}
SAAT: {mac['saat']}
SONUÇ: {mac['icSaha']} {mac['icSahaSkor']} - {mac['deplasmanSkor']} {mac['deplasman']}
KAZANAN TAKIM: {kazanan}
""")
