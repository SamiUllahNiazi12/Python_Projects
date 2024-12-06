from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Rest is important for a healthy health.Please take a rest.",
            
            timeout = 5)  # to close it go to task manger and close python task
        time.sleep(20)
