import requests
import urllib

def downloadPost():
    request_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=1837076894.6278dbd.697512baad2c400ead6b57fc206562b9'
    print 'DOWNLOADING MOST RECENT POST OF OWNER'
    print 'Request url : %s' % (request_url)
    Self_media = requests.get(request_url).json()
    if Self_media['meta']['code'] == 200:
        if len(Self_media['data']):
            print 'Recent Post: %s' % Self_media['data'][0]['id']
            name = Self_media['data'][0]['id'] + '.jpeg'
            url = Self_media['data'][0]['images']['low_resolution']['url']
            print url
            urllib.urlretrieve(url,name)
            print 'Your file has been Successfully downloaded!!! Check ur folder'

downloadPost();

