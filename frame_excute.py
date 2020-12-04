from data_driver.excel_excutor import ExcelExcutor
import os
import threading
import sys

path = r'E:\web_project\AutoTestFramework'
sys.path.append(path)

if __name__ == '__main__':
    # 读取'../cases/'路径下的case文件，获取到则基于excel执行自动化
    # 定义用于接收用例与线程的集合

    cases = []
    th = []
    # 读取指定路径下的所有文件，判断用例文件数
    # walk函数，可以读取指定路径下的所有内容：文件、文件路径、文件夹
    for path, dir, files in os.walk(r'./cases/'):
        # 读取到的所有文件进行二次处理
        for file in files:
            # 拼接用例路径，便于后续调用：提供给Openpyxl所写的excute执行
            excel_path = path + file
            # 获取文件后缀名：os下的path.splitext()函数用于获取文件的名称与后缀，拆分为list集合
            s = os.path.splitext(file)[1]
            # 通过后缀名判断文件是否为excel格式
            if s == '.xlsx':
                # excel格式用例添加到用例集合，并生成一条线程，添加到线程集中
                # 通过这个if可以生成到所有case的线程
                cases.append(file)
                t = threading.Thread(target=ExcelExcutor().excute_web, args=[excel_path])
                th.append(t)
            else:
                print('该文件无法识别，文件名称：' + file)
                # pass
    # 基于线程集，调用所有线程进行启动
    '''
        第一条线程启动后，基于excel的运行需要有时间来执行
        在时间运行过程中，会产生被动等待，于此同时启动第二条线程
    '''
    for t in th:
        t.start()
    # for case in cases:
    #     print(case)
