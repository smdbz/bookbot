def word_count(text):
    return len(text.split())


def character_count(text):
    result = {}
    text = text.lower()
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def sort_on(items):
    return items["num"]


def create_sorted_list(dictionary):
    result = []
    for key in dictionary:
        record = {"char": key, "num":dictionary[key]}
        result.append(record)

    result.sort(reverse=True, key=sort_on)
    return result
