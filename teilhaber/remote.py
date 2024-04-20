import requests

BASEROW_TOKEN = "cIGCSMBVwZHZcozqDwgtffKV9qGLU3Dk"

BASEROW_URL = "https://api.baserow.io/api/database/rows/table/286062/"


def get_data(filter=None):
    url = BASEROW_URL
    token = BASEROW_TOKEN

    url = url + '?'
    if filter is not None:
        url = url + '&search=' + filter
    url = url + '&user_field_names=true'

    resp = requests.get(
        url, headers={"Authorization": f"Token {token}"}
    )
    data = resp.json()

    if "results" not in data:
        raise RuntimeError(f"Could not get data from {url}")

    if data["next"]:
        return data["results"] + get_data(data["next"])
    return data["results"]

