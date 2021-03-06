# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pyrebase
from fbconfig import *


class JsonWriterPipeline(object):

	def process_item(self, item, spider):
		firebase = pyrebase.initialize_app(config)
		# Get a reference to the database service
		db = firebase.database()
		
		# data to save
		# Pass the user's idToken to the push method
		for key, value in item.items():
			if key == 'name':
				name = value
				track = db.child("tracks").order_by_child('name').equal_to(str(name)).get()
				try: 
					print(track.val())
				except IndexError:
					print( "No duplicated, do it." )
					data = item
					results = db.child("tracks").push(data)
		return item