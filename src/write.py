# Write to file
my_file = open("employees.txt", "w")
my_file.write("Mike")
my_file.close()

my_file = open("employees.txt", "w")
my_file.write("Mike\nJoe\nJenna")
my_file.close();

my_file = open("employees.txt", "r")
contents = my_file.read()
print(contents)

# append files

my_file = open("employees.txt", "a")
my_file.write("\nJack")
my_file.close()

my_file = open("employees.txt", "r")
contents = my_file.read()
print(contents)

help(my_file.seek)

# append and read

my_file = open("employees.txt", "a+")
my_file.seek(0)
content = my_file.read()
my_file.write("\nWalter")
my_file.close()

my_file = open("employees.txt", "r")
contents = my_file.read()
my_file.close()
print(contents)

# With context manager

with open("employees.txt", "a+") as my_file:
    my_file.write("\nWritten using with context manager")
    
with open("employees.txt", "r") as my_file:
    content = my_file.read()
    print(content)
