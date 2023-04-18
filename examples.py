from collections import Counter


def get_task1():
    return [20, 13, 32, 7, 11, 25, 107]
def check_task1():
    res_min, res_max = task1()
    expect_list = get_task1()
    expect_min, expect_max = min(expect_list), max(expect_list)

    assert res_min == expect_min and res_max == expect_max

    print("Task 1 success!")

# Повернути найменший та найбільший елемент масиву
def task1():
    array = get_task1()
    res_min = array[0]
    res_max = array[0]

    for element in array:
        if element > res_max:
            res_max = element

        if element < res_min:
            res_min = element

    return res_min, res_max

def get_task2():
    return [12, 32, 77, 15, 3, 104]
def check_task2():
    res = task2()
    expect = sum(get_task2())

    assert res == expect

    print("Task 2 success!")

# Порахувати суму елементів масиву
def task2():
    array = get_task2()
    result = 0

    for element in array:
        result = result + element

    return result

def get_task3():
    return [5, 10, 22, 15, 31, 7]
def check_task3():
    task_res = task3()
    expect = list(reversed(get_task3()))

    assert len(task_res) == len(expect)

    for i in range(len(task_res)):
        assert task_res[i] == expect[i]

    print("Task 3 success!")

# Віддзеркалити та повернути масив
def task3():
    array = get_task3()
    len_array = len(array)

    result = [None] * len_array
    """ for i in range(len_array-1, -1, -1):
        index_result = len_array-1 - i
        result[index_result] = array[i] """
    
    for index_result in range(len_array):
        i = len_array-1 - index_result
        result[index_result] = array[i]

    return result

def get_task4():
    return [3, 5, 7, 2, 3, 1, 5, 5, 8, 8, 9]
def check_task4():
    res = task4()
    expect = Counter(get_task4())
    expect = len({k: v for k, v in expect.items() if v >= 2})

    assert res == expect

    print("Task 4 success!")

# Визначити кількість елементів, які зустрічаються 2 або більше разів
def task4():
    array = get_task4()
    result = 0

    found_once = []
    found_more = []

    for element in array:
        if element in found_more:
            continue
        elif element in found_once:
            result += 1
            found_once.remove(element)
            found_more.append(element)
        else:
            found_once.append(element)

    return result

def get_task5():
    return [3, 5, 7, 2, 3, 1, 5, 5, 8, 8, 9]
def check_task5():
    res = task5()
    expect = Counter(get_task5())

    expect = {k: v for k, v in expect.items() if v == 1}

    assert len(res) == len(expect)
    for key in expect:
        assert key in res

    print("Task 5 success!")

# Повернути масив з елементів, які зустрічаються лише один раз
def task5():
    array = get_task5()

    found_once = []
    found_more = []

    for element in array:
        if element in found_more:
            continue
        elif element in found_once:
            found_once.remove(element)
            found_more.append(element)
        else:
            found_once.append(element)

    result = found_once
    return result

def get_task6():
    return [1, 3, 4, 6, 7, 11, 13, 15], 9
def check_task6():
    res = task6()
    expect = get_task6()
    expect[0].append(expect[1])

    expect = expect[0]
    expect.sort()

    assert len(res) == len(expect)
    for i in range(len(expect)):
        assert res[i] == expect[i]

    print("Task 6 success!")

# Вхід: відсортований масив та новий елемент
# Додати новий елемент у масив так, щоб від залишився відсортованим
def task6():
    array, new_element = get_task6()
    result = None

    for i in range(len(array)):
        if new_element < array[i]:
            result = array[:i] + [new_element] + array[i:]
            break

    return result


if __name__ == "__main__":
    check_task1()
    check_task2()
    check_task3()
    check_task4()
    check_task5()
    check_task6()