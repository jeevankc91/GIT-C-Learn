import sched, time
import ctypes
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    ctypes.windll.user32.MessageBoxA(0,"It's time to roll your eyes", "EYE CARE", 1)
    # do your stuff
    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
