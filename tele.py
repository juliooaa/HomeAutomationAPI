import time, datetime
import RPi.GPIO as GPIO    #I need see what a fuck is this
import teleport            #Teleport is a modern security gateway for remotely accessing
from telepot.loop import MessageLoop

led = 26
now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

 #LED
GPIO.setup(led, GPIO.OUT)
GPÌO.output(led, 0) #Off initially

 #Will call the action function and this function reads the message and separate the text from it
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Received: %s' % command

#Will check for keywords and toggle the led according to the keyword. While message string is used to reply back to the user
    if 'on' in command:
        message = "Turned on"
        if 'led' in command:
            message = message + "led"
            GPIO.output(led, 1)
            telegram_bot.sendMessage {chat_id, message}

        if 'off' in command:
            message = "Turned off"
            if 'led' in command:
                message = message + "led"
                GPIO.output(led, 0)
           telegram_bot.sendMessage (chat_id, message)