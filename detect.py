import urllib.request
import urllib.error


def url_open(url: str):
    return urllib.request.urlopen(urllib.request.Request(url, headers={
        'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/64.0.3282.186 Safari/537.36'),
    }))


def valid_response(url: str, f) -> bool:
    if url.endswith('.js'):
        return 'javascript' in f.headers['content-type']
    elif url.endswith('.css'):
        return 'text/css' in f.headers['content-type']
    elif url.endswith('.png'):
        return 'image/png' in f.headers['content-type']
    else:
        return True


def url_exists(url: str) -> bool:
    try:
        with url_open(url) as f:
            if valid_response(url, f):
                return True
    except urllib.error.HTTPError as exc:
        # print(exc)
        pass
    return False


def url_contains(url: str, text: bytes) -> bool:
    try:
        with url_open(url) as f:
            if valid_response(url, f):
                return text in f.read()
    except urllib.error.HTTPError as exc:
        # print(exc, url)
        pass
    return False


def detect(admin_static_url: str) -> str:
    admin_static_url = admin_static_url.rstrip('/') + '/'

    if url_exists(admin_static_url + 'css/autocomplete.css'):
        return '2.0'

    elif url_contains(admin_static_url + 'css/rtl.css',
                      b'.related-widget-wrapper'):
        return '1.11'

    elif url_exists(admin_static_url + 'js/change_form.js'):
        return '1.10'

    elif url_exists(admin_static_url + 'css/fonts.css'):
        return '1.9'
    
    elif url_exists(admin_static_url + 'js/related-widget-wrapper.js'):
        return '1.8'

    elif url_exists(admin_static_url + 'img/tooltag-arrowright.png'):
        return '1.7'

    elif url_contains(admin_static_url + 'css/changelists.css',
                      b'#changelist-form .results'):
        return '1.6'

    elif url_contains(admin_static_url + 'css/base.css',
                      b'.vBigIntegerField'):
        return '1.5'

    elif url_contains(admin_static_url + 'css/base.css',
                      b'img.help-tooltip'):
        return '1.4'

    elif url_contains(admin_static_url + 'css/base.css',
                      b'ul.messagelist li.warning'):
        return '1.3'

    elif url_exists(admin_static_url + 'media/js/collapse.js'):
        return '1.2'
