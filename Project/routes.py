
from Project import app
from flask import render_template , redirect, url_for


@app.route('/api/RSAData')
def RSAdata():
    from .design.model import RobotRSA
    Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
    Column_Res = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
    return(render_template('Table/Table.html',data = Beam_Res.RobotData))

@app.route('/api/PlottingData')
def PlottingData():
    from .design.model import RobotRSA
    Beam_Res = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
    Column_Res = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
    return(render_template('views/Data.html',Beam = Beam_Res.PlottingData , Column = Column_Res.PlottingData))

@app.route('/api/MaxMin')
@app.route('/api/MaxMin/<element>')
def MaxMin(element=None):
    from .design.model import RobotRSA
    if element == 'Beam':
        data = RobotRSA(csv_path='robotdata/Beam.csv',element_type='beam')
        return(render_template('Table/Table.html', data = data.SortedDataMaxMin))
    elif element == 'Column':
        data = RobotRSA(csv_path='robotdata/Column.csv',element_type='column')
        return(render_template('Table/Table.html', data = data.SortedDataMaxMin))
    else :
        return redirect(url_for('MaxMin',element='Beam'))

@app.route('/api/MaxMin/<element>/calculation')
    


@app.route('/user/Chart')
def Chart():
    return(render_template('views/Chart.html'))

@app.route('/')
@app.route('/home')
def Home():
    return(render_template('views/layout.html'))

