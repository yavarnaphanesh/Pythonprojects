import ctypes
import schedule
import time


def lock_computer():
    ctypes.windll.user32.LockWorkStation()


schedule.every().day.at("21:30").do(lock_computer)

while True:
    schedule.run_pending()
    time.sleep(1)
