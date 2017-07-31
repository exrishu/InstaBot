import requests
from UserRecentMedia import get_user_post

def comment_post():
        print ' Hi I am successfully executed'
        media_id = get_user_post()
        request_url = 'https://api.instagram.com/v1/media/%s/comments' % (media_id)
        payload = {"access_token": '1837076894.6278dbd.697512baad2c400ead6b57fc206562b9', "text": 'Superlike'}
        print 'POST request url : %s' % (request_url)
        hit_comment = requests.post(request_url, payload).json()
        if hit_comment['meta']['code'] == 200:
            print 'Successfully commented'
        else:
            print 'Try again!'

comment_post();