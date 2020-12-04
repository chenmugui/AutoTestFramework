from data_driver.excel_conf import ExcelConf
from framework.webui_autotest_init import WebUI_Framework
from logs.log import Logger


class ExcelExcutor(object):
    '''
        实例化对象
        结合参数调用关键字
        封装整合
    '''
    # 创建日志对象
    log = Logger().get_logger()
    ec = ExcelConf()
    excel_path = ''
    excel = ''

    def excute_get_sheets(self, excel_path_value):
        global excel_path
        global excel
        excel_path = excel_path_value
        excel = self.ec.load_excel(excel_path)
        sheets = self.ec.get_sheets(excel)
        return sheets

    # Excel执行读写操作
    def excute_web(self, excel_path_value):
        sheets = self.excute_get_sheets(excel_path_value)
        try:
            # 读取所有Sheet页面
            for sheet in sheets:
                self.log.info('获取{0}内容成功，现在开始执行自动化测试......'.format(sheet))
                sheet1 = excel[sheet]
                # 基于Sheet内容，运行测试用例
                for value in sheet1.values:
                    param = {}
                    param['loc'] = value[2]
                    param['value'] = value[3]
                    param['txt'] = value[4]
                    param['expect'] = value[6]
                    # 判断文件，从用例内容开始执行
                    if type(value[0]) is int:
                        # 判断关键字列，如果是open_browser，则实例化对象，如果不是，则进行其他元素操作
                        if value[1] == 'open_browser':
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            wf = WebUI_Framework(param['txt'])
                        # 判断是否为断言，若是断言则添加写入操作
                        elif 'assert' in value[1]:
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            status = getattr(wf, value[1])(**param)
                            row = value[0] + 1
                            if status is True:
                                self.log.info('流程测试通过！')
                                self.ec.cell_write('pass', sheet1, row)
                            else:
                                self.log.info('流程测试失败！')
                                self.ec.cell_write('false', sheet1, row)
                            self.ec.save_excel(excel, excel_path)
                        # 定义常规关键字调用
                        else:
                            self.log.info('现在执行关键字:{0}，操作描述：{1}'.format(value[1], value[5]))
                            getattr(wf, value[1])(**param)
                    else:
                        pass
        except Exception as e:
            self.log.exception('运行出现异常，信息描述：{0}'.format(e))
        finally:
            # 关闭读取的文件
            self.log.info("文件读取完毕，自动化执行结束！\n")
            self.ec.close(excel)
