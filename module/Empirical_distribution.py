import numpy as np
class EmpiricalDistribution:
    
    def __init__(self):
        self.points = []
        
    def addPoint(self, point: tuple):
        if point not in self.points:
                self.points.append(point)

    def removePoint(self, point: tuple):
         if point in self.points:
              self.points.remove(point)
    
    def getNumberOfPoints(self) -> int:
         return len(self.points)
    
    def getPoint(self, pointIndex: int) -> tuple | None:
         if len(self.points) > pointIndex:
               return self.points[pointIndex]
         return None
    
    def printDistribution(self):
         for point in self.points:
               print(f'For the minute {point[0]} the drive time is {point[1]}')

    def closest_time(self, time: int):
         if time>self.points[-1][0]: #If the given time is greater than the last time in the list, return None
              return None
         for i,point in enumerate(self.points):
              if point[0] == time:
                    return [point]
              if point[0] < time:
                   if self.points[i+1][0] > time:
                    return [self.points[i], self.points[i+1]]
    
    def interpolate(self, time):
        closest_time = self.closest_time(time)
        if closest_time is not None:
            #print(closest_time)
            if closest_time[0][0] == time:
                return closest_time[0][1]
            start = closest_time[0]
            end = closest_time[1]
            proportion = (time - start[0]) / (end[0] - start[0])
            interpolated_value = start[1] + proportion * (end[1] - start[1])
            return round(interpolated_value,2)
           
     def generate_distribution_constant(self):
         time_to_drive = np.random.randint(10, 60) 
         num_point = np.random.randint(20,100) 
         self.addPoint((0,time_to_drive)) 
         for _ in range(len(num_point)):
              self.addPoint(self.points[-1][0]+np.random.randint(0,120), time_to_drive - np.random.randint(-3,3)) 
     
     def generate_distribution_rush(self):
          rush_hours_morning = np.linspace(420, 540,1)
          rush_hours_afternoon = np.linspace(900, 1020,1)
          time_to_drive = np.random.randint(10,60)
          num_point = np.random.randint(20,100)
          self.addPoint((0,time_to_drive)) 
          for _ in range(len(num_point)):
               tmp = np.random.randint(0,120)
               if self.points[-1][0] + tmp in rush_hours_morning or self.points[-1][0] + tmp in rush_hours_afternoon:
                    self.addPoint(self.points[-1][0]+ tmp, time_to_drive - np.random.randint(15,40))
               else:
                    self.addPoint(self.points[-1][0]+tmp, time_to_drive - np.random.randint(-3,3))
          
              
              
               
               
               
    
                   
          
          


        


        
