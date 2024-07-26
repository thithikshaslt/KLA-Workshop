import pandas as pd

care_areas = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\2nd\CareAreas.csv', header=None)
metadata = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-1\2nd\metadata.csv')


main_field_dim = metadata['Main Field Size'].values[0]
sub_field_size = metadata['Sub Field Size'].values[0]

main_fields = []
sub_fields = []

min_x = care_areas[0].min()
max_x = care_areas[1].max()
min_y = care_areas[2].min()
max_y = care_areas[3].max()

num_main_fields_x = (max_x - min_x) // main_field_dim + 1
num_main_fields_y = (max_y - min_y) // main_field_dim + 1

sub_field_id = 0

for i in range(num_main_fields_x):
    for j in range(num_main_fields_y):
        x1 = min_x + i * main_field_dim 
        y1 = min_y + j * main_field_dim - 2
        x2 = x1 + main_field_dim
        y2 = y1 + main_field_dim
        main_fields.append([i * num_main_fields_y + j, x1, x2, y1, y2])



for _, care_area in care_areas.iterrows():
    care_x1, care_x2, care_y1, care_y2 = care_area[1:]
    sub_x1 = care_x1
    sub_x2 = sub_x1 + sub_field_size
    sub_y1 =care_y1
    sub_y2 = sub_y1 + sub_field_size
    
    sub_fields.append([sub_field_id, sub_x1, sub_x2, sub_y1, sub_y2, i * num_main_fields_y + j ])
    sub_field_id += 1
    
main_fields_df = pd.DataFrame(main_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2'])
sub_fields_df = pd.DataFrame(sub_fields, columns=['ID', 'x1', 'x2', 'y1', 'y2', 'MF_ID'])

main_fields_df.to_csv('MainFields2.csv', header=False, index=False)
sub_fields_df.to_csv('SubFields2.csv', header=False, index=False)

