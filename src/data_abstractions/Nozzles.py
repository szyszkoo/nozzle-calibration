import pandas as pd 
import matplotlib.pyplot as plt

from data_abstractions.DataSet import DataSet

class Nozzles(DataSet):
    """
    Representation of nozzle data set
    """
    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(
            self.get_file_path(1, "nozzle"),
            sep = ";",
            names=["timestamp", "locationID", "nozzleID", "tankID", "literCounter",
                    "totalCounter", "status"],
            parse_dates=[0],
            decimal=",",
            usecols=["timestamp", "nozzleID", "tankID", "literCounter", "totalCounter", "status"]
        )
    
    def get_nozzle(self, nozzleID: int) -> pd.DataFrame:
        """Get subset of nozzle data by nozzleID"""
        return self.data[self.data["nozzleID"] == nozzleID]