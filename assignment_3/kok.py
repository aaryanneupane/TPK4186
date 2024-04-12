import copy
from functools import partial
from CustomerOrder import CustomerOrder
from GUI import GUI
from Printer import Printer
from Product import Product
from Robot import Robot
from Truckload import Truckload
from Warehouse import Warehouse
from Parameters import *
from tkinter import *
from WarehouseStats import WarehouseStats
from tqdm import trange

#random.seed(0) #TODO fjerne

class Simulator():
    def __init__(self):
        self.timeStep = 0
        self.warehouseStats = None
        self.p = Printer()

    def getTimeStep(self):
        return self.timeStep
    def getWarehouseStats(self):
        return self.warehouseStats
    def setTimeStep(self, timeStep : int):
        self.timeStep = timeStep
    def setWarehouseStats(self, warehouseStats : WarehouseStats):
        self.warehouseStats = warehouseStats
    
    def increaseTimeStep(self):
        self.timeStep+=1

    def runSimulation(self, xSize : int, ySize : int, numberOfRobots : int, numProductsInCatalog : int, timeStepToGoTo : int, arrivalInterval : int, truckloadSizePer5000Time : int, customerOrderSizePer5000Time : int,   displayWarehouse : bool, shouldPrint : bool):
        """returns the warehouse of the simulation, and the warehouseStats of the simulation"""
        
        if (xSize < 6 or ySize < 6):
            raise Exception("Warehouse dimension must be atleast 6 in x direction, and 6 in y direction (else the warehouse cant have a reasonable shape)")

        warehouse = Warehouse()
        self.warehouseStats = WarehouseStats(warehouse)

        rootWindow, canvas, zones = warehouse.makeWarehouseInTkinter(xSize, ySize)
        if (shouldPrint):
            self.p.printWarehouse(warehouse)

        allStorageCells = warehouse.getAllStorageCells()
        if (len(allStorageCells)*2 < numProductsInCatalog):
            raise Exception("Number of products is too bigg in comparison to shelves in warehouse, warehouse will have trouble storing so many different products, try bigger warehouse or fewer unique products")
            
        robots = self.initializeRobots(numberOfRobots, warehouse)
       
        catalog, truckloadTime, customerOrderTimes = self.initializeTruckloadsAndCustomerOrders(numProductsInCatalog, arrivalInterval, truckloadSizePer5000Time, customerOrderSizePer5000Time, shouldPrint)
        
        
        for i in trange(timeStepToGoTo): #trange so I can see how long is left of running time, from tqdm package
            #TODO egen simulatorNextTimeStep ? 
            self.addTruckloadsAndCustomerOrders(warehouse, catalog, shouldPrint, arrivalInterval, truckloadTime, customerOrderTimes, truckloadSizePer5000Time, customerOrderSizePer5000Time)
            
            if (shouldPrint):
                print("___TIMESTEP: ", i, " ____")
            warehouse.nextTimeStep(shouldPrint, self.warehouseStats)
            self.timeStep += 1

        gui = GUI(self)
        gui.createGUI(robots, canvas, zones, warehouse, rootWindow, displayWarehouse, shouldPrint, self.warehouseStats, catalog, timeStepToGoTo, arrivalInterval, truckloadTime, customerOrderTimes, truckloadSizePer5000Time, customerOrderSizePer5000Time)
 
        return warehouse, self.warehouseStats

#helper functions for running simulation:
    def initializeRobots(self, numberOfRobots : int, warehouse : Warehouse):
        robots = []
        for i in range(numberOfRobots):
            robot = Robot(f"robot{i}", warehouse)   
            robots.append(robot)
        warehouse.setRobots(robots)
        return robots

    def initializeTruckloadsAndCustomerOrders(self, numProductsInCatalog, arrivalInterval, truckloadSizePer5000Time, customerOrderSizePer5000Time, shouldPrint):
        """returns a catalog, a time for truckloads to arrive at the warehouse, and 5 times for the customerOrders to arrive at the warehouse"""
        #make sure the customerOrders are divisible by 5 (have 5 orders come in per 5000 timesteps)
        if (customerOrderSizePer5000Time%5 != 0):
            customerOrderSizePer5000Time -= customerOrderSizePer5000Time%5

        catalog = generateCatalog("catalog1", numProductsInCatalog)
        self.warehouseStats.setCatalog(catalog)
        if (shouldPrint):
            self.p.printCatalog(catalog)

        #choosing randomly the times the truckload and customerorder should come, doing 5 customerOrders and 1 truckload per 5000 timesteps
        if (customerOrderSizePer5000Time > 0):
            customerOrderTimes = []
            for i in range(5):
                customerOrderTime = random.randint(0, arrivalInterval)
                customerOrderTimes.append(customerOrderTime)
        else:
            customerOrderTimes = [-1]
        if (truckloadSizePer5000Time > 0):
            truckloadTime = random.randint(0, arrivalInterval)
        else:
            print("Cant not have any truckloads, exiting simulation")
            return None
        return catalog, truckloadTime, customerOrderTimes

    def addTruckloadsAndCustomerOrders(self, warehouse : Warehouse, catalog : Catalog, shouldPrint : bool, arrivalInterval : int, truckloadTime : int, customerOrderTimes : list, truckloadSizePer5000Time : int, customerOrderSizePer5000Time : int):
        """add truckloads and customerOrders to warehouse in intervals, also stores all the truckloads and customerOrders in a stats class, so I can see how long each order took etc"""
        if ((self.timeStep%arrivalInterval == truckloadTime and self.timeStep>5000) or (self.timeStep==0)): #just adding truckload at timestep 0 so simulation starts at timestep 0
            truckload = generateTruckLoad(f"truckload{self.timeStep}", catalog, truckloadSizePer5000Time)
            warehouse.addTruckload(truckload)
            self.warehouseStats.addTruckload(copy.deepcopy(truckload))
            self.warehouseStats.addTruckloadArrivalTime(self.timeStep)
            if (shouldPrint):
                print("________ADDED TRUCKLOAD________")
                self.p.printTruckload(truckload)
        elif (self.timeStep%arrivalInterval in customerOrderTimes):
            customerOrder = generateCustomerOrder(f"order{self.timeStep}", catalog, customerOrderSizePer5000Time//5)
            warehouse.addCustomerOrder(customerOrder)
            self.warehouseStats.addCustomerOrder(copy.deepcopy(customerOrder))
            self.warehouseStats.addCustomerOrderArrivalTime(self.timeStep)
            if (shouldPrint):
                print("_________ADDED CUSTOMERORDER___________")
                self.p.printCustomerOrder(customerOrder)