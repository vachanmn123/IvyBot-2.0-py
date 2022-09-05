import requests


async def get_truth(rating: str) -> dict[str, str]:
    """Get a truth question from the API

    Args:
        rating (str): rating for question (r, pg13, pg)

    Returns:
        str: The truth question
    """
    res = requests.get(f"https://api.truthordarebot.xyz/v1/truth?rating={rating}")
    return res.json()


async def get_dare(rating: str) -> dict[str, str]:
    """Get a dare from the API

    Args:
        rating (str): rating for question (r, pg13, pg)

    Returns:
        str: The dare
    """
    res = requests.get(f"https://api.truthordarebot.xyz/v1/dare?rating={rating}")
    return res.json()


async def get_neverHaveIEver(rating: str) -> dict[str, str]:
    """Get a never have I ever from the API

    Args:
        rating (str): rating for question (r, pg13, pg)

    Returns:
        str: The never have I ever
    """
    res = requests.get(f"https://api.truthordarebot.xyz/v1/nhie?rating={rating}")
    return res.json()


async def get_paranoia(rating: str) -> dict[str, str]:
    """Get a paranoia question from the API

    Args:
        rating (str): rating for question (r, pg13, pg)

    Returns:
        str: The paranoia question
    """
    res = requests.get(f"https://api.truthordarebot.xyz/v1/paranoia?rating={rating}")
    return res.json()


async def get_wouldYouRather(rating: str) -> dict[str, str]:
    """Get a would you rather question from the API

    Args:
        rating (str): rating for question (r, pg13, pg)

    Returns:
        str: The would you rather question
    """
    res = requests.get(f"https://api.truthordarebot.xyz/v1/wyr?rating={rating}")
    return res.json()
