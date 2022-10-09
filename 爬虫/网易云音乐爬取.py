import requests, os, csv, ssl, time, random  # ssl全局关闭认证
from bs4 import BeautifulSoup
from urllib.request import urlretrieve  # 可以通过网络url下载资源

# ssl全局关闭认证
# ssl._create_stdlib_context = ssl._create_unverified_context
ssl._create_stdlib_context = ssl.create_default_context()


class SpiderWYMusicApp:  # 应用

    def __init__(self):  # 初始化
        self.id = input('请输入歌单ID：')  # 输入id

        self.url = 'https://music.163.com/playlist'

        self.download_url = 'https://music.163.com/song/media/outer/url'

        self.head = {  # 定制头部
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

        self.proxies = {  # 代理IP
            'https://': ('60.13.42.14:9999', '58.220.95.116:10122')
        }

        self.music_dict = {}  # 保存音乐信息

    def sendReqPlayList(self):  # 1 访问网易云歌单列表页面
        # 发起请求，提交参数
        # 访问创建一个客户端和服务器：会话对象追踪验证 session
        # session() 创建一个会话对象，在访问
        resp = requests.session().get(url=self.url, params={'id': self.id}, headers=self.head, proxies=self.proxies)
        # 验证路径、状态码
        print(resp.url, resp.status_code)
        # 解析数据源
        soup = BeautifulSoup(resp.content, 'html5lib')

        # 获取网页标题，作为csv文件名称使用
        self.title = soup.title.string

        # 根据抓包分析，获取隐藏的数据标签 ul
        ul = soup.find(name='ul', attrs={'class': 'f-hide'})
        # 获取ul内部的a标签
        a_list = ul.find_all(name='a')
        # 循环：获取音乐信息
        for a in a_list:
            music_name = a.string.strip()
            music_id = a.attrs.get('href')

            self.music_dict[music_name] = music_id

            # print(music_name,music_id)

        pass

    def save(self):  # 2 保存本地
        dir_path = 'D:/86101/Desktop/网易云音乐'
        # 验证是否存在
        if not os.path.exists(dir_path):
            # 创建
            os.mkdir(dir_path)

        file = open(dir_path + '/' + '网易云音乐' + self.title + '.csv', mode='w', encoding='utf-8', newline='')

        csvfile = csv.writer(file)

        csvfile.writerow(['音乐名称', '音乐路径'])

        # 音乐访问出现404，VIP音乐
        for key, value in self.music_dict.items():
            # 只获取/song?id=489998494中的id，所以前五位字符不需要
            value = self.download_url + value[5:]

            csvfile.writerow([key, value])

        file.flush()
        file.close()

        pass

        # 问题：音乐文件下载，内容缺失，播放不了
        # 后续完善.................
        for key, value in self.music_dict.items():
            # File文件url地址，可以下载
            try:
                value = self.download_url + value[5:]
                # urlretrieve(url=value, filename=dir_path + '/' + key + '.mp3')

                # 请求获取音乐文件的二进制
                resp = requests.get(url=value, headers=self.head, proxies=self.proxies)

                # r 读取 rb 读取字节 w 写入 wb写入字节
                music_file = open(dir_path + '/' + key + '.mp3', "wb")
                music_file.write(resp.content)

                print(key, '下载成功')

                # for速度很快的，需要睡眠,随机时间 1~3 秒
                time.sleep(random.random() * 2 + 1)

            except:
                print(key, '下载失败')

        pass

    def run(self):  # 3 入口
        self.sendReqPlayList()
        self.save()


# 实例对象，运行
app = SpiderWYMusicApp()
app.run()
