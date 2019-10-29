import oauth2 as oauth


def Request(url, key, secret, http_method='GET', post_body='', http_headers=''):
    consumer = oauth.Consumer(key='<your consumer key>', secret='<your consumer secret>')
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)

    request = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers)

    return request
