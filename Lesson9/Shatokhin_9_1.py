import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        while True:
            print(self.__color)
            if self.__color == 'Red':
                time.sleep(7)
                self.__color = 'Yellow'
            elif self.__color == 'Yellow':
                time.sleep(2)
                self.__color = 'Green'
            elif self.__color == 'Green':
                time.sleep(3)
                self.__color = 'Red'
#                break


MyTrafficLight = TrafficLight()
MyTrafficLight.running()
