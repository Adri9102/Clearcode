import calendar
import io
import sys

import pandas as pd

col_specification =[(0, 12), (13, 33), (34, 54), (55, 85), (86, 111), (112, 120),(121,143),(144,159),(160,192),(193,197),(198,218)]

def group_by(stream, field,success=None):
    if stream==None:
        print("No stream")
        sys.exit(1)
    if not isinstance(stream, io.IOBase):
        print("Oops! Invalid data value, excepted stream")
        sys.exit(1)
    if (success is not None) and (not isinstance(success, bool)):
        print("Oops! Invalid filter value, excepted 'bool' or 'None'")
        sys.exit(1)
    if (field !='year') and (field !='month'):
        print("Oops! Invalid field value, excepted 'month' or 'year'")
        sys.exit(1)

    data = pd.read_fwf(stream, colspecs=col_specification, header=0,skiprows=1)

    try:
        data.columns = ["Launch","Launch Date (UTC)", "COSPAR", "PL Name","Orig PL Name","SATCAT", "LV Type", "LV S/N", "Site", "Suc", "Ref"]
        data['Launch Date (UTC)'] = pd.to_datetime(data['Launch Date (UTC)'], format='%Y %b', exact=False)
    except ValueError:
        print("Wrong data format, e.g. excepted date format %Y %b")
        sys.exit(1)
    except NameError:
        print("Wrong file structure, excepted columns")
        print("Launch |","Launch Date (UTC) |", "COSPAR", "PL Name |","Orig PL Name |","SATCAT |", "LV Type |", "LV S/N |", "Site |", "Suc |", "Ref")
        sys.exit(1)

    if success:
        data=data.loc[data['Suc'] == 'S']
    elif success==False:
        data=data.loc[data['Suc'] == 'F']

    if(field=='year'):
        result=data.groupby(data['Launch Date (UTC)'].dt.year).groups
    else:
        result=data.groupby(data['Launch Date (UTC)'].dt.month).groups

    wynik={}
    for i in result:
        if (field=='month'):
            wynik[calendar.month_abbr[(int(i))]]=result[i].size
        else:
            wynik[str(int(i))] = result[i].size
    return wynik

group_by(open('launchlog.txt'),'year')
