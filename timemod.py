import time
ticks=time.time()#ticks of time
print("Number of ticks since ",ticks)
localtime=time.localtime(time.time())#localtime
print("###local current time:",localtime)
localtimeasc=time.asctime(time.localtime(time.time()))
print("####local curent time ASC :",localtimeasc)#local time asc format
print("time.altsone:-",time.altzone)
