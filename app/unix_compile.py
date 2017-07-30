import sys
import subprocess
from subprocess import call

"""Compile the code with the corresponding tools"""
def codeCompile(file_type, files):
    print("Exeucting Language:")
    output_file = language[file_type](files)
    #reset()
    with open(output_file, "r") as f:
        return f.read()


def parse(save_file, command):
    f = open(save_file, "w")
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in proc.stdout:
        sys.stdout.write(line.decode('utf-8'))
        f.write(line.decode('utf-8'))
    proc.wait


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
        compile_command = ["gcc", "-pedantic-errors", "-Wall", "-c", cfile]
        parse(compile_file, compile_command)
        # Prepare Object files
        ofiles.append(cfile[:-1])
        ofiles[len(ofiles) - 1] += "o"
        #print(ofiles[len(ofiles) - 1])
    # Link
    object_command = ["gcc", "-o", "code"] + ofiles
    parse(compile_file, object_command)
    #Execute
    exec_command = ["./code"]
    parse(exec_file, exec_command)
    return exec_file


"""C++ Code - Compile, Link, Execute"""
def langCpp(cppfiles):
    ofiles = []
    for cfile in cfiles:
        # Compile
        compile_command = ["g++", "-pedantic-errors", "-Wall", "-c", cfile]
        parse(compile_file, compile_command)
        # Prepare Object files
        ofiles.append(cfile[:-3])
        ofiles[len(ofiles) - 1] += "o"
        #print(ofiles[len(ofiles) - 1])
    # Link
    object_command = ["g++", "-o", "code"] + ofiles
    parse(compile_file, object_command)
    #Execute
    exec_command = ["./code"]
    parse(exec_file, exec_command)
    return exec_file


"""Java Code - Compile, Execute"""
def langJava(javafiles):
    exec_name = javafiles[0][:-5]
    for javafile in javafiles:
        # Compile
        with open(compile_file, "a") as outfile:
            compile_command = ["javac", javafile]
            subprocess.call(compile_command, stderr=outfile)
        compile_command = ["javac", javafile, "&>>", compile_file]
        subprocess.call(compile_command)
    # Execute
    exec_command = ["java", exec_name, "&>>", exec_file]
    subprocess.call(exec_command)


"""JavaScript Code - Execute"""
def langJS(jsfiles):
    exec_command = ["node", jsfiles[0]]
    parse(exec_file, exec_command)
    return exec_file


"""Python Code - Execute"""
def langPy(pyfiles):
    exec_command = ["python3", pyfile[0]]
    parse(exec_file, exec_command)
    return exec_file


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

#files = ["text.py"]
#codeCompile("Python", files);
#print("Exit!")
