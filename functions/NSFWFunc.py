import json
import requests
import random
import xmltodict
from datetime import datetime, timedelta


def getRealBooru(tag: str) -> dict | None:
    """Gets a random image from realbooru api after searching with provided tag

    Args:
        tag (str): the tag to search for

    Returns:
        dict: Image url
    """
    url = f"https://realbooru.com/index.php?page=dapi&s=post&q=index&limit=100&tags={tag}&json=1"
    resp = requests.get(url)
    try:
        post = random.choice(resp.json())
    except:
        return None
    return post


def get_realbooru_tags() -> list[str]:
    """Gets all the tags from realbooru

    Returns:
        list: the tags
    """
    get_new_tags = False
    try:
        if (
            json.load(open("data/realbooru_tags.json", "r"))["last_updated"]
            > (datetime.now() + timedelta(days=3)).timestamp()
        ):
            get_new_tags = True
    except:
        get_new_tags = True
    if not get_new_tags:
        return json.load(open("data/realbooru_tags.json", "r"))["tags"]
    print("Getting new tags, this will take a while.")
    tags = []
    for i in range(1, 1000):
        try:
            url = f"https://realbooru.com/index.php?page=dapi&s=tag&q=index&limit=100&pid={i}"
            resp = requests.get(url)
            parsed_resp = xmltodict.parse(resp.text)
            page_tags = [tag["@name"] for tag in parsed_resp["tags"]["tag"]]
            print(f"Got {len(page_tags)} tags from page {i}. Total tags: {len(tags)}")
            tags += page_tags
            if resp.status_code != 200:
                break
        except:
            break
    json.dump(
        {"tags": tags, "last_updated": datetime.now().timestamp()},
        open("data/realbooru_tags.json", "w"),
        indent=4,
    )
    return tags
