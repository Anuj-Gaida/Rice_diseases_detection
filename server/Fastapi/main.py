import uvicorn 
from socket import gethostname,gethostbyname
from sys import path  as sys_path
from os import path as os_path
sys_path.append(os_path.abspath('../model/'))
sys_path.append(os_path.abspath('../../model/'))
if(__name__=="__main__"):
    uvicorn.run("app.app:app",host=gethostbyname(gethostname()),port=5000,reload=True)

    