import requests
import os
import json
import time
import random
import threading
import queue

R = threading.Lock()

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'content-type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.20 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://juejin.cn/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

count = {
    'num': 0
}


def make_dir(path):
    exist = os.path.exists(path)
    if not exist:
        os.mkdir(path)
    else:
        print('“{}”目录已存在'.format(path))


def download_list(data, path, num):
    make_dir('database/{}'.format(path))
    with open('database/{}/juejin_{}.py'.format(path, num), 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        # count['num'] += 1


def get_data(url, data):
    r = requests.post(url, json.dumps(data), headers=headers)
    return r.json()


def get_article_list(cursor, tag_id, tag_name, num):
    try:
        url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_cate_tag_feed?aid=2608&uuid=6906668532231079437'
        data = {"id_type": 2, "sort_type": 200, "cate_id": "6809637767543259144", "tag_id": tag_id,
                "cursor": cursor, "limit": 20}
        r = get_data(url, data)
        download_list(r, tag_name, num)
        R.acquire()
        print('next -> ', r.get('cursor'), r.get('has_more'), num)
        num+=1
        R.release()
        # if not r.get('has_more'):
        #     time.sleep(random.random() * 2)
        if r.get('cursor') and r.get('has_more'):
            time.sleep(random.random())
            get_article_list(r.get('cursor'), tag_id, tag_name, num)
    except Exception as e:
        R.acquire()
        print('----------------error----------------', e)
        print(num, cursor)
        R.release()

        # time.sleep(random.random() * 2)
        # get_article_list(cursor)


# get_article_list('0', 'tag_id')


tags = [
    {
        "id": 2546526,
        "tag_id": "6809640407484334093",
        "tag_name": "前端",
        "color": "#60ADFF",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/bac28828a49181c34110.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 1,
        "ctime": 1435971546,
        "mtime": 1631691394,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 88819,
        "concern_user_count": 527704
    },
    {
        "id": 2546519,
        "tag_id": "6809640398105870343",
        "tag_name": "JavaScript",
        "color": "#616161",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/5d70fd6af940df373834.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1435884803,
        "mtime": 1631690979,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 67401,
        "concern_user_count": 398955
    },
    {
        "id": 2546498,
        "tag_id": "6809640369764958215",
        "tag_name": "Vue.js",
        "color": "#41B883",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/7b5c3eb591b671749fee.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1432234520,
        "mtime": 1631690561,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 31254,
        "concern_user_count": 313519
    },
    {
        "id": 2546516,
        "tag_id": "6809640394175971342",
        "tag_name": "CSS",
        "color": "#244DE4",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/66de0c4eb9d10130d5bf.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1432239426,
        "mtime": 1631688735,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 14981,
        "concern_user_count": 297034
    },
    {
        "id": 2546490,
        "tag_id": "6809640357354012685",
        "tag_name": "React.js",
        "color": "#61DAFB",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/f655215074250f10f8d4.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1432234367,
        "mtime": 1631690358,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 16998,
        "concern_user_count": 226420
    },
    {
        "id": 2546592,
        "tag_id": "6809640499062767624",
        "tag_name": "算法",
        "color": "#60ADFF",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/68a1097944c7fa1d7961.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1439503293,
        "mtime": 1631690351,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 23471,
        "concern_user_count": 310820
    },
    {
        "id": 2546524,
        "tag_id": "6809640404791590919",
        "tag_name": "面试",
        "color": "#545454",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/85dd1ce8008458ac220c.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1435971430,
        "mtime": 1631690269,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 15727,
        "concern_user_count": 349601
    },
    {
        "id": 2546625,
        "tag_id": "6809640543006490638",
        "tag_name": "TypeScript",
        "color": "#0061c4",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/d788a559489fa6e30b25.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1441228068,
        "mtime": 1631687225,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 3915,
        "concern_user_count": 48017
    },
    {
        "id": 2546614,
        "tag_id": "6809640528267706382",
        "tag_name": "Webpack",
        "color": "#6F94DB",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/73e856b07f83b4231c1e.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1440920866,
        "mtime": 1631684904,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 6703,
        "concern_user_count": 204077
    },
    {
        "id": 2546492,
        "tag_id": "6809640361531539470",
        "tag_name": "Node.js",
        "color": "#e81864",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/f16f548d25028a1fdd80.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1432234488,
        "mtime": 1631690352,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 11514,
        "concern_user_count": 280711
    },
    {
        "id": 2546704,
        "tag_id": "6809640653266354190",
        "tag_name": "微信小程序",
        "color": "#11a600",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/a1e7773920f51db40441.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1474932627,
        "mtime": 1631690623,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 7106,
        "concern_user_count": 221757
    },
    {
        "id": 2546983,
        "tag_id": "6809641039037464589",
        "tag_name": "LeetCode",
        "color": "#000000",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/155748584224691639f51dce773ead8d4233400c24546.jpg~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1489518382,
        "mtime": 1631678072,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 6296,
        "concern_user_count": 11300
    },
    {
        "id": 2546515,
        "tag_id": "6809640392770715656",
        "tag_name": "HTML",
        "color": "#E44D25",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/f18965b2a0ef9cac862e.png~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1432239419,
        "mtime": 1631683077,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 6109,
        "concern_user_count": 240134
    },
    {
        "id": 2547019,
        "tag_id": "6809641090145058824",
        "tag_name": "Flutter",
        "color": "",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/1519790365175e2d3ba2174d5c8f3fdc4687a8bbf5768.jpg~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1519761568,
        "mtime": 1631690413,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 9303,
        "concern_user_count": 42136
    },
    {
        "id": 2546923,
        "tag_id": "6809640956946546702",
        "tag_name": "Element",
        "color": "#000000",
        "icon": "https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/leancloud-assets/2c670995272515e48cea.svg~tplv-t2oaga2asx-image.image",
        "back_ground": "",
        "show_navi": 0,
        "ctime": 1489435335,
        "mtime": 1631690287,
        "id_type": 9,
        "tag_alias": "",
        "post_article_count": 1925,
        "concern_user_count": 15229
    }
]


s = []

for i in tags:
    t = threading.Thread(target=get_article_list, args=(
        '0', i['tag_id'], i['tag_name'], 0))  # 每次循环开启一个线程
    s.append(t)

for i in s:
    i.start()



