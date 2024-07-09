# Unit 3.2

def get_third_teacher():
    with open('data/teachers.txt') as f:
        lines = f.readlines()
    return lines[2]
