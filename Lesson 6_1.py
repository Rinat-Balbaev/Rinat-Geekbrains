from time import sleep


class TrafficLight:
    __color = ['Red', 'Amber', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Switching traffic light \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()