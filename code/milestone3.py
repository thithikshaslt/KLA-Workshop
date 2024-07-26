import pandas as pd
import numpy as np

# Load data
care_areas = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\3rd\CareAreas.csv', header=None)
meta_data = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\3rd\metadata.csv')

mainField_dim = meta_data.iloc[0, 0]
subField_dim_1 = meta_data.iloc[0, 1]  
subField_dim_2 = meta_data.iloc[1, 1]  

main_fields = []
sub_fields = []

min_x = care_areas[0].min()
max_x = care_areas[1].max()
min_y = care_areas[2].min()
max_y = care_areas[3].max()

num_main_fields_x = int(np.ceil((max_x - min_x) / mainField_dim))
num_main_fields_y = int(np.ceil((max_y - min_y) / mainField_dim))

for i in range(num_main_fields_x):
    for j in range(num_main_fields_y):
        x1 = min_x + i * mainField_dim
        y1 = min_y + j * mainField_dim
        x2 = x1 + mainField_dim
        y2 = y1 + mainField_dim
        main_fields.append([i * num_main_fields_y + j, x1, x2, y1, y2])

main_fields_df = pd.DataFrame(main_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2'])
print(main_fields_df)
sub_field_id_counter = 0

def add_sub_field(x1, y1, x2, y2, main_field_id):
    global sub_field_id_counter
    sub_fields.append([sub_field_id_counter, x1, x2, y1, y2, main_field_id])
    sub_field_id_counter += 1

for _, care_area in care_areas.iterrows():
    care_x1, care_x2, care_y1, care_y2 = care_area[1:]

    for x in np.arange(care_x1, care_x2, subField_dim_1):
        for y in np.arange(care_y1, care_y2, subField_dim_1):
            x2 = min(x + subField_dim_1, care_x2)
            y2 = min(y + subField_dim_1, care_y2)
            if x < x2 and y < y2:
                add_sub_field(x, y, x2, y2, None)  

    for x in np.arange(care_x1, care_x2, subField_dim_2):
        for y in np.arange(care_y1, care_y2, subField_dim_2):
            x2 = min(x + subField_dim_2, care_x2)
            y2 = min(y + subField_dim_2, care_y2)
            if x < x2 and y < y2:
                add_sub_field(x, y, x2, y2, None)  
print("hi")
for idx, main_field in enumerate(main_fields):
    main_field_id, mf_x1, mf_x2, mf_y1, mf_y2 = main_field
    for sub_field in sub_fields:
        sub_id, sub_x1, sub_x2, sub_y1, sub_y2, _ = sub_field
        if (sub_x1 >= mf_x1 and sub_x2 <= mf_x2 and sub_y1 >= mf_y1 and sub_y2 <= mf_y2):
            sub_fields[sub_id][5] = main_field_id

sub_fields_df = pd.DataFrame(sub_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2', 'MF_ID'])
print(sub_fields_df)
main_fields_df.to_csv('MainFields3.csv', header=False, index=False)
sub_fields_df.to_csv('SubFields3.csv', header=False, index=False)

