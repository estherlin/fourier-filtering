import numpy as np

def antialiased_circ(N, rad):
  # Make a kernel
  height, width = N, N # kernel size
  mid = height//2 # middle of kernel

  # Make a circular mask
  kernel_size = height
  kernel_radius = (kernel_size) // 2
  cen_x = 0
  cen_y = 0

  # make a grid
  x, y = np.ogrid[-kernel_radius:kernel_radius, -kernel_radius:kernel_radius]
  dist = (np.square(x-cen_y) + np.square(y-cen_x))**0.5 # shape (kernel_size, kernel_size)

  # Make second column the filter
  radii = np.array([rad])
  antialiased_kern = 1 - (dist - radii).clip(0,1) # shape (num_radii, kernel_size, kernel_size)
  return antialiased_kern


def aliased_circ(N, rad):

  aliased_kern = np.zeros((N, N))
  y, x = np.ogrid[-N//2:N//2, -N//2:N//2]
  mask = x**2 + y**2 <= rad**2
  aliased_kern[mask] = 1
  return aliased_kern
