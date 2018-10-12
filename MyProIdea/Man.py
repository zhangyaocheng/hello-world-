#coding:utf-8

from People import People

class Man(People):
    def __init__(self,sex):
        self.sex = 'man'
        
    def say(self):
        print 'I am man'
    
    def getsex(self):
        return man;