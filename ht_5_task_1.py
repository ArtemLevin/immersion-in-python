file_path = "C:/Users/User/Documents/example.txt"

def get_file_info(file_path):
    result = []
    result.append(file_path[len(file_path)-file_path[::-1].index(".")-1:])
    file_path = file_path[:len(file_path)-file_path[::-1].index(".")-1]
    result.append(file_path[len(file_path)-file_path[::-1].index("/"):])
    result.append(file_path[:len(file_path) - file_path[::-1].index("/")])
    return tuple(result[::-1])

print(get_file_info(file_path))