#importing the libraries
import requests

#Media Id of the recent post by owner
def get_own_post():
    request_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=1837076894.6278dbd.697512baad2c400ead6b57fc206562b9'
    print ' MOST RECENT MEDIA PUBLISHED BY OWNER'
    print 'Request url:%s' % (request_url)
    Self_media = requests.get(request_url).json()
    if Self_media['meta']['code'] == 200:
        if len(Self_media['data']):
            print 'Recent PostId: %s' % Self_media['data'][0]['id']
        else:
            print 'Post does not exist!'
    else:
        print 'No Response from server'
    return None


get_own_post();