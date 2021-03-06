import abc
import pandas as pd
from typing import Optional
import os
from pathlib import Path
from src.data.utils import LOG

class data_base(abc.ABC):

    data_dir :          Optional[str] = None
    raw_data_path :     Optional[str] = None
    interim_data_path : Optional[str] = None

    df :       Optional[pd.DataFrame] = None
    def __init__(self):

        if self.raw_data_path:
            Path(self.raw_data_path.parent).mkdir(parents=True, exist_ok=True)
        if self.interim_data_path:
            Path(self.interim_data_path.parent).mkdir(parents=True, exist_ok=True)


    def _does_file_exist(self)-> bool:
        if os.path.exists(self.raw_data_path):
            LOG.info("Data path {} detected. Reading now...".format(self.raw_data_path))
            return True
        else:
            LOG.info("Data path {} not detected. Applying query now...".format(self.raw_data_path))
            return False

    def get_dataframe(self, sorted: Optional[bool] = True)-> pd.DataFrame:

        if self._does_file_exist():
            df = pd.read_pickle(self.raw_data_path)
        else:
            df = self._apply_query(sorted=sorted)
        LOG.info("Done")
        return(df)



    """
     For child-classes, the following functions needs to be implemented.


    def sort_with_MP(self, entries: pd.DataFrame)-> pd.DataFrame:

    def _apply_query(self, sorted: Optional[bool])-> pd.DataFrame:

    def _sort(self, entries: pd.DataFrame)-> pd.DataFrame:

    def sort_with_MP(self, entries: pd.DataFrame)-> np.array:
    """
