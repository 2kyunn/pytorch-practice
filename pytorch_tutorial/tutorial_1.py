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

k = torch.tensor([5.5, 3])
print(k)

k = k.new_ones(5, 3, dtype=torch.double)
print(k)

k = torch.rand_like(k, dtype=torch.float)
print(k)

print(x.size())

y = torch.rand(5, 3)
print(k + y)

