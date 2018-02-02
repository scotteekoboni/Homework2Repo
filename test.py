# import time
# startTime = time.time()
# import torch
# import torch.nn as nn
# import torchvision.transforms as transforms
# from torch.autograd import Variable
# import numpy as np
# import random
# import cv2

# arrayZ = [2,4,3]

# ThetaDic = {}
# keys = []
# weights = []


# numHidLayers = len(arrayZ) -2 # of hidden layers 
# for i in range(0, numHidLayers+1):
#     keys.append(i)

# print("This is the keys list:", keys)

# #Populating the dictionary below!!

# for i in range(0, numHidLayers+1): #runs through the h1, h2, h3
#     numElements = arrayZ[i] 
#     mean = 0
#     SD = 1/(np.sqrt(numElements))

# for k in range(0, numElements+1):
#     for i in range(0, numHidLayers+1):
#         q = np.random.normal(mean, SD, ((arrayZ[i]+1),(arrayZ[i+1]))) #<--- use numpy thing where i can specify a mean = 0 and a SD
#         print("this is q:", q)
#         x = torch.Tensor(q)
#         print("this is x: ", x)
#         weights.append(x)

    
# ThetaDic = dict(zip(keys, weights))


# print("this is ThetaDic: ",ThetaDic)

# x = torch.Tensor()

# import torch
# from neural_network import NeuralNetwork

# structureList = [2,4,2]
# model = NeuralNetwork(structureList)
# input_array = torch.DoubleTensor([[3,4,4], [1,2,3]])

# output = model.forward(input_array)




from logic_gates import AND
from logic_gates import NOT
from logic_gates import OR
from logic_gates import XOR
And = AND()

xor = XOR()
Not = NOT()

Or = OR()

print(And(False, False))
print(xor(False, True))
print(Or(False, True))
print(Not(True))





