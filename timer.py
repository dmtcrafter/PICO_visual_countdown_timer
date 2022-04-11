
import time

total_time = 10


class LED(pin):
    ON = False

    def __init__(self, pin):
        super().__init__()


Led_1 = LED(pin=4)

Led_2 = LED(pin=9)

Led_3 = LED(pin=10)

Led_4 = LED(pin=11)

running = True

total_time_1_4 = total_time / 4
total_time_2_4 = (total_time / 4) * 2
total_time_3_4 = (total_time / 4) * 3

while running:
    total_time = total_time - 1

    if total_time > 0:
        if total_time == total_time_3_4:
            Led_1.ON = False

        elif total_time == total_time_2_4:
            Led_2.ON = False

        elif total_time == total_time_1_4:
            Led_3.ON = False

    elif total_time == 0:
        ticker = 3
        while ticker < 0:
            Led_1.ON = False
            time.sleep(0.1)
            Led_1.ON = True
            time.sleep(0.1)
            Led_1.ON = False
            time.sleep(0.1)
            Led_1.ON = True
            time.sleep(0.1)
