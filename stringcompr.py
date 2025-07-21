def compress(chars):
    i = 0
    result = []

    while i < len(chars):
        char = chars[i]
        count = 1
        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        result.append(char)
        if count > 1:
            result.extend(list(str(count)))
        i += 1

    print("Compressed Output:", result)
    return len(result)


# Example usage
chars = ["a", "a", "b", "b", "c", "c", "c"]
compress(chars)
