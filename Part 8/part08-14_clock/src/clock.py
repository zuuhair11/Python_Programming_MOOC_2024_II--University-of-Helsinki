# Write your solution here:
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

                if self.hours == 24:
                    self.hours = 0

    def set(self, hours: int=0, minutes: int=0, seconds: int=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return '{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds)


if __name__ == '__main__':
    clock = Clock(23, 59, 55)
    clock.tick()
    clock.tick()
    clock.tick()
    clock.tick()
    clock.tick()
    clock.tick()
    print(clock)
    clock.set(12, 5)
    print(clock)
