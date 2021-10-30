import time


class TrafficLight:
    __color = "white"

    def running(self):
        while True:
            print("Traffic is red")
            time.sleep(7)
            print("Traffic is yellow")
            time.sleep(2)
            print("Traffic is green")
            time.sleep(10)


a = TrafficLight()
a.running()
