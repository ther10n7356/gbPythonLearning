import time


class TrafficLight:

    def __init__(self):
        self.__color = "Red"

    def running(self):
        traffic_list = [self.__color]
        print("\33[31m {}" .format(self.__color))
        time.sleep(7)
        self.__color = "Yellow"
        traffic_list.append(self.__color)
        print("\33[32m {}" .format(self.__color))
        time.sleep(2)
        self.__color = "Green"
        traffic_list.append(self.__color)
        print("\33[33m {}" .format(self.__color))
        time.sleep(10)
        self.__color = "Red"
        return traffic_list


traffic_light = TrafficLight()
n = 3
my_list = ["Red", "Yellow", "Green"]
while n > 0:
    traffic_light = traffic_light.running()
    if traffic_light != my_list:
        print("Порядок режимов неверен!")
        break
    n -= 1
