from misc.rm_rf import rm_rf
import os
from wb_crawler.main import fetch_posts
import json

REGAIN = True


def init():
    if REGAIN:
        rm_rf("./data")
        os.mkdir("./data")
        os.mkdir("./data/imgs")
        print("Starting to fetch posts...")
        posts = fetch_posts()
        print("Saving posts to file...")
        with open("./data/posts.json", "w", encoding="utf8") as f:
            json.dump(posts, f, ensure_ascii=False)
    else:
        print("Loading posts...")
        with open("./data/post.json") as f:
            posts = json.load(f)


if __name__ == "__main__":
    init()
