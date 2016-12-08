# 有度企业应用API demo
## 依赖（请自行使用pip安装）
- Crypto
- requests
- requests_toolbelt
- struct
- aiohttp（可选，用于回调示例）

## 实现内容
- 企业应用主动调用接口封装entapp（支持python2或python3）
- 主动调用接口测试用例（支持python2或python3）
- 回调接口示例。（支持python3）

## 注意事项

关于Crypto.Cipher模块，ImportError: No module named 'Crypto'解决方案
请到官方网站 https://www.dlitz.net/software/pycrypto/ 下载pycrypto。
下载后，按照README中的“Installation”小节的提示进行pycrypto安装。
