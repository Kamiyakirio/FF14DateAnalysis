import requests
import os
from urllib.parse import urlparse


def get_file_name(url: str):
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = path.split("/")[-1]
    return filename


# Note that save path must be a dir!
def download_image_from_original_url(
    ourl: str, referer: str, save_path: str, save_name: str
):
    # print("start!")
    image_header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "accept": "text/html,applicationxhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    if "thumb150" in ourl:
        ourl = ourl.replace("thumb150", "large")
    if referer:
        image_header["referer"] = referer
    response = requests.get(ourl, headers=image_header)
    if response.status_code == 200:
        content_size = int(response.headers.get("Content-Length", 0))
        if content_size > 0:
            filename = get_file_name(ourl)
            if save_name:
                _, ext = os.path.splitext(filename)
                filename = save_name + ext
            with open(os.path.join(save_path, filename), "wb") as f:
                for i in response.iter_content(128):
                    f.write(i)
    pass
