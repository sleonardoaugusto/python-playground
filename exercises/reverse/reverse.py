def reverse_alpha(string):
    temp = list(string)
    h = 0

    for left_idx in range(len(string)):
        left_char = string[left_idx]

        if left_char.isalpha():
            for right_idx in range(len(string) - h - 1, left_idx, -1):
                right_char = string[right_idx]
                h += 1

                if right_char.isalpha():
                    temp[left_idx] = right_char
                    temp[right_idx] = left_char
                    break

    return ''.join(temp)
