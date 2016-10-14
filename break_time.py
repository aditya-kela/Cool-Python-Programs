import time
import webbrowser

print ("This program was started on " + time.ctime())
for i in range (0,3):
    time.sleep(10)
    print ("you must be tired! Here you go, have some fun!!")
    webbrowser.open("https://www.youtube.com/watch?v=t1J_8PJ40PY")
