import subprocess
from subprocess import call

"""Compile the code with the corresponding tools"""
def codeCompile(file_type, files):
    print("Exeucting Language:")
    # Compile
    language[file_type](files)
    #reset()


"""Clear the files after storing the data"""
def reset():
    with open(compile_file, "w"):
        pass
    with open(exec_file, "w"):
        pass


"""C Code - Compile, Link, Execute"""
def langC(cfiles):
    ofiles = []
    for cfile in cfiles:
        # Compile
        compile_command = ["gcc", "-ansi", "-pedantic-errors", "-Wall", "-c", cfile, "2>>", compile_file]
        subprocess.call(compile_command, shell=True)
        # Prepare Object files
        ofiles.append(cfile[:-1])
        ofiles[len(ofiles) - 1] += "o";
        #print(ofiles[len(ofiles) - 1])
    # Link
    object_command = ["gcc", "-o", "code"] + ofiles + ["2>>", compile_file]
    subprocess.call(object_command, shell=True)
    #Execute
    exec_command = ["code", "1>>", exec_file]
    subprocess.call(exec_command, shell=True)



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


"""Files"""
compile_file = "compile_file.txt"
exec_file = "exec_file.txt"
source_folder = "test_code"

#files = ["test.c", "cool.c"]
#codeCompile("C", files);
#print("Exit!")
