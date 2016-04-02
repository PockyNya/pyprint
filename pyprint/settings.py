#coding: utf-8


# website settings
username = 'Pocky Nya'
email = 'pocky@loli.club'
title = u'Pocky Nya - Pocky 盒子'
motto = u'我是好吃的 Pocky 喵~'
disqus_shortname = 'pockynya'

# themes name
theme = 'default'

# development
debug = True


analytics_code = '''
'''

post_of_page = 3


try:
    from localsettings import connect_str, cookie_secret
except ImportError:
    raise Exception('Please add connect_str and cookie_secret in localsettings.py')


try:
    module = __import__('themes.%s.config' % theme, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)
except ImportError:
    pass

