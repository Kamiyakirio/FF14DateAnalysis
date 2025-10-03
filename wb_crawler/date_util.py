from datetime import datetime


def parse_wb_time(time_str: str):
    dt = datetime.strptime(time_str, "%a %b %d %H:%M:%S %z %Y")
    return dt
