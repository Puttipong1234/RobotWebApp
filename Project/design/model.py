import csv
from operator import itemgetter
from itertools import groupby
import os

class RobotRSA():
    
    def __init__(self,csv_path,element_type):
        # element_type : beam , column , slab , wall , etc
        # csv path in your location
        # RobotData : List data from csv (raw data for plotting)
        self.csv_path = os.path.join('Project',csv_path)
        self.element_type = element_type
        self.RobotData = list()
        self.SortedData = list()
        self.SortedDataMaxMin = list()     
        self.PlottingData = list()   
        
        with open(self.csv_path,encoding='utf-16') as infile:
            reader = csv.DictReader(infile)
            self.Regenerate_by_Type(reader)
        
        self.PlottingData = self.Group_by_LoadCase()

    
    def Regenerate_by_Type(self,reader):
                
        for i in reader:
            BarNum , Point , Case , MomentX, MomentY , MomentZ , FX , FY, FZ  = i['Bar/Point/Case'].split(' ')[1].split('/')[0] , i['Bar/Point/Case'].split(' ')[2].split('/')[0] , i['Bar/Point/Case'].split(' ')[3] , i['MX (kNm)'], i['MY (kNm)'] , i['MZ (kNm)'] , i['FX (kN)'] , i['FY (kN)'], i['FZ (kN)']
            # if str(Point).strip() == '0.50':
            #     Point = 'Middle'
            # else :
            #     Point = 'End'
            
            self.RobotData.append([BarNum , Point , Case , MomentX , MomentY , MomentZ , FX , FY ,FZ])
            
        if str(self.element_type).lower() == 'beam':
            self.SortedDataMaxMin =self.SortbyMaxMin(sort_index=4)
            self.SortedData =self.Sortby(sort_index=4)
                      
        
        elif str(self.element_type).lower() == 'column':
            self.SortedDataMaxMin =self.SortbyMaxMin(sort_index=5)   
            self.SortedData =self.Sortby(sort_index=5)            
                      
            
        else :
            self.SortedDataMaxMin =self.SortbyMaxMin()
            self.SortedData =self.Sortby()         
                      
    
            
    def Sortby(self,sort_index = 4):
        #### sort data from Robot
        # 
        new_items = []
        for BarNum, items in groupby(self.RobotData, key=itemgetter(0)):
            sorted_item = []
            for i in items:
                sorted_item.append(i)
            sorted_item.sort(key=itemgetter(sort_index))
            new_items.append(sorted_item)
        return new_items        
        
            
    def SortbyMaxMin(self,sort_index = 4):
        #### sort data from Robot
        new_items = []
        for BarNum, items in groupby(self.RobotData, key=itemgetter(0)):
            sorted_item = []
            for i in items:
                sorted_item.append(i)
            sorted_item.sort(key=itemgetter(sort_index))
            new_items.append([sorted_item[0],sorted_item[-1]])
        return new_items
    
    def Group_by_LoadCase(self):
        data = self.Sortby(2)
        res = []
        for i in data:
            in_res = []
            for Case, items in groupby(i, key=itemgetter(2)):
                in_res.append([i for i in items])
                
            res.append(in_res)
        return res


    def __repr__(self):
        return 'Calculation Result Sorted for {} Success . Please print(SortedData) to watch the result'.format(self.element_type)
            
    
    
                

    
    
        
