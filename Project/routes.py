
from Project import app
from flask import render_template


@app.route('/api/RSAData')
def RSAdata():
    from .design.model import RobotRSA
    Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
    Column_Res = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
    return(render_template('views/Data.html',Beam = Beam_Res.RobotData,Column = Column_Res.RobotData))

@app.route('/api/PlottingData')
def PlottingData():
    from .design.model import RobotRSA
    Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
    Column_Res = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
    return(render_template('views/Data.html',Beam = Beam_Res.PlottingData,Column = Column_Res.PlottingData))

@app.route('/api/MaxMin')
def MaxMin():
    from .design.model import RobotRSA
    Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
    Column_Res = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
    return(render_template('views/Data.html',Beam = Beam_Res.SortbyMaxMin,Column = Column_Res.SortbyMaxMin))


@app.route('/user/Chart')
def Chart():
    return(render_template('views/Chart.html'))

@app.route('/')
@app.route('/home')
def Home():
    return(render_template('views/layout.html'))

