# P2-Image-Classifier-Digits

I learnt a lot from this project and was able to make an image classifier.

I used the MNIST dataset from torchvision package.
![MNIST Dataset](https://github.com/adinalini/P2-Image-Classifier-Digits/blob/master/Images/mnist.PNG)

print(images.shape) gives us torch.Size([64, 1, 28, 28])
It means that 64 is the batch size (Number of images per iteration), 1 is the colour channel (grey scale), next are dimensions 28 x 28.

At first, the model couldn't predict anything as expected:
![Before Training](https://github.com/adinalini/P2-Image-Classifier-Digits/blob/master/Images/before%20train.PNG)

After training, the model predicted the digit successfully:
![After Training 1](https://github.com/adinalini/P2-Image-Classifier-Digits/blob/master/Images/after%20train.PNG)
![After Training 2](https://github.com/adinalini/P2-Image-Classifier-Digits/blob/master/Images/after%20train%202.PNG)

By the end of this project, I now clearly understand various concepts used. And I also studied the various packages like optim, nn in depth.

