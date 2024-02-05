import numpy as np

'''This class represents an empirical distribution of drive times for a given day of the week.'''

class EmpiricalDistribution:
    def __init__(self):
        self.distribution = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": [],}
        
        for day in self.distribution:
            if day == "Saturday" or day == "Sunday":
                self.generate_distribution_constant(day)
            self.generate_distribution_rush(day)

    def addPoint(self, day: str, point: tuple):
        if point not in self.distribution[day]:
            self.distribution[day].append(point)

    def removePoint(self, day: str, point: tuple):
        if point in self.distribution[day]:
            self.distribution[day].remove(point)

    def getNumberOfPoints(self, day: str) -> int:
        return len(self.distribution[day])

    def getPoint(self, day: str, pointIndex: int) -> tuple | None:
        if len(self.distribution[day]) > pointIndex:
            return self.distribution[day][pointIndex]
        return None

    def printDistribution(self, day: str):
        for point in self.distribution[day]:
            print(f"For the minute {point[0]} the drive time is {point[1]}")

    def closest_time(self, day: str, time: int):
        if (time > self.distribution[day][-1][0]):  # If the given time is greater than the last time in the list, return None
            return None
        for i, point in enumerate(self.distribution[day]):
            if point[0] == time:
                return [point]
            if point[0] < time:
                if self.distribution[day][i + 1][0] > time:
                    return [self.distribution[day][i], self.distribution[day][i + 1]]

    def interpolate(self, day: str, time: int):
        closest_time = self.closest_time(day, time)
        if closest_time is not None:
            if closest_time[0][0] == time:
                return closest_time[0][1]
            start = closest_time[0]
            end = closest_time[1]
            proportion = (time - start[0]) / (end[0] - start[0])
            interpolated_value = start[1] + proportion * (end[1] - start[1])
            return round(interpolated_value, 2)

    def generate_distribution_constant(self, day: str):
        time_to_drive = np.random.randint(10, 60)
        num_point = np.random.randint(20, 100)
        self.addPoint(day, (0, time_to_drive))
        for _ in range(num_point):
            tmp = np.random.randint(0, 120)
            while self.distribution[day][-1][0] + tmp < 1440:
                self.addPoint(day,(self.distribution[day][-1][0] + tmp, time_to_drive - np.random.randint(-3, 3)))
                tmp = np.random.randint(0, 120)

    def generate_distribution_rush(self, day: str):
        rush_hours_morning = [i for i in range(420, 521)]
        rush_hours_afternoon = [i for i in range(900, 1021)]
        time_to_drive = np.random.randint(10, 60)
        num_point = np.random.randint(20, 100)
        self.addPoint(day, (0, time_to_drive))
        for _ in range(num_point):
            tmp = np.random.randint(0, 120)
            while self.distribution[day][-1][0] + tmp < 1440:
                if (self.distribution[day][-1][0] + tmp in rush_hours_morning 
                    or self.distribution[day][-1][0] + tmp in rush_hours_afternoon):
                    self.addPoint(day,(self.distribution[day][-1][0] + tmp,time_to_drive + np.random.randint(15, 40)))
                else:
                    self.addPoint(day,(self.distribution[day][-1][0] + tmp,time_to_drive - np.random.randint(-3, 3)))
                tmp = np.random.randint(0, 120)