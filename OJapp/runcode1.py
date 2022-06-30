import subprocess
import sys
import os

    # class RunPyCode(object):
    #     def __init__(self, typecode, inp, code=None):
    #         self.inp = inp
    #         self.code = code
    #         self.typeocde=typecode
    #         if not os.path.exists('running'):
    #             os.mkdir('running')
    # def compute(type):
    #     if(type=='C++'):
    #         return executeCpp()
    #     elif(type=='C'):
    #         return executeC()
    #     elif(type=='JAVA'):
    #         return executeJava()
    #     else:
    #         return executePython()
def executeC(inp):    

    try:
        stdout = []
        for dat in inp:
            data, temp = os.pipe()
        
            os.write(temp, bytes(dat, "utf-8"))
            os.close(temp)

            output = subprocess.check_output("gcc HelloWorld.c -o out1", shell = True,cwd="./running", stderr=subprocess.STDOUT)
            s = subprocess.check_output("out1", stdin = data, cwd="./running", shell = True, stderr=subprocess.PIPE)
            stdout.append(s.decode("utf-8"))
            stderr=None
        stdout = stdout
        
    except subprocess.CalledProcessError as e:
        stderr= e.output.decode()
        stdout=None
        
    except Exception as e:
        # check_call can raise other exceptions, such as FileNotFoundError
        stderr = str(e)
        stdout=None
    return stdout,stderr
def executeCpp(inp):

    try:
        stdout=[]
        for dat in inp:
            data, temp = os.pipe()

            os.write(temp, bytes(dat, "utf-8"))
            os.close(temp)

            output = subprocess.check_output("g++ HelloWorld.cpp -o out2", shell = True,cwd="./running", stderr=subprocess.STDOUT)
            p = subprocess.check_output('out2', stdin = data,cwd="./running",shell=True, stderr=subprocess.PIPE)
            stdout.append(p.decode("utf-8"))
            # print(p.decode("utf-8"))
            stderr=None
        stdout=stdout    
    except subprocess.CalledProcessError as e:
        stderr= e.output.decode()
        stdout=None
        
    except Exception as e:
        # check_call can raise other exceptions, such as FileNotFoundError
        stderr = str(e)
        stdout=None
    return stdout,stderr
def executeJava(inp):
    try:
        stdout = []
        for dat in inp:
            data, temp = os.pipe()    
    
            os.write(temp, bytes(dat, "utf-8"))
            os.close(temp)

            output = subprocess.check_output("javac Hello.java", shell = True,cwd="./running", stderr=subprocess.STDOUT)
            p = subprocess.check_output("java Hello", stdin = data,shell = True,cwd="./running", stderr=subprocess.PIPE)
            # self.stdout = p.decode("utf-8")
            stdout.append(p.decode("utf-8"))
            stderr=None
        stdout = stdout

    except subprocess.CalledProcessError as e:
        stderr= e.output.decode()
        stdout=None
    except Exception as e:
        # check_call can raise other exceptions, such as FileNotFoundError
        stderr = str(e)
        stdout=None
    return stdout,stderr
def executePython(inp, cmd="./running/a.py"):
    stdout = []
    cmd = [sys.executable, cmd]
    for dat in inp:
        # output = subprocess.run('docker run -i python:0.3', shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,input=dat.encode())
        # actual = output.stdout.decode().strip('\n')
        data, temp = os.pipe()    
    
        os.write(temp, bytes(dat, "utf-8"))
        os.close(temp)  

        p = subprocess.Popen(cmd, shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin = data)
        result = p.wait()
        
        a, b = p.communicate()
        stdout.append(a.decode("utf-8"))
        stderr = b.decode("utf-8")
        # stdout.append(actual)
        # stderr = output.stderr.decode()

    stdout = stdout
    return stdout,stderr

def writecode(filename, code=None):
    if not code:
        code = code
    with open(filename, "w") as f:
        f.write(code)
        f.close()


def run_py_code( typecode,inp, code=None):
    if(typecode=='C'):
        filename = "./running/HelloWorld.c"
        writecode(filename,code)
        return executeC(inp)

    elif(typecode=='C++'):
        filename = "./running/HelloWorld.cpp"
        writecode(filename,code)
        return executeCpp(inp)

    elif(typecode=='Java'):
        filename = "./running/Hello.java"
        writecode(filename,code)
        return executeJava(inp)

    elif(typecode=='Python'):
        filename = "./running/a.py"
        print("Aniket")
        writecode(filename,code)
        return executePython(inp)
    return 1,2    