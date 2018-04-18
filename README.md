## redis集群清除key工具

### 一 依赖模块安装
#### 1. 安装pip
wget https://bootstrap.pypa.io/get-pip.py  <br/>
python get-pip.py
#### 2. 安装依赖
pip install -r requirement.txt
#
### 二 执行
1. 保证config.json，redis_cleaner.py，redis_processor.py已经下载到运行环境<br/>
2. 以下面格式执行命令
#### python redis_cleaner.py key-pattern
例如： syscode开头的key全部删除 <br/>
__python redis_cleaner.py syscode*__