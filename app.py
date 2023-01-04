from utils.dataPipeline import *
from utils.loadData import *

datapipeline = dataPipeline(data_path="D:\My Projects\power_generation\dataset\historyData\historyData.csv")
loadingdata = loadData()

data = datapipeline.createPipeline()
#loadingdata.createTable()
loadingdata.loadDatatoSQL(data, type="replace") #type = ["append", "replace"]
loadingdata.closeDB()
#loadingdata.queryData()