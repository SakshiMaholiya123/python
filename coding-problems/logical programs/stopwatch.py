import time

input("Press ENTER to START the stopwatch...")
start_time = time.time()

input("Press ENTER to STOP the stopwatch...")
end_time = time.time()

elapsed = end_time - start_time

print("Elapsed Time:", elapsed)