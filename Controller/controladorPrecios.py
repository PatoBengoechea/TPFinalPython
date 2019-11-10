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
        for i in instrumentos:
            if i[0] > max['precio']:
                max['precio'] = i[0]
                max['simbolo'] = i[1]
        return max



    #Funcion clave de la perfomance de carga de precios
    def buscarInstrumentos(self):
        a = self.getInstrumentos()
        b = a['instruments']
        array = []
        for i in b:
            t = i['instrumentId']['symbol']
            if (t[:3] == self.simbolo) and (len(t) <= 12):
                a = self.armarTrades(t)
                b = a['trades']
                if(b != []):
                    n = (b[-1]['price'], t)
                    print(n)
                    array.append(n)

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

    def getListaSimbolos(self):
        instruments = pyRofex.get_all_instruments()
        lI = []
        for i in instruments['instruments']:
            lI.append(i['instrumentId']['symbol'])
        lI.sort()
        return lI
