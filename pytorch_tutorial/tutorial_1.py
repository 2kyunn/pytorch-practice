import torch

## not initialized Tensor
x = torch.empty(5, 3)
print(x)

## randomly initialized Tensor
y = torch.rand(5, 3)
print(y)

## dtype = long, initialized to 0
z = torch.zeros(5, 3, dtype=torch.long)
print(z)
