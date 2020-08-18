# En casos de requerir instaacion !pip3 install sodapy

import pandas as pd
from sodapy import Socrata


client = Socrata("www.datos.gov.co", None)
results = client.get("gt2j-8ykr", limit=1000000)
results_df = pd.DataFrame.from_records(results)
