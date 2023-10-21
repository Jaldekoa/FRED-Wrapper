# FRED Wrapper in Python

This repository contains a Python class that allows you to interact with and get data from the FRED website in a simple way without the need to connect to the API or register or get a KEY API.

## Methods

The Python class provides a way to get data from the FRED web page. Instead of using the official API, this class makes direct requests to the web page and gets the data in CSV format.

### get_fred_data()

This method allows obtaining single series as well as multiple series of FRED data. The data can be customized using various parameters, such as series ID, start date, end date, data transformation, frequency, aggregation method and applied formula. The function returns the data in the form of a pandas DataFrame, which facilitates its manipulation and analysis.

```python
  FRED_Wrapper.get_fred_data(**kwargs)
```

#### Keyword Args:

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `str or list[str]` | ID or key of the requested data series. |
| `start_date` | `str or list[str]` | Start date of the data series. Format: YYYY-MM-DD |
| `end_date` | `str or list[str]` | Start date of the data series. Format: YYYY-MM-DD |
| `transform` | `str or list[str]` | Transformation of the data series. Valid values: None: "lin", Change: "chg", Change from Year Ago: "ch1", Percent Change from Year Ago: "pc1", Compounded Annual Rate of Change: "pca", Continuously Compounded Rate of Change: "cch", Continuously Compounded Annual Rate of Change: "cca".|
| `freq` | `str or list[str]` | Frequency of the data series. |
| `agg` | `str or list[str]` | Aggregation method of the data series. Valid values: Average: "avg", Sum: "sum", End of Period: "eop".|
| `formula` | `str or list[str]` | Formula applied to the data series. |

#### Returns:
- `pd.DataFrame`: A DataFrame containing series data.

## Usage/Examples

### Single series

You can obtain the data for a single series as follows:

```python
from FRED_Wrapper import FRED_Wrapper

df = FRED_Wrapper.get_fred_data(id="WM1NS",
								start_date="2020-01-01",
								end_date="2023-08-31",
								transform="chg",
								freq="Monthly",
								agg="eop",
								formula="a/1000")
```

#### Result

```python
print(df.tail())
```

|    | DATE                |   WM1NS_CHG |
|---:|:--------------------|------------:|
| 39 | 2023-04-01 00:00:00 |     -0.3139 |
| 40 | 2023-05-01 00:00:00 |     -0.08   |
| 41 | 2023-06-01 00:00:00 |     -0.1384 |
| 42 | 2023-07-01 00:00:00 |     -0.0522 |
| 43 | 2023-08-01 00:00:00 |     -0.1316 |

### Multiple series

You can obtain the data from a multiple series in either of the following two ways:

```python
from FRED_Wrapper import FRED_Wrapper

df = FRED_Wrapper.get_fred_data(id=["WM1NS", "WM2NS"],
                   start_date=["2020-01-01", "2020-01-01"],
                   end_date=["2023-08-31", "2023-08-31"],
                   transform=["chg", "chg"],
                   freq=["Monthly", "Monthly"],
                   agg=["eop", "eop"],
                   formula=["a/1000", "a/1000"])
)
```

```python
from FRED_Wrapper import FRED_Wrapper

PARAMS = {  
    "id": ["WM1NS", "WM2NS"],  
    "start_date": ["2020-05-01", "2020-05-01"],  
    "end_date": ["2023-08-31", "2023-08-31"],
    "transform": ["chg", "chg"],  
    "freq": ["Monthly", "Monthly"],  
    "agg": ["eop", "eop"],  
    "formula": ["a/1000", "a/1000"],  
}  
  
df = FRED_Wrapper.get_fred_data(**PARAMS)
```

#### Result

```python
print(df.tail())
```

|    | DATE                |   WM1NS_CHG |   WM2NS_CHG |
|---:|:--------------------|------------:|------------:|
| 39 | 2023-04-01 00:00:00 |     -0.3139 |     -0.1962 |
| 40 | 2023-05-01 00:00:00 |     -0.08   |      0.081  |
| 41 | 2023-06-01 00:00:00 |     -0.1384 |     -0.0595 |
| 42 | 2023-07-01 00:00:00 |     -0.0522 |      0.0354 |
| 43 | 2023-08-01 00:00:00 |     -0.1316 |     -0.0562 |
