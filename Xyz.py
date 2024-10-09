#coding=utf-8
import os, sys, platform
os.system("git pull")
os.system('rm -rf JD.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf JD.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('JD.so'):
        os.system('curl -L https://github.com/younis-dgk/Xyz/blob/main/JD.cpython-312.so?raw=true -o JD.so') 
        import JD
    else:
        import JD
 
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m Sorry Baby 32 Bit Not Supported! 🥺💔\033[1;90m]");exit()
 
 
 
