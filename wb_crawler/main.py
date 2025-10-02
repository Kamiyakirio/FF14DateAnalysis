import requests
SES_UID = 7959616376
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}
#  https://weibo.com/ajax/statuses/mymblog?uid=7959616376&page=1&feature=0

BASE_URL = "https://weibo.com/ajax/statuses/mymblog?uid=7959616376&page=1&feature=0"

def fetch_posts():
    cookie_from_file = None
    with open("cookie.txt","r") as f:
        cookie_from_file=f.read()
    requests.get(BASE_URL,)
    pass

def main():
    
    pass