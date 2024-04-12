# NOJ Server

## 工具依赖

- Python 3.8
- MySQL（可选）

> [!NOTE]
>
> 如果开发机器没有安装 MySQL，也可以在 “数据库设置“ 环节直接将数据库配置修改为代码中的注释内容，使用默认的 sqlite 引擎。

## 环境配置

进入 `server` 目录，执行以下命令：

```
pip install -r requirements.txt
```

其中，安装 mysqlclient 大概率会出现报错，需要访问 [Pypi](https://pypi.org/project/mysqlclient/) 下载 `.whl` 文件进行安装，如果使用 sqlite 可以忽略。

## 数据库设置

创建 `NOJ` 数据库，打开 `server/server/settings.py` 文件，修改 `else` 语句之后的内容：

```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NOJ',
        'USER': os.environ.get("DB_USER") if os.environ.get("DB_USER") else 'root',
        'PASSWORD': os.environ.get("DB_PASSWORD") if os.environ.get("DB_PASSWORD") else 'dbpasswd',
        'HOST': os.environ.get("DB_HOST") if os.environ.get("DB_HOST") else 'localhost',
        'PORT': os.environ.get("DB_PORT") if os.environ.get("DB_PORT") else 3306,
    }
}
```

也可以不修改代码，而是直接将上面四个参数设置为环境变量。

## 运行

首先同步数据库：

```
python manage.py makemigrations
python manage.py migrate
```

然后运行服务：

```
python manage.py runserver 0.0.0.0:8000
```

接着访问 http://127.0.0.1:8000/swagger 即可获取后端文档。
