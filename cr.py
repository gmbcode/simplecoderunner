import os
import sys
import argparse
parser = argparse.ArgumentParser(
                    prog='C / CPP Runner',
                    description='Runs the C/C++ file after compiling it')
parser.add_argument('filename',type=str,help='The filename to run')
parser.add_argument('optimization',type=str,choices=['O0','O1','O2','O3','Ofast','Og','Os'],default='O0',help='The level of optimization to compile with',nargs='?')
args = parser.parse_args()

ext_code = None
ext_map = {'cpp' : 'g++' , 'c' : 'gcc' }
if os.path.isfile(args.filename) and os.access(args.filename,os.R_OK):
    if '.' in args.filename:
        pass
    else :
        raise Exception("Invalid file extension")
    if len(os.path.dirname(args.filename)) > 1 :
        arg_dir = os.path.dirname(args.filename)
    else:
        arg_dir = os.getcwd()
    args.filename = os.path.basename(args.filename)
    if args.filename.split('.')[-1] in ['cpp','c']:
        ext_code = ext_map[args.filename.split('.')[-1]]
    else :
        raise Exception("Invalid file extension")
else:
    raise Exception("File does not exist / File is not accessible")
os.chdir(arg_dir)
print(f"{ext_code} {args.filename} -{args.optimization} -o {args.filename.split('.')[0]}.exe")
e_code_1 = os.system(f"{ext_code} {args.filename} -{args.optimization} -o {args.filename.split('.')[0]}.exe")
if e_code_1 != 0 :
    print("Error compiling code " )
    sys.exit(1)
print(f"{ext_code} exited successfully with exit code {e_code_1}")
print(f"Running {args.filename.split('.')[0]}.exe ")
e_code_2 = os.system(f"{args.filename.split('.')[0]}.exe ")
print(f"Program exited successfully with exit code {e_code_2}")
sys.exit(0)



