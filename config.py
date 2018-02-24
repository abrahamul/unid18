import web

db_host = 'h40lg7qyub2umdvb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'bbuamv3cc6r4z8ux'
db_user = 'b6p53xplkqk3b5mo'
db_pw = 't0ngykolnqv3mhuf'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )