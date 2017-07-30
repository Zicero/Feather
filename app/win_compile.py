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
        compile_command = ["gcc", "-pedantic-errors", "-Wall", "-c", cfile, "&>>", compile_file]
        subprocess.call(compile_command, shell=True)
        # Prepare Object files
        ofiles.append(cfile[:-1])
        ofiles[len(ofiles) - 1] += "o"
        #print(ofiles[len(ofiles) - 1])
    # Link
    object_command = ["gcc", "-o", "code"] + ofiles + ["&>>", compile_file]
    subprocess.call(object_command, shell=True)
    #Execute
    exec_command = ["code", "&>>", exec_file]
    subprocess.call(exec_command, shell=True)


"""C++ Code - Compile, Link, Execute"""
def langCpp(cppfiles):
    ofiles = []
    for cppfile in cppfiles:
        # Compile
        compile_command = ["g++", "-pedantic-errors", "-Wall", "-c", cppfile, "&>>", compile_file]
        subprocess.call(compile_command, shell=True)
        # Prepare Object files
        ofiles.append(cppfile[:-3])
        ofiles[len(ofiles) - 1] += "o"
    # Link
    object_command = ["g++", "-o", "code"] + ofiles + ["&>>", compile_file]
    subprocess.call(object_command, shell=True)
    #Execute
    exec_command = ["code", "&>>", exec_file]
    subprocess.call(exec_command, shell=True)


"""Java Code - Compile, Execute"""
def langJava(javafiles):
    exec_name = javafiles[0][:-5]
    for javafile in javafiles:
        # Compile
        compile_command = ["javac", javafile, "&>>", compile_file]
        subprocess.call(compile_command, shell=True)
    # Execute
    exec_command = ["java", exec_name, "&>>", exec_file]
    subprocess.call(exec_command, shell=True)


"""JavaScript Code - Execute"""
def langJS(jsfiles):
    print("WIP")


"""Python Code - Execute"""
def langPy(pyfiles):
    for pyfile in pyfiles:
        exec_command = ["py", pyfile, ">>", exec_file]
        subprocess.call(exec_command)


"""Dictionary of Supported Languages"""
language = {
    "C": langC,
    "C++": langCpp,
    "Java": langJava,
    "JavaScript": langJS,
    "Python": langPy
}


"""Files"""
compile_file = "compile_file.txt"
exec_file = "exec_file.txt"
source_folder = "test_code"

files = ["text.py"]
codeCompile("Python", files);
print("Exit!")
