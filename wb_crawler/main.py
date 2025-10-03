import requests
import time
from tqdm import tqdm
import html

from wb_crawler.concurrent_works import (
    fetch_full_content_for_posts,
    download_all_images_within_posts,
)
from wb_crawler.settings import *


def fetch_one_page(url, page, since_id):
    params = BASE_URL_PARAMS.copy()
    if page > 1 and since_id:
        params["since_id"] = since_id
    elif page > 1 and not since_id:
        print("Page is greater then 1 but no since_id provided!")
        return
    resp = requests.get(url, headers=HEADERS, params=params)
    if not (200 <= resp.status_code < 300):
        print("Request failed, status code: " + resp.status_code)
        return
    return resp.json()


def fetch_posts():
    posts = []
    since_id = ""
    pbar = tqdm(total=MAX_PAGES)

    for i in range(1, MAX_PAGES + 1):
        result = fetch_one_page(BASE_URL, i, since_id)
        since_id = result["data"]["since_id"]
        posts.extend(
            [
                _
                for _ in result["data"]["list"]
                if _["text_raw"] and "打捞" not in _["text_raw"]
            ]
        )
        pbar.update(1)
        time.sleep(1.2)

    pbar.close()

    posts = fetch_full_content_for_posts(posts)
    for i in posts:
        i["text_raw"] = html.unescape(i["text_raw"].replace("\u200b", "")).strip()
        i["full_content"] = html.unescape(
            i["full_content"].replace("\u200b", "")
        ).strip()

    download_all_images_within_posts(posts)

    return posts
