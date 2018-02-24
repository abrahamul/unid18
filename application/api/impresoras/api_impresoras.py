import web
import config
import json


class Api_impresoras:
    def get(self, id_impresora):
        try:
            # http://0.0.0.0:8080/api_impresoras?user_hash=12345&action=get
            if id_impresora is None:
                result = config.model.get_all_impresoras()
                impresoras_json = []
                for row in result:
                    tmp = dict(row)
                    impresoras_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(impresoras_json)
            else:
                # http://0.0.0.0:8080/api_impresoras?user_hash=12345&action=get&id_impresora=1
                result = config.model.get_impresoras(int(id_impresora))
                impresoras_json = []
                impresoras_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(impresoras_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            impresoras_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(impresoras_json)

# http://0.0.0.0:8080/api_impresoras?user_hash=12345&action=put&id_impresora=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, modelo,existencias,precio):
        try:
            config.model.insert_impresoras(modelo,existencias,precio)
            impresoras_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(impresoras_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_impresoras?user_hash=12345&action=delete&id_impresora=1
    def delete(self, id_impresora):
        try:
            config.model.delete_impresoras(id_impresora)
            impresoras_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(impresoras_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_impresoras?user_hash=12345&action=update&id_impresora=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_impresora, modelo,existencias,precio):
        try:
            config.model.edit_impresoras(id_impresora,modelo,existencias,precio)
            impresoras_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(impresoras_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            impresoras_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(impresoras_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_impresora=None,
            modelo=None,
            existencias=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_impresora=user_data.id_impresora
            modelo=user_data.modelo
            existencias=user_data.existencias
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_impresora)
                elif action == 'put':
                    return self.put(modelo,existencias,precio)
                elif action == 'delete':
                    return self.delete(id_impresora)
                elif action == 'update':
                    return self.update(id_impresora, modelo,existencias,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
