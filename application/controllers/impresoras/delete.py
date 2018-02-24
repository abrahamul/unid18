import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_impresora, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_impresora) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_impresora, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_impresora) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_impresora, **k):

    @staticmethod
    def POST_DELETE(id_impresora, **k):
    '''

    def GET(self, id_impresora, **k):
        message = None # Error message
        id_impresora = config.check_secure_val(str(id_impresora)) # HMAC id_impresora validate
        result = config.model.get_impresoras(int(id_impresora)) # search  id_impresora
        result.id_impresora = config.make_secure_val(str(result.id_impresora)) # apply HMAC for id_impresora
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_impresora, **k):
        form = config.web.input() # get form data
        form['id_impresora'] = config.check_secure_val(str(form['id_impresora'])) # HMAC id_impresora validate
        result = config.model.delete_impresoras(form['id_impresora']) # get impresoras data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_impresora = config.check_secure_val(str(id_impresora))  # HMAC user validate
            id_impresora = config.check_secure_val(str(id_impresora))  # HMAC user validate
            result = config.model.get_impresoras(int(id_impresora)) # get id_impresora data
            result.id_impresora = config.make_secure_val(str(result.id_impresora)) # apply HMAC to id_impresora
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/impresoras') # render impresoras delete.html 
