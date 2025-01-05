tasks = [
    {'time': 3, 'reward': 10},
    {'time': 2, 'reward': 5},
    {'time': 1, 'reward': 8},
    {'time': 4, 'reward': 7}
]

def optimizeTaskProcedural(tasks):
    tasks.sort(key=lambda x: -x['reward'] / x['time'])

    total_reward = 0
    total_time = 0
    task_order = []

    for task in tasks:
        task_order.append(task)
        total_time += task['time']
        total_reward += task['reward']

    return total_reward, task_order

print(optimizeTaskProcedural(tasks))

#Funkcyjnie

def optimizeTaskMapSort(tasks):
    key_func = lambda task: -task['reward'] / task['time']

    sorted_task = sorted(tasks, key=key_func)

    total_reward = sum(map(lambda task: task['reward'], sorted_task))

    return total_reward, sorted_task

print(optimizeTaskMapSort(tasks))