import random

ip_list = [
    'bl.xyhy.ink',
    'c.shcn2.xlddns.xyz',
    'c.shcn2.xlddns.xyz',
    '120.232.40.147',
    '120.232.181.232',
    '120.240.47.66',
    '23.97.53.186',
    '120.232.181.232',
    '129.226.156.35',
    '101.69.128.84',
    '52.155.107.28',
    '101.69.128.84',
    'zjx2.cu.xlddns.xyz',
    '101.69.128.84',
    '122.192.189.40',
    '49.51.189.231',
    '120.232.40.195',
    '40.83.92.74',
    '52.231.202.251',
    '120.232.40.147',
    '101.69.128.84'
]


def get_random_ip():
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    proxies = get_random_ip(ip_list)
    print(proxies)