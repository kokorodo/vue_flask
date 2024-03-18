class Config(object):
    DEBUG = True
    HTTP_PORT = 5000

    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql://flask_test:ezP5ce7aiwbBne3R@192.168.0.191:3306/flask_test?charset=utf8mb4"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 15


