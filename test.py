import time
import hmac
import hashlib
import base64
import urllib.parse
import requests,json

#加签
webhook='https://oapi.dingtalk.com/robot/send?access_token=daf14e7a71895c1d2d71fbb542656435508db44789a6e988c73a033ea4a0ca0e' #钉钉机器人webhook
timestamp = str(round(time.time() * 1000))
secret = 'SECc0d0c0abbda0949ef70dfdc08702c9f180c2c8ab442a59c778cc2b430d3cfade'  #钉钉机器人秘钥
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
# print(string_to_sign)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
webhook=webhook+'&timestamp='+timestamp+'&sign='+sign
print(webhook)
#定义数据类型
headers={'Content-Type':'application/json'}
data={"msgtype":"text","text":{"content":'测试： 忽略'},"isAtAll":True}
#发送post请求
res=requests.post(webhook,data=json.dumps(data),headers=headers)
print(res.text)