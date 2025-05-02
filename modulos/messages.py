import pywhatkit as pwk
import time
phone_number = "+5511967596163"
message = "HELLO, WORLD!"
# Send the message
cont = 1
while cont <= 10:
    pwk.sendwhatmsg_instantly(phone_number, message)
    time.sleep(1)
