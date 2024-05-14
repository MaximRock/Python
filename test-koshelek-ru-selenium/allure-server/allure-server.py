import zipfile
import os
import json
import requests
from requests_toolbelt import MultipartEncoder

# path_file = './docker-results/'
#
# my_zip = zipfile.ZipFile(r'test_py.zip', 'w')
#
# for folder, subfolder, files in os.walk(path_file):
#     for file in files:
#         my_zip.write(os.path.join(folder, file),
#                      os.path.relpath(os.path.join(folder, file), path_file),
#                      compress_type=zipfile.ZIP_DEFLATED)
#
# my_zip.close()


# respons_get = requests.get(
#     url='http://192.168.1.100:8080/api/result',
#     headers={
#         'accept': '*/*'
#     }
# )

# url = "http://192.168.1.100:8080/api/result"
# headers = {
#         'accept': '*/*',
#         'Content-Type': 'multipart/form-data'
#         }
# multipart_data = MultipartEncoder(
#     fields={
#         "allureResults": "@@test_3.zip",
#         "type": "application/zip"
#     }
# )
#
# files = {
#     "allureResults": "@test_3.zip",
#     "type": "application/zip"
#         }
#
# files_json = json.dumps(files)
#
# respons_post = requests.post(url=url, headers=headers, files=files)
#
# # print(respons_get.json())
# print(respons_post.json())


# res = os.system("curl -X 'POST' \
#   'http://192.168.1.100:8080/api/result' \
#   -H 'accept: */*' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'allureResults=@test_3.zip;type=application/zip'")
#
# print(res)