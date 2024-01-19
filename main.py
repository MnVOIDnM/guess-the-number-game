import sys
import random

# TODO: add validation
sys.stdout.buffer.write(b'Enter a minimum number.\n')
sys.stdout.flush()
min_num = int(sys.stdin.buffer.readline().decode())

sys.stdout.buffer.write(b'Enter a maximum number.\n')
sys.stdout.flush()
max_num = int(sys.stdin.buffer.readline().decode())

if min_num >= max_num:
    sys.stdout.buffer.write(b'Enter a number greater than the minimum number.\n')
    sys.stdout.flush()
    max_num = int(sys.stdin.buffer.readline().decode())

answer = random.randint(min_num, max_num)
attempt_count = int((min_num + max_num) / 2)

for i in range(attempt_count):
    sys.stdout.buffer.write(b'Guess the number.\n')
    sys.stdout.flush()
    guess_num = int(sys.stdin.buffer.readline().decode())

    if answer == guess_num:
        sys.stdout.buffer.write(b"That's correct!!\n")
        sys.stdout.flush()
        break
    else:
        sys.stdout.buffer.write(b"That's wrong >_<. ")
        sys.stdout.flush()


