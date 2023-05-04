def make_diff(data1: dict, data2: dict) -> list:
    diff = []
    # набор всех ключей
    all_keys = set(data1.keys()) | set(data2.keys())
    # набор вложенных словарей
    nested_keys = set(
        k for k in all_keys if
        isinstance(data1.get(k), dict) and isinstance(data2.get(k), dict))
    # Работаем циклом по всем сортированным ключам
    for key in sorted(all_keys):
        # Значение из первого словаря
        value1 = data1.get(key)
        # Значение из второго словаря
        value2 = data2.get(key)
        # Если ключ в наборе вложенных словарей
        if key in nested_keys:
            # то рекурсивно вызываем функцию make_diff
            child_diff = make_diff(value1, value2)
            # если получен дифф, то добавляем его в результат
            if child_diff:
                diff.append({
                    'key': key, 'operation': 'nested', 'value': child_diff
                })
        # Если значений1 не равно значению 2
        elif value1 != value2:
            # то присваиваем значению operation статус change
            # или добавлен, если только во втором словаре
            # в других случаях removed
            operation = 'changed' if key in data1 and key in data2 \
                else 'add' if key in data2 else 'removed'
            # добавляем в результат
            diff.append({
                'key': key, 'operation': operation, 'old': value1, 'new': value2
            })
        # Иначе ключи равны, добавляем результат со статусом same
        else:
            diff.append({
                'key': key, 'operation': 'same', 'value': value1
            })
    # Вернуть дифф
    return diff
