def TransformToValidExpression(e):
    t = e.split()
    operators = ["*", "-", "+", "/"]
    for i in range(len(t) - 1):
        if t[i].isdigit() and t[i + 1] in operators and t[i + 2].isdigit() and (i + 3 < len(t) and t[i + 3] == ")"):
            t.insert(i + 3, "(")  # expl. 3 + 5

    j = 0
    while j < len(t):
        if t[j] == "(" and j >= 3:
            # Move '(' on position j-3. expl. ( 3 + 5
            t.pop(j)
            t.insert(j - 3, "(")
        j += 1

    # Insert difference of (,) on 0-th position
    difference = t.count(")") - t.count("(")
    helper_t = []
    for i in range(1, difference + 1):
        helper_t.append("(")
    result = helper_t + t
    joined_result = ' '.join(result)

    return joined_result


intput = input()  # input the expression. Remember to use spaces after each element.
print(TransformToValidExpression(intput))