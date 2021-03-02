from progressbar import ProgressBar
import time

bar = ProgressBar(maxval=100)
bar.start()

for i in range(1, 101):
    bar.update(i)
    time.sleep(0.025)

bar.finish()
