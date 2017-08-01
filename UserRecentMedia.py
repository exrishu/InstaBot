#importing the libraries and function from from other file
import requests
from UserDetails import getUserDetail

#getting recently post posted by the user
def get_user_post():
  print ('Enter usename to get most recent media by user')
  user_id = getUserDetail()
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = 'https://api.instagram.com/v1/users/%s/media/recent/?access_token=1837076894.6278dbd.697512baad2c400ead6b57fc206562b9' % (user_id)
  print 'MOST RECENT MEDIA PUBLISHED BY USER'
  print 'Request url:%s' % (request_url)
  user_media = requests.get(request_url).json()
  if user_media['meta']['code'] == 200:
      if len(user_media['data']):
          print 'Recent MediaID: %s' % (user_media['data'][0]['id'])
          return (user_media['data'][0]['id'])
      else:
          print "There is no recent post!"
  else:
      print "No response from server!"
  return None

#get_user_post();
