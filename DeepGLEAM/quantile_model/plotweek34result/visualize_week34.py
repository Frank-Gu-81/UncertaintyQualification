import numpy as np
import os
import matplotlib.pyplot as plt

# path = "seed34epo0.npz"
# # print("----------------------")
# # print(os.getcwd() + path)
# data = np.load(path)
# print(data.files)
# print("----------------------")
# print("Prediction Dimension: ", data['prediction'].shape)
# print("Groud Truth Dimension: ", data['truth'].shape)
# print("----------------------")

# print("Prediction: ", data['prediction'][0,0,:,2])
# # print("prediction dimension: ", data['prediction'][0,0,:].shape)
# print("Ground Truth: ", data['truth'][0,0,:])

# #visualize the prediction and ground truth
# plt.figure(figsize=(10, 5))
# plt.plot(data['prediction'][0, 0, :, 1], label='Prediction')
# plt.plot(data['truth'][0, 0, :], label='Ground Truth')
# plt.legend()
# plt.show()


path = "../week34/test.npz"
data = np.load(path)
print(data.files)
print("----------------------")
print("x: ", data['x'][0,0,:])