#importing the libraries and function from from other file
import requests

#getting user detail such as username and userID
def getUserDetail():
    user_name= raw_input('Please enter your UserName \n')
    request_url = 'https://api.instagram.com/v1/users/search?q=' + user_name + '&access_token=1837076894.6278dbd.697512baad2c400ead6b57fc206562b9'
    print 'USERNAME AND USER ID OF INPUT USER'
    print 'Request url:%s' % (request_url)
    user_details = requests.get(request_url).json()
    if user_details['meta']['code'] == 200:
        if len(user_details['data']):
            print 'Username: %s' % (user_details['data'][0]['username'])
            print 'UserID: %s'   % (user_details['data'][0]['id'])
            return (user_details['data'][0]['id'])

        else:
            return None
    else:
        print 'No Response from server'


#getUserDetail();