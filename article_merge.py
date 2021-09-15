import os
import time
import json

root = ['微信小程序', '算法', 'CSS', 'React.js', 'LeetCode', 'TypeScript', 'Element',
        'HTML', '面试', 'Webpack', 'Flutter', 'Node.js', 'Vue.js', 'JavaScript', '前端']


def file_name(file_dir):
    all = []
    for root, dirs, files in os.walk(file_dir):
        print(root, '-----------------------')
        # 当前路径下所有非目录子文件
        for file in files:
            print(root + file)
            with open(file_dir + '/' + file, 'r+', encoding='utf-8') as f:
                box = json.load(f)
                articles = box.get('data')
                for art in articles:
                    # print(art)
                    article = art.get('article_info')
                    row = {
                        'id': article.get('article_id'),
                        'title': article.get('title'),
                        'desc': article.get('brief_content')
                    }
                    all.append(row)
                    # print(all)
            # fs.write(str(all))
    # print(all)
    return all

t = []
for i in root:
    arr = file_name('database/{}'.format(i))
    print(arr)
    # with open('database/_{}.py'.format(i), 'w+', encoding='utf-8')as f:
    #     json.dump(arr, f, ensure_ascii=False)

