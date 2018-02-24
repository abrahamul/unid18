import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_impresora, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_impresora) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_impresora, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_impresora) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_impresora, **k):

    @staticmethod
    def POST_EDIT(id_impresora, **k):
        
    '''

    def GET(self, id_impresora, **k):
        message = None # Error message
        id_impresora = config.check_secure_val(str(id_impresora)) # HMAC id_impresora validate
        result = config.model.get_impresoras(int(id_impresora)) # search for the id_impresora
        result.id_impresora = config.make_secure_val(str(result.id_impresora)) # apply HMAC for id_impresora
        return config.render.edit(result, message) # render impresoras edit.html

    def POST(self, id_impresora, **k):
        form = config.web.input()  # get form data
        form['id_impresora'] = config.check_secure_val(str(form['id_impresora'])) # HMAC id_impresora validate
        # edit user with new data
        result = config.model.edit_impresoras(
            form['id_impresora'],form['modelo'],form['existencias'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_impresora = config.check_secure_val(str(id_impresora)) # validate HMAC id_impresora
            result = config.model.get_impresoras(int(id_impresora)) # search for id_impresora data
            result.id_impresora = config.make_secure_val(str(result.id_impresora)) # apply HMAC to id_impresora
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/impresoras') # render impresoras index.html
