# -*- coding: utf-8 -*-

# Pour me lancer : python bin/app.py 8080

import web

# URL Handling : première partie est le regex, ensuite la classe que ça appelle
urls = (
	'/hello', 'Index'
)

# Les objets du framework
app = web.application(urls, globals())
# Toutes les pages seront wrappées dans layout.html
render = web.template.render('templates/',base="layout")

# Ma page Index, déclarée dans l'urls, avec ces méthodes http
class Index(object):
	
	def GET(self):
		return render.hello_form()
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

# Code magique
if __name__ == "__main__":
	app.run()
