# Letterboxd

I've created this piece of code to find anyone you follow, who doesn't follow you back.
My motivation behind this was that there are quite a few people who, apparently, need to have a high follower count and a low following count. Maybe i care too much about it, but i just can't stand the motivation behind this behavior.

You have to adjust the code in some parts. Look for "yourUserName" in the code and replace it with... you know... your Username in Letterboxd.
Secondly you have to adjust the for-loop, change the "7" to the amount of pages your follower/following list has. In my case, my follower/following ratio is exactly 1, so I have closely always the same page amount. If your ratio is not 1, you will need to do two seperate for-loops to iterate through your follower/following lists.

It will print out the usernames of the people, where there is no mutual following and the number of the page you can find the person on. I always hunt for only one person, who unfollowed me, so the number is not accurate for multiple people. 
