# 有度企业应用SDK

## 依赖（请自行使用pip安装）

- pycrypto
- requests
- requests_toolbelt
- struct
- aiohttp（可选，用于回调示例）

## 实现内容

- 企业应用主动调用接口封装entapp（支持python2或python3）
- 主动调用接口测试用例（支持python2或python3）
- 回调接口示例。（支持python3.5）

## 注意事项

关于`Crypto.Cipher`模块，ImportError: No module named 'Crypto'解决方案
请到官方网站 https://www.dlitz.net/software/pycrypto/ 下载`pycrypto`。  
下载后，按照README中的“Installation”小节的提示进行`pycrypto`安装。  
windows下安装出现问题可以参考这个帖子：  
http://stackoverflow.com/questions/11405549/how-do-i-install-pycrypto-on-windows

## 运行测试用例

测试用例`app_client_test.py`基于`unitest`测试库。  
请先填写该文件内必要的参数，并确保测试账号已经的登录有度客户端。  
可以直接使用`python app_client_test.py`运行，也可以在`Intellij IDEA`中直接运行。

## 运行回调示例

回调示例`app_demo.py`使用`aiohttp`建立HTTP Server。  
由于使用到了`python3.5`的`async/await`特性，所以需要安装`python3.5`以上的版本才能正常运行。  
请先填写该文件内必要的参数，并确保测试账号已经的登录有度客户端。  
可以直接使用`python app_demo.py`运行，也可以在`Intellij IDEA`中直接运行。
