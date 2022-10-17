# -*- coding: utf-8 -*-
"""1. Computer Vision.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18wQiS6PJBqDA6a4Lf7-9kZjVeTlyu8rp

Computer Vision Object Dectection

Computer Vision API를 사용해서 이미지속에 있는 사물을 인식하는 데모 입니다.

네트워크 통신을 위해서 requests 패키지를 import 합니다.
"""

import requests

"""이미지처리를 위해서 matplotlib.pyplot, Image, BytesIO 세 개의 패키지를 import 합니다.

matplotlib.pyplot는 import 할 때 시간이 조금 걸릴 수 있습니다.
"""

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

import json

"""Subscription Key와 접속에 필요한 URL을 설정합니다."""

subscription_key = 'abd13873a3da4274b75c878c3379ffd2'
vision_base_url = 'https://labuser3computervision.cognitiveservices.azure.com/vision/v2.0/'

analyze_url = vision_base_url + 'analyze' #이미지 분석을 하기위한 주소가 됨

"""분석에 사용되는 이미지를 확인 합니다."""

image_url = 'https://previews.123rf.com/images/erix2005/erix20051611/erix2005161101164/69515606-%EC%84%9C%EC%9A%B8-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-2016-%EB%85%84-3-%EC%9B%94-14-%EC%9D%BC-%EC%84%9C%EC%9A%B8-%EB%AA%85%EB%8F%99-%EA%B8%B8%EA%B1%B0%EB%A6%AC%EC%97%90%EC%84%9C-%EC%A7%80%EB%82%98%EA%B0%80%EB%8A%94-%ED%95%9C%EA%B5%AD%EC%9D%B8.jpg'

con = requests.get(image_url).content
byte = BytesIO(con)   #이미지를 풀어서 메모리에 올려줌
image = Image.open(byte)

image = Image.open(BytesIO(requests.get(image_url).content))

image

headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}   #줄을 꼭 맞춰야 하진 않지만
data = {'url' : image_url}   #실제 분석에 들어갈 이미지의 주소

response = requests.post(analyze_url, headers = headers, params = params, json = data)  #웹 호출 get or
result = response.json()

result

"""json값 뽑아내서 사용하는 방법"""

#{ }1개,[1,2,3...][1] [1,2.3...]여러개 중 [1]을 가져오겠다

image_caption = result['description']['captions'][0]['text']

image_caption

"""Object Detection """

objectDetection_url = vision_base_url + 'detect'

image_url = 'https://mblogthumb-phinf.pstatic.net/20151124_140/gatoblancokr_14483451465787xwfe_JPEG/2015-11-24_14%3B59%3B08_copy.jpg?type=w2'

image = Image.open(BytesIO(requests.get(image_url).content))

image

headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}   #줄을 꼭 맞춰야 하진 않지만
data = {'url' : image_url}   #실제 분석에 들어갈 이미지의 주소

response = requests.post(objectDetection_url, headers = headers, params = params, json = data)

result = response.json()

result

from PIL import Image, ImageDraw, ImageFont

draw = ImageDraw.Draw(image)    
#위에서 불러온 패키지 이름이 ImageDraw
#이미지를 그리기 모드로 여는 명령어

# boundingBox를 위한 함수
def DrawBox(detectData):
  objects = detectData['objects']

  for obj in objects:     #안에 있는 요소의 수 만큼 반복. 요소2개.
    #print(obj)               #요소 전체 출력

    rect = obj['rectangle']   #좌표 뽑아내기
    print(rect)

    x = rect['x']
    y = rect['y']
    w = rect['w']
    h = rect['h']

    draw.rectangle(((x,y),(x+w,y+h)),outline='red')    #사각형 그리기 ((첫번째 꼭지점), (두번째 꼭지점))

    objectName = obj['object']
    draw.text((x,y),objectName,fill='red')       #원하는 곳에 글자쓰기 가능

DrawBox(result)  #result가 파라메터로 들어옴

image

"""여기까지 object detection"""

