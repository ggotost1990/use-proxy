# Python代理隧道使用方法
`proxyaddr = ip.json().get("result")[0]["ip"]`  # 代理IP地址
`proxyport = ip.json().get("result")[0]["port"]`  # 代理IP端口
`proxyusernm = "xcy004bb2ac4d739"`  # 代理帐号
`proxypasswd = "37429104"`  # 代理密码

`proxyurl = "http://"+proxyusernm+":" + \
proxypasswd+"@"+proxyaddr+":"+"%d" % proxyport` #连接地址
