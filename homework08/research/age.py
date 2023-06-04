import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends  # type: ignore


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    items = get_friends(user_id, fields=["bdate"]).items  # получить информацию о друзьях пользователя с указанными
    # полями, включая даты рождения.
    today = dt.datetime.now()  # текущая дата и время.
    year = today.year  # извлекается текущий год
    age = []  # пустой список, в который будут добавляться возраста друзей.
    for element in items:  # перебор каждого элемента в списке.
        if "bdate" in element and len(element["bdate"]) >= 9:  # проверяется, что в словаре есть ключ "bdate" и
            # значение по этому ключу имеет длину не меньше 9 символов
            birthdate_ = element["bdate"]  # извлекается значение даты рождения
            birth_year = int(birthdate_[-4:])  # Из последних четырех символов извлекается год рождения
            age.append(year - birth_year)  # Вычисляется возраст, вычитая год рождения из текущего года
    average_ = statistics.mean(age) if age else None  # вычисляется среднее значение возрастов
    return average_


if __name__ == "__main__":
    print(age_predict(239843379))
