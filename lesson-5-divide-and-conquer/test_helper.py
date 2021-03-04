'''Define some helper functions.'''

def today():
    '''Return today's date in YYYY-MM-DD.'''
    import datetime
    return datetime.date.today().isoformat()

def download_file(url):
    '''Download file from particular URL.'''
    from urllib.request import urlretrieve

    filename = url.split('/')[-1]
    urlretrieve(url, filename)
