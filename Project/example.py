from design.model import RobotRSA

Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
# Column_Res = RobotRSA(csv_path='robotdata\Column.csv',element_type='column')


a = Beam_Res.SortedDataMaxMin

for i in a:
    print(i[0][0])



        
        
        
    
    
