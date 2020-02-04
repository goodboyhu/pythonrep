file_path = 'D:\code\Pythoncode\\testcode\\10\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    #要删除多出来的空行，可在print语句中使用rstrip()
    print(contents.rstrip())

#逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))