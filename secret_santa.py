import random
import smtplib
from email.mime.text import MIMEText

#import text file where you have a list of [name, email, address]
name_list = open("list.txt").readlines()

print name_list