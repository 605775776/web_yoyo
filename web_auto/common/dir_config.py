import os
dir_config= os.path.abspath(__file__)
base = os.path.dirname(os.path.dirname(dir_config))
test_data_dir = os.path.join(base, 'common/test_data.xlsx')
test_case_dir = os.path.join(base, "case")
test_report_dir = os.path.join(base, "report/report.html")
# print(test_case_dir)
# print(base)
