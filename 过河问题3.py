import copy
from itertools import combinations

"""
1.n=3,m=2时的情况请写出模型，并编程序完成策略。
2.n=4,m=2时，策略是否有解? 请给出最佳策略。
3.当n>4,m>=2时，请寻找一种有解的情况，并给出最佳策略。
"""

n = 5
m = 5


def is_valid_state(state):
    # 检查每一岸的状态是否合法
    for bank in state:
        # 一个岸边的商人数量
        num_merchants = state[bank].count('M')
        # 一个岸边的随从数量
        num_followers = state[bank].count('F')
        # 判断合法性
        if num_followers > num_merchants > 0:
            return False
    return True


def is_valid_repeat(state, path):
    # 检查path中的状态重复
    for i in path:
        # 判断路径中重复的状态，通过比较一个岸上的商人和随从的数量
        num_merchants = state["left"].count("M")
        num_followers = state["left"].count('F')
        num_merchants1 = i["left"].count("M")
        num_followers1 = i["left"].count('F')
        # 如果两个数量均相等，则返回重复结果
        if num_followers == num_followers1 and num_merchants == num_merchants1:
            return True
    return False


def generate_next_states(state):
    next_states = []
    banks = ['left', 'right']

    # 遍历每个岸的商人和随从组合
    for bank in banks:
        merchants = [x for x in state[bank] if x == 'M']
        followers = [x for x in state[bank] if x == 'F']
        people_combinations = []

        # 生成商人和随从的所有组合
        for i in range(1, m + 1):
            for combination in combinations(merchants + followers, i):
                people_combinations.append(combination)
        # 去除重复组合
        people_combinations = list(set(people_combinations))
        # 遍历每个组合，尝试将它们移动到对岸
        for combination in people_combinations:
            new_state = copy.deepcopy(state)
            for person in combination:
                new_state[bank].remove(person)  # state[bank][person]
                new_state[banks[1 - banks.index(bank)]].append(person)  # state[bank][person]
            if is_valid_state(new_state):
                next_states.append(new_state)

    return next_states


# 移除生成的下一个状态列表中重复的状态
def removeRepeat(states):
    new_list = []
    for element in states:
        if is_valid_repeat(element, new_list) is not True:
            new_list.append(element)
    return new_list


def output(state, path):
    with open("result/n" + str(n) + "m" + str(m) + ".txt", mode="a") as f:
        for i, state in enumerate(path):
            print(f"Step {i + 1}: {state}", file=f)
        print("----------------------------------------", file=f)


def traverse_path(state, path):
    if not state["left"]:
        output(state, path)
        return
    next_states = generate_next_states(state)
    next_states = removeRepeat(next_states)
    if goal_state in next_states:
        traverse_path(goal_state, path + [goal_state])
    for next_state in next_states:
        if is_valid_repeat(next_state, path) is not True:
            traverse_path(next_state, path + [next_state])


# 初始状态
initial_state = {'left': ["M" for i in range(n)] + ["F" for i in range(n)], 'right': []}
# 目标状态
goal_state = {'left': [], 'right': ["M" for i in range(n)] + ["F" for i in range(n)]}

# 开始遍历
traverse_path(initial_state, [initial_state])
print("end")
