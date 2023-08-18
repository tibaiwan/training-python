import requests, re, json, os

url = "https://cn.noxinfluencer.com/tiktok-channel-rank/top-100-all-all-sorted-by-followers-weekly"
# url = "https://v.douyin.com/iJQnrxLs/"
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'cookie' : ''
}

data = requests.get(url=url, headers=headers)
data.encoding = 'utf-8'
data = data.text
print(data)
data_en = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>',data)[0]
data_all = requests.utils.unquote(data_en)

# 解析视频url：正则
video_url = 'https:' + re.findall('"playAddr":\[{"src":".*?{"src":"(.*?)"}]',data_all)[0]
print(video_url)

# 正则
comments = re.findall("\"comments\":\[(.*?)],\"consumerTime\":",data_all)
print(comments)

# title
title = re.findall(']}},"desc":"(.*?)","authorUserId"',data_all)[0].replace(' ','')
print('-----------------------------------------------------------------------------------------')
print(title)

#保存
if not os.path.exists('./video'):
    os.mkdir('./video')
video_content = requests.get(url=video_url, headers=headers).content
# 由于直接将文案作为保存视频的文件名，所以在文案过长的时候会报错，把这两行注释然后打开最后两行的注释就行，一个简单的切片，也可以用自己的方法替换
with open(f'./video/{title}.mp4', 'wb+') as f:
    f.write(video_content)

# with open(f'./video/{title[0:10]}.mp4', 'wb+') as f:
#     f.write(video_content)
