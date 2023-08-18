import requests
import re

word = input('请输入链接： ')
# url = 'https://www.douyin.com/video/6967296943450066214?previous_page=main_page'
# url = 'https://www.douyin.com/video/6967296943450066214?previous_page=main_page'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get(url=word, headers=headers)
html_data = re.findall('src(.*?)vr%3D%2', response.text)[1]
dem = requests.utils.unquote(html_data)
video_url = html_data.replace('%2F', '/').replace('%22%3A%22', 'https:').replace('%3F', '?').replace('%26', '&')
title = re.findall('<title data-react-helmet="true"> (.*?)</title>', response.text)[0]
video_content = requests.get(url=video_url).content
with open(title + '.mp4', mode='wb') as f:
    f.write(video_content)
    print(title, '下载完成')
