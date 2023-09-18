import io
import cv2
import base64
import requests


from PIL import Image


# A1111 URL
#url = "http://ec2-13-57-213-9.us-west-1.compute.amazonaws.com:80"
url = "http://localhost:8080"

# Read Image in RGB order
img = cv2.imread('image/emptyroomtouse.jpg')

# Encode into PNG and send to ControlNet
retval, bytes = cv2.imencode('.png', img)
encoded_image = base64.b64encode(bytes).decode('utf-8')

# A1111 payload
# payload = {
#     "prompt": 'a handsome man',
#     "negative_prompt": "",
#     "batch_size": 1,
#     "steps": 20,
#     "cfg_scale": 7,
#     "alwayson_scripts": {
#         "controlnet": {
#             "args": [
#                 {
#                     "input_image": encoded_image,
#                     "module": "canny",
#                     "model": "control_v11p_sd15_canny [d14c016b]",
#                 }
#             ]
#         }
#     }
# }

payload = {
  "init_images": ["image/emptyroomtouse.jpg"],
  "resize_mode": 0,
  "denoising_strength": 0.75,
  "image_cfg_scale": 0,
  "mask": "string",
  "mask_blur": 0,
  "steps": 50,
  "cfg_scale": 7,
  "width": 512,
  "height": 512
}


img2img_payload = {
    "init_images": [encoded_image],
    "prompt": "a fully furnihsed bedroom",
    "negative_prompt": "amateur",
    "denoising_strength": 0.9,
    "width": 1000,
    "height": 768,
    "cfg_scale": 7,
    "sampler_name": "Euler a",
    "restore_faces": False,
    "steps": 30,
}




# Trigger Generation
response = requests.post(url=f'{url}/sdapi/v1/img2img', json=img2img_payload)

# Read results
r = response.json()
result = r['images'][0]
image = Image.open(io.BytesIO(base64.b64decode(result.split(",", 1)[0])))
image.save('image/output.png')