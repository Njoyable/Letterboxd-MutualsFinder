import requests
from bs4 import BeautifulSoup

def get_parsed_page(url: str) -> None:
    
    headers = {
        "referer": "https://letterboxd.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

pagef = get_parsed_page("https://letterboxd.com/yourUserName/followers/")
dataf = pagef.find_all("img", attrs={'height': '40'})
page = get_parsed_page("https://letterboxd.com/yourUserName/following/")
data = page.find_all("img", attrs={'height': '40'})

i = 2

following = []
followers = []

for person in data:
    following.append(person['alt'])
    
for person in dataf:
    followers.append(person['alt'])

#look up the number of pages your follower/following list has on your profile
for i in range(2,7):
    page = get_parsed_page("https://letterboxd.com/yourUserName/following/page/" + str(i) + "/")
    data = page.find_all("img", attrs={'height': '40'})
    pagef = get_parsed_page("https://letterboxd.com/yourUserName/followers/page/" + str(i) + "/")
    dataf = pagef.find_all("img", attrs={'height': '40'})
   
    for person in data:
        following.append(person['alt'])
    for person in dataf:
        followers.append(person['alt'])
    
    i = i + 1

diff = list(set(following) - set(followers))
print(diff)
