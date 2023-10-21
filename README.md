# FRED Script in Python
This repository contains a Python class to interact with the FRED web in a simple way without the need to register and get a KEY API.

## Methods

The FRED_API class provides a way to get data from the FRED web page. Instead of using the official API, this class makes direct requests to the web page and gets the data in CSV format.

### get_fred_data

This method allows obtaining single series as well as multiple series of FRED data. The data can be customized using various parameters, such as series ID, start date, end date, data transformation, frequency, aggregation method and applied formula. The function returns the data in the form of a pandas DataFrame, which facilitates its manipulation and analysis.

```python
  FRED_API.get_fred_data(**kwargs)
```

#### Keyword Args:

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `str or list[str]` | ID or key of the requested data series. |
| `start_date` | `str or list[str]` | Start date of the data series. Format: YYYY-MM-DD |
| `end_date` | `str or list[str]` | Start date of the data series. Format: YYYY-MM-DD |
| `transform` | `str or list[str]` | Transformation of the data series. |
| `freq` | `str or list[str]` | Frequency of the data series. |
| `agg` | `str or list[str]` | Aggregation method of the data series. |
| `formula` | `str or list[str]` | Formula applied to the data series. |

#### Returns:
- `pd.DataFrame`: A DataFrame containing series data.

## Usage/Examples

```python
from FRED_API import FRED_API

# Get WSHOMCB and WSHOTSL series at the same time
df = FRED_API.get_fred_data(id=["WSHOMCB", "WSHOTSL"],
                   start_date=["2020-01-01", "2020-01-01"],
                   end_date=["2020-12-31", "2020-12-31"],
                   transform=["chg", "chg"]
                   freq=["Monthly", "Monthly"],
                   agg=["eop", "eop"],
                   formula=["a/1000", "a/1000"])
)
```
