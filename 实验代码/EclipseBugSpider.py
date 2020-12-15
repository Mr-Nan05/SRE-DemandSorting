import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.183Safari / 537.36'
}


def get_bugs():
    url = 'https://bugs.eclipse.org/bugs/buglist.cgi?chfield=%5BBug%20creation%5D&chfieldfrom=30d'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    bug_items = soup.select('tr.bz_bugitem>td.bz_short_desc_column a')

    for item in bug_items:
        bug_title = item.text.strip()
        bug_url = 'https://bugs.eclipse.org/bugs/' + item['href']

        error_counter = 1
        index = bug_items.index(item)
        while True:
            try:
                bug_degree = get_degree(bug_url)
                filename = bug_degree[0] + bug_degree[1].title() + '.txt'


                (filename, bug_title)
                print(index, bug_degree, bug_title)
                break
            except:
                error_counter += 1
                print(index, '第' + str(error_counter) + '次尝试重连')
                time.sleep(0.5)


def get_degree(url):
    # 获取分类等级
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.select('#bz_show_bug_column_1 > table > tr:nth-child(11) > td')[0].text.strip().split()[:2]
    except:
        pass


def write2file(filename, content):
    # 写入文件
    with open(filename, 'a', encoding='utf8') as file:
        file.write(content + '\n')


if __name__ == '__main__':
    get_bugs()
    print('程序正常运行结束')

