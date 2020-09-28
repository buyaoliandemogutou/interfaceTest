import os
import configparser
import getpathInfo

path = getpathInfo.MakePath().get_Path()#调用实例化，记得这个类返回的路径为
config_path = os.path.join(path, 'config.ini')#这句话是在path路径下再加一级
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value
    def get_mysql(self, name): #写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value
    def get_token(self,token):
        token=config.get('TOKEN', token)
        return token
    def set_token(self,token):
        try:
            config.set('TOKEN', 'token', token)
            config.write(open(config_path, "w"))
        except Exception as e:
            print(e)

if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
    ReadConfig().set_token('222')
    print(ReadConfig().get_token('token'))


