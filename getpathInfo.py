import os
import time

nowTime=time.strftime("%Y-%m-%d", time.localtime())
class MakePath():
    #获取当前路径
    def get_Path(self):
        path = os.path.split(os.path.realpath(__file__))[0]
        return path

    #创建保存测试结果的目录
    def get_resultpath(self,pathName):
        path=MakePath().get_Path()
        resultpath=os.path.join(path,pathName)
        resultpath=os.path.join(resultpath,nowTime)
        if os.path.exists(resultpath):
            return resultpath
        else:
            # os.mkdir(resultpath)  #路径不存在则创建,创建单个文件夹
            os.makedirs(resultpath) # 创建多层目录
            return resultpath
    #命名html文件并添加到路径
    def set_reportPath(self,reportNmae):
        reportPath=MakePath().get_resultpath()
        #reportName='report.'+nowTime+'.html'
        resultPath = os.path.join(reportPath, reportNmae)
        return resultPath

if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', MakePath().get_Path())
    print('测试路径是否OK,路径为：', MakePath().get_resultpath('result'))
    print('测试报告的路径：'+MakePath().set_reportPath(nowTime+'html'))
