#from LikePost import like_post
import LikePost
#from CommentPost import comment_post
import CommentPost

#taking input to like or post the comment

user_input = raw_input('What do you want to do: \n 1:like the post \n 2.Comment on the post')
if (user_input == '1'):
    LikePost.like_post()
elif(user_input =='2'):
    CommentPost.comment_post()

#likeORcomment();

