import requests
import json

# Get the api key from the config file
apikey = json.load(open("config.json"))["random_stuff_api_key"]


def get_random_joke(allow_nsfw=False) -> tuple[str, list[str]]:
    """Gets a random joke from the api

    Args:
        allow_nsfw (bool, optional): If jokes can be offensive/NSFW. Defaults to False.

    Returns:
        tuple: The joke and the tags
    """
    url = "https://v6.rsa-api.xyz/joke/random"
    if not allow_nsfw:
        # If NSFW jokes are not allowed, then we need to get a joke that is not NSFW
        url = f"https://v6.rsa-api.xyz/joke/random?exclude=sex,marriage,dirty,insults,rude,ugly,hate,political,alcohol,death,blonde,racist,black,gay,drug,fat"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    # return a tuple with the joke and the tags
    return (resp.json()["message"], resp.json()["tags"])


def get_all_joke_tags() -> list[str]:
    """Get all the tags allowed.

    Returns:
        list: A list of all the tags
    """
    url = "https://v6.rsa-api.xyz/joke/tags"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    # return a list of all the tags
    return resp.json()


def get_tag_joke(tag: str) -> tuple[str, list[str]]:
    """Gets a joke with a specific tag

    Args:
        tag (str): The tag to get the joke from

    Returns:
        tuple[str, list]: The joke and the tags
    """
    # Get a joke with a specific tag
    url = f"https://v6.rsa-api.xyz/joke/{tag}"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    # return a tuple with the joke and the tags
    return (resp.json()["message"], resp.json()["tags"])


def get_random_meme(allow_nsfw: bool = False) -> dict[str, str | list[str] | int]:
    """Gets a random meme from the api

    Args:
        allow_nsfw (bool, optional): Allow NSFW memes. Defaults to False.

    Returns:
        dict[str, str | list[str] | int]: The post info
    """
    # Get a random meme
    url = "https://v6.rsa-api.xyz/reddit/RandomMeme?searchType=hot"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    if allow_nsfw is False and resp.json()["NSFW"]:
        # If NSFW memes are not allowed, then we need to get a meme that is not NSFW
        while resp.json()["NSFW"]:
            url = "https://v6.rsa-api.xyz/reddit/RandomMeme?searchType=hot"
            headers = {"Authourization": apikey}
            resp = requests.get(url, headers=headers)
    # return the post info
    return resp.json()
