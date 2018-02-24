import web

db_host = 'localhost'
db_name = 'unid'
db_user = 'uniduser'
db_pw = 'unid.2018'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )