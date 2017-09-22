# Python logging
+ Warm up
+ Important concepts
+ Template for complex system
+ Ref
## Warm up
By three learning case, familiar with Python logging

### Case1
```py
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
```

### Case2
```py
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

# 通过下面的方式进行简单配置输出方式与日志级别
logging.basicConfig(filename='logger.log', level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
```


### Case3
```
[loggers]
keys=root,example01

[handlers]
keys=hand01,hand02

[formatters]
keys=simple,detail

[logger_root]
level=NOTSET
handlers=hand01,hand02

[logger_example01]
handlers=hand01,hand02
qualname=example01
propagate=0

[handler_hand01]
class=StreamHandler
level=INFO
formatter=simple
args=(sys.stderr,)

[handler_hand02]
class=FileHandler
level=DEBUG
formatter=detail
args=('log.log', 'a')

[formatter_detail]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s

[formatter_simple]
format=%(name)s - %(levelname)s - %(message)s
```

```py
# -*- encoding:utf-8 -*-
import logging

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create file handler
log_path = "./log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

```
## 重要的概念
Logger 记录器，暴露了应用程序代码能直接使用的接口。
Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 格式化器，指明了最终输出中日志记录的布局。

## template for complex system
+ INPUT: log.py, log_test.py, __init__.py(nothing in this file)
+ OUTPUT: 
    + file: logs/tapnews.log
    + terminal: run by self

log.py
```py
# coding:utf-8
'''
Logging module for Tap News
'''

import os
import logging
import logging.config as log_conf

LOG_DIR = os.path.dirname(os.path.dirname(__file__))+'/logs'
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_PATH = os.path.join(LOG_DIR, 'tapnews.log')

LOG_CONFIG = {
    'version': 1.0,
    'formatters': {
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'optional': {
            'format': '%(filename)s %(lineno)d - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'optional'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': LOG_PATH,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'news_monitor': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'news_fetcher': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'other': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'news_deduper': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}

log_conf.dictConfig(LOG_CONFIG)

LOGGING_NEWS_MONITOR = logging.getLogger('news_monitor')
LOGGING_NEWS_FETCHER = logging.getLogger('news_fetcher')
LOGGING_NEWS_DEDUPER = logging.getLogger('news_deduper')
LOGGING_OHTER = logging.getLogger('other')

__all__ = ['LOGGING_NEWS_MONITOR', 'LOGGING_NEWS_FETCHER', 'LOGGING_NEWS_DEDUPER', 'LOGGING_OHTER']

```
log_test.py
```py
'''
test LOGGING module
'''
# import common package in parent directory
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'logger'))

# from log import parser, crawler, storage
from log import LOGGING_NEWS_MONITOR, LOGGING_NEWS_FETCHER
from log import LOGGING_NEWS_DEDUPER, LOGGING_OHTER

LOGGING_NEWS_MONITOR.info('This is crawler')

LOGGING_NEWS_FETCHER.info('This is info')

LOGGING_NEWS_DEDUPER.info('tihs is error')

LOGGING_OHTER.info('tihs is error')

```


## Ref:
Author：好吃的野菜
Link:http://www.jianshu.com/p/feb86c06c4f4

Author:rookiefly
Link:https://github.com/ResolveWang/weibospider/blob/master/logger/log.py
