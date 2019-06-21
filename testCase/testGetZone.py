from common.configHttp import RunMain
import readExcel
import paramunittest
import unittest
import common.Log

getZone=readExcel.readExcel().excel_data_list('userCase.xlsx','getZone')
log=common.Log.logger

@paramunittest.parametrized(*getZone)
class testZone(unittest.TestCase):
    def setParameters(self,casename,method,path,url,params,msg):
        self.casename=casename
        self.method=method
        self.path=path
        self.url=url
        self.params=params
        self.msg=msg

    def testcheckResult(self):
        self.checkResult()

    def checkResult(self):
        url=self.url+self.path

        result=RunMain().run_main('get',url,self.params)
        #print(result.text,self.params)
        if result.status_code == 200:
            if self.assertIn(self.msg, result.text) is False:
                log.info('断言失败:' + '实际输出=' + result.text + 'msg=' + self.msg)
        else:
            print( '请求失败，响应码：',result.status_code)



if __name__ == '__main__':
    unittest.main()