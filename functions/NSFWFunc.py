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
        # Check if the tags are older than 3 days. If so, get new tags
        if (
            json.load(open("data/realbooru_tags.json", "r"))["last_updated"]
            > (datetime.now() + timedelta(days=3)).timestamp()
        ):
            get_new_tags = True
    except:
        # Exception is raised when the file doesnt exist. So we need to get new tags
        get_new_tags = True
    if not get_new_tags:
        # If there is no need to get new tags, just return the tags from the file.
        return json.load(open("data/realbooru_tags.json", "r"))["tags"]
    print("Getting new tags, this will take a while.")
    tags = []
    for i in range(1, 1000):
        # Get the tags from the first 1000 pages(100,000 tags)(should be enough).
        try:
            url = f"https://realbooru.com/index.php?page=dapi&s=tag&q=index&limit=100&pid={i}"
            resp = requests.get(url)
            # parse the xml to dict
            parsed_resp = xmltodict.parse(resp.text)
            # append the tags to the list
            page_tags = [tag["@name"] for tag in parsed_resp["tags"]["tag"]]
            print(f"Got {len(page_tags)} tags from page {i}. Total tags: {len(tags)}")
            tags += page_tags
            if resp.status_code != 200:
                # If the status code is not 200, it means that there are no more pages.
                break
        except:
            # If there is an error(can occur when pages end too), just break the loop.
            break
    # Save the tags to the file
    json.dump(
        {"tags": tags, "last_updated": datetime.now().timestamp()},
        open("data/realbooru_tags.json", "w"),
        indent=4,
    )
    # Return the tags
    return tags
