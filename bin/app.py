# -*- coding: utf-8 -*-

# Pour me lancer : python bin/app.py 8080

import web

# URL Handling : première partie est le regex, ensuite la classe que ça appelle
urls = (
	'/', 'Index'
)

# Les objets du framework
app = web.application(urls, globals())
render = web.template.render('templates/')

# Ma page Index, déclarée dans l'urls, avec ces méthodes http
class Index(object):
	def GET(self):
		greeting = "Hello there!"
		# La syntaxe magique : render.XXX, XXX le nom du fichier dans \templates
		return render.index(greeting = greeting)

# Code magique
if __name__ == "__main__":
	app.run()
