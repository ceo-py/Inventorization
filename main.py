import pandas as pd

filename = '1.xlsx'

workbook = pd.read_excel(filename, sheet_name=None)

total = workbook["сборно"].iloc[4:, :].values.tolist()
main_sklad = workbook["Основен Склад"].iloc[4:, :].values.tolist()
buffer_sklad = workbook["Буферен склад"].iloc[4:, :].values.tolist()


def nan_to_zero(items):
    for i in range(2):
        item = str(items[i])
        if item == "nan":
            items[i] = 0


def compere_two_tabs_col_row_single_value(row, compere_colon, tab_one, tab_two):
    if tab_one[row][7] and str(tab_one[row][compere_colon]).strip() != str(tab_two[row][compere_colon]).strip():
        print(buffer_sklad[i])
        print(f'Row {i + 6}')
        print()


for i in range(1196):
    nan_to_zero(buffer_sklad[i])
    nan_to_zero(main_sklad[i])
    compere_two_tabs_col_row_single_value(i, 0, buffer_sklad, main_sklad)

