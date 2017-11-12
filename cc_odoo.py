# -*- coding: utf-8 -*-

import sys  
import xmlrpclib
import base64
from time import sleep
from pgmagick import Image
import os

from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import HexListToBinString
from smartcard.CardMonitoring import CardMonitor, CardObserver

from win10toast import ToastNotifier
import webbrowser

reload(sys)  
sys.setdefaultencoding('utf8')
toaster = ToastNotifier()
        
class ReadCard:
    def __init__(self, srv, db, user, pwd):
        # this will wait until card inserted in any reader
        self.channel = CardRequest(timeout=10, cardType=AnyCardType()).waitforcard().connection

        # using T=0 for compatibility (i.e., DigiID) and simplicity
        self.channel.connect()
        print "[+] Leitor:", self.channel.getReader()
        
        # Card Results
        self.card_results()
        
        # Odoo connection
        common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % (srv))
        self.api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % (srv))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'res.partner'

        toaster.show_toast(
            "CART\xc3O DO CIDAD\xc3O",
            "A ligar ao odoo!",
            icon_path="custom.ico",
            duration = 0,
            )

        # Insert in Odoo
        #a = self.get()
        id = self.set()
        print "/n>>> Registo inserido no odoo/n"
        
        url = 'http://odoo9-cartaocidadao-pedroposeiro.c9users.io/web#id=%s&view_type=form&model=res.partner' %(id)
        webbrowser.open_new(url)
        
    def execute(self, method, args, kwargs=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, args, kwargs or {})

    def get(self, ids=None):
        return self.execute('search_read', [ids or [], ['id', 'name']], )

    def set(self, id=None):
        if id:
            self.execute('write', [[id], {'name': self.nome}])
        elif self.addr == 1:
            print u'%s' %(self.pais)
            id = self.execute('create', [{  'name': u'%s %s' %(self.nome, self.apelido), 
                                            'vat': u'PT%s' %(self.nif), 
                                            'image': base64.b64encode(self.jpgdata),
                                            'street': u'%s %s' %(self.via, self.endereco),
                                            'street2': u'nº %s %s %s' %(self.porta, self.andar, self.lado),
                                            'city': u'%s' %(self.localidade),
                                            'zip': u'%s-%s %s' %(self.cod_postal_1,self.cod_postal_2,self.cod_postal_3),
                                        }])
        else:
            id = self.execute('create', [{  'name': u'%s %s' %(self.nome, self.apelido), 
                                            'vat': u'PT%s' %(self.nif), 
                                            'image': base64.b64encode(self.jpgdata)
                                        }])
        return id        

class PrintObserver(CardObserver):
        
    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            print("\n>>>> CARTAO INSERIDO <<<<\n")
            
            toaster.show_toast(
                "CART\xc3O DO CIDAD\xc3O",
                "A ler os dados!",
                 icon_path="custom.ico",
                 duration = 0,
                )
            srv, db = 'http://odoo9-cartaocidadao-pedroposeiro.c9users.io', 'test_db'
            user, pwd = 'demo', 'demo'
            ReadCard(srv, db, user, pwd)
            
        for card in removedcards:
            print("\n>>>> CARTAO REMOVIDO <<<<\n")
            toaster.show_toast(
                "CART\xc3O DO CIDAD\xc3O",
                "O cart\xe3o foi removido!",
                 icon_path="custom.ico",
                 duration = 0,
                )
  
if __name__ == '__main__':

    cardmonitor = CardMonitor()
    cardobserver = PrintObserver()
    cardmonitor.addObserver(cardobserver)
    
    toaster.show_toast(
            "CART\xc3O DO CIDAD\xc3O",
            "Pode inserir um cart\xe3o no leitor!",
            icon_path="custom.ico",
            duration = 0,
            )
            
    print "A espera do cartao..."
    sleep(-1)
    # don't forget to remove observer, or the
    # monitor will poll forever...
    cardmonitor.deleteObserver(cardobserver)   
    