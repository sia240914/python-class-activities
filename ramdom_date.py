import random
import time
def getrandomdate(startdate,enddate):
    print("start date : ",startdate, " end date :" , enddate)
    randomgenerator=random.random()
    dateformat="%Y%m%d"
    
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate

print(getrandomdate("19990901","20260601"))

    