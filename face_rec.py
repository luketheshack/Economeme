import requests
import json

# set to your own subscription key value
subscription_key = '83a292c2019141d98afdec9abcbedf26'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://alvin.cognitiveservices.azure.com/face/v1.0/detect'

image = input('Upload your profile picture: ')
image_url = image

# image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
faces = json.loads(json.dumps(response.json()))

for face in faces:
    print('This is a', face['faceAttributes']['age'], 'year old', face['faceAttributes']['gender'])