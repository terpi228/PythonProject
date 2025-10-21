from src.read_file import read_csv_file, read_excel_file

if __name__ == "__main__":
    r_ex = read_excel_file("data/transactions_excel.xlsx")
    print(r_ex)
    print("==" * 50)
    r_csv = read_csv_file("data/transactions.csv")
    print(r_csv)
