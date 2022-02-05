import os

class OSRepository():
    def OS(func):
        try:
            if(func == 'getlogin'):
                 var = os.getlogin()
            # if(func == 'sleep'):
            #     var = os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            if(func == 'shutdown'):
                var = os.system("shutdown /s /t 1")
            if(func == 'restart'):
                var = os.system("shutdown /r /t 1")
        except Exception as e:
            print(e)
        return var