{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "clothe_classification_using_deep_learning.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM0rErzVEEB7WT4tCwYVWqE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sajeelahmed34/Articles-Recognition-Using-Deep-Neural-Network/blob/main/mnist_fashion_data_classification.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c9sEXvTBiZv0"
      },
      "source": [
        "# Classification of products using Fashion MNIST Dataset \n",
        "\n",
        "Fashion-mnist is a dataset of Zalando's article images. It consists of a 60,000 training images and a test set of 10,000 images. Each image is a 28x28 grayscale image, associated with a label from 10 classes. In the following we will build a deep learning model which can classify different fashion products into their respective classes. \n",
        "\n",
        "To start with, first we need to import te tensorflow library and set the version to 2.0"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vSRk7fNTD0L-"
      },
      "source": [
        "# importing tensorflow lib\n",
        "import tensorflow as tf\n",
        "\n",
        "# changing the version of tensorflow to 2.0\n",
        "%tensorflow_version 2.x\n",
        "print(tf.version)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B_1fvNniENVQ"
      },
      "source": [
        "# importing helper libraries \n",
        "import numpy as np \n",
        "import matplotlib.pyplot as plt "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZF9Crqe-EV6R"
      },
      "source": [
        "# Import dataset\n",
        "For this self project we will use a MNIST Fasion dataset. This is the dataset that is inclused in keras and this dataset contains 60,000 images for training and 10,000 images for validating/testing the model."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SovH5drEEcUC"
      },
      "source": [
        "from tensorflow import keras\n",
        "\n",
        "fashion_mnist = keras.datasets.fashion_mnist # loading dataset \n",
        "(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() # getting tuples of training and testing data"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "59GXZ9GhGc04",
        "outputId": "963bf05f-9f44-490e-eca9-bf25a6c9d11d"
      },
      "source": [
        "# we can look at the size of the train and test data \n",
        "print('train images: ', train_images.shape)\n",
        "print('test images: ', test_images.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "train images:  (60000, 28, 28)\n",
            "test images:  (10000, 28, 28)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "M-Ry41MGGypT"
      },
      "source": [
        "The training dataset contains 60,000 images and each image consists of 28x28 pixels. Similarly the test dataset contains 10,000 images and each image consists of 28x28 pixels. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GSCgW7lpHR-M"
      },
      "source": [
        "We can look at some of the images to see what clothe articles we are having in our dataset "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "6rf64Oy4Hbj_",
        "outputId": "1bcaa61c-3895-4fba-9dd7-f410f74b9d0a"
      },
      "source": [
        "plt.figure()\n",
        "plt.imshow(train_images[0]) # display first image on a 2D regular raster \n",
        "plt.colorbar()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6n49NobDIAd6"
      },
      "source": [
        "The above image probably looks like a sneaker. lets check other ones"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "it3J9IXAIHPD",
        "outputId": "50258f4e-825b-4afc-bf74-1baf4acef74f"
      },
      "source": [
        "plt.figure()\n",
        "plt.imshow(train_images[1]) # display first image on a 2D regular raster \n",
        "plt.colorbar()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UnLbMv2GIPn1"
      },
      "source": [
        "It looks like a T-shirt "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5ONSgtm6IpTT"
      },
      "source": [
        "# Preprocessing data \n",
        "We are having grayscale images and the pixel values ranges from 0 to 255. What we can do is to preprocess our data before feeding it to our model. We will transform each pixel value in the range of 0 to 1 by diving it by 255.0.We do this because smaller values will make it easier for the model to process our values."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NiQIBCfGJZ8H"
      },
      "source": [
        "train_images = train_images.astype('float32')/255.0\n",
        "test_images = test_images.astype('float32')/255.0"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cjkySmVsJjRP"
      },
      "source": [
        "# Building the Model\n",
        "\n",
        "Lets use a simple keras sequential model with three different layers."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fRWUUonpJmyp"
      },
      "source": [
        "model = keras.Sequential()\n",
        "model.add(keras.layers.Flatten(input_shape=(28, 28))) # input layer \n",
        "model.add(keras.layers.Dense(128, activation='relu')) # hiddel layer\n",
        "model.add(keras.layers.Dense(10, activation='softmax')) # output layer "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AVy9DU0BMmMN"
      },
      "source": [
        "# Compiling the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GtFVIvzGMQ0W"
      },
      "source": [
        "model.compile(optimizer='adam', \n",
        "              loss='sparse_categorical_crossentropy', \n",
        "              metrics=['accuracy'])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mkKUhMX-MqUJ"
      },
      "source": [
        "# Training the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fq0ld5H3MtP5",
        "outputId": "91beb5ec-9b88-4f75-d140-9552c965bc45"
      },
      "source": [
        "model.fit(train_images, train_labels, epochs=10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/10\n",
            "1875/1875 [==============================] - 5s 2ms/step - loss: 0.4954 - accuracy: 0.8249\n",
            "Epoch 2/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.3759 - accuracy: 0.8634\n",
            "Epoch 3/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.3380 - accuracy: 0.8766\n",
            "Epoch 4/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.3130 - accuracy: 0.8857\n",
            "Epoch 5/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2942 - accuracy: 0.8905\n",
            "Epoch 6/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2795 - accuracy: 0.8970\n",
            "Epoch 7/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2690 - accuracy: 0.8997\n",
            "Epoch 8/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2577 - accuracy: 0.9034\n",
            "Epoch 9/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2483 - accuracy: 0.9072\n",
            "Epoch 10/10\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 0.2397 - accuracy: 0.9107\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.callbacks.History at 0x7fb156740c10>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tR_oopjLUo8W"
      },
      "source": [
        "# Evaluating the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TNlJF6ynUsjF",
        "outputId": "dca42ab9-71d8-432a-b5a3-06e9309b3eee"
      },
      "source": [
        "test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)\n",
        "print('Test accuracy:', test_acc)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "313/313 [==============================] - 1s 1ms/step - loss: 0.3472 - accuracy: 0.8786\n",
            "Test accuracy: 0.878600001335144\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "11jp-ZLMV2Ar"
      },
      "source": [
        "The test accuracy is 85.45% which is less than the training accuracy (87.72%). This is due to the **overfitting**. We can avoid this overfitting by choosing less value for the epochs. **epochs** indicates how many times our model will see the entire dataset. Choosing higher value for epochs indicating that our model is seeing dataset so many times that actually it has memorize the training data and will not generalize well on the test data. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pn_A_4f1ismF"
      },
      "source": [
        "# Hyperparameter Tuning "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jUmGJujRaQY4"
      },
      "source": [
        "Another important thing to notice that we have randomly choosen the hyperparameters. In this network we are having many hyperparameters such as **number of hidden neurons**, **optimizers**, **learning rate** \n",
        "\n",
        "We can choose the best hyperparameters with the help of a **keras tuner**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iXGviDhvdAGt"
      },
      "source": [
        "# install and import the keras tuner \n",
        "!pip install -q -U keras-tuner\n",
        "\n",
        "import keras_tuner as kt "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t6Vqn2TQd6VX"
      },
      "source": [
        "# Re-build the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QVXUROKPd9wV"
      },
      "source": [
        "# we can use the model builder function to define the image classification model \n",
        "def model_builder(hp):\n",
        "  model = keras.Sequential() # choose sequential model\n",
        "  model.add(keras.layers.Flatten(input_shape=(28, 28))) # input layer \n",
        "\n",
        "  # tune the number of neurons in the first hidden layer \n",
        "  hp_units = hp.Int(name='units', min_value=32, max_value=512, step=32)\n",
        "  model.add(keras.layers.Dense(units=hp_units, activation='relu')) # hidden layer \n",
        "\n",
        "  model.add(keras.layers.Dense(10)) # output layer \n",
        "\n",
        "  # tune the learning rate for the optimizer\n",
        "  hp_learning_rate = hp.Choice(name='learning_rate', values=[0.01, 0.001, 0.0001])\n",
        "\n",
        "  # compile the model \n",
        "  model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate), \n",
        "                loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), \n",
        "                metrics=['accuracy'])\n",
        "\n",
        "  return model"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TuRmC7wAeTid"
      },
      "source": [
        "# Instantiate the tuner and performing hyperparamter tuning "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3VcQQULzgIYJ"
      },
      "source": [
        "There are four different hyperparameter tunning methods including `RandomSearch`, `Hyperband`, `BayessianOptimization` and `sklearn`\n",
        "\n",
        "Lets try `Hyperband` technique"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AWIhS0qFh5En"
      },
      "source": [
        "tuner = kt.Hyperband(model_builder, \n",
        "                     objective='val_accuracy',\n",
        "                     max_epochs=10,\n",
        "                     factor=3,\n",
        "                     overwrite=True,\n",
        "                     directory='hyperband', \n",
        "                     project_name='fasion_mnist')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uc0Ahz7Alh-6"
      },
      "source": [
        "# we can avoid overfitting by early stopping that means stops training as the validation loss begins rissing again \n",
        "# we can creat a callback for this\n",
        "stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5) "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bbr-dwesmz2C",
        "outputId": "8f0e4ace-7acc-4e64-a4dc-eb6fe4f275f5"
      },
      "source": [
        "# run the hyperparameter searching \n",
        "tuner.search(train_images, train_labels, epochs=50, validation_split=0.2, callbacks=[stop_early])\n",
        "\n",
        "# get the optimal hyperparameters\n",
        "best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Trial 30 Complete [00h 00m 53s]\n",
            "val_accuracy: 0.8645833134651184\n",
            "\n",
            "Best val_accuracy So Far: 0.8910833597183228\n",
            "Total elapsed time: 00h 14m 35s\n",
            "INFO:tensorflow:Oracle triggered exit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mxywelhHidRj",
        "outputId": "d4765b3f-d891-4c94-e92b-9857791be4ad"
      },
      "source": [
        "# printing the best combination of hypermeters \n",
        "print('The optimal number of neurons in the first densly connected hidden layer is {} \\nThe optimal value for the learning rate is {}'.format(best_hp.get('units'), best_hp.get('learning_rate')))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The optimal number of neurons in the first densly connected hidden layer is 416 \n",
            "The optimal value for the learning rate is 0.001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UA5Ojr7ijcLa"
      },
      "source": [
        "# Re-train the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "biJfe2OBjgg6",
        "outputId": "84b3614f-eda8-4bce-fcd4-ea8481368a02"
      },
      "source": [
        "# build the model with the optimal hyperparamters and train it on the data for 50 epochs\n",
        "model = tuner.hypermodel.build(best_hp)\n",
        "history = model.fit(train_images, train_labels, validation_split=0.2, epochs=50)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.4969 - accuracy: 0.8231 - val_loss: 0.3925 - val_accuracy: 0.8594\n",
            "Epoch 2/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.3719 - accuracy: 0.8646 - val_loss: 0.3852 - val_accuracy: 0.8604\n",
            "Epoch 3/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.3324 - accuracy: 0.8777 - val_loss: 0.3590 - val_accuracy: 0.8725\n",
            "Epoch 4/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.3073 - accuracy: 0.8869 - val_loss: 0.3292 - val_accuracy: 0.8832\n",
            "Epoch 5/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2843 - accuracy: 0.8949 - val_loss: 0.3342 - val_accuracy: 0.8827\n",
            "Epoch 6/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2730 - accuracy: 0.8988 - val_loss: 0.3559 - val_accuracy: 0.8768\n",
            "Epoch 7/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2579 - accuracy: 0.9036 - val_loss: 0.3128 - val_accuracy: 0.8860\n",
            "Epoch 8/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2462 - accuracy: 0.9085 - val_loss: 0.3081 - val_accuracy: 0.8926\n",
            "Epoch 9/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2350 - accuracy: 0.9130 - val_loss: 0.3318 - val_accuracy: 0.8864\n",
            "Epoch 10/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2265 - accuracy: 0.9144 - val_loss: 0.3154 - val_accuracy: 0.8910\n",
            "Epoch 11/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2167 - accuracy: 0.9185 - val_loss: 0.3231 - val_accuracy: 0.8877\n",
            "Epoch 12/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2066 - accuracy: 0.9229 - val_loss: 0.3028 - val_accuracy: 0.8958\n",
            "Epoch 13/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2018 - accuracy: 0.9256 - val_loss: 0.3216 - val_accuracy: 0.8928\n",
            "Epoch 14/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1920 - accuracy: 0.9282 - val_loss: 0.3242 - val_accuracy: 0.8931\n",
            "Epoch 15/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1859 - accuracy: 0.9309 - val_loss: 0.3295 - val_accuracy: 0.8940\n",
            "Epoch 16/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1785 - accuracy: 0.9337 - val_loss: 0.3149 - val_accuracy: 0.8960\n",
            "Epoch 17/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1737 - accuracy: 0.9348 - val_loss: 0.3393 - val_accuracy: 0.8927\n",
            "Epoch 18/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1675 - accuracy: 0.9376 - val_loss: 0.3543 - val_accuracy: 0.8868\n",
            "Epoch 19/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1628 - accuracy: 0.9376 - val_loss: 0.3500 - val_accuracy: 0.8937\n",
            "Epoch 20/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1584 - accuracy: 0.9411 - val_loss: 0.3631 - val_accuracy: 0.8924\n",
            "Epoch 21/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1540 - accuracy: 0.9426 - val_loss: 0.3503 - val_accuracy: 0.8913\n",
            "Epoch 22/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1477 - accuracy: 0.9453 - val_loss: 0.3570 - val_accuracy: 0.8965\n",
            "Epoch 23/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1435 - accuracy: 0.9459 - val_loss: 0.3600 - val_accuracy: 0.8975\n",
            "Epoch 24/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1379 - accuracy: 0.9486 - val_loss: 0.3541 - val_accuracy: 0.8959\n",
            "Epoch 25/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1367 - accuracy: 0.9492 - val_loss: 0.3680 - val_accuracy: 0.8929\n",
            "Epoch 26/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1319 - accuracy: 0.9496 - val_loss: 0.3665 - val_accuracy: 0.8968\n",
            "Epoch 27/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1264 - accuracy: 0.9521 - val_loss: 0.4193 - val_accuracy: 0.8895\n",
            "Epoch 28/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1272 - accuracy: 0.9523 - val_loss: 0.4189 - val_accuracy: 0.8918\n",
            "Epoch 29/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1185 - accuracy: 0.9551 - val_loss: 0.3978 - val_accuracy: 0.8930\n",
            "Epoch 30/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1176 - accuracy: 0.9555 - val_loss: 0.3996 - val_accuracy: 0.8958\n",
            "Epoch 31/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1142 - accuracy: 0.9567 - val_loss: 0.4153 - val_accuracy: 0.8931\n",
            "Epoch 32/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1123 - accuracy: 0.9580 - val_loss: 0.4379 - val_accuracy: 0.8881\n",
            "Epoch 33/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1102 - accuracy: 0.9581 - val_loss: 0.4326 - val_accuracy: 0.8889\n",
            "Epoch 34/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1100 - accuracy: 0.9584 - val_loss: 0.4214 - val_accuracy: 0.8953\n",
            "Epoch 35/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1057 - accuracy: 0.9609 - val_loss: 0.4237 - val_accuracy: 0.8990\n",
            "Epoch 36/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1022 - accuracy: 0.9610 - val_loss: 0.4570 - val_accuracy: 0.8932\n",
            "Epoch 37/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0995 - accuracy: 0.9628 - val_loss: 0.4352 - val_accuracy: 0.8978\n",
            "Epoch 38/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0970 - accuracy: 0.9635 - val_loss: 0.4433 - val_accuracy: 0.8956\n",
            "Epoch 39/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0960 - accuracy: 0.9640 - val_loss: 0.4448 - val_accuracy: 0.8952\n",
            "Epoch 40/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0953 - accuracy: 0.9639 - val_loss: 0.4791 - val_accuracy: 0.8919\n",
            "Epoch 41/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.0937 - accuracy: 0.9653 - val_loss: 0.4615 - val_accuracy: 0.8960\n",
            "Epoch 42/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0892 - accuracy: 0.9664 - val_loss: 0.4790 - val_accuracy: 0.8943\n",
            "Epoch 43/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0885 - accuracy: 0.9667 - val_loss: 0.4801 - val_accuracy: 0.8913\n",
            "Epoch 44/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.0840 - accuracy: 0.9681 - val_loss: 0.5271 - val_accuracy: 0.8891\n",
            "Epoch 45/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.0837 - accuracy: 0.9679 - val_loss: 0.4953 - val_accuracy: 0.8933\n",
            "Epoch 46/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0838 - accuracy: 0.9688 - val_loss: 0.5278 - val_accuracy: 0.8921\n",
            "Epoch 47/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0785 - accuracy: 0.9703 - val_loss: 0.5333 - val_accuracy: 0.8933\n",
            "Epoch 48/50\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.0780 - accuracy: 0.9706 - val_loss: 0.5332 - val_accuracy: 0.8933\n",
            "Epoch 49/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.0778 - accuracy: 0.9702 - val_loss: 0.5119 - val_accuracy: 0.8928\n",
            "Epoch 50/50\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.0759 - accuracy: 0.9720 - val_loss: 0.5393 - val_accuracy: 0.8952\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x8EE79Dul_2Z",
        "outputId": "bc305f13-8ea9-4991-8b2d-82be4d6a36d6"
      },
      "source": [
        "# now we can select the best epoch which gives us the smallest validation loss \n",
        "val_accuracy_per_epoch = history.history['val_accuracy']\n",
        "best_epoch = val_accuracy_per_epoch.index(max(val_accuracy_per_epoch))+1\n",
        "print('best epoch: ', best_epoch)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "best epoch:  35\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m3XWVlNltBuD"
      },
      "source": [
        "Re-instantiate the hypermodel and train the model with the best hyperparameters "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J9dYsTZ3tJu0",
        "outputId": "895cea3e-baf2-478b-ba66-964bcc0b61d4"
      },
      "source": [
        "hypermodel = tuner.hypermodel.build(best_hp)\n",
        "\n",
        "# re-train the model\n",
        "hypermodel.fit(train_images, train_labels, epochs=best_epoch, validation_split=0.2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.4959 - accuracy: 0.8243 - val_loss: 0.4030 - val_accuracy: 0.8553\n",
            "Epoch 2/35\n",
            "1500/1500 [==============================] - 7s 4ms/step - loss: 0.3713 - accuracy: 0.8653 - val_loss: 0.3495 - val_accuracy: 0.8691\n",
            "Epoch 3/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.3342 - accuracy: 0.8763 - val_loss: 0.3530 - val_accuracy: 0.8714\n",
            "Epoch 4/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.3074 - accuracy: 0.8865 - val_loss: 0.3349 - val_accuracy: 0.8758\n",
            "Epoch 5/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2881 - accuracy: 0.8913 - val_loss: 0.3213 - val_accuracy: 0.8845\n",
            "Epoch 6/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2730 - accuracy: 0.8986 - val_loss: 0.3236 - val_accuracy: 0.8821\n",
            "Epoch 7/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2569 - accuracy: 0.9040 - val_loss: 0.3184 - val_accuracy: 0.8832\n",
            "Epoch 8/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2474 - accuracy: 0.9065 - val_loss: 0.3259 - val_accuracy: 0.8855\n",
            "Epoch 9/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2353 - accuracy: 0.9118 - val_loss: 0.3196 - val_accuracy: 0.8877\n",
            "Epoch 10/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2249 - accuracy: 0.9165 - val_loss: 0.3181 - val_accuracy: 0.8873\n",
            "Epoch 11/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.2175 - accuracy: 0.9181 - val_loss: 0.3340 - val_accuracy: 0.8871\n",
            "Epoch 12/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.2090 - accuracy: 0.9210 - val_loss: 0.3280 - val_accuracy: 0.8863\n",
            "Epoch 13/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1997 - accuracy: 0.9251 - val_loss: 0.3206 - val_accuracy: 0.8917\n",
            "Epoch 14/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1928 - accuracy: 0.9271 - val_loss: 0.3263 - val_accuracy: 0.8907\n",
            "Epoch 15/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1852 - accuracy: 0.9313 - val_loss: 0.3343 - val_accuracy: 0.8912\n",
            "Epoch 16/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1788 - accuracy: 0.9332 - val_loss: 0.3310 - val_accuracy: 0.8917\n",
            "Epoch 17/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1731 - accuracy: 0.9363 - val_loss: 0.3566 - val_accuracy: 0.8912\n",
            "Epoch 18/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1690 - accuracy: 0.9371 - val_loss: 0.3337 - val_accuracy: 0.8944\n",
            "Epoch 19/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1656 - accuracy: 0.9365 - val_loss: 0.3515 - val_accuracy: 0.8923\n",
            "Epoch 20/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1565 - accuracy: 0.9411 - val_loss: 0.3352 - val_accuracy: 0.8970\n",
            "Epoch 21/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1531 - accuracy: 0.9428 - val_loss: 0.3728 - val_accuracy: 0.8879\n",
            "Epoch 22/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1467 - accuracy: 0.9448 - val_loss: 0.3451 - val_accuracy: 0.8923\n",
            "Epoch 23/35\n",
            "1500/1500 [==============================] - 7s 4ms/step - loss: 0.1435 - accuracy: 0.9456 - val_loss: 0.3586 - val_accuracy: 0.8975\n",
            "Epoch 24/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1438 - accuracy: 0.9468 - val_loss: 0.3646 - val_accuracy: 0.8927\n",
            "Epoch 25/35\n",
            "1500/1500 [==============================] - 7s 4ms/step - loss: 0.1327 - accuracy: 0.9496 - val_loss: 0.3628 - val_accuracy: 0.8957\n",
            "Epoch 26/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1351 - accuracy: 0.9487 - val_loss: 0.3990 - val_accuracy: 0.8919\n",
            "Epoch 27/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1271 - accuracy: 0.9524 - val_loss: 0.4023 - val_accuracy: 0.8894\n",
            "Epoch 28/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1215 - accuracy: 0.9551 - val_loss: 0.3851 - val_accuracy: 0.8943\n",
            "Epoch 29/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1191 - accuracy: 0.9546 - val_loss: 0.3918 - val_accuracy: 0.8932\n",
            "Epoch 30/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1176 - accuracy: 0.9554 - val_loss: 0.4092 - val_accuracy: 0.8887\n",
            "Epoch 31/35\n",
            "1500/1500 [==============================] - 8s 5ms/step - loss: 0.1135 - accuracy: 0.9569 - val_loss: 0.3910 - val_accuracy: 0.8980\n",
            "Epoch 32/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1130 - accuracy: 0.9560 - val_loss: 0.4145 - val_accuracy: 0.8902\n",
            "Epoch 33/35\n",
            "1500/1500 [==============================] - 7s 4ms/step - loss: 0.1093 - accuracy: 0.9587 - val_loss: 0.4258 - val_accuracy: 0.8887\n",
            "Epoch 34/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1043 - accuracy: 0.9610 - val_loss: 0.4270 - val_accuracy: 0.8957\n",
            "Epoch 35/35\n",
            "1500/1500 [==============================] - 7s 5ms/step - loss: 0.1039 - accuracy: 0.9615 - val_loss: 0.4453 - val_accuracy: 0.8952\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.callbacks.History at 0x7fb154d3ac50>"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AD1hQQdmus8U"
      },
      "source": [
        "# Re-evaluating the Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9FeacZkuusJN",
        "outputId": "2e34b44a-1b97-4a38-8041-94232313fbc4"
      },
      "source": [
        "eval_result = hypermodel.evaluate(test_images, test_labels)\n",
        "\n",
        "print('[test loss, test_accuracy]= ', eval_result)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "313/313 [==============================] - 1s 3ms/step - loss: 0.5219 - accuracy: 0.8860\n",
            "[test loss, test_accuracy]=  [0.5219339728355408, 0.8859999775886536]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BuImNXXSvKHp"
      },
      "source": [
        "# Prediction on test data \n",
        "\n",
        "Our labels are integers ranging from 0 - 9. Each integer represents a specific article of clothing. We'll create an array of label names to indicate which is which."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VAlyfN17ve1Y"
      },
      "source": [
        "predictions = hypermodel.predict(test_images)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5Df2IC7NwiLF"
      },
      "source": [
        "# Verifying Predictions"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "iXSyG2a6wmtd",
        "outputId": "968b5480-e405-4637-e074-86807f1e03cf"
      },
      "source": [
        "COLOR = 'white'\n",
        "plt.rcParams['text.color'] = COLOR\n",
        "plt.rcParams['axes.labelcolor'] = COLOR\n",
        "\n",
        "def predict(hypermodel, image, correct_label):\n",
        "  class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',\n",
        "               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']\n",
        "  prediction = hypermodel.predict(np.array([image]))\n",
        "  predicted_class = class_names[np.argmax(prediction)]\n",
        "\n",
        "  show_image(image, class_names[correct_label], predicted_class)\n",
        "\n",
        "\n",
        "def show_image(img, label, guess):\n",
        "  plt.figure()\n",
        "  plt.imshow(img, cmap=plt.cm.binary)\n",
        "  plt.colorbar()\n",
        "  plt.grid(False)\n",
        "  plt.show()\n",
        "  print('correct class: ', label)\n",
        "  print('prediced class: ' , guess)\n",
        "num = 10\n",
        "image = test_images[num]\n",
        "label = test_labels[num]\n",
        "predict(hypermodel, image, label)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "correct class:  Coat\n",
            "prediced class:  Coat\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3pjb3jljk22A"
      },
      "source": [
        "# Summary\n",
        "\n",
        "The followwing important points to notice:\n",
        "\n",
        "*   Developed a deep neural network classifier with three layers, the `input layer`, `1 hidden layer` and `output layer` \n",
        "*   Input layer consists of 784 neurons, output layer consists of 10 neurons this is due to the fact that we are having fashion articles from 10 different classes. \n",
        "* For hyperparameter tuning, we have used Hyperband technique although there are other methods available. \n",
        "* After hyperparameter tuning, we got 416 neurons are required for the hidden layer, it requires 35 epochs to train the model and an early stopping scheme is used to prevent model from overfitting. \n",
        "* The validation accuracy is 89.52% while the test accuracy is 88.60%\n",
        "\n"
      ]
    }
  ]
}