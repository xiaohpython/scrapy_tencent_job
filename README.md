# 添加的配置注明
```python
# 打开MongoDB，并创建表(database)，创建Collection
# 运行项目
scrapy crawl tenxu_spider
```
## 项目中的相关配置
### tenxu_spider.py 就不说了
### pipelines.py
```python
# 实例化MongoDB客户端
client =MongoClient()
# 实例化库(database)和表(Collection)
collection = client["tencent"]["tenxu_spider"]

```
### settings.py
```python
# 添加日志级别
LOG_LEVEL ="WARNING"     # 大概18行

# 添加请求头
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'  # 大约22行

# 取消注释   大约71行
ITEM_PIPELINES = {
   'tencent.pipelines.TencentPipeline': 300,
}
```