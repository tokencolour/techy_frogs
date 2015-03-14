import requests
from bs4 import BeautifulSoup 

print('hmmm.... to hotel dekhna hai?? To dekho na mana kon kiya hai...')
s=requests.get('http://www.holidayiq.com/hotels')

soup_main_hotels=BeautifulSoup(s.content)

ob1=soup_main_hotels.div

li=ob1.find_all('li')

print('Input the city of your choice')
print('Please ensure the initial letter is in caps')
inp_city=raw_input()
print('Your choice is '+inp_city)
try:
        for x in li:
                t=list(x.stripped_strings)
                for y in t:
                        if y=='Hotels in '+inp_city:
                                re=x.a['href']
        if re:
                print('Hotel list is being loaded, this may not take long...')
except:
        print('Dekh bhai, popular jagah ka naam daal aur')
        print('kg k bachche k tarah spelling mistake mat kar')


s2=requests.get(re)
soup_city_hotel=BeautifulSoup(s2.content)

q=list(soup_city_hotel.find_all(True))

load_hotel_names=[]
i=0
for x in q:
    if(x.has_attr('class')):
        if 'hotel-list-hotel-name' in x['class']:
            load_hotel_names.append([])
            load_hotel_names[i].append(x.a['title'])
            load_hotel_names[i].append(x.a['href'])
            i+=1
        elif 'hotel-semlayout-title' in x['class']:
            load_hotel_names.append([])
            load_hotel_names[i].append(x.a.string.encode('ascii','ignore'))
            load_hotel_names[i].append(x.a['href'])
            i+=1

                                
j=1
print('Kitne hotel k reviews chahiye??')
tmp=int(raw_input())
if tmp>len(load_hotel_names): tmp=len(load_hotel_names)
if tmp>10:
        print('itna sara review dekhega to pgla jayega..')
        print('par ab bola hai to dekho')
for x in load_hotel_names[:tmp]:
        try:
                print
                print(str(j)+')')
                j+=1
##                print(x)
                print(x[0])
                print
                s3=requests.get(x[1])
                soup_hotel=BeautifulSoup(s3.content)
                q2=list(soup_hotel.find_all(True))
                for y in q2:
                        if y.has_attr('class'):
                                try:
                                    if 'reviews-tag-line-link' in y['class']:
                                        print
                                        print
                                        print('## '+y.a.string.encode('ascii','ignore'))
                                except: continue
                                
                                try:
                                    if y.name=='blockquote':
                                        print(y.string.encode('ascii','ignore'))
                                except: continue
                                
                                        
        except: continue
                                



