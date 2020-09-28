import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpathInfo
import readConfig as readConfig
from common.Log import MyLog
import zipfile
import time

localReadConfig = readConfig.ReadConfig()

nowTime = time.strftime("%Y-%m-%d", time.localtime())
# resultPath = getpathInfo.MakePath().set_reportPath()

class Email:
    def __init__(self):
        global host, user, password, port, sender, title, content
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        sender = localReadConfig.get_email("sender")
        mail_title = nowTime + " "+' API测试报告'
        content = localReadConfig.get_email("content")
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        # get receiver list
        for n in str(self.value).split("/"):
            self.receiver.append(n)
        self.subject = mail_title
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def get_zipfile(self,input_path, result):
        """
        对目录进行深度优先遍历
        :param input_path:
        :param result:
        :return:
        """
        files = os.listdir(input_path)
        for file in files:
            if os.path.isdir(input_path + '/' + file):
                self.get_zipfile(input_path + '/' + file, result)
            else:
                result.append(input_path + '/' + file)


    def zip_file_path(self,input_path, output_path, output_name):
        """
        压缩文件
        :param input_path: 压缩的文件夹路径
        :param output_path: 解压（输出）的路径
        :param output_name: 压缩包名称
        :return:
        """
        f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
        filelists = []
        #self.get_zipfile(input_path, filelists)
        for file in filelists:
            f.write(file)
        # 调用了close方法才会保证完成压缩
        f.close()
        return output_path + r"/" + output_name


    def config_file(self,filehtml):
        # if the file content is not null, then config the email file
        with open(filehtml, 'r') as f:
            content = f.read()
        # 设置html格式参数
        part1 = MIMEText(content, 'html', 'utf-8')
        self.msg.attach(part1)

    def check_file(self,reportpath):
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def config_html(self,resultPath):
        f = open(resultPath, 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
        mail_body = f.read()
        f.close()
        message = MIMEText(mail_body, 'html', 'utf-8')
        self.msg.attach(message)

    def send_email(self,resultPath):
        self.config_header()
        self.config_html(resultPath)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            print('The test report has send to developer by email')
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))

if __name__ == "__main__":
    reportpath1 = getpathInfo.MakePath().set_reportPath('result',nowTime+'.html')
    Email().send_email(reportpath1)