import numpy as np
import os
import matplotlib.pyplot as plt

path_lists = ["seed31epo0.npz", "seed32epo0.npz", "seed33epo0.npz", "seed34epo0.npz"]
week_counter = 31
plt.figure(figsize=(20,10))
for index, path in enumerate(path_lists):
    cur_data = np.load(path)
    print("----------------------")
    print("Prediction Dimension: ", cur_data['prediction'].shape)
    print("Ground Truth Dimension: ", cur_data['truth'].shape)
    print("----------------------")

    # Create a subplot for each file
    plt.subplot(2, 2, index + 1)  # Arrange plots in 2 rows and 2 columns
    plt.title(f'Prediction and Ground Truth for Week {week_counter}')
    plt.plot(cur_data['prediction'][0, 0, :, 0], label='Prediction 1')
    plt.plot(cur_data['prediction'][0, 0, :, 1], label='Prediction 2')
    plt.plot(cur_data['prediction'][0, 0, :, 2], label='Prediction 3')
    plt.plot(cur_data['truth'][0, 0, :], label='Ground Truth')
    plt.legend()
    week_counter += 1

# Show all subplots
plt.tight_layout()
plt.show()


# path = "seed34epo0.npz"
# # # print("----------------------")
# # # print(os.getcwd() + path)
# data = np.load(path)
# # print(data.files)
# print("----------------------")
# print("Prediction Dimension: ", data['prediction'].shape)
# print("Groud Truth Dimension: ", data['truth'].shape)
# print("----------------------")

# print("Prediction: ", data['prediction'][0,0,:,2])
# # print("prediction dimension: ", data['prediction'][0,0,:].shape)
# print("Ground Truth: ", data['truth'][0,0,:])

# #visualize the prediction and ground truth
# plt.figure(figsize=(10, 5))
# plt.title('Prediction and Ground Truth for Week 34')
# plt.plot(data['prediction'][0, 0, :, 0], label='Prediction 1')
# plt.plot(data['prediction'][0, 0, :, 1], label='Prediction 2')
# plt.plot(data['prediction'][0, 0, :, 2], label='Prediction 3')
# plt.plot(data['truth'][0, 0, :], label='Ground Truth')
# plt.legend()
# plt.show()


# path = "../week34/test.npz"
# data = np.load(path)
# print(data.files)
# print("----------------------")
# print("x: ", data['x'][0,0,:])