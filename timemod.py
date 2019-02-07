import time
ticks=time.time()#ticks of time
print("Number of ticks since ",ticks)
localtime=time.localtime(time.time())#localtime
print("###local current time:",localtime)
localtimeasc=time.asctime(time.localtime(time.time()))
print("####local curent time ASC :",localtimeasc)#local time asc format
print("time.altsone:-",time.altzone)
print("time asctime(t):",time.asctime(time.localtime()))
def procedure():
	time.sleep(2.5)
t0=time.clock()
procedure()
print(time.clock())
t0=time.time()
procedure()
print( time.time()-t0)
print("time.ctime():%s"% time.ctime())
print ("time.gmtime() :",time.gmtime())
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print("time.mktime(t) : %f" %  secs)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))struct_time = time.strptime("30 Nov 00", "%d %b %y")
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("returned tuple: %s",struct_time)