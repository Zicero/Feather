import subprocess
from subprocess import call

def codeCompile(file_type, files):
    print("Exeucting Language:")
    language[file_type](files)


"""C Code - Compile, Link, Execute"""
def langC(cfiles):
    ofiles = []
    # Script
    script_command = ["script"] + compile_file
    subprocess.call(script_command, shell=True)
    # Build C File
    for cfile in cfiles:
        # Compile
        compile_command = ["gcc", "-ansi", "-pedantic-errors", "-Wall", "-c", cfile] + compile_file
        subprocess.call(compile_command, shell=True)
        # Prepare Object files
        ofiles.append(cfile[:-1])
        ofiles[len(ofiles) - 1] += "o";
        #print(ofiles[len(ofiles) - 1])
    # Link
    object_command = ["gcc", "-o", "code"] + ofiles + compile_file
    subprocess.call(object_command, shell=True)
    #Execute
    exec_command = ["./code"] + exec_file
    subprocess.call(exec_command, shell=True)
    # End Script
    subprocess.call("exit", shell=True)


"""Python Code - Execute"""
def langPy(pyfiles):
    for pyfile in pyfiles:
        exec_command = ["py", pyfile]
        subprocess.call(exec_command, shell=True)


"""JavaScript Code - Execute"""
def langJS(jsfiles):
    print("WIP")


"""Dictionary of Supported Languages"""
language = {"C": langC, "Python": langPy, "JavaScript": langJS}
compile_file = ["compile_file.txt"]
exec_file = ["exec_file.txt"]

files = ["test.c", "cool.c"]
codeCompile("C", files);
print("Exit!")
