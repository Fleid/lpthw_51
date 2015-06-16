# -*- coding: utf-8 -*-

# Pour me lancer : python bin/app2.py 8081

import web

# URL Handling : première partie est le regex, ensuite la classe que ça appelle
urls = (
	'/', 'Index',
	'/add', 'Add'
)

# Les objets du framework
app = web.application(urls, globals())
render = web.template.render('templates/')

# Connexion à la DB
db = web.database(dbn='postgres', user='Fleid', pw='Z2rywax', db='Fleid')

class Index(object):
	def GET(self):
	    todos = db.select('todo')
	    return render.foo(todos)

class Add(object):
    def POST(self):
		#Méthode magique, voir le html dans le template foo
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

if __name__ == "__main__":
	app.run()