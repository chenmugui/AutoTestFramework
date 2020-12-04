from data_driver.excel_excutor import ExcelExcutor

if __name__ == '__main__':
    yaml_path = r'../config/data.yaml'
    key1 = 'webui'
    key2 = 'file'
    ExcelExcutor().excute_web(yaml_path, key1, key2)
