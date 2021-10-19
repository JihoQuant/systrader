CALL C:\Users\%username%\Anaconda3x86\Scripts\activate.bat
python C:\Users\%username%\quantylab-systrader\bin\creon\kill.py
python C:\Users\%username%\quantylab-systrader\quantylab\systrader\creon\_creon.py disconnect
python C:\Users\%username%\quantylab-systrader\quantylab\systrader\creon\_creon.py connect --id=%1 --pwd=%2 --pwdcert=%3
START CMD /C CALL C:\Users\%username%\quantylab-systrader\bin\creon\run_bridge.bat ^& PAUSE
START CMD /C CALL C:\Users\%username%\quantylab-systrader\bin\creon\run_pub.bat ^& PAUSE
