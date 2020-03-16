import string

import random
from .models import ShortURL


def shorten_url(short_url):
    url_content = string.ascii_letters + '0123456789'
    while True:
        short_url = ''.join(random.choice(url_content) for _ in range(6))
        print('*' * 80)
        print('iron man ShortURL.objects.filter(short_url=short_url).exists()',
              ShortURL.objects.filter(short_url=short_url).exists(), short_url)
        if not ShortURL.objects.filter(short_url=short_url).exists():
            return short_url
