aboud_user = {
    "full_name": "Ф.И.О? (Пример ввода: Иванов Иван Иванович)",
    "birthdate": "Дата рождения? (ЧЧ.ММ.ГГГГ)",
    "birthplace": "Место рождения? (Как в паспорте)",
    "passport_number": "Серия и номер паспорта? (Пример ввода: 1234 567890)",
    "department_code": "Код подразделения? (Пример ввода: 123-456)",
    "date_of_issue": "Дата выдачи (ЧЧ.ММ.ГГГГ)?",
    "issued_by": "Кем выдан?",
    "address": "Адрес регистрации (Как в паспорте)?",
    "actual_address": "Фактический адрес жительства (*опционально)",
    "i_c": "СНИЛС? (Пример ввода: 111-222-333 44)",
    "phone_number": "Мобильный телефон?",
    "email": "Email?"
}

about_family = {
    "civil_status": "Семейное положение",
    "amount_of_children": "Количество детей",
    "education": "Образование",
    "contact_phone": "Телефон контактного лица (родственник, супруг(а))",
    "international_passport": "Заграничный паспорт *опционально"
}

about_work = {
    "place_of_work": "Место работы (название организации)",
    "inn": "ИНН Организации",
    "type": "Тип организации (ООО, ИП ...)",
    "activity": "Вид деятельности",
    "number_of_employees": "Количество сотрудников",
    "address": "Физический адресс",
    "work_phone": "Рабочий телефон",
    "position": "Должность",
    "type_of_position": "Тип должности",
    "extra_work": "Дополнительная работа *опционально",
    "experience": "Стаж на основном месте работы (год, месяц)",
    "seniority": "Стаж на предыдущем месте работы (год, месяц)"
}

about_mortgage = {
    "amount": "Желаемая сумма (от 500 тыс.руб до 20 млн.руб)",
    "term": "Срок кредитования (от 1 года до 30 лет)"
}

extra = {
    "additional_income": "Дополнительный доход (тип дохода, сумма) *опционально",
    "apartment": "Квартира в собственности *опционально",
    "car": "Автомобиль в собственности *опционально",
    "vacation_home": "Загородный дом *опционально"
}

by_theme = {
    "Вклад": [aboud_user],
    "Кредит": [aboud_user, about_family, about_work, extra],
    "Ипотека": [aboud_user, about_mortgage],
    "Дебетовые карты": [aboud_user]
}

def start(service: str):
    for block in by_theme[service]:
        for key, value in block.items():
            yield key, value