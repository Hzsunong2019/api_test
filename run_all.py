import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)  # 从配置文件中读取用例路径

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="接口测试报告", description="测试描述",tester='邹赟').run(suite)

send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")