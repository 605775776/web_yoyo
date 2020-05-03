import unittest
# from web_auto.report.HTMLTextRunnerNew import HTMLTestRunner
from common.HTMLTestRunner_cn import HTMLTestRunner
import sys
import os
from common.dir_config import *
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# coding:utf-8
# 用例地址



# 测试套件收集用例
# discover方法加载多个用例集合
discover = unittest.defaultTestLoader.discover(start_dir=test_case_dir,
                                               pattern="test*.py",
                                               top_level_dir=None)
# print(discover)
with open(test_report_dir, 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title="login",
                            description=None,
                            retry=1)

    runner.run(discover)
