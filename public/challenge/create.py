import numpy as np
import matplotlib.pylab as plt
from PIL import Image

msg = np.array(Image.open("orig.png"))[:, :, 3]
vals = np.uint8(300 * np.random.random((638, 1078, 3)))
vals[:, :, 0] = msg / 100
Image.fromarray(vals, mode="RGB").save('ghost.png')

# this is the solution
solution = np.array(Image.open("ghost.png"))[:, :, 0]
plt.imshow(solution)
