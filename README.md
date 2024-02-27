# asd
astronomy seeing davos (ASD) scraper for scraping the daily data from the [meteoblue page in davos]('https://www.meteoblue.com/de/wetter/outdoorsports/seeing/davos_schweiz_2661039')  
# How to use
### Running it directly as main
Clone this repo into a local directory. Create a new environment with you favorite python environment manager. Install the requirements file 
'''cmd
pip install -r requirements.txt
'''
run the programm file itself to get an example df of the current day.
'''cmd
python asd.py
'''

### import as package
you will need to install the source. For this go to the root directory of the package. There you will see the `pyproject.toml` file. In this root directory run
'''cmd
pip install .
'''
Once the package is installed in your virtual environment you can use it like this:
'''python
from asd import get_day
df = get_day()
print(df)
'''
This will gets you an pandas dataframe of the data of the current day.

# Contribute
Happy for every merge request!  