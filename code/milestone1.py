import pandas as pd
import math

care_area_blocks = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-0\1st\CareAreas.csv', header=None)
meta_data = pd.read_csv(r'D:\Sem 5\other\KLA-Workshop\resources\Dataset-0\1st\metadata.csv')

mainField_dim = meta_data.iloc[0, 0]
subField_dim = meta_data.iloc[0, 1]

def main_field_coverage(care_area_blocks, mainField_dim):
    main_fields = []
    for index, row in care_area_blocks.iterrows():
        x1 = row[1]
        x2 = row[2]
        y1 = row[3]
        y2 = row[4]

        x_field = math.ceil((x2 - x1) / mainField_dim)
        y_field = math.ceil((y2 - y1) / mainField_dim)

        for i in range(x_field):
            for j in range(y_field):
                main_field_x1 = x1 + i * mainField_dim
                main_field_y1 = y1 + j * mainField_dim
                main_field_x2 = main_field_x1 + mainField_dim
                main_field_y2 = main_field_y1 + mainField_dim

                main_fields.append([main_field_x1, main_field_x2, main_field_y1, main_field_y2])
    return pd.DataFrame(main_fields, columns=['x1', 'x2', 'y1', 'y2'])

def sub_field_coverage(main_fields, subField_dim):
    sub_fields = []
    for index, row in care_area_blocks.iterrows():
        x1 = row[1]
        x2 = row[2]
        y1 = row[3]
        y2 = row[4]

        x_field = math.ceil((x2 - x1) / subField_dim)
        y_field = math.ceil((y2 - y1) / subField_dim)

        for i in range(x_field):
            for j in range(y_field):
                sub_field_x1 = x1 + i * subField_dim
                sub_field_y1 = y1 + j * subField_dim
                sub_field_x2 = sub_field_x1 + subField_dim
                sub_field_y2 = sub_field_y1 + subField_dim

                sub_fields.append([sub_field_x1, sub_field_x2, sub_field_y1, sub_field_y2, index])
    return pd.DataFrame(sub_fields, columns=['x1', 'x2', 'y1', 'y2', 'MainFieldID'])

main_fields = main_field_coverage(care_area_blocks, mainField_dim)
sub_fields = sub_field_coverage(main_fields, subField_dim)

main_fields.to_csv('MainFields.csv', header=False)
sub_fields.to_csv('SubFields.csv', header=False)

