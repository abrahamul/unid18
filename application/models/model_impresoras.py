import web
import config

db = config.db


def get_all_impresoras():
    try:
        return db.select('impresoras')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_impresoras(id_impresora):
    try:
        return db.select('impresoras', where='id_impresora=$id_impresora', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_impresoras(id_impresora):
    try:
        return db.delete('impresoras', where='id_impresora=$id_impresora', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_impresoras(modelo,existencias,precio):
    try:
        return db.insert('impresoras',modelo=modelo,
existencias=existencias,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_impresoras(id_impresora,modelo,existencias,precio):
    try:
        return db.update('impresoras',id_impresora=id_impresora,
modelo=modelo,
existencias=existencias,
precio=precio,
                  where='id_impresora=$id_impresora',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
