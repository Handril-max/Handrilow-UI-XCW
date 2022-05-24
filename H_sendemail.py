#py:3
#Handrilsoft
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='2311025225@qq.com'    # 发件人邮箱账号
my_pass = 'rrsabrzyakgvdiij'     # 发件人邮箱授权码，第一步得到的
my_user='2311025225@qq.com'      # 收件人邮箱账号，可以发送给自己
 
def mail():
    ret=True
    try:
        #msg=MIMEText('填写邮件内容','plain','utf-8')
        mail_msg = """
            <p>你好呀，我是梁雨虹，很高兴成为你的朋友</p>
            """
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From']=formataddr(["梁雨虹",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="嘿"                # 邮件的主题，也可以说是标题
 
        # 发件人邮箱中的SMTP服务器，端口是25
        #server=smtplib.SMTP("smtp.qq.com", 25)
        
        '''
        QQ邮箱使用下面这种方式才成功
        '''
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465，固定的，不能更改
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.set_debuglevel(1)
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(err)
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
