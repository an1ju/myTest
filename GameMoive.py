# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:35:23 2018

写文本操作
本段代码写的是html文件
但现在提供的链接是有实效性的。暂时没法解决。
@author: an1ju
"""


# 基本操作，写txt的方法
def write_txt(filePathAndName, new_context):
    txtName = filePathAndName
    f = open(txtName, "a")
    f.write(new_context + "\n")
    f.close()


''''''
# 创建的html文件名称，可包含路径  比如：d:\\【游戏】《我的总裁女友》 视频全集.html"  不写路径就是这个python文件的当前路径了。
# 这个变量由于多次使用，因此提前创建好。
global filename
filename = "【游戏】《我的总裁女友》 视频全集.html"
global title
title = "【游戏】《我的总裁女友》陈子溪 视频全集"
global url_main
url_main = "https://lg.173funny.com/h5/gs/3/api.php?A=GetVideoURL&T=oJBYAIY5VdsH9I76zy2JlGcSDqdcnHDMiWmMAtY0NePLP1m7Kqd2zZaNnguw3%2Fh9%2BUG%2FLYkpVJ2nCA0gRF%2F96mNZA%2BS3FZq8F8tFkEN5woDzOhfoXrg5dKcokkC9Jx7ru4r54Q95wUGIDgvJaDua95FaKq7%2FoG%2Fw55CjnwRcO2WCpKIOCENn6xGPCwXdqBgkISQIKEqF5BLMYloNR%2Bp%2F8Lt7l2iRBoRJQ6fO24C5qIE2ApNQ0lBOjzKDTE4I4luGm%2F88DQZi1XYG57DZWKtQ%2BA%3D%3D&G=%5B1103%5DOjzKDTE4I4luGm/88DQZi1XYG57DZWKtQ+A==&G=["
global url_end
url_end = "]"
global begin_no
begin_no = 1101
global end_no
end_no = 1153
global others_begin_no
others_begin_no = 1101


# 写html的基本元素和标题，其实也可以不写。
def step0():
    write_txt(filename, "<html><title>%s</title>%s<br>" % (title, title))


# 循环写入链接地址
def step1():
    # 创建超链接
    for i in range(begin_no, end_no):
        markAbegin = "<a href="
        strA = "\"" + url_main
        strB = "%s" % i + url_end + "\">"
        word = "第%s集" % (i - begin_no + 1)  # 第几集 把初始的数减掉
        markAend = "</a>"
        write_txt(filename, markAbegin + strA + strB + word + markAend)
    '''
    # 可能出现的分支剧情
    write_txt(filename, "<br><br>可能出现的分支剧情：<br><br><br>")
    for x in range(end_no - begin_no):
        for i in range(1, 4):
            strA = url_main
            strB = str(others_begin_no + x) + "%s" % i
            write_txt(filename, strA + strB + url_end + "   <br>")

    # 给迅雷等提供链接
    write_txt(filename, "<br><br>给下载器提供链接(复制后，进入迅雷等下载器。再粘贴在新建任务中，可多文件批量下载)：<br><br><br>")
    for i in range(begin_no, end_no):
        strA = url_main
        strB = "%s" % i
        write_txt(filename, strA + strB + url_end + "<br>")
    '''

# 写html结尾
def step2():
    write_txt(filename, "</html>")


# 陈子溪的  其中全局变量数据在此处更改。为了其他视频也能快速建立。这里的方法同样适用其他视频。
# https://lg.173funny.com/h5/gs/3/api.php?A=GetVideoURL&T=oJBYAIY5VdsH9I76zy2JlGcSDqdcnHDMiWmMAtY0NePLP1m7Kqd2zZaNnguw3%2Fh9%2BUG%2FLYkpVJ2nCA0gRF%2F96mNZA%2BS3FZq8F8tFkEN5woDzOhfoXrg5dKcokkC9Jx7ru4r54Q95wUGIDgvJaDua95FaKq7%2FoG%2Fw55CjnwRcO2WCpKIOCENn6xGPCwXdqBgkZ5YTeAWAZCOCbBaoB4liK6OY3Un4i9jVlgRdj8Dc7GokpkweXjE063noo0zwy62zM4%2B%2BnT%2BOa4s2%2FJvNBg%2FvHw%3D%3D&G=%5B1104%5D
def chenzixi_Coming():
    global filename
    filename = "【游戏】《我的总裁女友》陈子溪 视频全集.html"
    global title
    title = "999rewrwerwrwe"
    global url_main
    #url_main = "https://lg.173funny.com/h5/gs/3/api.php?A=GetVideoURL&T=oJBYAIY5VdsH9I76zy2JlGcSDqdcnHDMiWmMAtY0NePLP1m7Kqd2zZaNnguw3%2Fh9%2BUG%2FLYkpVJ2nCA0gRF%2F96mNZA%2BS3FZq8F8tFkEN5woDzOhfoXrg5dKcokkC9Jx7ru4r54Q95wUGIDgvJaDua95FaKq7%2FoG%2Fw55CjnwRcO2WCpKIOCENn6xGPCwXdqBgkISQIKEqF5BLMYloNR%2Bp%2F8Lt7l2iRBoRJQ6fO24C5qIE2ApNQ0lBOjzKDTE4I4luGm%2F88DQZi1XYG57DZWKtQ%2BA%3D%3D&G=%5B1103%5DOjzKDTE4I4luGm/88DQZi1XYG57DZWKtQ+A==&G=["

    #url_main = "https://lg.173funny.com/h5/gs/3/api.php?A=GetVideoURL&T=oJBYAIY5VdsH9I76zy2JlGcSDqdcnHDMiWmMAtY0NePLP1m7Kqd2zZaNnguw3%2Fh9%2BUG%2FLYkpVJ2nCA0gRF%2F96mNZA%2BS3FZq8F8tFkEN5woDzOhfoXrg5dKcokkC9Jx7ru4r54Q95wUGIDgvJaDua95FaKq7%2FoG%2Fw55CjnwRcO2WCpKIOCENn6xGPCwXdqBgkZ5YTeAWAZCOCbBaoB4liK6OY3Un4i9jVlgRdj8Dc7GokpkweXjE063noo0zwy62zM4%2B%2BnT%2BOa4s2%2FJvNBg%2FvHw%3D%3D&G=%5B"
    global url_end
    url_end = "]"
    global begin_no
    begin_no = 1101
    global end_no
    end_no = 1153
    global others_begin_no
    others_begin_no = 1201
    # 操作  按照步骤进行
    step0()
    step1()
    step2()

    # 运行结束提示用户
    print("%s  写入结束：%s>>>> 已保存！！" % (filename, title))


# https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&G=%5B1101%5D    '''第一行可能是初始化'''
# https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&T=N8DVEQe814aW1ugHakp6w1Mezw%2Fs0SC%2FKhRWDCsWsudizHe%2Ft3uPEdbBn%2BHRZdzUpjxCvGnzjSN164hOQvhss5QRlJHLFRljtp%2FuCfaQmi8qv8yNfV4FNVWJ5t82PzodAHJOTNLnj5RnWxmFhAMnZGKYnnln7112rFBKvjI%2F3VWlC31pm51YVNXvB5lpW58r7VjgAnbcNRF3c4sKdnz3kBfzK5CBLbWvtMSBxaY66yHcEbisSsO6dNzkK6a0IT2HneKMlsKjV9veWHkaSQLELw%3D%3D&G=%5B1102%5D
# https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&T=N8DVEQe814aW1ugHakp6w1Mezw%2Fs0SC%2FKhRWDCsWsudizHe%2Ft3uPEdbBn%2BHRZdzUpjxCvGnzjSN164hOQvhss5QRlJHLFRljtp%2FuCfaQmi8qv8yNfV4FNVWJ5t82PzodAHJOTNLnj5RnWxmFhAMnZGKYnnln7112rFBKvjI%2F3VWlC31pm51YVNXvB5lpW58rv9vfd5CUjxcsZUDt7XkTRt%2BEODQHQjx1W14P22hvLsnnMGdhqLrItaIlJtHYURhAE3NpUx8LZRRBrw4AXc%2FX3g%3D%3D&G=%5B1103%5D     '''主线剧情11开头'''
# https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&T=N8DVEQe814aW1ugHakp6w1Mezw%2Fs0SC%2FKhRWDCsWsudizHe%2Ft3uPEdbBn%2BHRZdzUpjxCvGnzjSN164hOQvhss5QRlJHLFRljtp%2FuCfaQmi8qv8yNfV4FNVWJ5t82PzodAHJOTNLnj5RnWxmFhAMnZGKYnnln7112rFBKvjI%2F3VWlC31pm51YVNXvB5lpW58rv9vfd5CUjxcsZUDt7XkTRt%2BEODQHQjx1W14P22hvLsnnMGdhqLrItaIlJtHYURhAE3NpUx8LZRRBrw4AXc%2FX3g%3D%3D&G=%5B12031%5D    '''分支剧情12开头'''
# https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&T=N8DVEQe814aW1ugHakp6w1Mezw%2Fs0SC%2FKhRWDCsWsudizHe%2Ft3uPEdbBn%2BHRZdzUpjxCvGnzjSN164hOQvhss5QRlJHLFRljtp%2FuCfaQmi8qv8yNfV4FNVWJ5t82PzodAHJOTNLnj5RnWxmFhAMnZGKYnnln7112rFBKvjI%2F3VWlC31pm51YVNXvB5lpW58rv9vfd5CUjxcsZUDt7XkTRt%2BEODQHQjx1W14P22hvLsnnMGdhqLrItaIlJtHYURhAE3NpUx8LZRRBrw4AXc%2FX3g%3D%3D&G=%5B12032%5D    '''分支剧情'''
def linyiwen_Coming():
    global filename
    filename = "【游戏】《我的心动女友》林依雯 视频全集.html"
    global title
    title = "【游戏】《我的心动女友》林依雯 视频全集"
    global url_main
    url_main = "https://lg.173funny.com/h5/gs/1/api.php?A=GetVideoURL&T=N8DVEQe814aW1ugHakp6w1Mezw%2Fs0SC%2FKhRWDCsWsudizHe%2Ft3uPEdbBn%2BHRZdzUpjxCvGnzjSN164hOQvhss5QRlJHLFRljtp%2FuCfaQmi8qv8yNfV4FNVWJ5t82PzodAHJOTNLnj5RnWxmFhAMnZGKYnnln7112rFBKvjI%2F3VWlC31pm51YVNXvB5lpW58rv9vfd5CUjxcsZUDt7XkTRt%2BEODQHQjx1W14P22hvLsnnMGdhqLrItaIlJtHYURhAE3NpUx8LZRRBrw4AXc%2FX3g%3D%3D&G=%5B"
    global url_end
    url_end = "%5D"
    global begin_no
    begin_no = 1101
    global end_no
    end_no = 1182
    global others_begin_no
    others_begin_no = 1201
    # 操作  按照步骤进行
    step0()
    step1()
    step2()


chenzixi_Coming()
linyiwen_Coming()
