import pandas as pd

try: 
    df = pd.read_csv('d1f.csv')

    # Проверка, пуст ли файл
    if df.empty:
        raise ValueError("Ошибка: CSV-файл пуст!")

    # Проверка наличия обязательных столбцов
    required_columns = ["1", "2", "3"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Ошибка: Отсутствуют столбцы {missing_columns}")

    # Вывод данных
    print(df)

except FileNotFoundError:
    print("Ошибка: Файл не найден!")
except pd.errors.ParserError:
    print("Ошибка: Файл поврежден или имеет неверный формат!")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Неожиданная ошибка: {e.__class__} - {e}")
