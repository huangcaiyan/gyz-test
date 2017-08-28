# 1、启用期初账页面
# 导入按钮 xpath
import_btn_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[3]/button'
# 编辑按钮 xpath
edit_btn_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[2]/button'
# 启用期初账按钮 xpath
start_book_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[1]/button'
# 银行分配按钮
bank_distribute_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[4]/div/div/table/tbody/tr[4]/td[9]/button'
# 支付宝分配按钮
alipay_distribute_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[4]/div/div/table/tbody/tr[5]/td[9]/button'
# 微信分配按钮xpath
wechat_distribute_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[4]/div/div/table/tbody/tr[6]/td[9]/button'
# 借方金额xpath
debit_sum_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]'
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 2、银行分配
# 银行分配按钮
bank_distribute_elem = '//*[@id="body"]/finance/div/beginning-period/div/div[4]/div/div/table/tbody/tr[4]/td[9]/button'
# 账户名input xpath
account_name_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/input'
# 开户银行input xpath
bank_name_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[2]/input'
# 支行 input xpath
bank_branch_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[3]/input'
# 账户号 input xpath
bank_num_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[4]/input'
# 本年期初余额 input xpath
bank_initial_balance_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[5]/ng2-numeric-input/div/div[1]/input[1]'
# 保存银行 按钮 xpath
save_bank_btn_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[3]/button[1]'
# 取消银行分配 按钮 xpath
cancel_bank_btn_elem = '//*[@id="body"]/finance/div/beginning-period/gpw-bp-addbankaccount/div/div[2]/div/div[3]/button[2]'


