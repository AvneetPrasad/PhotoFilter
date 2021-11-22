import time
import threading
from PhotoFilter import *

start = time.time()

thread = threading.Thread(target = photoFilter)


thread.start()
thread.join()

end = time.time()

print("Photo Filter has run for ", end - start)