import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    # 发送GET请求获取网页内容
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 在这里可以根据网页结构提取需要的数据
        # 以下是一个示例，提取所有的超链接
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print('请求失败:', response.status_code)

# 调用函数并传入目标网页的URL
crawl_website('http://example.com')
