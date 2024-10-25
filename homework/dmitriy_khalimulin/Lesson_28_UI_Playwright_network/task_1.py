from playwright.sync_api import Page, expect, Route
import json
import re


def test_substitution_of_answer(page: Page):
    new_value_title = 'яблокофон 16 про'

    def replacing_an_answer(route: Route):
        """Функция для подстановки значения в теле ответа"""

        # Отправка запроса на сервер и получение исходного HTTP-ответа
        response = route.fetch()

        # Преобразование ответа в словарь Python
        body = response.json()

        # Замена значения в поле productName
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_value_title

        # Преобразрвание измененного ответа обратно в JSON
        body = json.dumps(body)

        # Отправка измененного ответа
        route.fulfill(
            response=response,
            body=body
        )

    # Эндпоинт для перехвата и передача данных в функцию replacing_an_answer
    page.route(re.compile('shop/api/digital-mat'), replacing_an_answer)

    # Переход на сайт, поиск элемента для перехода в Popup и клик на него
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role("button", name="Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max").click()

    # Поиск элемента подменного заголовка
    samsung2 = page.locator('#rf-digitalmat-overlay-label-0', has_text=new_value_title)

    # Проверка соответствия заголовка с подменным текстом
    expect(samsung2).to_have_text(new_value_title)
