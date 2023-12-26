import time
from storage import BitStorage

max_bit = 9_999_999_999
num_of_runs = 1000
interval = max_bit // num_of_runs

start_time = time.time()

for i in range(0, max_bit, interval):
    BitStorage.write_bit(i, 1)

end_time = time.time()
print(f"Time taken to write {num_of_runs} bits: {end_time - start_time} seconds")
print(f"Write time per bit: {(end_time - start_time) / max_bit} seconds")



start_time = time.time()

for i in range(0, max_bit, interval):
    BitStorage.read_bit(i)

end_time = time.time()
print(f"Time taken to read {num_of_runs} bits: {end_time - start_time} seconds")
print(f"Read time per bit: {(end_time - start_time) / max_bit} seconds")
