import requests
import json

def find_driving_distance(origin_place, destination_place):
##    print(origin_place, destination_place)
    
    yo=[]#contains origin,destination in sendable format
    for place in [origin_place, destination_place]:
        new_place=place.replace(',','')#removing commas
        newer=new_place.replace(' ','+')#replacing spaces with plus
        yo.append(newer)

        
    url='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+yo[0]+'&destinations='+yo[1]+'&key=AIzaSyB0Z5xwCsHNYnkA1YSYFePn_qNOQ-R27MM'

    for y in range(10):
        try:
            response=requests.get(url)
            break
        except:
            continue
    j_res= json.loads(response.content)
    result=[]
    try:
        for elem in j_res["rows"]:
            for each in elem["elements"]:
    ##            result.append(each["distance"]["text"])
    ##            result.append(each["duration"]["text"])
                tmp=each["duration"]["text"].split()
                if len(tmp)==2:
                    time=float(tmp[0])/60
                elif len(tmp)==4:
                    time=float(tmp[0])+(float(tmp[2])/60)
                else:
                    time=2
                
        return time
    except: return 1.3
        
###################################################


def get_prox_factor(travel_time):
    if travel_time<=0.5:
        prox_factor=0.85
    elif travel_time<=1:
        prox_factor=0.65
    elif travel_time<=1.5:
        prox_factor=0.5
    elif travel_time<=2:
        prox_factor=0.2
    elif travel_time<=2.5:
        prox_factor=0.1
    else:
        prox_factor=0
    print('travel time',travel_time)
    print(prox_factor)
    return prox_factor


###################################################



def recommend_package(city_rank,ss_list,time):
    city_points=(40-(2*(city_rank-1)))
    visited={}
    day_plans=[]
    dis=[]
    time_limit=7.5

    pk=[]
    pk_points=0
    pk_time=0
    while(len(visited)!=len(ss_list)):
        
        for x in ss_list:
            if x not in visited:
                ss_name=ss_list[x][0]
                ss_rank=x
                ss_points=(400-((ss_rank-1)*(ss_rank-1))) 
                
                if len(pk)==0:
                    pk.append(ss_name)
                    visited[ss_rank]=ss_name
                    ss_time=time[ss_rank-1]
                    base=ss_name
                    pk_points+=ss_points
                    pk_time+=ss_time
                    
                else:    
                    ss_time=time[ss_rank-1] 
                    travel_time=find_driving_distance(base,ss_name)*(1.2)
                    tot_time=ss_time+travel_time
                    
                    prox_factor=get_prox_factor(travel_time)

                    if pk_time+tot_time>time_limit:
                        continue
                    else:
                        pk.append(ss_name)
                        visited[ss_rank]=ss_name
                        pk_time+=tot_time
                        pk_points+=ss_points
                        tmp=0
                        for x in visited:
                            tmp+=(40-(2*(x-1)))
                        pk_points+=tmp*prox_factor
##                        print(visited)
            
        pk_points+=city_points
        tmp=[pk,pk_time,pk_points]
        day_plans.append(tmp)
        pk=[]
        pk_points=0
        pk_time=0



    return(day_plans)

###############################################

sample_ss_list={1:'Gandhi Maidan, Patna', 
                2:'Sanjay Gandhi Jaivik Udyan, Patna', 3:'Mahatma Gandhi Setu, Patna',
                4:'Mahavir Mandir, Patna', 5:'Mangal Talab, Patna'}
sample_time=[2.5,3,2,1,1]
sample_city_rank=1

          
##print(recommend_package(sample_city_rank, sample_ss_list, sample_time))
