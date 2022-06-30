import subprocess
import sys
import os

class RunPyCode(object):
    def __init__(self, typecode, inp, code=None):
        self.inp = inp
        self.code = code
        self.typeocde=typecode
        if not os.path.exists('running'):
            os.mkdir('running')

    def executeC(self, inp):    

        try:
            stdout = []
            for dat in inp:
                data, temp = os.pipe()
            
                os.write(temp, bytes(dat, "utf-8"))
                os.close(temp)

                output = subprocess.check_output("gcc HelloWorld.c -o out1", shell = True,cwd="./running", stderr=subprocess.STDOUT)
                s = subprocess.check_output("out1", stdin = data, cwd="./running", shell = True, stderr=subprocess.PIPE)
                stdout.append(s.decode("utf-8"))
                self.stderr=None
            self.stdout = stdout
            
        
        except subprocess.CalledProcessError as e:
             self.stderr= e.output.decode()
             self.stdout=None
             
        except Exception as e:
            # check_call can raise other exceptions, such as FileNotFoundError
            self.stderr = str(e)
            self.stdout=None
    
    def executeCpp(self, inp):
    
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
                self.stderr=None
            self.stdout=stdout    

        except subprocess.CalledProcessError as e:
             self.stderr= e.output.decode()
             self.stdout=None
             
        except Exception as e:
            # check_call can raise other exceptions, such as FileNotFoundError
            self.stderr = str(e)
            self.stdout=None
    
    def executeJava(self, inp):
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
                self.stderr=None
            self.stdout = stdout

        except subprocess.CalledProcessError as e:
             self.stderr= e.output.decode()
             self.stdout=None
        except Exception as e:
            # check_call can raise other exceptions, such as FileNotFoundError
            self.stderr = str(e)
            self.stdout=None

    def executePython(self, inp, cmd="./running/a.py"):
        stdout = []
        cmd = [sys.executable, cmd]
        for dat in inp:
            output = subprocess.run('docker run -i python:0.3', shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,input=dat.encode())
            actual = output.stdout.decode().strip('\n')
            # data, temp = os.pipe()    
        
            # os.write(temp, bytes(dat, "utf-8"))
            # os.close(temp)  

            # p = subprocess.Popen(cmd, shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin = data)
            # result = output.wait()
            
            # a, b = output.communicate()
            # stdout.append(a.decode("utf-8"))
            # self.stderr = b.decode("utf-8")
            stdout.append(actual)
            self.stderr = output.stderr.decode()

        self.stdout = stdout

    def writecode(self, filename, code=None):
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
            f.close()


    def run_py_code(self, typecode,inp, code=None):
        if(typecode=='C'):
            filename = "./running/HelloWorld.c"
            self.writecode(filename,code)
            self.executeC(inp)

        elif(typecode=='C++'):
            filename = "./running/HelloWorld.cpp"
            self.writecode(filename,code)
            self.executeCpp(inp)

        elif(typecode=='Java'):
            filename = "./running/Hello.java"
            self.writecode(filename,code)
            self.executeJava(inp)

        elif(typecode=='Python'):
            filename = "./running/a.py"
            self.writecode(filename,code)
            self.executePython(inp)

        return self.stderr, self.stdout