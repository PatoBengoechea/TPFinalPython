import pyRofex
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from _datetime import datetime
import sys
from datetime import datetime
import pymongo
from pymongo import MongoClient
import json
from pymongo.errors import ConnectionFailure


class controladorPrecios:

    def __init__(self, simbolo):
        pyRofex.initialize(user='juanichacho2557',
               password='gpovgB1!',
               account='sampleAccount',
               environment=pyRofex.Environment.REMARKET)

        self.simbolo = simbolo[:3].upper()

    def definirMejor(self):
        max = {'precio': 1, 'simbolo':""}
        instrumentos = self.buscarInstrumentos()
        for t in instrumentos:
            if t['precio'] > max['precio']:
                max['precio'] = t['precio']
                max['simbolo'] = t['nombre']
        print('este es el precio maximo', max['precio'])
        return max['precio']



    def buscarInstrumentos(self):

        a = self.getInstrumentos()

        b = a['instruments']

        print(b)
        array = []
        p = {"precio":0, "nombre": ""}
        for i in b:
            t = i['instrumentId']['symbol']
            if (t[:3] == self.simbolo) and (len(t) <= 12):

                print(t)
                a = self.armarTrades(t)
                b = a['trades']
                if(b != []):
                    p['precio'] = b[-1]['price']
                    print(p['precio'])

                p['nombre'] = i['instrumentId']['symbol']

                array.append(p)
                print(array)

        return array

    def getInstrumentos(self):
        instruments = pyRofex.get_all_instruments()
        return instruments

    def armarTrades(self, inst):
        trades = pyRofex.get_trade_history(ticker= inst,
                                           start_date='2019-11-07',
                                           end_date='2019-11-07')

        return trades
