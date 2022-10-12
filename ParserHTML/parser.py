import requests
import urllib.request
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.spbkit.edu.ru/index.php?option=com_timetable&Itemid=82'
url2 = 'http://service.spbcoit.ru:3080/replacements/view.html'

response = requests.get(url)
response2 = requests.get(url2)
soap = BeautifulSoup(response.text, "html.parser")
rasp = soap.find("div", id="gruppi-17")
soup = BeautifulSoup(response2.text, "html.parser")
raszam = soup.find("td", "127")

def ponedelnik():
    global den_nedeli
    den1 = 0
    den2 = 0
    den3 = 10
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == " ":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 1
    para = str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def vtornik():
    den1 = 12
    den2 = 1
    den3 = 20
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 2
    para = str(den_nedeli) + "\n" + "\n" + str(para)
    den1 = den1
    return para
def sreda():
    den1 = 20
    den2 = 2
    den3 = 30
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == " ":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 1
    para = str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def chetverg():
    den1 = 30
    den2 = 3
    den3 = 40
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == " ":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 1
    para = str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def pyatnica():
    den1 = 40
    den2 = 4
    den3 = 50
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == " ":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 1
    para = str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def sybbota():
    den1 = 50
    den2 = 5
    den3 = 60
    para = ""
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == " ":
            para = "Пары нет" + str(para) + "\n" + str(predmet)

        else:
            para = str(para) + "\n" + str(predmet)
        den1 = den1 + 1
    para = str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def zaminka():
    page = 'http://service.spbcoit.ru:3080/replacements/api/fetch-rep'
    html = urlopen(page).read()
    soup = BeautifulSoup(html, "html.parser")
    group = soup.find_all("tr")
    data = soup.find_all(class_="content")
    all = soup.find("table")
    al = all.find_all('tr')
    zampr = data[1].text.strip()
    newpr = data[3].text.strip()
    i = 0
    daaaa = 0
    otvet2 = ""
    otvet = ""
    while True:

        if "214" in group:
            i = 0
        else:
            daaaa:int = 0
            break

        i = i + 1
        if "214" == group[i].text.strip():
            gru = group[i].text.strip()
            i = i + 2
            grp = group[i].find_all('td')
            num1 = grp[0].text.strip()
            naz1 = grp[1].text.strip()
            deist1 = grp[2].text.strip()
            newpar1 = grp[3].text.strip()
            i = i + 2
            daaaa:int = 1
            otvet = al[0].text.strip() + "\n" + "⠀⠀⠀" + str(zampr) + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(newpr)
            if naz1 == "":
                naz1 = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
            num1_1 = int(num1) + 1
            pervii = num1 + "-" + str(num1_1) + "  " + naz1 + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + deist1 + "  " + newpar1
            otvet2 = pervii + "\n"
            grp1 = group[i].find_all('td')

            if len(grp1) > 1:
                num2 = grp1[0].text.strip()
                naz2 = grp1[1].text.strip()
                deist2 = grp1[2].text.strip()
                newpar2 = grp1[3].text.strip()
                num2_2 = int(num2) + 1
                if naz2 == "":
                    naz2 = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
                vtoroi = num2 + "-" + str(num2_2) + "  " + naz2 + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + deist2 + "  " + newpar2
                otvet2 = otvet2 + vtoroi + "\n"
            else:
                break
            i = i + 2
            grp2 = group[i].find_all('td')
            if len(grp2) > 1:
                num3 = grp2[0].text.strip()
                naz3 = grp2[1].text.strip()
                deist3 = grp2[2].text.strip()
                newpar3 = grp2[3].text.strip()
                num3_3 = int(num2) + 1
                if naz3 == "":
                    naz3 = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
                tretii = num3 + "-" + str(num3_3) + "  " + naz3 + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + deist3 + "  " + newpar3
                otvet2 = otvet2 + tretii
            else:
                break
            break

        else:
            est:int = 0

    if daaaa != 1:
        zameni = "Замен нет"
    else:
        zameni = otvet + "\n" + otvet2
    return zameni

def zvonki():
    zvonok = """1. 09:00 - 09:45 
2. 09:50 - 10:35
3. 11:05 - 11:50 
4. 11:55 - 12:40 
5. 13:10 - 13:55 
6. 14:00 - 14:45 
7. 14:55 - 15:40
8. 15:45 - 16:30
9. 16:35 - 17:20
10. 17:25 - 18:10"""
    return zvonok

