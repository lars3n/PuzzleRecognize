#coding:utf-8
from io import BytesIO
import requests
requests.packages.urllib3.disable_warnings()
from PIL import Image

import puzzle_tools

findGap = puzzle_tools.FindGap()


def get_img(url, headers):
    resp = requests.get(url, headers=headers, verify=False)
    content = resp.content
    img = Image.open(BytesIO(content))
    return img

def find_gap(img_url_a, img_url_b, headers):
    # print img_url_a, img_url_b
    img1 = get_img(img_url_a, headers)
    img2 = get_img(img_url_b, headers)

    img = puzzle_tools.RGB2BlackWhite(img1)
    arr = findGap.get_curve(img)
    img = puzzle_tools.RGB2BlackWhite(img2)
    x_start = findGap.find_match(img, arr)
    return x_start








