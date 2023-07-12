import io
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
import math
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui_layout import Ui_MainWindow
from PyQt5.QtCore import QThread, QObject, pyqtBoundSignal
from PyQt5 import QtGui
import time
pd.options.mode.chained_assignment = None
# pip install pyqt5
# pyuic5 -x layout.ui -o gui_layout.py

  
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        # self.setFixedSize(800,800)
        # self.resize(1050,950)
        self.setWindowIcon(QtGui.QIcon('jbs.png'))
        
        # self.uic.pushButton_onlineMoney.clicked.connect(self.startToMakeMoney)
        self.uic.getColorRate.clicked.connect(self.GetColorRate)
        self.uic.getForecastByColor.clicked.connect(self.getForeCastByColor)
        self.uic.getBomInOrders.clicked.connect(self.getBomInOrders)
        self.uic.getPigComRate.clicked.connect(self.getPigComRate)
        self.uic.sales_Database.clicked.connect(self.sales_Database)
        self.uic.align_sales_Database.clicked.connect(self.align_sales_Database)
        self.uic.getcurrentorder.clicked.connect(self.getcurrentorder)
        self.uic.alignOrderData.clicked.connect(self.alignOrderData)
        self.uic.historyConsum.clicked.connect(self.historyConsum)
        self.uic.getIntransit.clicked.connect(self.getIntransit)
        self.uic.getChemicalStock.clicked.connect(self.getChemicalStock)
        self.uic.allthingtogether.clicked.connect(self.allthingtogether)
        self.uic.RunSolve.clicked.connect(self.RunSolve)
     
    
    def GetColorRate(self):
        try:
            sku_rate = pd.read_excel(open('D:\\GUI\\machineLearning\\JBS Planning Next 2022.xlsx','rb'), sheet_name='Orders Plan')
            sku_rate_col = sku_rate.columns.values.tolist()
            sku_rate_col = list(map(lambda x: x.strip().upper(), sku_rate_col))
            sku_rate.set_axis(sku_rate_col, axis='columns', inplace=True)
            sku_rate= sku_rate[sku_rate['S/O'].notnull()]
            # function to get the articles name
            def getArticles_full(data_df):
                match_object = re.findall(r'\w+-\w+\s(.+?)(?=\s*\d)', data_df['ART.'])
                if len(match_object)>0:
                    return match_object[0]
                else:
                    return "Can Not Match The Name"
            # sku_rate = sku_rate.apply(lambda x: x.replace({'ELLINGTON':'ELLI', 'MALDONADO':'MALD','VINTAGE':'VINT'}, regex=True))
            sku_rate['FAMILY_ARTICLES_FULL'] = sku_rate.apply(getArticles_full, axis=1)

            def getArticles(data_df):
                match_object = re.findall(r'\w+-\w\s(\w+-?\w+)', data_df['ART.'])
                if len(match_object)>0:
                    return match_object[0]
                else:
                    return "Can Not Match The Name"
            sku_rate['FAMILY_ARTICLES'] = sku_rate.apply(getArticles, axis=1)

            artType_Conditions = [
                sku_rate['ART.'].str.contains("TS "),
                sku_rate['ART.'].str.contains("RAC-"),
                sku_rate['ART.'].str.contains("SPLIT"),
                sku_rate['ART.'].str.contains("TSF"),
                ]

            artType_values = ['SPLIT','SPLIT','SPLIT','SPLIT']
            sku_rate['ART_TYPE'] = np.select(artType_Conditions, artType_values, default='TOP')

            # get neccessary column
            sku_rate = sku_rate[['FAMILY_ARTICLES', 'FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE','SF (ALREADY +15%)']]
            sku_rate = sku_rate.loc[sku_rate['SF (ALREADY +15%)'] >= 2000]
            # group the articles demand on articles name
            sku_rate_groupArtCol = pd.DataFrame({'SF.' : sku_rate.groupby(['FAMILY_ARTICLES', 'FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE'])['SF (ALREADY +15%)'].sum()}).reset_index()
            sku_rate_groupArt = pd.DataFrame({'SF.' : sku_rate.groupby(['FAMILY_ARTICLES'])['SF (ALREADY +15%)'].sum()}).reset_index()
            onePOvolumn_byArt = pd.DataFrame({'AvgOnePO' : round(sku_rate.groupby(['FAMILY_ARTICLES_FULL'])['SF (ALREADY +15%)'].mean(),0)}).reset_index()
            sku_rate = sku_rate_groupArtCol.merge(sku_rate_groupArt, how='left', on=['FAMILY_ARTICLES'])            
            sku_rate = sku_rate.merge(onePOvolumn_byArt, how='left', on=['FAMILY_ARTICLES_FULL'])
            sku_rate['RATE'] = round(sku_rate['SF._x']/sku_rate['SF._y'],3)
            
            # sku_rate.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\sku_rate.csv")
            io.StringIO(sku_rate.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\sku_rate.csv",index=False))
            # sku_rate.to_csv(f"D:\\GUI\\machineLearning\\Database\\sku_rate.csv")
            io.StringIO(sku_rate.to_csv(f"D:\\GUI\\machineLearning\\Database\\sku_rate.csv",index=False))            
            self.uic.lineEdit_showColorRate.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')
        except Exception as e:
            self.uic.lineEdit_showColorRate.setText(f'{e}')
            pass
        
    def getForeCastByColor(self):
        try:
            # CHECK IF ARTICLES IN SALES ALREADY PRODUCED
            # get sales forecast, strip and upercase column lables
            salesData = pd.read_csv('D:\\GUI\\machineLearning\\salesForecast.csv', encoding='cp1252')
            sku_rate = pd.read_csv('D:\\GUI\\machineLearning\\Database\\sku_rate.csv', encoding='cp1252')
            salesData_col = salesData.columns.values.tolist()
            salesData_col = list(map(lambda x: x.strip().upper(), salesData_col))
            salesData.set_axis(salesData_col, axis='columns', inplace=True)

            # upper case and check if articles in Sales are in database
            months = salesData.columns.values.tolist()[1:]
            salesData['FAMILY_ARTICLES'] = salesData['FAMILY_ARTICLES'].apply(lambda x: x.upper())
            sale_listArt = salesData['FAMILY_ARTICLES'].tolist()
            sku_rate_listArt = sku_rate['FAMILY_ARTICLES'].tolist()
            salesArt_NOTin_Artlist = [i for i in sale_listArt if i not in sku_rate_listArt]

            # GET SALES FORECAST BY COLOR
            salesForecast = sku_rate.merge(salesData, how='left', on=['FAMILY_ARTICLES'])
            

            # get volumn sales for each color
            months = list(map(lambda x: x.strip().upper(), months))
            for mth in months:
                salesForecast[f'{mth}_SF.'] = round(salesForecast[f'{mth}']*salesForecast['RATE'],0)
            
            # salesForecast.to_csv(f'D:\\GUI\\machineLearning\\RunSolveFile\\test.csv',index=False)          
            
            # sort new column
            sales_col_sort = ['FAMILY_ARTICLES','FAMILY_ARTICLES_FULL','COLOR','ART_TYPE','AvgOnePO','RATE']
            for mth in months:
                sales_col_sort.append(f'{mth}_SF.')
            salesForecast = salesForecast[salesForecast.columns.intersection(sales_col_sort)]

            # asign back to original column name
            sales_col_srt = ['FAMILY_ARTICLES','FAMILY_ARTICLES_FULL', 'COLOR','ART_TYPE','AvgOnePO','RATE']
            for mth in months:
                sales_col_srt.append(mth)
            salesForecast.set_axis(sales_col_srt, axis='columns', inplace=True)

            months_forecast = salesForecast.columns.values.tolist()[-3:]
            salesForecast['monthlyFORECAST'] = round((salesForecast[f'{months_forecast[0]}']+salesForecast[f'{months_forecast[1]}']+salesForecast[f'{months_forecast[2]}'])/3,0)
            salesForecast['SetupTimes'] = round(salesForecast['monthlyFORECAST']/salesForecast['AvgOnePO'],3)
            salesForecast= salesForecast[salesForecast['monthlyFORECAST'].notnull()]
            salesForecast= salesForecast[salesForecast['SetupTimes'].notnull()]
            salesForecast = salesForecast[['FAMILY_ARTICLES_FULL','COLOR','ART_TYPE','SetupTimes','monthlyFORECAST']]
            salesForecast = salesForecast.apply(lambda x: x.replace({'ELLINGTON':'ELLI', 'MALDONADO':'MALD','VINTAGE':'VINT'}, regex=True))
            salesForecast = salesForecast.apply(lambda x: x.replace({'MALD SOFT':'MALD SO', 'VINT DULL':'VINT DU', 'VINT SHEEN':'VINT SHE', 'VINT SOFT':'VINT SO', 'VINT K TT SOFT':'VINT K TT SO', 'BALI \(PC\)':'BALI [PC]'}, regex=True))
            # salesForecast.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\salesForecastColorBreakdown.csv",index=False)
            io.StringIO(salesForecast.to_csv(f'D:\\GUI\\machineLearning\\RunSolveFile\\salesForecastColorBreakdown.csv',index=False))
            # salesForecast.to_csv(f"D:\\GUI\\machineLearning\\Database\\salesForecast.csv",index=False)
            io.StringIO(salesForecast.to_csv(f'D:\\GUI\\machineLearning\\Database\\salesForecast.csv',index=False))
            self.uic.lineEdit_getForecastByColor.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")} Missed: {salesArt_NOTin_Artlist}')
        except Exception as e:
            self.uic.lineEdit_getForecastByColor.setText(f'{e}')
            pass
        
    

    def getBomInOrders(self):
        try:
            # PUT BOM INFORMATION IN HORIZONTAL
            data = pd.read_excel(open('D:\\GUI\\machineLearning\\CONTROL BOM.xlsx','rb'), sheet_name='DATA')
            data_colorCode = data.loc[(data['Material type descr.'] == 'WIP FINISHED')]
            data_mixture = data.loc[(data['Material type descr.'] == 'MIXTURES AND FORMULATIONS')]
            data_mixture = data_mixture[['Material', 'Material Description','Component', 'Component Description', 'Component quantity']]
            # data_colorCode = data.loc[~(data['Material type descr.'] == 'WIP FINISHED')]
            def getArticles(data_df):
                match_object = re.findall(r'\w+-\w+\s(.+?)(?=\s*\d)', data_df['Material Description'])
                if len(match_object)>0:
                    return match_object[0]
                else:
                    return "Can Not Match The Name"
                
            def getColorCode(data_df):
                match_object = re.findall(r'\((\d+)\)', data_df['Material Description'])
                if len(match_object)>0:
                    return match_object[0]
                else:
                    return "Can Not Match The Name"
                
            data_colorCode['colorCode'] = data_colorCode.apply(getColorCode, axis=1)
            data_colorCode['FAMILY_ARTICLES_FULL'] = data_colorCode.apply(getArticles, axis=1)

            artType_Conditions = [
                data_colorCode['Material Description'].str.contains("TS "),
                data_colorCode['Material Description'].str.contains("RAC-"),
                data_colorCode['Material Description'].str.contains("SPLIT"),
                data_colorCode['Material Description'].str.contains("TSF"),
                ]
                
            artType_values = ['SPLIT','SPLIT','SPLIT','SPLIT']
            data_colorCode['ART_TYPE'] = np.select(artType_Conditions, artType_values, default='TOP')

            data_colorCode = data_colorCode.loc[~(data_colorCode['colorCode'] == 'Can Not Match The Name')]
            data_colorCode.drop_duplicates(subset=['FAMILY_ARTICLES_FULL', 'Component', 'colorCode', 'ART_TYPE'], keep='first', inplace=True)

            data_colorCode = data_colorCode.merge(data_mixture, how='left', left_on=['Component'], right_on='Material')
            data_colorCode= data_colorCode[data_colorCode['Component Description_y'].notnull()]
            data_colorCode = data_colorCode.drop(['Material_y', 'Material Description_y'], axis=1)

            data_colorCode.set_axis(['Material', 'Material Description', 'BOM status', 'Alternative BOM',
                'Item Category', 'Item Number', 'Component',
                'Component Description', 'Component quantity', 'Base quantity',
                'Material type descr.', 'Created on', 'colorCode', 'FAMILY_ARTICLES_FULL', 'ART_TYPE','Componenty',
                'Component Descriptiony', 'Component quantityy'], axis='columns', inplace=True)

            data_formulation_base = data_colorCode[data_colorCode["Component Descriptiony"].str.contains("FR PIN TBH")]
            data_formulation_base = data_formulation_base.merge(data_mixture, how='left', left_on=['Componenty'], right_on='Material')
            data_formulation_base = data_formulation_base.drop(['Componenty', 'Component Descriptiony','Component quantityy','Material_y','Material Description_y'], axis=1)
            data_formulation_base.set_axis(['Material', 'Material Description', 'BOM status', 'Alternative BOM',
                'Item Category', 'Item Number', 'Component',
                'Component Description', 'Component quantity', 'Base quantity',
                'Material type descr.', 'Created on', 'colorCode', 'FAMILY_ARTICLES_FULL', 'ART_TYPE','Componenty',
                'Component Descriptiony', 'Component quantityy'], axis='columns', inplace=True)

            all_formulationData = pd.concat([data_colorCode, data_formulation_base], ignore_index=True)
            all_formulationData = all_formulationData[~all_formulationData["Component Descriptiony"].str.contains("FR PIN TBH")]
            # all_formulationData.to_csv(f"C:\\Users\\danglc\\Desktop\\machineLearning\\all_formulationData.csv")

            # adding Gam per sf to database
            G_sf_Conditions = [
                all_formulationData['Component Description'].str.contains("WASH OFF"),
                all_formulationData['Component Description'].str.contains("KE TIPSHINE"),
                all_formulationData['Component Description'].str.contains(" FI WA "),
                all_formulationData['Component Description'].str.contains("FI NI DECO"),
                all_formulationData['Component Description'].str.contains(" PB "),
                all_formulationData['Component Description'].str.contains(" EMU "),
                all_formulationData['Component Description'].str.contains(" CC "),
                all_formulationData['Component Description'].str.contains(" EF "),    
                all_formulationData['Component Description'].str.contains(" TA "),
                all_formulationData['Component Description'].str.contains(" BC "),
                all_formulationData['Component Description'].str.contains(" KE "),
                all_formulationData['Component Description'].str.contains(" FS "),
                all_formulationData['Component Description'].str.contains(" FI NI "),    
                all_formulationData['Component Description'].str.contains(" DYE "),
                all_formulationData['Component Description'].str.contains(" AGG "),    
                all_formulationData['Component Description'].str.contains(" WAX "),
                all_formulationData['Component Description'].str.contains(" SPOT "),
                all_formulationData['Component Description'].str.contains(" FI VINT ")
                ]
                
            G_sf_values = [0.9,0.9,5.5,10,4,4,15,7,3.5,18,0.9,4,10,6.5,10,7,3,10]
            all_formulationData['G_sf'] = np.select(G_sf_Conditions, G_sf_values)
            pigments_list = ['ISOLAC', 'OPERA', 'OXY FINE', 'OXY CAR', 'CONTEX', 'SAMIANIL']
            all_formulationData['PIGCOM'] = all_formulationData['Component Descriptiony'].apply(lambda column: 'PIGMENT' if any(pigment in column for pigment in pigments_list) else 'COMPOUND' )

            all_formulationData.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\all_formulationData.csv")
            all_formulationData.to_csv(f"D:\\GUI\\machineLearning\\Database\\all_formulationData.csv")
            self.uic.lineEdit_getBomInOrder.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')
        except Exception as e:
            self.uic.lineEdit_getBomInOrder.setText(f'{e}')
            pass
    
    def getPigComRate(self):
        try:
            # GET RATE FOR PIGMENTS and COMPOUND
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            all_formulationData = all_formulationData.loc[:,~all_formulationData.columns.str.match("Unnamed")]
            pigcom_total = pd.DataFrame({'TOTAL' : all_formulationData.groupby(['Component Description', 'PIGCOM'])['Component quantityy'].sum()}).reset_index()
            pigments_total = pigcom_total.loc[pigcom_total['PIGCOM'] == 'PIGMENT']
            compound_total = pigcom_total.loc[pigcom_total['PIGCOM'] == 'COMPOUND']
            pigcom_Rate = compound_total.merge(pigments_total, how='left', on=['Component Description'])
            pigcom_Rate['PIGCOM_rate'] = round((pigcom_Rate['TOTAL_x'] - pigcom_Rate['TOTAL_y'])/pigcom_Rate['TOTAL_x'],4)
            pigcom_Rate = pigcom_Rate[['Component Description', 'PIGCOM_rate']]
            all_formulationData = all_formulationData.merge(pigcom_Rate, how='left', on=['Component Description'])
            pigcom_cond = [
                (all_formulationData['PIGCOM'] == 'PIGMENT'),
                (all_formulationData['PIGCOM'] == 'COMPOUND'),]
            pigcom_choices = [1, all_formulationData['PIGCOM_rate']]
            all_formulationData['PIGCOM_RATE'] = np.select(pigcom_cond, pigcom_choices, default=np.nan)
            # fill all with 1
            all_formulationData[['PIGCOM_RATE']] = all_formulationData[['PIGCOM_RATE']].fillna(1)
            all_formulationData = all_formulationData.drop(['PIGCOM_rate'], axis=1)
            all_formulationData = all_formulationData.astype({'colorCode':'float'})
            # all_formulationData.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\all_formulationDataWithRatePIGCOM.csv")
            io.StringIO(all_formulationData.to_csv(f'D:\\GUI\\machineLearning\\RunSolveFile\\all_formulationDataWithRatePIGCOM.csv',index=False))
            # all_formulationData.to_csv(f"D:\\GUI\\machineLearning\\Database\\all_formulationDataWithRatePIGCOM.csv")
            io.StringIO(all_formulationData.to_csv(f'D:\\GUI\\machineLearning\\Database\\all_formulationDataWithRatePIGCOM.csv',index=False))
            all_formulationData.to_csv(f"D:\\GUI\\machineLearning\\Database\\all_formulationData.csv")
            self.uic.lineEdit_getPigComRate.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')
        except Exception as e:
            self.uic.lineEdit_getPigComRate.setText(f'{e}')
            pass
    
    def lstNoDuplication(self, x):
        return list(dict.fromkeys(x))
    
    def sales_Database(self):
        try:
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            all_formulationData = all_formulationData.loc[:,~all_formulationData.columns.str.match("Unnamed")]
            salesForecast = pd.read_csv('D:\\GUI\\machineLearning\\Database\\salesForecast.csv', encoding='cp1252')
            salesForecast = salesForecast.loc[:,~salesForecast.columns.str.match("Unnamed")]
            # CHECK IF ARTICLES IN SALES FORECAST LIST CONTAINED IN DATABASE


            sale_listArt = salesForecast['FAMILY_ARTICLES_FULL'].tolist()
            data_listArt = all_formulationData['FAMILY_ARTICLES_FULL'].tolist()

            sale_listArt = self.lstNoDuplication(sale_listArt)
            data_listArt = self.lstNoDuplication(data_listArt)
            missedlist = [i for i in sale_listArt if i not in data_listArt]
            self.uic.lineEdit_sale_Database.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')
            self.uic.lineEdit_missedArticles.setText(f'missed Articles: {missedlist}')
        except Exception as e:
            self.uic.lineEdit_sale_Database.setText(f'{e}')
            pass

    
    def matcher(self, col, missArt_lst):    
        for i in missArt_lst:
            if col.upper().str.contains(i.upper()).any():
                return i
        else:
            return col
    def align_sales_Database(self):
        try:
            salesForecast = pd.read_csv('D:\\GUI\\machineLearning\\Database\\salesForecast.csv', encoding='cp1252')
            salesForecast = salesForecast.loc[:,~salesForecast.columns.str.match("Unnamed")]
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            all_formulationData = all_formulationData.loc[:,~all_formulationData.columns.str.match("Unnamed")]
            # CORRECTION ON THE ARTICLE NAME IF IT MISMATCH COMPARING TO DATABASE ARTICLE NAME
            missArt_lst = self.uic.lineEdit_alignSale_Database.text()
            missArt_lst = missArt_lst.split(',')                  
            salesForecast['FAMILY_ARTICLES_FULL'] = salesForecast['FAMILY_ARTICLES_FULL'].apply(lambda x: self.matcher(x,missArt_lst))  
            salesForecast.to_csv(f"D:\\GUI\\machineLearning\\Database\\salesForecast.csv")
            
            sale_listArt = salesForecast['FAMILY_ARTICLES_FULL'].tolist()
            data_listArt = all_formulationData['FAMILY_ARTICLES_FULL'].tolist()

            sale_listArt = self.lstNoDuplication(sale_listArt)
            data_listArt = self.lstNoDuplication(data_listArt)
            missedlist = [i for i in sale_listArt if i not in data_listArt]          
            self.uic.lineEdit_alignSale_Database_1.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")} missed Articles: {missedlist}')            
        except Exception as e:
            self.uic.lineEdit_alignSale_Database_1.setText(f'{e}')

    def getcurrentorder(self):
        try:
            # CURRENT SALES ORDER INFACTORY
            # curretnOrders = pd.read_excel(open('L:\\PLANNING\\Lê Tín\\BACK-UP\\JBS Planning Next 2022.xlsx','rb'), sheet_name='Orders Plan')
            curretnOrders = pd.read_excel(open('D:\\GUI\\machineLearning\\JBS Planning Next 2023.xlsx','rb'), sheet_name='Orders Plan')
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            curretnOrders_col = curretnOrders.columns.values.tolist()
            curretnOrders_col = list(map(lambda x: x.strip().upper(), curretnOrders_col))
            curretnOrders.set_axis(curretnOrders_col, axis='columns', inplace=True)
            # get out all the NaN from Sales Order Columns
            curretnOrders= curretnOrders[curretnOrders['S/O'].notnull()]

            # get three days ago timeline
            fivedayDaysAhead = datetime.now() + timedelta(days=2)

            # function to get the articles name
            def getArticles(data_df):
                match_object = re.findall(r'\w+-\w+\s(.+?)(?=\s*\d)', data_df['ART.'])
                if len(match_object)>0:
                    return match_object[0]
                else:
                    return "Can Not Match The Name"
            curretnOrders['FAMILY_ARTICLES_FULL'] = curretnOrders.apply(getArticles, axis=1)

            # get articles type TOP and Split
            artType_Conditions = [
                curretnOrders['ART.'].str.contains("TS "),
                curretnOrders['ART.'].str.contains("RAC-"),
                curretnOrders['ART.'].str.contains("SPLIT"),
                curretnOrders['ART.'].str.contains("TSF"),
                ]
                
            artType_values = ['SPLIT','SPLIT','SPLIT','SPLIT']
            curretnOrders['ART_TYPE'] = np.select(artType_Conditions, artType_values, default='TOP')

            # get neccessary column
            curretnOrders = curretnOrders[['FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE', 'SF (ALREADY +15%)','DE.DATE']]

            # convert to datetime
            curretnOrders['DE.DATE'] = pd.to_datetime(curretnOrders['DE.DATE'], dayfirst=True, errors='coerce')

            # fill all NaT to current time
            curretnOrders[['DE.DATE']] = curretnOrders[['DE.DATE']].fillna(f'{datetime.now()}')

            # filter data from 3days ago onwards
            curretnOrders = curretnOrders.loc[curretnOrders['DE.DATE']>fivedayDaysAhead]

            # group the articles demand on articles name
            curretnOrders = pd.DataFrame({'CurrentOrders' : curretnOrders.groupby(['FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE'])['SF (ALREADY +15%)'].sum()}).reset_index()
            curretnOrders = curretnOrders.apply(lambda x: x.replace({'ELLINGTON':'ELLI', 'MALDONADO':'MALD','VINTAGE':'VINT', 'EXPRESSE':'EXPRESS', 'NEW PRESTIGE':'NEW-PRESTIGE','NEW RESTIGE':'NEW-PRESTIGE'}, regex=True))
            curretnOrders = curretnOrders.apply(lambda x: x.replace({'MALD SOFT':'MALD SO', 'VINT DULL':'VINT DU', 'VINT SHEEN':'VINT SHE', 'VINT SOFT':'VINT SO', 'SC WASH OFF AUTO':'WASH-OFF SC AUTO', 'SC WASH OFF MALD':'WASH-OFF SC MALD', 'SC WASH OFF MALD TS':'WASH-OFF SC MA TS', 'VINT K TT SOFT':'VINT K TT SO', 'BALI \(PC\)':'BALI [PC]'}, regex=True))
            curretnOrders = curretnOrders.apply(lambda x: x.replace({'WASH-OFF SC MALD TS':'WASH-OFF SC MA TS'}, regex=True))
            # Check if articles in sale  list in database
            def lstNoDuplication(x):
                return list(dict.fromkeys(x))

            orders_listArt = curretnOrders['FAMILY_ARTICLES_FULL'].tolist()
            data_listArt = all_formulationData['FAMILY_ARTICLES_FULL'].tolist()

            orders_listArt = lstNoDuplication(orders_listArt)
            data_listArt = lstNoDuplication(data_listArt)
            missedLst = [i for i in orders_listArt if i not in data_listArt]
            self.uic.lineEdit_getcurrentorder.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')
            self.uic.lineEdit_missedArticleOrdervsData.setText(f' missed Articles: {missedLst}')
            curretnOrders.to_csv(f"D:\\GUI\\machineLearning\\Database\\curretnOrders.csv")         
        except Exception as e:
            self.uic.lineEdit_getcurrentorder.setText(f'{e}')
    def alignOrderData(self):
        try:
            curretnOrders = pd.read_csv('D:\\GUI\\machineLearning\\Database\\curretnOrders.csv', encoding='cp1252')
            curretnOrders = curretnOrders.loc[:,~curretnOrders.columns.str.match("Unnamed")]
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            all_formulationData = all_formulationData.loc[:,~all_formulationData.columns.str.match("Unnamed")]
            # CORRECTION ON THE ARTICLE NAME IF IT MISMATCH COMPARING TO DATABASE ARTICLE NAME
            missArt_lst = self.uic.lineEdit_alignOrder_Database.text()
            missArt_lst = missArt_lst.split(',')                  
            curretnOrders['FAMILY_ARTICLES_FULL'] = curretnOrders['FAMILY_ARTICLES_FULL'].apply(lambda x: self.matcher(x,missArt_lst))  
            curretnOrders.to_csv(f"D:\\GUI\\machineLearning\\Database\\curretnOrders.csv")
            def lstNoDuplication(x):
                return list(dict.fromkeys(x))

            orders_listArt = curretnOrders['FAMILY_ARTICLES_FULL'].tolist()
            data_listArt = all_formulationData['FAMILY_ARTICLES_FULL'].tolist()

            orders_listArt = lstNoDuplication(orders_listArt)
            data_listArt = lstNoDuplication(data_listArt)
            missedLst = [i for i in orders_listArt if i not in data_listArt]          
            self.uic.lineEdit_alignOrder_Database1.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")} missed Articles: {missedLst}')            
        except Exception as e:
            self.uic.lineEdit_alignOrder_Database1.setText(f'{e}')

    def historyConsum(self):
        try:
            # GET HISTORYCONSUMPTION
            historyConsumption = pd.read_csv('D:\\GUI\\machineLearning\\historyConsumption.csv', encoding='cp1252')
            historyConsumption['Mon_Year'] = historyConsumption['Mon_Year'].apply(lambda x: x.upper())
            curConsumption = pd.read_excel(open('D:\\GUI\\machineLearning\\curConsumption.xlsx','rb'), sheet_name='Sheet1')
            curConsumption = curConsumption.loc[:,['Material','Consumption on Current Month']]
            curConsumption= curConsumption[curConsumption['Material'].notnull()]
            curConsumption.to_csv(f"D:\\GUI\\machineLearning\\Database\\curConsumption.csv")

            # Functions to get last 6 months as format in data
            def convertNumToMonth(num):
                if num == -5:
                    mth= 'JUL'
                if num == -4:
                    mth= 'AUG'
                if num == -3:
                    mth= 'SEP'
                if num == -2:
                    mth= 'OCT'
                if num == -1:
                    mth= 'NOV'
                if num == 0:
                    mth= 'DEC'
                if num == 1:
                    mth= 'JAN'
                if num == 2:
                    mth= 'FEB'
                if num == 3:
                    mth= 'MAR'
                if num == 4:
                    mth= 'APR'
                if num == 5:
                    mth= 'MAY'
                if num == 6:
                    mth= 'JUN'
                if num == 7:
                    mth= 'JUL'
                if num == 8:
                    mth= 'AUG'
                if num == 9:
                    mth= 'SEP'
                if num == 10:
                    mth= 'OCT'
                if num == 11:
                    mth= 'NOV'
                if num == 12:
                    mth= 'DEC'
                return mth
            def getLast6months(tuday):
                mth = tuday.month
                yr = tuday.year
                m1,m2,m3,m4,m5,m6 = mth-1, mth-2, mth-3, mth-4, mth-5,mth-6
                lst6mth = [m1,m2,m3,m4,m5,m6]
                lst6mth = sorted(lst6mth, reverse=False)
            #     return lst6mth
                lstyr =[]
                for mth in lst6mth:
                    mth_intext = convertNumToMonth(mth)
                    if mth > 0:
                        yrConvert=str(yr)[-2:]
                    else:
                        yrConvert = str(yr-1)[-2:]
                    lstyr.append(f'{mth_intext}_{yrConvert}')
                return lstyr
            # get last 6 month Consumption
            last_6mth = getLast6months(date.today())
            last_3mth = last_6mth[-3:]

            lst3mth_Consumption = historyConsumption[historyConsumption['Mon_Year'].isin(last_3mth)]
            lst6mth_Consumption = historyConsumption[historyConsumption['Mon_Year'].isin(last_6mth)]

            # get last 6 month consumption as horizontal view
            lst6mth_Consumption_horizontal = pd.pivot_table(lst6mth_Consumption, index= ['Material', 'Component_Description'], columns=['Mon_Year'], values=['Consumption'], aggfunc = 'sum', fill_value = 0 )
            lst6mth_Consumption_horizontal.columns = lst6mth_Consumption_horizontal.columns.droplevel(0)
            lst6mth_Consumption_horizontal = lst6mth_Consumption_horizontal.reset_index().rename_axis(None, axis=1)
            lst = ["Material", "Component_Description"]
            for col in last_6mth:
                lst.append(col)
            lst6mth_Consumption_horizontal = lst6mth_Consumption_horizontal[lst]
            lst6mth_Consumption_horizontal.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\History_Consumption.csv")
            lst6mth_Consumption_horizontal.to_csv(f"D:\\GUI\\machineLearning\\Database\\History_Consumption.csv")

            #Get chemical MonthlyConsumption 6 month average
            col_list = lst6mth_Consumption[["Mon_Year"]]
            col_list = col_list.drop_duplicates(subset= ['Mon_Year'], keep='first', inplace=False)
            col_list_count = col_list['Mon_Year'].count()
            hisConsumption = pd.DataFrame({'monthly Consumption (6months)' : round(lst6mth_Consumption.groupby(['Material'])['Consumption'].sum()/col_list_count,0)}).reset_index()
            hisConsumption.to_csv(f"D:\\GUI\\machineLearning\\Database\\hisConsumption.csv")
            #Get chemical MonthlyConsumption 3 month average
            col_list3month = lst3mth_Consumption[["Mon_Year"]]
            col_list3month = col_list3month.drop_duplicates(subset= ['Mon_Year'], keep='first', inplace=False)
            col_list3month_count = col_list3month['Mon_Year'].count()
            hisConsumption_3month = pd.DataFrame({'monthly Consumption (3months)' : round(lst3mth_Consumption.groupby(['Material'])['Consumption'].sum()/col_list3month_count,0)}).reset_index()
            hisConsumption_3month.to_csv(f"D:\\GUI\\machineLearning\\Database\\hisConsumption_3month.csv")
            self.uic.lineEdit_historyConsum.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')            
        except Exception as e:
            self.uic.lineEdit_historyConsum.setText(f'{e}')
    
    def getIntransit(self):
        try:
            # GET UPDATE FOR INTRANSIT
            ETA_update = pd.read_excel(open('D:\\GUI\\machineLearning\\Chemical planning 2023.xls','rb'), sheet_name='Sheet1')

            # get out all the NaN from Code
            ETA_update = ETA_update[ETA_update['Code'].notnull()]

            # get columns list
            ETA_columns = ETA_update.columns.tolist()

            # trim all columns and assign back to dataframe
            ETA_columns = [col.strip() for col in ETA_columns]
            ETA_update.set_axis(ETA_columns, axis=1, inplace=True)
            ETA_update = ETA_update.loc[ETA_update['Shoe/Fur']=='Fur']

            # change data type of "ETA Vietnam PORT" to string
            ETA_update = ETA_update.astype({'ETA Vietnam PORT':'str', 'Shipping Qty':'str'})

            # combine quantity with ETA
            ETA_update['toVNport'] = ETA_update[["ETA Vietnam PORT", "Shipping Qty"]].apply("::".join, axis=1)

            # convert back Shipping Qty back to float
            ETA_update = ETA_update.astype({'Shipping Qty':'float'})

            # combine all ETA in one row and group all same chemical
            ETA_quantity = ETA_update.groupby(['Code'])['Shipping Qty'].sum().reset_index()
            ETA_shipment = ETA_update.groupby(['Code'])['toVNport'].apply(lambda x: '|||'.join(x)).reset_index()

            # combine all ETA, quantity for one chemical
            ETA_allCombine = ETA_quantity.merge(ETA_shipment, how='left', on=['Code'])
            ETA_allCombine.set_axis(['Material','Intransit', 'Intransit_Notes'], axis=1, inplace=True)
            ETA_allCombine.to_csv(f"D:\\GUI\\machineLearning\\Database\\ETA_allCombine.csv")
            self.uic.lineEdit_getIntransit.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')            
        except Exception as e:
            self.uic.lineEdit_getIntransit.setText(f'{e}')
    
    def getChemicalStock(self):
        try:
            # GET CHEMICAL STOCK
            chemicalStock = pd.read_csv('D:\\GUI\\machineLearning\\chemicalStock.csv', encoding='cp1252')
            #Get chemical stock
            chemicalStock = chemicalStock[['Material', 'Storage Location', 'Long Material Description', 'Unrestricted']]
            chemicalStock = chemicalStock[chemicalStock['Material'] < 1700000]
            chemicalStock_CH01 = chemicalStock[chemicalStock['Storage Location'] == 'CH01']
            chemicalStock_CH01 = pd.DataFrame({'Stock_CH01' : round(chemicalStock_CH01.groupby(['Material'])['Unrestricted'].sum(),0)}).reset_index()
            chemicalStock_CH10 = chemicalStock[chemicalStock['Storage Location'] == 'CH10']
            chemicalStock_CH10 = pd.DataFrame({'Stock_CH10' : round(chemicalStock_CH10.groupby(['Material'])['Unrestricted'].sum(),0)}).reset_index()

            chemicalStock_CH01.to_csv(f"D:\\GUI\\machineLearning\\Database\\chemicalStock_CH01.csv")
            chemicalStock_CH10.to_csv(f"D:\\GUI\\machineLearning\\Database\\chemicalStock_CH10.csv")
            self.uic.lineEdit_getChemicalStock.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')            
        except Exception as e:
            self.uic.lineEdit_getChemicalStock.setText(f'{e}')
    
    def allthingtogether(self):
        try:
            # COMBINE ALL THINGS TOGETHER
            # MERGE SALES FORECAST TO OUR DATABASE
            all_formulationData = pd.read_csv('D:\\GUI\\machineLearning\\Database\\all_formulationData.csv', encoding='cp1252')
            all_formulationData = all_formulationData.loc[:,~all_formulationData.columns.str.match("Unnamed")]
            salesForecast = pd.read_csv('D:\\GUI\\machineLearning\\Database\\salesForecast.csv', encoding='cp1252')
            salesForecast = salesForecast.loc[:,~salesForecast.columns.str.match("Unnamed")]
            curretnOrders = pd.read_csv('D:\\GUI\\machineLearning\\Database\\curretnOrders.csv', encoding='cp1252')
            curretnOrders = curretnOrders.loc[:,~curretnOrders.columns.str.match("Unnamed")]
            ETA_allCombine = pd.read_csv('D:\\GUI\\machineLearning\\Database\\ETA_allCombine.csv', encoding='cp1252')
            ETA_allCombine = ETA_allCombine.loc[:,~ETA_allCombine.columns.str.match("Unnamed")]
            chemicalStock_CH01 = pd.read_csv('D:\\GUI\\machineLearning\\Database\\chemicalStock_CH01.csv', encoding='cp1252')
            chemicalStock_CH01 = chemicalStock_CH01.loc[:,~chemicalStock_CH01.columns.str.match("Unnamed")]
            chemicalStock_CH10 = pd.read_csv('D:\\GUI\\machineLearning\\Database\\chemicalStock_CH10.csv', encoding='cp1252')
            chemicalStock_CH10 = chemicalStock_CH10.loc[:,~chemicalStock_CH10.columns.str.match("Unnamed")]
            hisConsumption = pd.read_csv('D:\\GUI\\machineLearning\\Database\\hisConsumption.csv', encoding='cp1252')
            hisConsumption = hisConsumption.loc[:,~hisConsumption.columns.str.match("Unnamed")]
            hisConsumption_3month = pd.read_csv('D:\\GUI\\machineLearning\\Database\\hisConsumption_3month.csv', encoding='cp1252')
            hisConsumption_3month = hisConsumption_3month.loc[:,~hisConsumption_3month.columns.str.match("Unnamed")]
            curConsumption = pd.read_csv('D:\\GUI\\machineLearning\\Database\\curConsumption.csv', encoding='cp1252')
            curConsumption = curConsumption.loc[:,~curConsumption.columns.str.match("Unnamed")]
            # Chemical Setup
            setup_chemical = pd.read_excel(open('D:\\GUI\\machineLearning\\dataSetup_Rao.xlsx','rb'), sheet_name='setup')
            setup_chemical = setup_chemical.loc[:,~setup_chemical.columns.str.match("Unnamed")]
            setup_chemical = setup_chemical[['MATERIAL DESCRIPTION', 'COMPONENT DESCRIPTION', 'ART_TYPE','Gam_SF','Setup']]
            setup_chemical.columns = ['Material Description','Component Description','ART_TYPE', 'Gam_SF','Setup']
            
            all_formulationData = all_formulationData.merge(setup_chemical, how='left', on=['Material Description','Component Description','ART_TYPE'])
            formulation_Forecast = all_formulationData.merge(salesForecast, how='left', left_on=['FAMILY_ARTICLES_FULL', 'colorCode', 'ART_TYPE'], right_on=['FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE'])
            # formulation_Forecast.to_csv(f"C:\\Users\\danglc\\Desktop\\machineLearning\\all_formulationDataForecast.csv")

            # MERGE CURRENT SALES ORDERS TO OUR DATABASE, SALES FORECAST
            formulation_Forecast_CurrentOrder = formulation_Forecast.merge(curretnOrders, how='left', left_on=['FAMILY_ARTICLES_FULL', 'colorCode', 'ART_TYPE'], right_on=['FAMILY_ARTICLES_FULL', 'COLOR', 'ART_TYPE'])
            # formulation_Forecast_CurrentOrder.to_csv(f"C:\\Users\\danglc\\Desktop\\machineLearning\\formulation_Forecast_CurrentOrder.csv")
            # Align Gam_SF
            def f(row):
                if (row['Gam_SF'] > 0):
                    val = row['Gam_SF']
                else:
                    val = row['G_sf']
                return val
            def f_gam(row):
                if (row['Setup'] > 0):
                    val = row['Setup']
                else:
                    val = 0
                return val
            formulation_Forecast_CurrentOrder['Gam_SF'] = formulation_Forecast_CurrentOrder.apply(f, axis=1)
            formulation_Forecast_CurrentOrder['Setup'] = formulation_Forecast_CurrentOrder.apply(f_gam, axis=1)
            # CALCULATE MONTHLY CHEMICAL FORECAST AND CURRENT CHEMICAL DEMAND
            formulation_Forecast_CurrentOrder['monthly Chemical Forecast'] = round((formulation_Forecast_CurrentOrder['Gam_SF']*formulation_Forecast_CurrentOrder['monthlyFORECAST']/1000)*(formulation_Forecast_CurrentOrder['Component quantityy']*formulation_Forecast_CurrentOrder['PIGCOM_RATE']/1000)+(formulation_Forecast_CurrentOrder['SetupTimes']*formulation_Forecast_CurrentOrder['Setup']*formulation_Forecast_CurrentOrder['Component quantityy']*formulation_Forecast_CurrentOrder['PIGCOM_RATE']/1000),3)
            formulation_Forecast_CurrentOrder['current Chemical Demand'] = round(((formulation_Forecast_CurrentOrder['Gam_SF']*formulation_Forecast_CurrentOrder['CurrentOrders']/1000)*(formulation_Forecast_CurrentOrder['Component quantityy']*formulation_Forecast_CurrentOrder['PIGCOM_RATE']/1000) + (formulation_Forecast_CurrentOrder['SetupTimes']*formulation_Forecast_CurrentOrder['Setup']*formulation_Forecast_CurrentOrder['Component quantityy']*formulation_Forecast_CurrentOrder['PIGCOM_RATE']/1000)),3)
            formulation_Forecast_CurrentOrder.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\all_formulationDataForecastCurOrder.csv")

            # MONTHLY CHEMICAL FORECAST, DEMAND BY EACH CHEMICAL COMBINE
            monthly_ChemicalForecast = pd.DataFrame({'monthly Chemical Forecast' : round(formulation_Forecast_CurrentOrder.groupby(['Componenty', 'PIGCOM'])['monthly Chemical Forecast'].sum(),0)}).reset_index()
            monthly_ChemicalDemand = pd.DataFrame({'current Chemical Demand' : round(formulation_Forecast_CurrentOrder.groupby(['Componenty'])['current Chemical Demand'].sum(),0)}).reset_index()
            # print(monthly_ChemicalDemand)
            # read Chemical Control file
            chemicalInfo = pd.read_csv('D:\\GUI\\machineLearning\\CHEMICAL CONTROL.csv', encoding='cp1252')

            # combine intransit infor to Chemical Control
            chemicalInfo_Intransit = chemicalInfo.merge(ETA_allCombine, how='left', on=['Material'])

            # combine stock CH10, CH01 infor to Chemical Control
            chemicalInfo_Intransit_curStock = chemicalInfo_Intransit.merge(chemicalStock_CH01, how='left', on=['Material'])
            chemicalInfo_Intransit_curStock = chemicalInfo_Intransit_curStock.merge(chemicalStock_CH10, how='left', on=['Material'])
            chemicalInfo_Intransit_curStock = chemicalInfo_Intransit_curStock.merge(curConsumption, how='left', on=['Material'])

            # combine monthly Chemical Forecast and monthly Chemical Demand forecast to chemicalInfo
            chemicalInfo_Intransit_curStock_Forecast = chemicalInfo_Intransit_curStock.merge(monthly_ChemicalForecast, how='left', left_on=['Material'], right_on=['Componenty'])
            chemicalInfo_Intransit_curStock_Forecast_curDemand = chemicalInfo_Intransit_curStock_Forecast.merge(monthly_ChemicalDemand, how='left', left_on=['Material'], right_on=['Componenty'])
            chemicalInfo_Intransit_curStock_Forecast_curDemand = chemicalInfo_Intransit_curStock_Forecast_curDemand.drop(['Componenty_x', 'Componenty_y'], axis=1)

            # combine monthly history Chemical Consumption to chemical Info
            chemicalInfo_Intransit_curStock_Forecast_curDemand_Consumption = chemicalInfo_Intransit_curStock_Forecast_curDemand.merge(hisConsumption, how='left', on=['Material'])
            chemicalInfo_Intransit_curStock_Forecast_curDemand_Consumption = chemicalInfo_Intransit_curStock_Forecast_curDemand_Consumption.merge(hisConsumption_3month, how='left', on=['Material'])
            # ALL DATA

            chemicalInfo_Intransit_curStock_Forecast_curDemand_Consumption.to_csv(f"D:\\GUI\\machineLearning\\Database\\AllData.csv")
            chemicalInfo_Intransit_curStock_Forecast_curDemand_Consumption.to_csv(f"D:\\GUI\\machineLearning\\RunSolveFile\\AllData.csv")
            self.uic.lineEdit_allthingtogether.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')            
        except Exception as e:
            self.uic.lineEdit_allthingtogether.setText(f'{e}')

    def RunSolve(self):
        try:
            #CALCULATE PROPOSAL
            # fill NaN with 0,-
            allData = pd.read_csv(f"D:\\GUI\\machineLearning\\Database\\AllData.csv")
            allData[["Leadtime","Intransit","Stock_CH01","Stock_CH10","monthly Chemical Forecast", "monthly Consumption (6months)","current Chemical Demand"]] = allData[["Leadtime","Intransit","Stock_CH01","Stock_CH10","monthly Chemical Forecast", "monthly Consumption (6months)","current Chemical Demand"]].fillna(0)
            allData[["PIGCOM", "Intransit_Notes", "Comments"]] = allData[["PIGCOM", "Intransit_Notes", "Comments"]].fillna('-')

            # define either forecast or consumption as standard
            conditions = [
                (allData['monthly Chemical Forecast'] >= allData['monthly Consumption (6months)']),
                (allData['monthly Chemical Forecast'] < allData['monthly Consumption (6months)']),
            ]

            # proposal Consumption balance btw forecast and consumption
            results_monthStandard = [round(allData['monthly Chemical Forecast'],0),
                                            round(allData['monthly Chemical Forecast'],0)]

            allData['Aveage ForeCast Consumption'] = np.select(conditions, results_monthStandard)
            local_list = [
                100094,
104538,
105282,
104541,
104690,
104727,
104987,
105283,
104601,
104680,
105159,
105157,
104672,
105161,
105094,
105114,
104642,
104819,
85447,
104858,
105127,
105126,

            ]
            # Default minumum Stock (round up to month and plus 2 for compuond, 2.5 for pigment)
            def minStock(data_df):
                if (data_df['Aveage ForeCast Consumption'] == 0) and (data_df['Material'] not in local_list) and (data_df['PIGCOM'] == 'COMPOUND'):
                    return round(data_df['Leadtime']/30 + 2, 1)
                elif (data_df['Aveage ForeCast Consumption'] == 0) and (data_df['PIGCOM'] == 'PIGMENT'):
                    return round(data_df['Leadtime']/30 + 2.5, 1)
                elif (data_df['Aveage ForeCast Consumption'] != 0) and (data_df['Material'] not in local_list)and (data_df['PIGCOM'] == 'COMPOUND'):
                    return round(data_df['Leadtime']/30 + 2, 1)
                elif (data_df['Aveage ForeCast Consumption'] != 0) and (data_df['PIGCOM'] == 'PIGMENT'):
                    return round(data_df['Leadtime']/30 + 2.5, 1)
                elif (data_df['PIGCOM'] == 'COMPOUND') and (data_df['Material'] in local_list) and (data_df['Aveage ForeCast Consumption'] == 0):#local
                    return round(data_df['Leadtime']/30 + 1, 1)
                elif (data_df['PIGCOM'] == 'COMPOUND') and (data_df['Material'] in local_list) and (data_df['Aveage ForeCast Consumption'] != 0):#local
                    return round(data_df['Leadtime']/30 + 1, 1)
                else:
                    return round(data_df['Leadtime']/30 + 2, 1)
                
            allData['StockSet InHouse and Intransit'] = allData.apply(minStock, axis = 1)
            # chemicalData_Info_Intransit_Forecast_Consumption['minimumStock_inMonth'] = np.ceil(chemicalData_Info_Intransit_Forecast_Consumption['Leadtime']/30) + 1.5

            # Current Stock
            def currentStock(data_df):
                if data_df['Aveage ForeCast Consumption'] == 0:
                    return data_df['Stock_CH01']+data_df['Stock_CH10']+data_df['Intransit']
                elif data_df['Aveage ForeCast Consumption'] != 0:
                    return round((data_df['Stock_CH01']+data_df['Stock_CH10']+data_df['Intransit'])/data_df['Aveage ForeCast Consumption'], 1)

            allData['Current InHouse and Intransit'] = allData.apply(currentStock, axis = 1)
            # chemicalData_Info_Intransit_Forecast_Consumption['CurrentStockInMonth'] = round((chemicalData_Info_Intransit_Forecast_Consumption['Stock_CH01']+chemicalData_Info_Intransit_Forecast_Consumption['Stock_CH10']+chemicalData_Info_Intransit_Forecast_Consumption['Intransit'])/chemicalData_Info_Intransit_Forecast_Consumption['ForeCast_Consumption'], 1)

            # BuyToHitMinimumStock
            allData['Buy To StockSet'] = (allData['StockSet InHouse and Intransit'] - allData['Current InHouse and Intransit'])*allData['Aveage ForeCast Consumption']
            allData['Buy To StockSet'] = allData['Buy To StockSet'].apply(lambda x: x if (x>0) else 0)
            allData['ByTank'] = round(allData['Buy To StockSet']/allData['Tank_Drum_Size'],1)

            # current Stock vs current orders
            allData['InHouse vs. curOrders'] = round(allData['Stock_CH01']+allData['Stock_CH10']-allData['current Chemical Demand'],0)
            allData['InHouse vs. oneMonth'] = round(allData['Stock_CH01']+allData['Stock_CH10']-allData['Aveage ForeCast Consumption'],0)


            # InHouse Stock
            def inhouseStock(data_df):
                if data_df['Aveage ForeCast Consumption'] == 0:
                    return data_df['Stock_CH01']+data_df['Stock_CH10']
                elif data_df['Aveage ForeCast Consumption'] != 0:
                    return round((data_df['Stock_CH01']+data_df['Stock_CH10'])/data_df['Aveage ForeCast Consumption'], 1)
            # InHouse Stock
            allData['InHouse Stock InMonth'] = allData.apply(inhouseStock, axis = 1)


            allData.replace([np.inf, -np.inf], 0, inplace=True)
            allData[["Current InHouse and Intransit"]] = allData[["Current InHouse and Intransit"]].fillna(0)
            allData['revised To Buy'] = ''
            allData['stock included Buy'] = ''
            allData = allData[['Material', 'Long Material Description','Supplier','Location', 'PIGCOM','Comments', 'Leadtime', 'Tank_Drum_Size', 'Intransit','Intransit_Notes','Stock_CH01','Stock_CH10', 'monthly Chemical Forecast','monthly Consumption (6months)','monthly Consumption (3months)','Consumption on Current Month', 'InHouse Stock InMonth','StockSet InHouse and Intransit','Current InHouse and Intransit','Buy To StockSet','ByTank', 'revised To Buy', 'stock included Buy', 'Aveage ForeCast Consumption', 'current Chemical Demand', 'InHouse vs. curOrders', 'InHouse vs. oneMonth']]
            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y%H%M%S")

            allData.to_csv(f"D:\\GUI\\machineLearning\\RunSolve\\Consolidation_{dt_string}.csv")
            self.uic.lineEdit_RunSolve.setText(f'run it at {datetime.now().strftime("%m-%d-%Y, %H:%M:%S")}')            
        except Exception as e:
            self.uic.lineEdit_RunSolve.setText(f'{e}')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())   
    
    