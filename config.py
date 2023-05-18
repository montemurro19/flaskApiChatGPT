class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}