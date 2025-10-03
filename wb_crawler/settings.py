SES_UID = 7959616376
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "client-version": "v2.47.121",
    "cookie": "SCF=ApxEZNQo3q7WU3nZof3eNh1g1p09VaOKAwAKfs4F9eq8sgBtO1hzbZASH84mRav_rSw1oCfkNXacwAHtnAvnNY8.; SINAGLOBAL=7043845792933.323.1740637730433; UOR=,,cloud.tencent.com; ULV=1747720793298:19:4:2:8236420129.427157.1747720793287:1747710573823; XSRF-TOKEN=LsZ-0i-VfJ0DGZGxzzvciquk; PC_TOKEN=0e04ea540e; SUB=_2A25F2knQDeRhGeFP41EX8S_KyT2IHXVmlsMYrDV8PUNbmtANLWuikW9NQREwKaHYGTzxCJurE5RJkN89TpliSsf5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhgDQO799mOYgqqleofqMfz5JpX5KzhUgL.FoMp1heceK2ceo22dJLoI0qLxKqLBKzL1h-LxKnL12qLBozLxKqL1KqLB-qLxKqL1h.L1KnLxK-L1hnLBK.LxKBLB.2L1--t; ALF=02_1761986176; WBPSESS=99w8i7WTwyOAgyB37DuG-cNnQkWah3jLMdBYb8NitvUf7qz9fbcrUoFf4pWp9JWhX4iljjkhumn0KHaicg4-9BQPrKTsjxjU5RDhxK4vPhjBGGhnEyvx6GekOv3BW2vowikz7esd26kbwunfjq6bzQ==",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": f"https://weibo.com/u/{SES_UID}",
    "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "server-version": "v2025.10.02.1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "LsZ-0i-VfJ0DGZGxzzvciquk",
}

BASE_URL = f"https://weibo.com/ajax/statuses/mymblog"
BASE_URL_PARAMS = {"uid": SES_UID, "page": 1, "feature": 0}
MAX_PAGES = 20
