
import os
for i in range(1, 3):

    with open(f'file_{i}.txt', 'w+', encoding='utf-8') as f:
        print(f'writing file {i=}', file=f)


def rename_files(desired_name, num_digits, source_ext, target_ext):
    i = 1
    for name in [x for x in os.listdir() if x.endswith(source_ext)]:
        os.rename(name, f"{desired_name}{str(0) * (num_digits - len(str(i)))}{i}.{target_ext}")
        i += 1

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
