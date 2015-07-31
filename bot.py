import cgi
import logging
import socket
import http.server
import socketserver
import threading
import queue
#from bot_config import *

network = 'irc.freenode.net'
channel = '#astronauci'
nick = 'R2G2'

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        logging.warning('post started')
        logging.warning(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                        }
            )
        logging.warning('post data')
        for item in form.list:
            logging.warning(item)
        logging.warning("\n")
        http.server.SimpleHTTPRequestHandler.do_GET(self)

class HackBot(object):

    def __init__(self, network, channel, nick):
        self.network = network
        self.channel = channel
        self.nick = nick
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Estabilishing connection...")
        self.irc.connect((network, 6667))
        self.irc.send("")
        self.irc.send("USER %s %s %s :salty bot\n" % (self.nick, self.nick, self.nick))
        self.irc.send("NICK %s\n" % self.nick)
        self.irc.send("JOIN %s\n" % self.channel)
        print("Connected!")

    def ping(self):
        logging.warning("ping")
        self.irc.send("PONG :Pong\n")

    def sendMsg(self, msg):
        self.irc.send("PRIVMSG {} :{}\n".format(self.channel, msg))

    def check_for_command(self, irc_msg, command, return_command):
        if irc_msg.find(command) != -1:
            return_command()

    def start_server(self):
        self.port = 9000
        self.handler = ServerHandler
        try:
            self.httpd = socketserver.TCPServer(("", self.port), self.handler)
        except:
            print("Server fucked up")
        self.httpd.serve_forever()

    def main_loop(self):
        alive = True
        logging.warning("Running main loop")
        self.thread = threading.Thread(target=self.start_server)
        self.thread.daemon = True
        self.thread.start()
        self.sendMsg("Hello world!")
        while alive:
            self.ircmsg = self.irc.recv(2048)
            self.ircmsg = self.ircmsg.strip('\n\r')
            self.check_for_command(self.ircmsg, "PING :", self.ping)

if __name__ == "__main__":
    r2g2 = HackBot(network, channel, nick)
    r2g2.main_loop()
