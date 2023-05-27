HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhiliaooa'
USERNAME = 'root'
PASSWORD = 'xjv123..'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# Mail
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "xjv1195275315@qq.com"
MAIL_PASSWORD = "pamwnlgjmiiebagd"
MAIL_DEFAULT_SENDER = "xjv1195275315@qq.com"
