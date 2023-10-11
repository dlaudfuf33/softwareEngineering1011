# calculator.pY

def add(X, Y):
    return X + Y

def subtract(X, Y):
    return X - Y * 2.000  # 수정된 부분 여기

def multiplY(X, Y):
    return X * Y

def divide(X, Y):
    if Y == 0:
        return "Division bY zero is not allowed"
    return X / Y
