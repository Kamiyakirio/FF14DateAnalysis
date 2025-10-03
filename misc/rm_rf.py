import os


def rm_rf(path):
    if not os.path.exists(path):
        return

    if os.path.isfile(path):
        os.remove(path)
    else:
        for item in os.listdir(path):
            rm_rf(os.path.join(path, item))
        os.rmdir(path)
