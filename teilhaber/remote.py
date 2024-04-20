import requests

BASEROW_TOKEN = "cIGCSMBVwZHZcozqDwgtffKV9qGLU3Dk"

BASEROW_URL = "https://api.baserow.io/api/database/rows/table/286062/?user_field_names=true"

def get_data(url=BASEROW_URL):
    token = BASEROW_TOKEN
    resp = requests.get(
        url, headers={"Authorization": f"Token {token}"}
    )
    data = resp.json()

    if "results" not in data:
        raise RuntimeError(f"Could not get data from {url}")

    if data["next"]:
        return data["results"] + get_data(data["next"])
    return data["results"]

