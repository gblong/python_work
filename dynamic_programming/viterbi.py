import numpy as np

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

    V = np.zeros((T, N))  # Viterbi 表
    backtrack = np.zeros((T, N), dtype=int)  # 回溯表

    # 初始化
    for i in range(N):
        V[0, i] = start_p[i] * emit_p[i, obs[0]]

    # 递推
    for t in range(1, T):
        for j in range(N):
            prob, state = max((V[t-1, i] * trans_p[i, j], i) for i in range(N))
            V[t, j] = prob * emit_p[j, obs[t]]
            backtrack[t, j] = state

    # 终止
    best_last_state = np.argmax(V[T-1])

    # 回溯找到最优路径
    best_path = [best_last_state]
    for t in range(T-1, 0, -1):
        best_path.insert(0, backtrack[t, best_path[0]])

    return [states[i] for i in best_path]

# 定义HMM模型
states = ['Sunny', 'Rainy']
obs = ['walk', 'shop', 'clean']
obs_map = {name:index for index, name in enumerate(obs)}
obs_seq = [obs_map['walk'], obs_map['shop'], obs_map['clean']]

start_p = np.array([0.6, 0.4])  # 初始概率
trans_p = np.array([[0.7, 0.3], [0.4, 0.6]])  # 状态转移概率
emit_p = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])  # 观测概率

# 运行维特比算法
best_path = viterbi(obs_seq, states, start_p, trans_p, emit_p)
print("最可能的状态序列:", best_path)

