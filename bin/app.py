# -*- coding: utf-8 -*-

# Pour me lancer : python bin/app.py 8080

import web

# URL Handling : première partie est le regex, ensuite la classe que ça appelle
urls = (
	'/hello', 'Index'
)

# Les objets du framework
app = web.application(urls, globals())
render = web.template.render('templates/')

# Ma page Index, déclarée dans l'urls, avec ces méthodes http
class Index(object):
	def GET(self):
		
		#On récupère l'info via l'url : http://localhost:8080/hello?name=Frank
		form = web.input(name="Nobody") #On donne une valeur par défaut, sinon y'a erreur à l'appel
		greeting = "Hello, %s" % form.name
		
		# La syntaxe magique : render.XXX, XXX le nom du fichier dans \templates
		return render.index(greeting = greeting)

# Code magique
if __name__ == "__main__":
	app.run()
