def time_signature(time_sig):
    if time_sig == 4:
        print("We're going to play in 4/4 time")
        return True
    elif time_sig == 3:
        print("We're going to play in 3/4 time")
        return True
    else:
        print("Unsupported time signature!")
        return False