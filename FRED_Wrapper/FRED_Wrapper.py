from urllib.parse import urlencode
import functools as ft
from io import BytesIO
import pandas as pd
import requests
import zipfile


class FRED_Wrapper:
    """
    Class to obtain data from FRED website.
    The official API is not used.
    """

    def __init__(self):
        pass

    @staticmethod
    def __encode_kwargs(params: dict) -> str:
        """
        Encode the url with the params

        Args:
            params (dict): Dictionary with parameter variables.

        Return:
            str: Encoded url
        """
        base_url = "https://fred.stlouisfed.org/graph/fredgraph.csv"
        valid_params = {"id": "id", "start_date": "cosd", "end_date": "coed", "transform": "transformation", "freq": "fq", "agg": "fam", "formula": "fml"}

        params = {k: ",".join(v) for k, v in params.items()} if (all(isinstance(v, list) for v in params.values())) else params
        web_params = {v: params[k] for k, v in valid_params.items() if k in params and params[k]}
        return f"{base_url}?{urlencode(web_params)}"

    @staticmethod
    def __read_data_from_url(url: str) -> pd.DataFrame:
        """
        Read the data from the FRED URL. It takes into account if it returns a zip file with multiple csv inside.

        Args:
            url (str): Encoded url.

        Return:
            pd.DataFrame: DataFrame with FRED data
        """
        res = requests.get(url)

        if res.headers["content-type"] == "application/zip":
            with zipfile.ZipFile(BytesIO(res.content)) as zf:
                dfs = [pd.read_csv(zf.open(file_info)) for file_info in zf.infolist()]
                df = ft.reduce(lambda left, right: pd.merge(left, right, on="DATE", how="outer"), dfs)
            return df

        else:
            return pd.read_csv(BytesIO(res.content))

    @staticmethod
    def __split_dict(params: dict, max_len: int) -> list:
        """
        Split the parameter dictionary into several whose length is less than or equal to the allowed length.

        Args:
            params (dict[str: str]): Original parameter dictionary
            max_len (int): Maximum allowed dictionary length.

        Return:
            list[dict]: List of parameter dictionaries with appropriate length
        """
        return [{k: v[idx:idx+max_len] for k, v in params.items()} for idx in range(0, len(params["id"]), max_len)]

    @classmethod
    def get_fred_data(cls, **kwargs) -> pd.DataFrame:
        """
        Get FRED series data

        Keyword Args:
            id (str or list[str]): Id or key of the data series.
            start_date (str or list[str]): Start date of the data series. Format: YYYY-MM_DD
            end_date (str or list[str]): End date of the data series. Format: YYYY-MM_DD
            transform (str or list[str]): Transformation of the data series.
            freq (str or list[str]): Frequency of the data series.
            agg (str or list[str]): Aggregation method of the data series.
            formula (str or list[str]): Formula applied to the data series.

        Return:
            pd.DataFrame: DataFrame with FRED data
        """
        if isinstance(kwargs["id"], str) or (isinstance(kwargs["id"], list) and len(kwargs["id"]) <= 10):
            url = cls.__encode_kwargs(kwargs)
            res = cls.__read_data_from_url(url)

        else:
            urls = [cls.__encode_kwargs(kw) for kw in cls.__split_dict(kwargs, max_len=10)]
            dfs = [cls.__read_data_from_url(url) for url in urls]
            res = ft.reduce(lambda left, right: pd.merge(left, right, on="DATE", how="outer"), dfs)

        cols = res.columns.drop(res.columns[0])
        res.iloc[:, 0], res[cols] = pd.to_datetime(res.iloc[:, 0]), res[cols].apply(pd.to_numeric, errors='coerce')
        return res
