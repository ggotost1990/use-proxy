
import requests

ip = requests.get(
    "http://xcy004bb2ac4d739.user.xiecaiyun.com/api/proxies?action=getJSON&key=NP7C8721D0&count=1&word=&rand=false&norepeat=false&detail=false&ltime=120")

proxyaddr = ip.json().get("result")[0]["ip"]  # 代理IP地址
proxyport = ip.json().get("result")[0]["port"]  # 代理IP端口
# print(proxyaddr, proxyport)
proxyusernm = "xcy004bb2ac4d739"  # 代理帐号
proxypasswd = "37429104"  # 代理密码

proxyurl = "http://"+proxyusernm+":" + \
    proxypasswd+"@"+proxyaddr+":"+"%d" % proxyport
proxies = {
    "http": proxyurl,
    "https": proxyurl
}
print(f"正在使用ip:{proxyaddr}:{proxyport}")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
url = "https://www.gucci.com/fr/zh/pr/women/ready-to-wear-for-women/jackets-for-women/down-jackets-windbreakers-for-women/the-north-face-x-gucci-padded-vest-p-663739XLUHP6168"
# ip_test = "http://httpbin.org/ip"
try:
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    print(response.text)
except Exception as e:
    print(f"error is {e}")
else:
    print("请求成功")
