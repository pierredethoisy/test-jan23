leCurseur       = uneConnexionBDD.cursor()
unAuteur        = "'Zola'"
leCurseur.execute(""" SELECT title, description FROM books WHERE author = %s """ % (unAuteur,))
pprint.pprint(leCurseur.fetchall())
leCurseur.query("update books set title='assommoir' where author='Zola'")
uneConnexionBDD.commit()
var abc = "test-pierre-payload-webhook"
