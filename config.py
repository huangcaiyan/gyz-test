class Config(object):

    # base_url
    # BASE_URL = 'https://firms.guanplus.com'
    # BASE_URL = 'http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn'
    BASE_URL = 'https://web-gyz-stage.guanplus.com'

    # 登录信息
    # pro
    # LOGIN_DATA = ['13683139989','qq123456']
    # dev
    # LOGIN_DATA = ['18612198503','qq123456']
    # stage
    LOGIN_DATA = ['13683139989','qq123456']

    # 公司信息
    # comp_json ［'username','password','comp_name']
    # stage
    # COMP_NAME = 'auto_test'
    # COMP_NAME_YB ='auto_test_yb'
    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    # stage
    COMP_NAME = 'auto_test'
    COMP_NAME_YB = 'auto_test_0828'


    ENTER_COMP_INFO= [LOGIN_DATA,COMP_NAME]
    ENTER_COMP_INFO_YB = [LOGIN_DATA,COMP_NAME_YB]

