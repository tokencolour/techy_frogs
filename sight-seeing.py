print('kon se state me ghumne ka hai ??')
print('Jammu & Kashmir jana hai to Jammu-Kashmir likhna')
state=raw_input()

if ' ' in state:
    state=state.split()
    state=state[0]+'-'+state[1]


import requests
from bs4 import BeautifulSoup

state_url='http://www.holidayiq.com/states/'+state+'/'

state_page=requests.get(state_url)
state_ob=BeautifulSoup(state_page.content)

print('state me jo log ghum chuke hai unke review chahiye to Ha likho')
print('aur agar seedhe sight-seeing menu pe jana hai to Na likho')
resp=raw_input()

review=[]
title=[]
if resp=='Ha':
    j=1
    q=list(state_ob.find_all(True))
    for y in q:
        if y.has_attr('class') and y.has_attr('style'):
            try:
                if 'h2' in y['class']:
                    if "color: #000000; margin-top: 0 !important;" in y['style']:
                        title.append('## '+y.a.string.encode('ascii','ignore'))
            except: continue
        try:
            if y.name=='div' and y.has_attr('class'):
                comment=y.blockquote.string.encode('ascii','ignore')
                if comment not in review:
                    review.append(comment)
        except: continue

    for i in range(len(review)):
        print title[i]
        print review[i]
        print

city={}
q2=list(state_ob.find_all(True))
for x in q2:
    try:
        if x.has_attr('class'):
            city_name=x.h5.string.encode('ascii','ignore')
            if city_name not in city:
                city[city_name]=[]
                city[city_name].append(x.h5.a['href'])

        if x.name=='a':
            tmp=x.string.encode('ascii','ignore')
            if 'sightseeing' in tmp:
                city[city_name].append(x['href'])
            
    except: continue

print
print
print('ye dekho sight-seeing ka menu, serial number enter karo')
print
i_d=1
for x in city:
    city[x].append(i_d)
    print(str(i_d)+')')
    i_d+=1
    print(x)
    print

print
print('karo karo jaldi karo')
response_serial=int(raw_input())

for x in city:
    if len(city[x])==3:
        if city[x][2]==response_serial:
            load_url= city[x][1]
            break
    else:
        print('Data not available for this choice')
        assert(False)
        
place_page=requests.get(load_url)
place=BeautifulSoup(place_page.content)
q4=list(place.find_all(True))

place_folder={}
i_d=1
for x in q4:
    if x.name=='h5':
        tmp=x.string.encode('ascii','ignore')
        place_folder[i_d]=[tmp,x.a['href']]
        i_d+=1

print('Now choose your sight-seeing destination')
print

for x in place_folder:
    print(str(x)+')')
    print(place_folder[x][0])
    print

response=int(raw_input())
load_url=place_folder[response][1]


##load_url2='http://www.holidayiq.com/Kufri-Shimla-Sightseeing-549-18633.html'
sight_page=requests.get(load_url)
sight=BeautifulSoup(sight_page.content)

q4=list(sight.find_all(True))

print('""""Chief Features"""')
print
c=0
for x in q4:
    if x.name=='span':
        try:
            if 'travellers-recommended-for' in x['class']:
                tmp=x.string.encode('ascii','ignore')
                print(tmp)
            if 'travellers-recommendation-details' in x['class']:
                
                tmp=x.string.encode('ascii','ignore')
                print('##'+tmp)
        except: continue

print
print('ab iska review dekhna hai to 1 dabao')
print
response=int(raw_input())
if response==1:
    for x in q4:
        try:
            if x.name=='p':
                if x.has_attr('class') and x.has_attr('style'):
                    print('###')
                    print(x.a.string.encode('ascii','ignore'))
                    print
            if x.name=='blockquote':
                print(x.string.encode('ascii','ignore'))
                print
                print
        except: continue

