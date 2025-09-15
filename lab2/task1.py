input_str = input().strip()
if not input_str:
    print("")
    exit()

answer = []
same_letters_counter = 1

for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]:
        same_letters_counter += 1
    else:
        answer.append(str(same_letters_counter) if same_letters_counter > 1 else "")
        answer.append(input_str[i - 1])
        same_letters_counter = 1

answer.append(str(same_letters_counter) if same_letters_counter > 1 else "")
answer.append(input_str[-1])

print("".join(answer))
