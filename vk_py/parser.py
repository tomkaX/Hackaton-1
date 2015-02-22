
# -*- coding: utf-8 -*-

import vk
from peewee import *

from mysql.connector import connect

con = connect(user='root', password='123',
                              host='192.168.0.253',
                              database='phrase')

cursor = con.cursor()

vkapi = vk.API('4475564', 'login',  'pass')

#mysql_db = MySQLDatabase("phrase", host="192.168.0.253", user="root", passwd="123")

#class BaseModel(Model):
    """A base model that will use our MySQL database"""
#    class Meta:
#        database = mysql_db

#class Post(BaseModel):
#    text = CharField()
#    post_id = IntegerField()
#    date = DateField()


wall = vkapi.wall.get(domain="antimaydan")
#posts = []
for i in wall['items']:
    e=+1
    print e, i['text']

