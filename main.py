from src.processing import sort_by_date, filter_by_state
from tests.test_processing import TEST_DATA

if __name__ == "__main__":
    print("Исходные данные:", TEST_DATA)

    state_filter = input("Введите state для фильтрации (ENTER для EXECUTED): ") or "EXECUTED"
    filtered_data = filter_by_state(TEST_DATA, state_filter)
    print("\nОтфильтрованные данные:", filtered_data)

    sorted_data = sort_by_date(TEST_DATA)
    print("\nОтсортированные данные (новые сначала):", sorted_data)

    processed_data = sort_by_date(filter_by_state(TEST_DATA))
    print("\nEXECUTED + сортировка:", processed_data)
