import models
import os

# Get X_DOMAINS
X_DOMAINS = os.getenv('X_DOMAINS', '').split(',')

CONFIG = {
    'DOMAIN': {
        'comments': models.comments.model
    },
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'SOFT_DELETE': True,
    'LAST_UPDATED': 'updated',
    'DATE_CREATED': 'created',
    'DELETED': 'disabled',
    'ETAG': 'etag',
    'LINKS': 'links',
    'ITEMS': 'data',
    'ISSUES': 'errors',
    'ERROR': 'dev_error',
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'X_HEADERS': ['If-Match', 'Content-Type', 'Authorization'],

    # Read from environment if possible
    'DEBUG': os.getenv('DEBUG', 'True') == 'True',
    'X_DOMAINS': '*' if X_DOMAINS == ['*'] else X_DOMAINS,
    'MONGO_URI': os.getenv('MONGO_URI', 'mongodb://localhost:27017/apitest'),
    'JWT_SECRET': os.getenv('JWT_SECRET', '')
}
