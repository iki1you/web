# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return s[::-1]


# Обязательно начинайте тест с префикса 'test_'
def test_reverse():
    assert reverse('abc') == 'cba'