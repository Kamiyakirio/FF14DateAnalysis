import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from wb_crawler.settings import *
from wb_crawler.image_util import download_image_from_original_url
from tqdm import tqdm


def fetch_long_text(mblogid="Q7owU4jWw"):
    resp = requests.get(
        "https://weibo.com/ajax/statuses/longtext",
        params={"id": mblogid},
        headers=HEADERS,
    )
    if not (200 <= resp.status_code < 300):
        print("Error when fetching long text! " + mblogid)
        return mblogid, ""

    return mblogid, resp.json()


def fetch_full_content_for_posts(posts: list[dict]):
    print("Starting fetching full content for posts...")
    pbar = tqdm(total=len(posts))
    with ThreadPoolExecutor() as executor:
        workers = []
        for i in posts:
            mblogid = i["mblogid"]
            worker = executor.submit(fetch_long_text, mblogid)
            workers.append(worker)

        for i in as_completed(workers):
            mblogid, full_content = i.result()
            obj = next((_ for _ in posts if _["mblogid"] == mblogid))
            if full_content["data"] and full_content["data"]["longTextContent"]:
                obj["full_content"] = full_content["data"]["longTextContent"]
            else:
                obj["full_content"] = obj["text_raw"]
            pbar.update()

    pbar.close()
    return posts


def download_all_images_within_posts(posts: list[dict]):
    print("Starting downloading images...")

    with ThreadPoolExecutor() as executor:
        workers = []
        for i in posts:
            mblogid = i["mblogid"]
            cnt = 0
            if "pic_infos" in i.keys():
                for _, value in i["pic_infos"].items():
                    url = value["large"]["url"]
                    worker = executor.submit(
                        download_image_from_original_url,
                        url,
                        "https://weibo.com/",
                        "./data/imgs",
                        f"{mblogid}_{cnt}",
                    )
                    workers.append(worker)
                    cnt += 1

        pbar = tqdm(total=len(workers))

        for i in as_completed(workers):
            # mblogid, full_content = i.result()
            # obj = next((_ for _ in posts if _["mblogid"] == mblogid))
            # if full_content["data"] and full_content["data"]["longTextContent"]:
            #     obj["full_content"] = full_content["data"]["longTextContent"]
            # else:
            #     obj["full_content"] = obj["text_raw"]
            pbar.update()

        pbar.close()
    return posts
