import requests
import json

apikey = json.load(open("config.json"))["random_stuff_api_key"]


def get_random_joke(allow_nsfw=False):
    url = "https://v6.rsa-api.xyz/joke/random"
    if not allow_nsfw:
        url = f"https://v6.rsa-api.xyz/joke/random?exclude=sex,marriage,dirty,insults,rude,ugly,hate,political,alcohol,death,blonde,racist,black,gay,drug,fat"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    return (resp.json()["message"], resp.json()["tags"])


def get_all_joke_tags():
    url = "https://v6.rsa-api.xyz/joke/tags"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    return resp.json()


def get_tag_joke(tag: str):
    url = f"https://v6.rsa-api.xyz/joke/{tag}"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    return (resp.json()["message"], resp.json()["tags"])


def get_random_meme(allow_nsfw: bool = False):
    url = "https://v6.rsa-api.xyz/reddit/RandomMeme?searchType=hot"
    headers = {"Authorization": apikey}
    resp = requests.get(url, headers=headers)
    if allow_nsfw is False and resp.json()["NSFW"]:
        while resp.json()["NSFW"]:
            url = "https://v6.rsa-api.xyz/reddit/RandomMeme?searchType=hot"
            headers = {"Authourization": apikey}
            resp = requests.get(url, headers=headers)
    return resp.json()
