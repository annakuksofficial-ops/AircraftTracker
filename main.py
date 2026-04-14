from src.api_client import NominatimClient, OpenSkyClient
from src.aeroplane import Aeroplane
from src.file_saver import JSONSaver
from src.utils import filter_by_country, filter_by_altitude, get_top_n_by_altitude, sort_by_velocity


def user_interaction() -> None:
    """Функция взаимодействия с пользователем"""
    print("\n" + "=" * 50)
    print("Добро пожаловать в программу мониторинга самолётов!")
    print("=" * 50 + "\n")

    country = input("Введите название страны: ").strip()

    print(f"\nИщем информацию о самолётах в воздушном пространстве {country}...\n")

    try:
        nominatim = NominatimClient()
        country_data = nominatim.get_data(country)
        boundingbox = country_data.get('boundingbox')

        if not boundingbox:
            print("Не удалось получить координаты страны")
            return

        opensky = OpenSkyClient()
        data = opensky.get_data(
            lamin=boundingbox[0],
            lamax=boundingbox[1],
            lomin=boundingbox[2],
            lomax=boundingbox[3]
        )

        states = data.get('states', [])

        if not states:
            print("Самолётов в данном воздушном пространстве не найдено")
            return

        aeroplanes = []
        for state in states:
            try:
                aeroplane = Aeroplane.from_state_vector(state)
                aeroplanes.append(aeroplane)
            except Exception:
                continue

        print(f"Найдено самолётов: {len(aeroplanes)}\n")

        saver = JSONSaver()
        for a in aeroplanes:
            saver.add_aeroplane(a)
        print("Данные сохранены в файл data/aeroplanes.json\n")

        print("Что вы хотите сделать?")
        print("1. Показать топ N самолётов по высоте")
        print("2. Отфильтровать самолёты по стране регистрации")
        print("3. Отфильтровать самолёты по диапазону высот")
        print("4. Показать все самолёты")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == '1':
            n = int(input("Введите количество N: "))
            top = get_top_n_by_altitude(aeroplanes, n)
            print(f"\nТоп {n} самолётов по высоте:")
            for i, a in enumerate(top, 1):
                print(f"{i}. {a}")

        elif choice == '2':
            countries = input("Введите страны через пробел: ").split()
            filtered = filter_by_country(aeroplanes, countries)
            print(f"\nНайдено самолётов: {len(filtered)}")
            for a in filtered:
                print(f"  {a}")

        elif choice == '3':
            min_alt = float(input("Минимальная высота (м): "))
            max_alt = float(input("Максимальная высота (м): "))
            filtered = filter_by_altitude(aeroplanes, min_alt, max_alt)
            print(f"\nНайдено самолётов: {len(filtered)}")
            for a in filtered:
                print(f"  {a}")

        elif choice == '4':
            print("\nВсе самолёты:")
            for a in aeroplanes:
                print(f"  {a}")

        else:
            print("Неверный выбор")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    user_interaction()
