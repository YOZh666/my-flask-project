class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/flask_blog'
	SECRET_KEY = 'something very secret'

	#Flask Security
	SECURITY_PASSWORD_SALT = 'salt_for_bath)'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'