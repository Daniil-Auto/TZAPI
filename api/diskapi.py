import requests

url_disk_api = 'https://cloud-api.yandex.net/v1/disk/resources'
token = 'AQAAAABjN35fAAhDJ5jpEb90z0jvrm2FrbG1XHM'
headersd = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

def create_folder(path):
    response = requests.put(f'{url_disk_api}?path={path}', headers=headersd)
    assert response.status_code == 201

def get_info_folder(path):
    response = requests.get(f'{url_disk_api}?path={path}&fields=name', headers=headersd)
    assert response.status_code == 200
    body = '{"name":"SimbirSoftFolder"}'
    assert response.text == body

def delete_folder(path):
   response = requests.delete(f'{url_disk_api}?path={path}', headers=headersd)
   assert response.status_code == 204