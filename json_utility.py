#!/usr/bin/python3

import json
'''
This is a json utility I made for myself for my Bookstore project.
This basically formats the scraped json files with books data in a format
that can be imported in the site and put to SQL database.

'''

structure = {
	'title' : 'title',
	'title_alt' : 'title_alt',
	'language' : 'lan',
	'language_alt' : 'lan_alt',
	'publisher' : 'pub',
	'summary' : 'sum',
	'author' : 'auth',
	'author_alt' : 'auth_alt',
	'category' : 'cat',
	'category_alt' : 'cat_alt',
	'topics' : 'topics',
	'pages' : '123',
	'image' : 'image',
	'dlink' : 'dlink',
	'rlink' : 'rlink',
}
alts = {
	'title' : ['name'],
	'title_alt' : ['nameu'],
	'summary' : ['description'],
	'dlink' : ['link'],
	'image' : ['thumbl'],
}


def go(source, destination=''):
	if '.json' in source:
		source_name = source.split('.json')[0]
	else:
		source_name = source
	if destination == '' : destination = source_name + '_exported'
	try:
		print('loading %s' % source)
		f = open(source_name+'.json')
	except:
		print('Error loading file')
		return	
	
	js = json.load(f)
	f.close()
	final_json = []
	for j in js:
		
		# Title
		try:
			title = j['title']
		except:
			try:
				title = j['name']
			except:
				title = ''
		
		# Title_alt
		try:
			title_alt = j['title_alt']
		except:
			try:
				title_alt = j['nameu']
			except:
				title_alt = ''
		
		# Language
		try:
			language = j['language']
		except:
			language = ''
			
		# Language_alt
		try:
			language_alt = j['language']
		except:
			language_alt = ''
			
		# Publisher
		try:
			publisher = j['publisher']
		except:
			publisher = ''
				
		# Summary
		try:
			summary = j['summary']
		except:
			try:
				summary = j['description']
			except:
				summary = ''
				
		# Author
		try:
			author = j['author']
		except:
			author = ''
			
		# author_alt
		try:
			author_alt = j['author_alt']
		except:
			try:
				author_alt = j['authoru']
			except:
				author_alt = ''
			
		# category
		try:
			category = j['category']
		except:
			category = ''
			
		# category_alt
		try:
			category_alt = j['category_alt']
		except:
			try:
				category_alt = j['categoryu']
			except:
				category_alt = ''
		
		# topics
		try:
			topics = j['topics']
		except:
			try:
				topics = [j['topic']]
			except:
				topics = []
				
		# pages
		try:
			pages = j['pages']
		except:
			pages = ''
			
		# image
		try:
			image = j['image']
		except:
			try:
				image = j['thumbl']
			except:
				try:
					image = j['thumbnail']
				except:
					image = ''
		
		# dlink
		try:
			dlink = j['dlink']
		except:
			try:
				dlink = j['link']
			except:
				dlink = ''
				
		# rlink
		try:
			rlink = j['rlink']
		except:
			rlink = ''
			
		semifinal_json = {
			'title' : title,
			'title_alt' : title_alt,
			'language' : language,
			'language_alt' : language_alt,
			'publisher' : publisher,
			'summary' : summary,
			'author' : author,
			'author_alt' : author_alt,
			'category' : category,
			'category_alt' : category_alt,
			'topics' : topics,
			'pages' : pages,
			'image' : image,
			'dlink' : dlink,
			'rlink' : rlink,
		}
		final_json.append(semifinal_json)
	
	f = open(destination + '.json', 'w')
	json.dump(final_json, f)
	f.close()
	print('Done...')

if __name__ == '__main__':
	import sys
	s = sys.argv[1]
	try:
		d = sys.argv[2]
		go(s, d)
	except:
		go(s)
	
