
import os

class Config:

    NEWS_API_KEY_URL = 'https://newsapi.org/v2/sources?apiKey=dee975e3266146058769b7868b62736f'


    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    NEWS_API_SOURCES_URL='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=dee975e3266146058769b7868b62736f'



    
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
