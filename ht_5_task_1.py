file_path = ['C:/Users/User/Documents/example.txt',
                 '/home/user/data/file',
                 'D:/myfile.txt',
                 'C:/Projects/project1/code/script.py',
                 '/home/user/docs/my.file.with.dots.txt',
                 'file_in_current_directory.txt']


# def get_file_info(file_path):
#     result = []
#     result.append(file_path[len(file_path)-file_path[::-1].index(".")-1:])
#     file_path = file_path[:len(file_path)-file_path[::-1].index(".")-1]
#     result.append(file_path[len(file_path)-file_path[::-1].index("/"):])
#     result.append(file_path[:len(file_path) - file_path[::-1].index("/")])
#     return tuple(result[::-1])
#
# print(get_file_info(file_path))


def get_file_info(file_path):
    result = []

    if "." not in file_path:
        result.append("." + file_path[len(file_path) - file_path[::-1].index("/"):])
        result.append("")
        result.append(file_path[:len(file_path) - file_path[::-1].index("/")])
        return tuple(result[::-1])
    elif "/" in file_path:
        result.append(file_path[len(file_path) - file_path[::-1].index(".") - 1:])
        file_path = file_path[:len(file_path) - file_path[::-1].index(".") - 1]
        result.append(file_path[len(file_path) - file_path[::-1].index("/"):])
        result.append(file_path[:len(file_path) - file_path[::-1].index("/")])
        return tuple(result[::-1])
    elif "/" not in file_path:
        result.append(file_path[len(file_path) - file_path[::-1].index(".") - 1:])
        result.append(file_path[:len(file_path) - file_path[::-1].index(".") - 1])
        result.append("")
        return tuple(result[::-1])

for el in file_path:
    print(get_file_info(el))
