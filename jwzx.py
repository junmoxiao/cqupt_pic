__author__ = 'junmoxiao'
import Queue
import threading
import urllib2

threads = 20

a = Queue.Queue()


for i in range(2010210001, 2010214910):
    a.put(i)

for i in range(2011210001, 2011214856):
    a.put(i)

for i in range(2012210001, 2012215214):
    a.put(i)

for i in range(2013210001, 2013214484):
    a.put(i)

for i in range(2014210001, 2014214571):
    a.put(i)

def connect_remote():
while not a.empty():
        num = a.get()
        url = 'http://jwzx.cqupt.edu.cn/showstuPic.php?xh=' + str(num)
        body = urllib2.urlopen(url)
        fd = open(str(num) + '.jpg', 'wb')
        fd.write(body.read())
        fd.close()
print 'saved %d' % num


for i in range(threads):
print 'Spawning thread:%s' % i
    t = threading.Thread(target=connect_remote)
    t.start()