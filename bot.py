import socket
#from bot_config import *

network = 'irc.freenode.net'
channel = '#astronauci'
nick = 'R2G2'

class HackBot(object):

    def __init__(self, network, channel, nick):
        self.network = network
        self.channel = channel
        self.nick = nick
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Estabilishing connection..."
        self.irc.connect((network, 6667))
        self.irc.send("")
        self.irc.send("USER %s %s %s :salty bot\n" % (self.nick, self.nick, self.nick))
        self.irc.send("NICK %s\n" % self.nick)
        self.irc.send("JOIN %s\n" % self.channel)
        print "Connected!"

    def ping(self):
        print "Got pinged, returning"
        self.irc.send("PONG :Pong\n")

    def sendMsg(self, msg):
        self.irc.send("PRIVMSG {} :{}\n".format(self.channel, msg))

    def check_for_command(self, irc_msg, command, return_command):
        if irc_msg.find(command) != -1:
            return_command()

    def main_loop(self):
        alive = True
        print "Running main loop"
        self.sendMsg("Established connection")
        self.sendMsg("Running main loop...")
        self.sendMsg("Hello world!")
        while alive:
            self.ircmsg = self.irc.recv(2048)
            self.ircmsg = self.ircmsg.strip('\n\r')
            self.check_for_command(self.ircmsg, "PING :", self.ping)

if __name__ == "__main__":
    r2g2 = HackBot(network, channel, nick)
    r2g2.main_loop()
