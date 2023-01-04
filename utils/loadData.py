import sqlite3
from utils.dataPipeline import dataPipeline
from utils.constants import col_name_type_map
class loadData(dataPipeline):
    def __init__(self):
        self.data_db = None
        try:
            self.data_db = sqlite3.connect("D:\\My Projects\\power_generation\\app\\database\\PreprocessData.db")
            print("Opened databases successfully")
        except Exception as e:
            print(e)
    
    def generateDDL(self):
        ddl = "create table hospitalData("
        for col_name, col_type in col_name_type_map.items():
            ddl = ddl + col_name + " " + col_type + "," 
        ddl = ddl + ");"
        ddl = ddl[:-3] + ddl[-3+1]
        ddl = ddl+";"
        return ddl
    
    def createTable(self):
        ddl = self.generateDDL()
        self.data_db.execute(ddl)
        self.data_db.commit()
    
    
    def loadDatatoSQL(self, dataset, type="append"):
        dataset.to_sql("hospitalData", self.data_db, if_exists=type, index=False)
        self.data_db.commit()
        self.data_db.close()
        print("Data Loaded successfully")
    
    def queryData(self):
        query = "SELECT count(*) FROM hospitalData"
        cur = self.data_db.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for i in rows:
            print(i)
    
    def closeDB(self):
        self.data_db.close()
