#

task = "410 15 1225 243 2434 65 835 124 1359 1 259 187 1932 197 2016 89 1050 225 2275 35 563 191 1963 82 983 170 1774 62 806 191 1963 93 1084"

answer_sol = "410 15 13736 1 1 0 1 1 1 1 0 1 0 1 1 1 0 1 " # SOLUTION
answer_tmp = "410 15 13736 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 " # MY_RESULT

def getTask(task):
    task = task.split()[3:]
    task = [(int(task[i]), int(task[i+1])) for i in range(0, len(task), 2)]
    return task

def getAnswer(answer):
    answer = answer.split()
    ans_sum = answer[2]
    answer = answer[3:]
    return ans_sum, answer

def equation(task, answer):
    print("Equation (weight sum):")
    item_sum = 0
    for idx, ii in enumerate(answer):
        s = "=" if (idx == 0) else "+"
        print(f"{s}{int(ii)*int(task[idx][1])}", end='')
        item_sum += int(ii)*int(task[idx][1])
    print(end="\n\n")
    return item_sum

def printItems(task, answer):
    print(f"\nw:", end="\t")
    for i in task: print(i[0], end="\t")
    print(f"\nv:", end="\t")
    for i in task: print(i[1], end="\t")
    print(f"\n?:", end="\t")
    for a in answer: print(a, end="\t")
    print(end="\n\n")
    # for : print(i[0], end="\t")
    # print("\nv: ")
    # for i in task: print(i[1], end="\t")
    # print("\n?: ")
    # for a in answer: print(i[0], end="\t")
    # print()

# MAIN

task = getTask(task)
# print(task)

ans_sum, answer_sol = getAnswer(answer_sol)
ans_sum, answer_tmp = getAnswer(answer_tmp)

# print(answer, end='\n\n')

printItems(task, answer_sol)

# s = 0
# for idx, i in enumerate(answer):
#     s += int(i)*task[idx][0]

# print(s, end="\n\n")

item_sum = equation(task, answer_tmp)
item_sum = equation(task, answer_sol)

print(f"Answer ({ans_sum}) == sum(items) ({item_sum})? {int(ans_sum)==int(item_sum)}")
