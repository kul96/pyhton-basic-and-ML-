# pathlib -- object-oriented filesystem paths

#Absolute path
# ex. c:\program\wmap\www\kuldeep
#Relative path
# ex. folder present in current dirctory 
# like p directory

from pathlib import Path

path = Path("p")
# check path exists or not
print(path.exists())
# make a path
path = Path("a")
print(path.exists())
print(path.mkdir())

# remove dir
print(path.rmdir())

# print all file and dir
path = Path() # current path
#   * all file+dir
#   *.* only file not dir
print(path.glob('*'))
for file in path.glob('*'):
    print(file)

    


