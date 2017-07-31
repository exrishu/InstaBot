import requests
from UserRecentMedia import get_user_post

def like_post():
    media_id = get_user_post()
    request_url = 'https://api.instagram.com/v1/media/%s/likes' % (media_id)
    payload = {"access_token":'1837076894.6278dbd.697512baad2c400ead6b57fc206562b9'}
    print 'POST request url : %s' % (request_url)
    hit_like = requests.post(request_url, payload).json()
    if hit_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

like_post();


