def solution(s):

    result = '_'
    unique_char = {}
    repeated_char = {}

    for idx, char in enumerate(s):
        if char not in unique_char and char not in repeated_char:
            # Register in unique_char dict
            unique_char[char] = idx

        elif char in unique_char:
            # Unregister from unique_char dict
            unique_char.pop(char)

            # Register in repeated_char dict
            repeated_char[char] = idx

    if unique_char:
        sort_orders = sorted(unique_char.items(), key=lambda x: x[1], reverse=False)

        # sort_order looks like [('c', 3), ('d', 7)]
        # We need key of second occurence with minimal index
        result = sort_orders[0][0]

    return result

print(solution('abacabad'))