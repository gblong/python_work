"""
HMM(隐马尔可夫模型)是用来描述隐含未知状态的统计模型
HMM特点:
1. 未来状态只依赖于当前状态，与过去状态无关（即 无记忆性）。
2. 观测值由隐藏状态生成，并且只依赖于当前状态。
举一个经典的例子：一个东京的朋友每天根据天气['Sunny', 'Rainy']决定当天的活动['walk', 'shop', 'clean']中的一种，
我每天只能在twitter上看到她发的推"我前天公园散步、昨天购物、今天清理房间了"
那么我可以根据她发的推特推断东京这三天的天气。在这个例子里，显状态是活动，隐状态是天气。
维特比算法 是一种 动态规划算法,用于在隐马尔可夫模型(HMM, Hidden Markov Model)中寻找最可能的隐藏状态序列推断

算法步骤:
1. 初始化：计算初始时刻每个状态的最大概率及其路径。
2. 递归：对于每个后续时刻，计算每个状态的最大概率及其路径，基于前一时刻的结果。
3. 终止：在最后一个时刻，选择概率最大的状态作为终点。
4. 回溯：从终点回溯，得到完整的最优状态序列。
"""

states = ['Sunny', 'Rainy']
observations = ['walk', 'shop', 'clean']
start_probability = {'Sunny': 0.6, 'Rainy': 0.4}

transition_probability = {
    'Sunny' : {'Sunny': 0.7, 'Rainy': 0.3},
    'Rainy' : {'Sunny': 0.4, 'Rainy': 0.6},
    }
 
emission_probability = {
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
}

def viterbi(obs, states, start_p, trans_p, emit_p):
    """
    :param obs: 观测序列
    :param states: 隐状态集合
    :param start_p: 初始状态概率
    :param trans_p: 状态转移概率矩阵
    :param emit_p: 观测概率矩阵
    :return: 最可能的状态序列
    """
    T = len(obs)
    N = len(states)

    V =         [[0] * N for _ in range(T)] # Viterbi表，存储到当前时刻的最高概率
    backtrack = [[0] * N for _ in range(T)] # 回溯表，存储最优路径的前一个状态，以便回溯找到最优路径

    # 初始化
    for i in range(N):
        V[0][i] = start_p[i] * emit_p[i][obs[0]]

    # 递推
    for t in range(1, T):
        for j in range(N):
            prob, from_state = max((V[t-1][i] * trans_p[i][j], i) for i in range(N))
            V[t][j] = prob * emit_p[j][obs[t]]
            backtrack[t][j] = from_state

    # 终止
    best_last_state = max(range(len(V[T-1])), key=lambda i: V[T-1][i])

    # 回溯找到最优路径
    best_path = [best_last_state]
    for t in range(T-1, 0, -1):
        best_path.insert(0, backtrack[t][best_path[0]])

    return [states[i] for i in best_path]

# 定义HMM模型
states = ['Sunny', 'Rainy']
obs = ['walk', 'shop', 'clean']
obs_map = {name:index for index, name in enumerate(obs)}
obs_seq = [obs_map['walk'], obs_map['shop'], obs_map['clean']]

start_p = [0.6, 0.4]  # 初始概率
trans_p = [[0.7, 0.3], [0.4, 0.6]]  # 状态转移概率
emit_p = [[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]]  # 观测概率

# 运行维特比算法
best_path = viterbi(obs_seq, states, start_p, trans_p, emit_p)
print("最可能的状态序列:", best_path)

