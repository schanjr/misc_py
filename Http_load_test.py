# -*- coding: utf-8 -*-
import requests
import json
import time


get_all_entitlement='https://enterprise-api-dev.autodesk.com/service/entitlements/v1/user/'
oxygen_id='RFTAKYFJ8L5M'
apikey='apikey=1vKOxAnJL3Ns0mm2M5QqHYnY7SJYoLYr'
includeExpired='includeExpired=true'
counter=0
ent_list=[]
result_list=[]
file=open('get_all_entitlement.log','w+')
file.write('Oxygen  Pelican  Legacy  Seconds'+'\n')
file.write('################################'+'\n')
for i in range(100):
    url="%s%s?%s&%s" % (get_all_entitlement, oxygen_id, apikey,includeExpired)
    start=time.clock()
    r=requests.get(url)
    js_load=r.json()
    stop=time.clock()
    oxygen=int(js_load["endpointStatus"]["oxygen"]["status"])
    pelican=int(js_load["endpointStatus"]["pelican"]["status"])
    legacy=int(js_load["endpointStatus"]["legacy"]["status"])
    result=oxygen,pelican,legacy,(stop-start)
    result_list.append(result)
    file.write(str(result)+"\n") 
    ent_list.append(stop-start)
sort_list=sorted(ent_list)
file.close()
##Computation for basic average
min=sort_list[0]
max=sort_list[len(sort_list)-1]
average=reduce(lambda x,y: x + y, sort_list)/len(sort_list)
print "Minimum %f, Maximum %f, Average %f" % (min,max,average)

print result_list

##Function for detecting any error codes were received from any backend
oxygen_err=0
pelican_err=0
legacy_err=0
for i in result_list:
    for j, x in enumerate(i[0:3]):
        if x!=200:
            if j==0:
                oxygen_err+=1
            if j==1:
                pelican_err+=1
            if j==2:
                legacy_err+=1
            print "Oxygen Errors: %d, Pelican Errors: %d, Legacy Errors: %d" %(oxygen_err,pelican_err,legacy_err)
        
