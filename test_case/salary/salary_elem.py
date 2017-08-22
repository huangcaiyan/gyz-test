# element loc
"""员工管理"""
# 员工管理页面url
stuff_list_url = '/app/salary/stuff-list'
# 员工页面判定xpath
stuff_list_elem = '//*[@id="body"]/stuff-list/div[2]/div/div/ol/li[3]/button[1]'

"""添加员工"""
# 添加员工页面url
add_stuff_url = '/app/salary/stuff'
# 添加员工页面判定xpath
add_stuff_elem = '//*[@id="body"]/stuff/div[3]/div[1]/span'

"""导入员工"""
# 导入员工页面url
import_stuff_url = '/app/salary/stuff-import'
# 导入员工页面判定xpath
import_stuff_elem = '//*[@id="body"]/stuff-import/div[2]/div/div[2]/upload-attachments/div/div/span/label'

"""工资表"""
# 工资表页面url
salary_list_url = '/app/salary/salary-sheet/salary'
# 工资表页面判定xpath
salary_list_elem = '//*[@id="body"]/salary/salary-sheet/div[2]/div/div/div[2]/div/div/div/table/thead/tr[1]/th[1]'

"""务表"""
# 劳务表页面url
labour_list_url = '/app/salary/salary-sheet/labour'
# 劳务表页面判定xpath
labour_list_elem = '//*[@id="body"]/salary/labour-sheet/div[2]/div/div/div[2]/div/div/div/table/thead/tr/th[1]'

"""工资发放记录"""
# 工资发放记录页面url
salary_record_url = '/app/salary/salary-record/salary'
# 工资发放记录页面判定xpath
salary_record_elem = '//*[@id="body"]/salary-router-record/salary-record/div/div/div/div[2]/div/div/div/table/thead/tr[1]/th[1]'

"""劳务发放记录"""
# 劳务发放记录页面url
labour_record_url = '/app/salary/salary-record/labour'
# 劳务发放记录页面判定xpath
labour_record_elem = '//*[@id="body"]/salary-router-record/labour-record/div/div/div/div[2]/div/div/div/table/thead/tr/th[1]'
