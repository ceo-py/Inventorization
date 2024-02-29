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

errors = 0
for i in range(1196):

    nan_to_zero(main_sklad[i])
    nan_to_zero(buffer_sklad[i])
    nan_to_zero(total[i])

    if buffer_sklad[i][7] and str(buffer_sklad[i][0]).strip() != str(main_sklad[i][0]).strip():
        print(buffer_sklad[i])
        print(f'Row {i + 6}')
        print()
        errors +=1

    # if any(str(main_sklad[i][x]).strip() != str(buffer_sklad[i][x]).strip() != str(total[i][x]).strip() for x in range(2)):
    #     print(f'Row {i + 6}')
    #
    #     for item in range(2):
    #         if str(main_sklad[i][item]) == str(buffer_sklad[i][item]) == str(total[i][item]):
    #             continue
    #         print(f'{str(total[i][item])} - Сборно')
    #         print(f'{str(main_sklad[i][item])} - Основен Склад')
    #         print(f'{str(buffer_sklad[i][item])} - Буферен Склад')

        print()

print(errors)