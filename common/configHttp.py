import requests
import json
from common.Log import logger
logger = logger

class RunMain():
    def requests(self,httpMethod,url, data,headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        if httpMethod.lower()==('post'):#.upper（）小写转大写
            try:
                if isinstance(data,str):#判断数据类型，类型为str则不需要转格式
                    result = requests.post(url=url, data=data, headers=headers, verify=False)
                else:
                    result = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
                return result
            except BaseException as e:
                print("post请求出现了异常：{0}".format(e))
        elif httpMethod.lower()==('get'):
            try:
                if isinstance(data,str):
                    result = requests.get(url=url, params=data, headers=headers, verify=False)
                else:
                #数据格式转换
                    result = requests.get(url=url, params=json.dumps(data), headers=headers, verify=False)
                return result
            except Exception as e:
                print("get请求出现了异常：{0}".format(e))
                logger.exception(format(e))
        else:
            print("method值错误:",httpMethod)
            logger.info("method值错误:",httpMethod)

    # def getToken(self,result):
    #     return result.json()['loginInfo']['tokenVo']['token']
    #
    # def getStatus(self,result):
    #     return result.json()['result']['status']

    def getValue(self,response,param):
        try:
            if response.status_code != 200:
                print('请求失败：',response.status_code)
            else:
                if param.lower() == 'token':
                    return response.json()['loginInfo']['tokenVo']['token']
                elif param.lower() == 'status':
                    return response.json()['result']['status']
                elif param.lower() == 'userid':
                    return response.json()['loginInfo']['userId']
                elif param.lower() == 'message':
                    return response.json()['result']['message']
                elif param.lower() == 'targetid':
                    return response.json()['loginInfo']['targetId']
                elif param.lower() == 'userid':
                    return response.json()['loginInfo']['userId']
        except Exception as e:
            print(format(e))
            logger.info(e)

if __name__ == '__main__':
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    param = {"uniqueCode":"9f773cdde5d268c0c191000a6ded7ec9","pwd":"7c4a8d09ca3762af61e59520943dc26494f8941b","login":"18900000000","appType":"SYN_HEALTH_MED"}
    test=RunMain().requests('post','https://cloud.synwing.com:8443/health_app_v2/noAuth/users/pwd/login', param,headers=headers)
    print(test.json())
    print(RunMain().getValue(test,'targetId'))
    print(RunMain().getValue(test,'userid'))
    token=RunMain().getValue(test,'token')
    headers['Authorization']=token # 新增dict
    param1={'osType':'Android'}
    result=RunMain().requests('get','https://cloud.synwing.com:8443/health_app_v2/app/verUpdate/check/SYN_HEALTH_MED', param1, headers)
    # result=requests.get('https://cloud.synwing.com:8443/health_app_v2/app/verUpdate/check/SYN_HEALTH_MED',{"osType":"Android"},headers=token)
    print(result)
    print(result.json())



