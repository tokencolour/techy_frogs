import requests
from bs4 import BeautifulSoup



def get_state_reviews(state):
    if ' ' in state:
        state=state.split()
        state=state[0]+'-'+state[1]
    if 'jammu' in state:
        state='jammu-kashmir'
    
    state_url='http://www.holidayiq.com/states/'+state+'/'

    state_page=requests.get(state_url)
    state_ob=BeautifulSoup(state_page.content)

    
    review=[]
    title=[]
    review_person_name=[]
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
        
        try:
            if y.name=='li' and y.has_attr('class'):
                if y['class']=='reviewer-name':
                    person=y.span.string.encode('ascii','ignore')
                    if person not in review_person_name:
                        review_person_name.append(person)
        except:
            continue

    return(review_person_name,title,review)

def display_city_reviews(state):
    print('under construction')
##    isko banana padega


def get_city_list_with_details(state):
    if ' ' in state:
        state=state.split()
        state=state[0]+'-'+state[1]
    if 'jammu' in state:
        state='jammu-kashmir'
    
    state_url='http://www.holidayiq.com/states/'+state+'/'

    state_page=requests.get(state_url)
    state_ob=BeautifulSoup(state_page.content)

    q=list(state_ob.find_all(True))
    
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
    """ yamuna nagar haryana check karna hai, kuch gadbad hai"""
    i_d=1
    for x in city:
        city[x].append(x.split(',')[0])
        city[x].append('http://www.holidayiq.com/hotels/'+x.split(',')[0])
##        city[x].append(i_d)
        i_d+=1

    ##city[0]=city_page link
    ##city[1]=sight-seeing_page link
    ##city[2]=hotels_page link
    ##city[3]=city name
    return city


def get_sightseeing_list(state,city):
    city_details=get_city_list_with_details(state)
    for x in city_details:
        if city_details[-1]==city:
            try:
                ss_url=x[1]
                ss_page=requests.get(load_url)
                ss_ob=BeautifulSoup(place_page.content)
            except:
                print('Data not available for this choice')
                assert(False)
    q4=list(ss_ob.find_all(True))
    ss_list={}
    i_d=1
    for x in q4:
        if x.name=='h5':
            tmp=x.string.encode('ascii','ignore')
            ss_list[i_d]=[tmp,x.a['href']]
            i_d+=1
    ##ss_list[0]=sight-seeing destination name
    ##ss_list[1]=destination url

    return ss_list

def get_sightseeing_reviews(state,city,ss_id):
    ss_list=get_sightseeing_list(state,city)
    for x in ss_list:
        if x==ss_id:
            sight_page_url=x[-1]
            break
    
    sight_page=requests.get(sight_page_url)
    sight=BeautifulSoup(sight_page.content)

    q4=list(sight.find_all(True))
    details=[]
    c=0
    for x in q4:
        if x.name=='span':
            try:
                if 'travellers-recommended-for' in x['class']:
                    tmp=x.string.encode('ascii','ignore')
                    details.append(tmp)
                if 'travellers-recommendation-details' in x['class']:
                    tmp=x.string.encode('ascii','ignore')
                    details.append(tmp)
            except: continue
    title=[]
    review=[]
    p_name=[] ## abhi karna hai
    for x in q4:
        try:
            if x.name=='p':
                if x.has_attr('class') and x.has_attr('style'):
                    tmp=(x.a.string.encode('ascii','ignore'))
                    title=title.append(tmp)
            if x.name=='blockquote':
                tmp=(x.string.encode('ascii','ignore'))
                review.append(tmp)
        except: continue
        
    return(details,title,review)

def get_hotel_list(state,city):
    city_details=get_city_list_with_details(state)
    for x in city_details:
        if city_details[-1]==city:
            city_hotels_url=city_details[2]
    
    s2=requests.get(city_hotels_url)
    soup_city_hotel=BeautifulSoup(s2.content)

    q=list(soup_city_hotel.find_all(True))

    load_hotel_names=[]
    i=0
    for x in q:
        if(x.has_attr('class')):
            if 'hotel-list-hotel-name' in x['class']:
                load_hotel_names.append([])
                load_hotel_names[i].append(i)
                load_hotel_names[i].append(x.a['title'])
                load_hotel_names[i].append(x.a['href'])
                i+=1
            elif 'hotel-semlayout-title' in x['class']:
                load_hotel_names.append([])
                load_hotel_names[i].append(i)
                load_hotel_names[i].append(x.a.string.encode('ascii','ignore'))
                load_hotel_names[i].append(x.a['href'])
                i+=1
    return(load_hotel_names)

def get_hotel_reviews(state,city,hotel_id):
    hotel_list=get_hotel_list(state,city)
    c=0
    for x in hotel_list:
        if x[0]==hotel_id:
            c=1
            hotel_url=x[2]
    if c==0:
        return('id does noe exist')
    

    s3=requests.get(x[1])
    soup_hotel=BeautifulSoup(s3.content)
    q2=list(soup_hotel.find_all(True))

    title=[]
    review=[]
    p_name=[]  ##abhi karna hai
    for y in q2:
        if y.has_attr('class'):
            try:
                if 'reviews-tag-line-link' in y['class']:
                    tmp=('## '+y.a.string.encode('ascii','ignore'))
                    tiile.append(tmp)
            except: continue
            
            try:
                if y.name=='blockquote':
                    tmp=(y.string.encode('ascii','ignore'))
                    review.append(tmp)
            except: continue

    return(title,review,p_name)


    
    



