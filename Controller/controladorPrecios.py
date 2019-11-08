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
        print(self.simbolo)
        self.definirMejor()

    def definirMejor(self):
        max = {'precio': 0, 'simbolo':""}
        instrumentos = self.buscarInstrumentos()
        for t in instrumentos:
            a = self.armarTrades(t)
            b = a['trades']
            if(b != []):
                if(b[-1]['price'] > max['precio']):
                    max['precio'] = b[-1]['price']
                    max['simbolo'] = t
        print('el maximo es ', max)
        return max


    def buscarInstrumentos(self):

        a = self.getInstrumentos()

        b = a['instruments']

        print(b)
        array = []
        for i in b:
            if i['instrumentId']['symbol'][:3] == self.simbolo:
                print(i['instrumentId']['symbol'])
                array.append(i['instrumentId']['symbol'])

        return array

    def getInstrumentos(self):
        instruments = pyRofex.get_all_instruments()
        return instruments

    def armarTrades(self, inst):
        trades = pyRofex.get_trade_history(ticker= inst,
                                           start_date='2019-11-07',
                                           end_date='2019-11-07')

        return trades
