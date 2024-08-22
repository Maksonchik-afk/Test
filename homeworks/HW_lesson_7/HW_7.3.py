def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1 or not some_str:
        return None
    second_occurrence_index = text.find(some_str, first_index + len(some_str))

    return second_occurrence_index if second_index != -1 else None


result = second_index("Hello, hello", "lo")
print(result)
