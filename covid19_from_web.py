"""

covid19_from_web.py
2020-09-15

"""

from datetime import date
import wget
import os

#https://covid.ourworldindata.org/data/owid-covid-data.csv

def GetCurrentDate():
    return date.today().strftime("%Y%m%d")

def GetFilename():
    return 'covid19_' + GetCurrentDate() + '.csv'

def main():
    file_name = r'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
    filename = wget.download(file_name)

    file_name = GetFilename()

    if os.path.exists(file_name):
      os.remove(file_name)

    os.rename(filename, file_name)

    print("\nCriado ficheiro: (%s)\n" % (file_name))

                            
if __name__ == '__main__':
    main()


