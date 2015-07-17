import socket
#from bot_config import *

network = 'irc.freenode.net'
channel = '#astronauci'
nick = 'R2G2'
chanMsg = "PRIVMSG %s :" %channel

alive = True

def ping():
    irc.send("PONG :Pong\n")

def joinChan(chan):
    irc.send("JOIN %s\n" %chan)

def sendMsg(msg):
    irc.send("PRIVMSG %s :%s\n" % channel, msg)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,6667))
irc.send("USER %s %s %s :salty bot\n" %(nick,nick,nick))
irc.send("NICK %s\n" %nick)

joinChan(channel)

if __name__ == "__main__":
    while alive:
        ircmsg = irc.recv(2048)
        ircmsg = ircmsg.strip('\n\r')
        print ircmsg

        if ":!status" in ircmsg:
            irc.send(chanMsg+"ALL SYSTEMS ONLINE\n")

        if ircmsg.find(":Hello "+nick) != -1:
            irc.send(chanMsg+"Hello!\n")

        if ircmsg.find("PING :") != -1:
            ping()
