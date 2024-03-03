import requests
from bs4 import BeautifulSoup

url_following = "https://letterboxd.com/userName/following/"
url_followers = "https://letterboxd.com/userName/followers/"

def get_user_list(url):
    page = BeautifulSoup(requests.get(url).content, "lxml")
    return [img['alt'].lower() for img in page.find_all("img", attrs={'height': '40'})]

following_users = get_user_list(url_following)
follower_users = get_user_list(url_followers)

num_pages = 9
for i in range(2, num_pages):
    following_users += get_user_list(f"{url_following}page/{i}/")
    follower_users += get_user_list(f"{url_followers}page/{i}/")


follower_users = sorted(follower_users)
following_users = sorted(following_users)

diff = [name for name in following_users if name not in follower_users]
print(diff)