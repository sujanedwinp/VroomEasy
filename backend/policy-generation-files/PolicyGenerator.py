from fastapi import FastAPI
from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()
import random
import csv

app = FastAPI()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

res = supabase.table("insurer_info").select("*").execute()
insurers_data = res.data
@app.get("/insurers")
def get_insurers():
    return insurers_data

class PolGen:

    def __init__(self, miIR=150000, maIR=500000, mBT=5000, mCT=5000):
        self.minIdvRange=miIR
        self.maxIdvRange=maIR
        self.maxBikeType=mBT
        self.maxCarType=mCT
        self.maxCount=mBT+mCT

    def getRandomInsurerId(self):
        return random.randint(1, insurers_data[len(insurers_data)-1]['id'])

    def getRandomVehicle(self):
        vType= random.randint(1, 2)
        if vType==1 and self.maxBikeType>0:
            self.maxBikeType=self.maxBikeType-1
        elif vType==2 and self.maxCarType>0:
            self.maxCarType=self.maxCarType-1
        return vType
    
    def getIdvRanges(self):
        minIdv=random.randint(self.minIdvRange, self.minIdvRange+self.minIdvRange)
        maxIdv=random.randint(self.maxIdvRange, self.maxIdvRange+self.maxIdvRange)

        avgIdv=(minIdv+ maxIdv)/2

        return [minIdv, avgIdv, maxIdv]

    def getRiskFactor(self):
        return random.randint(1, 5)

    def getMaxTenure(self):
        return random.randint(1, 3)

    def getAddonsFormat(self):
        def getAddonState():
            return random.randint(0, 1)
        
        return f"{getAddonState()}{getAddonState()}{getAddonState()}{getAddonState()}"

    def generateData(self):
        finalList = []
        for _ in range(self.maxCount):  
            idvList = self.getIdvRanges()
            finalList.append([
                self.getRandomInsurerId(),
                self.getRandomVehicle(),
                idvList[0],
                idvList[1],
                idvList[2],
                self.getRiskFactor(),
                self.getMaxTenure(),
                self.getAddonsFormat()
            ])
        return finalList
    
    def createCSV(self, policy_data_list):
        with open("backend/policy-generation-files/output.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["insurer_id", "vehicle_type", "min_idv", "avg_idv", "max_idv", "risk_factor", "tenure", "addons"])
            writer.writerows(policy_data_list)


policy_generator=PolGen()
policy_generator.createCSV(policy_generator.generateData())