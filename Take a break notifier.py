'''
TAKE A BREAK
'''


from plyer import notification
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon ='C:\\Users\\Dell\\Desktop\\clock.ico',
        timeout = 10,
        )



if __name__ == '__main__':
    while True:
        notifyMe("Hey Prashant, take a break now !!", "You should follow the 20-20-20 rule to keep your eyes healthy")
        time.sleep(30)

    
        
