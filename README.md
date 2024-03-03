# Letterboxd

I've created this piece of code to find anyone you follow, who doesn't follow you back.
My motivation behind this was that there are quite a few people who, apparently, need to have a high follower count and a low following count. I am a hater and won't let it slide. GET OUT MY SWAMP!

You have to adjust the code in some parts. Look for "userName" in the code and replace it with... you know... your Username in Letterboxd. 
Secondly you have to adjust the num_pages, change the "9" to the amount of pages your follower/following list has. In my case, my follower/following ratio is exactly 1, so I have closely always the same page amount. If your ratio is not 1, you will need to do two seperate for-loops to iterate through your follower/following lists.

The script prints out the usernames of the people, where there is no mutual following.
