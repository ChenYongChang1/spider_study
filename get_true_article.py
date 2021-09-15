import requests
import time
import random
import json
import os
import threading

file_path = ['算法', '微信小程序', 'CSS', 'React.js', 'LeetCode', 'TypeScript', 'Element',
             'HTML', '面试', 'Webpack', 'Flutter', 'Node.js', 'Vue.js', 'JavaScript', '前端']

base_url = 'https://api.juejin.cn/content_api/v1/article/detail?uuid='


def make_dir(path):
    exist = os.path.exists(path)
    if not exist:
        os.mkdir(path)
    else:
        print('“{}”目录已存在'.format(path))


def get_requests_marked(article_id):
    url = base_url.replace('{id}', article_id)
    user_agent = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    ]
    user_choose = random.choice(user_agent)
    headers = {
        'User-Agent': user_choose,
        'Content-Type': 'application/json',
        'cookie': 'MONITOR_WEB_ID=43f3d2ad-8023-4439-97a7-c525b4a7e901; _ga=GA1.2.1127104855.1631701093; _gid=GA1.2.2077682329.1631701093',
        'origin': 'https://juejin.cn',
        'referer': 'https://juejin.cn/'
        # 'Sec-Fetch-Mode': 'no-cors'
    }
    data = {"article_id": article_id}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    # r.encoding = 'utf-8'
    # [title, desc, content] = r.json()
    data = r.json()
    info = data.get('data').get('article_info')
    md = info.get('mark_content') or info.get('content')
    # print(md)
    return md


def get_article_list(path):
    with open(path, 'r+', encoding='utf-8') as f:
        arr = json.load(f)
    return arr


def get(base_path, name):
    arr = get_article_list('./database/_{}.py'.format(name))
    path = base_path + name
    make_dir(path)
    for i in arr:
        print(i['id'])
        try:
            md = get_requests_marked(i['id'])
        except Exception as e:
            time.sleep(1800 + 1800 * random.random())
            get(base_path, name)
            return 
        str = 'url:{}\n标题:{}\n描述:{}\n\n'.format('https://juejin.cn/post/{}'.format(i['id']), i['title'], i['desc'])
        with open('{}/{}.md'.format(path, i['title'].replace('\\', '_').replace('/', '_')), 'w+', encoding='utf-8') as f:
            f.write(str + md)
        time.sleep(30 + 30 * random.random())

# get('article/', '面试')


s = []

for i in file_path:
    get('article/', i)
    # t = threading.Thread(target=get, args=(
    #     'article/', i))  # 每次循环开启一个线程
    # s.append(t)

# for i in s:
#     i.start()
