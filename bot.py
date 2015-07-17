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
        self.irc.connect((network, 6667))
        self.irc.send("")
        self.irc.send("USER %s %s %s :salty bot\n" % (self.nick, self.nick, self.nick))
        self.irc.send("NICK %s\n" % self.nick)
        self.irc.send("JOIN %s\n" % self.channel)

    def ping(self):
        self.irc.send("PONG :Pong\n")

    def sendMsg(self, msg):
        self.irc.send("PRIVMSG %s :%s\n" % channel, msg)

    def check_for_command(self, irc_msg, command, return_command):
        if irc_msg.find(command) != -1:
            return return_command()

    def main_loop(self):
        alive = True
        while alive:
            self.ircmsg = self.irc.recv(2048)
            self.ircmsg = self.ircmsg.strip('\n\r')

            if self.ircmsg.find("PING :") != -1:
                self.ping()

if __name__ == "__main__":
    r2g2 = HackBot(network, channel, nick)
    r2g2.main_loop()
