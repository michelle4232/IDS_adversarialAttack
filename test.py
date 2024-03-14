import torch

# Create a 4 dim tensor
x = torch.tensor([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(x.shape)
new_x = x.view(-1) 
print(new_x)
print(new_x.shape)