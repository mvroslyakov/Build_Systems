import json
import sys
import numpy as np


if __name__ == '__main__':
  new_img = np.loadtxt('array.txt', dtype=int)
  new_img = new_img.reshape((3, 256, 3))
  with open('array.h', 'w') as fp:
    h, w, c = new_img.shape
    fp.write('int arr[3][256][3] = {')
    for hi in range(h):
      fp.write('{')
      for wi in range(w):
        fp.write('{')
        fp.write(', '.join([str(element) for element in new_img[hi,wi]]))
        if wi == w-1:
          fp.write('}')
        else:
          fp.write('},\n')
      if hi == h-1:
        fp.write('}')
      else:
        fp.write('},\n')
    fp.write('};')
