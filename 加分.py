# 要覆写的英文字母映射
letters = {
    '7.html': {'row1': 285, 'row2': 300, 'letter1': 'N', 'letter2': 'S'},
    '8.html': {'row1': 285, 'row2': 300, 'letter1': 'N', 'letter2': 'S'},
    '9.html': {'row1': 285, 'row2': 300, 'letter1': 'N', 'letter2': 'S'},
    '10.html': {'row1': 285, 'row2': 300, 'letter1': 'N', 'letter2': 'S'},
    '11.html': {'row1': 285, 'row2': 300, 'letter1': 'F', 'letter2': 'T'},
    '12.html': {'row1': 285, 'row2': 300, 'letter1': 'F', 'letter2': 'T'},
    '13.html': {'row1': 285, 'row2': 300, 'letter1': 'F', 'letter2': 'T'},
    '14.html': {'row1': 285, 'row2': 300, 'letter1': 'F', 'letter2': 'T'},
    '15.html': {'row1': 285, 'row2': 300, 'letter1': 'J', 'letter2': 'P'},
    '16.html': {'row1': 285, 'row2': 300, 'letter1': 'J', 'letter2': 'P'},
    '17.html': {'row1': 285, 'row2': 300, 'letter1': 'J', 'letter2': 'P'},
    '18.html': {'row1': 285, 'row2': 300, 'letter1': 'J', 'letter2': 'P'}
}

# 执行覆写操作
for filename, positions in letters.items():
    row1 = positions['row1']
    row2 = positions['row2']
    letter1 = positions['letter1']
    letter2 = positions['letter2']

    # 读取目标文件的内容
    with open(filename, 'r', encoding='utf-8') as target_file:
        target_lines = target_file.readlines()

    # 确保目标文件至少有指定的行数
    while len(target_lines) < max(row1, row2):
        target_lines.append('\n')

    # 覆写指定位置的英文字母
    target_lines[row1 - 1] = target_lines[row1 - 1][:12] + letter1 + target_lines[row1 - 1][13:]
    target_lines[row2 - 1] = target_lines[row2 - 1][:12] + letter2 + target_lines[row2 - 1][13:]

    # 写回目标文件
    with open(filename, 'w', encoding='utf-8') as target_file:
        target_file.writelines(target_lines)

print("已完成覆写操作。")
