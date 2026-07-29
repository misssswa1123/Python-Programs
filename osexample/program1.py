import os as a

if not a.path.exists('swapnali'):
    a.mkdir('swapnali')

# for i in range(1,11):
#     a.mkdir(f"osexample/file{i}")

# for i in range(1,11):
#     a.rename(f'osexample/file{i}',f'osexample/direct{i}')

# folder=a.listdir('osexample')
# print(folder)

# cmd='date'
# a.system(cmd)
print(a.getcwd())
a.chdir('osexample')
print(a.getcwd())

for i in range(1,11):
    a.rmdir(f'direct{i}')