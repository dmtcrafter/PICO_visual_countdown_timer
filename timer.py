
import time

led_pin_A = 4

led_pin_B = 9

led_pin_C = 10

led_pin_D = 11

total_time = 10


class LED:
    ON = False

    def __init__(self):
        super().__init__()
        self.pin_num = ''


Led_1 = LED()
Led_1.pin_num = 4

Led_2 = LED()
Led_2.pin_num = 9

Led_3 = LED()
Led_3.pin_num = 10

Led_4 = LED()
Led_4.pin_num = 11

running = True

total_time_1_4 = total_time / 4
total_time_2_4 = (total_time / 4) * 2
total_time_3_4 = (total_time / 4) * 3

while running:

    if total_time < 0:
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
