class Time:
    def __init__(self, h, m, s):
        # save the given time
        self.h = h
        self.m = m
        self.s = s

    def hours(self):
        # return the hour part of the time
        return self.h

    def minutes(self):
        # return the minute part of the time
        return self.m

    def seconds(self):
        # return the second part of the time
        return self.s

    def totalHours(self):
        # return the time as hours. Simply return hours
        return self.hours()

    def totalMinutes(self):
        # return the time as minutes.
        # first transform hours to minutes
        return self.totalHours() * 60 + self.minutes()

    def totalSeconds(self):
        # return time as seconds
        return self.totalMinutes() * 60 + self.seconds()

    def ToString(self):
        return (f"{self.hours():02d}:{self.minutes():02d}:{self.seconds():02d}")

# Create time object
time = Time(22, 5, 0)
print(time.hours())
print(time.minutes())
print(time.seconds())
print(time.totalHours())
print(time.totalMinutes())
print(time.totalSeconds())
print(time.ToString())