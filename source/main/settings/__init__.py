from .common import *

if APP_ENV == 'dev':
    from .development import *
else:
    from .common import *
