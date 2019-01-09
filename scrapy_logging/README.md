## 此scrapy_logging可以设置 继承scrapy中自带log，并可以设置过期时间并删除

#### 每个添加的文件中都有注释，从最外级目录往里一个个看看
```
├── README.md
├── scrapy_logging
│   ├── __init__.py
│   ├── items.py
│   ├── logger_conf.py       # 添加这个文件
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── show_log_cfg.py  # 注意导入
├── logger.cfg               # 创建这个log的配置文件
├── logs
│   └── CristianoRonaldo.py  # 无用，只为方便创建 /logs 这个文件夹
└── scrapy.cfg
```