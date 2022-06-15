# https://www.codingame.com/ide/puzzle/frame-the-picture
import sys

frame_pattern = input()  # the ASCII art pattern to use to frame the picture
print("frame_pattern", frame_pattern, file=sys.stderr, flush=True)
# h: the height of the picture
# w: the width  of the picture
h, w = [int(i) for i in input().split()]
print("h", h, "w", w, frame_pattern, file=sys.stderr, flush=True)
for i in range(h):
    line = input()  # the ASCII art picture line by line
    print("line", line, file=sys.stderr, flush=True)

print("Write framed picture line by line here")
