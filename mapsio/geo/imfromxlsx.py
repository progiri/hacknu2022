from cmath import nan
import pandas as pd
from .models import GeoDataPacket
from django.contrib.gis.geos import Point
import numpy as np
# data = pyexcel.get_book_dict(file_name="/home/progiri/hacknu-dev-data.xlsx")

# def import_from_xlsx():
#     for count in range(1, 9):
#         excel_data = pd.read_excel('/home/progiri/hacknu-dev-data.xlsx', sheet_name=f"dev{count}")
#         # Read the values of the file in the dataframe
#         data = pd.DataFrame(excel_data, columns=['Latitude', 'Longitude', 'Altitute', 'Identifier', 'Timestamp', 'Floor label', 'Horizontal accuracy', 'Vertical accuracy', 'Confidence in location accuracy', 'Activity'])
#         print(data.values)
#         for el in data.values:
#             print(el[0], el[1], el[2])
#             geo = GeoDataPacket.objects.create(
#                 point=Point(el[0], el[1], el[2]),
#                 identifier=el[3] if el[3] != "null" else None,
#                 timestamp=el[4] if el[4] != "null" else None,
#                 floor_label=el[5] if el[5] != "null" else None,
#                 hor_accuracy=el[6] if el[6] != "null" else None,
#                 ver_accuracy=el[7] if el[7] != "null" else None,
#                 cil_accuracy=el[8] if el[8] != "null" else None,
#                 activity=el[9] if el[9] != "null" else None,
#                 dev=dev,
#             )

#     print("done!")
#     return None


#  for dat in data:
# ...     for i, d in enumerate(data[dat]):
# ...             con = 0
# ...             if i == 0: continue
# ...             for n in d: 
# ...                     if n == '': continue
# ...                     else: con += 1
# ...             if con > 0:
# ...                     if result.get(dat):
# ...                             result[dat].append(d)
# ...                     else:
# ...                             result[dat] = [d]