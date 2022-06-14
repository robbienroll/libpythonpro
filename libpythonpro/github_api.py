import requests


def search_avatar(user):
    """
    Searches for the user avatar on GitHub

    :param user: str with the GitHub user's name
    :return: str with the avatar's weblink
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('robbienroll'))
