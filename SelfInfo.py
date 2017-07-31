import requests
def self_info():
    request_url = 'https://api.instagram.com/v1/users/self/?access_token=1837076894.6278dbd.697512baad2c400ead6b57fc206562b9'
    print 'SELF CREDENTIALS'
    print 'Request url: %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'UserId: %s' % (user_info['data']['id'])
            print 'No. of post: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'No Response from server'


self_info();