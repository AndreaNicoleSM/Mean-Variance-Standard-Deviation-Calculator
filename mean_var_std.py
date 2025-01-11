import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    userMatrix = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [np.mean(userMatrix, axis=0).tolist(), np.mean(userMatrix, axis=1).tolist(), np.mean(userMatrix)],
        'variance': [np.var(userMatrix, axis=0).tolist(), np.var(userMatrix, axis=1).tolist(), np.var(userMatrix)],
        'standard deviation': [np.std(userMatrix, axis=0).tolist(), np.std(userMatrix, axis=1).tolist(), np.std(userMatrix)],
        'max': [np.max(userMatrix, axis=0).tolist(), np.max(userMatrix, axis=1).tolist(), np.max(userMatrix)],
        'min': [np.min(userMatrix, axis=0).tolist(), np.min(userMatrix, axis=1).tolist(), np.min(userMatrix)],
        'sum': [np.sum(userMatrix, axis=0).tolist(), np.sum(userMatrix, axis=1).tolist(), np.sum(userMatrix)]
}

    return calculations