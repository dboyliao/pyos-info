from string import ascii_uppercase


def camel_to_pyname(name: str):
    n_chars = len(name)
    if n_chars < 2:
        return name
    words = []
    slow = 0
    fast = 1
    while fast < n_chars:
        end_char = name[fast]
        if end_char in ascii_uppercase:
            words.append(name[slow:fast])
            slow = fast
        fast += 1
    else:
        words.append(name[slow:fast])

    return "_".join(words)
