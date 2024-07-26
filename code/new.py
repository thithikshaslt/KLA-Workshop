import pandas as pd
import math

care_areas = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\2nd\CareAreas.csv', header=None)
metadata = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\2nd\metadata.csv')

main_field_dim = metadata['Main Field Size'].values[0]
sub_field_size = metadata['Sub Field Size'].values[0]

main_fields = []
sub_fields = []

x1 = row[1]
x2 = row[2]
y1 = row[3]
y2 = row[4]

num_main_fields_x = (max_x - min_x) // main_field_dim + 1
num_main_fields_y = (max_y - min_y) // main_field_dim + 1

for i in range(num_main_fields_x):
    for j in range(num_main_fields_y):
        print(j)
        x1 = min_x + i * main_field_dim
        y1 = min_y + j * main_field_dim
        x2 = x1 + main_field_dim
        y2 = y1 + main_field_dim
        main_fields.append([i * num_main_fields_y + j, x1, x2, y1, y2])

for main_field in main_fields:
    main_field_id, mf_x1, mf_x2, mf_y1, mf_y2 = main_field
    sub_field_id = 0
    for _, care_area in care_areas.iterrows():
        care_x1, care_x2, care_y1, care_y2 = care_area[1:]
        if not (care_x1 >= mf_x2 or care_x2 <= mf_x1 or care_y1 >= mf_y2 or care_y2 <= mf_y1):
            sub_x1 = max(mf_x1, care_x1)
            sub_x2 = min(mf_x2, care_x2)
            sub_y1 = max(mf_y1, care_y1)
            sub_y2 = min(mf_y2, care_y2)
            sub_fields.append([sub_field_id, sub_x1, sub_x2, sub_y1, sub_y2, main_field_id])
            sub_field_id += 1

main_fields_df = pd.DataFrame(main_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2'])
sub_fields_df = pd.DataFrame(sub_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2', 'MF_ID'])

main_fields_df.to_csv('MainFields2.csv', header=False, index=False)
sub_fields_df.to_csv('SubFields2.csv', header=False, index=False)
