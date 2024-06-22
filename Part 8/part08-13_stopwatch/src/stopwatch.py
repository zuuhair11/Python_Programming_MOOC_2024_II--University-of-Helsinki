# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    # Increment the seconds by 1, and when it gets to 60, increment the minutes by 1
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0

    def __str__(self):
        # second = str(self.seconds) if self.seconds > 9  else '0' + str(self.seconds)
        # minute = str(self.minutes) if self.minutes > 9  else '0' + str(self.minutes)
        # return '{}:{}'.format(minute, second)
        return f'{self.minutes:02}:{self.seconds:02}'


if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()
