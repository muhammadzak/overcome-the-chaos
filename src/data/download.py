import requests



def download_file(url, file):
    print(dir(file))
    response = requests.get(url)
    return response.content
