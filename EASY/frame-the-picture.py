# https://www.codingame.com/ide/puzzle/frame-the-picture
import sys

frame_pattern = input()  # the ASCII art pattern to use to frame the picture
print("frame_pattern", frame_pattern, file=sys.stderr, flush=True)
h, w = [int(i) for i in input().split()]
print("h", h, "w", w, frame_pattern, file=sys.stderr, flush=True)

banners = []
reversedFramePattern = frame_pattern[::-1] # slicer

lines = []
for i in range(h):
    pic = input()
    if w == 1:
        multi = w
    else:
        multi = (w-len(pic))//2
    
    if multi == 0: multi = 1
    
    lines.append(frame_pattern + (multi * " ") + pic +  (multi * " ") + reversedFramePattern)

lineSize = max([len(x) for x in lines])

index = 0
while index < len(frame_pattern):
    tmp = ""
    if index > 0:
        fill = frame_pattern[:index]
        tmp = fill + frame_pattern[index] * (lineSize - (len(fill)*2)) + fill[::-1]
    else:
        tmp = frame_pattern[index] * lineSize
    
    banners.append(tmp)
    index +=1

between = frame_pattern + (lineSize - (2*len(frame_pattern))) * " " + reversedFramePattern

for b in banners:
    print(b)

print(between)

for l in lines:
    print(l)

print(between)

for b in banners[::-1]:
    print(b)