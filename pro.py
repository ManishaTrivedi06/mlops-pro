{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"pro.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyPLYVDE+iLKtJnLSnDISE9X"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"fPwbDBfAxX0O","colab_type":"code","colab":{}},"source":["import keras\n","import numpy as np"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"NKJU3EK52pd6","colab_type":"code","colab":{}},"source":["from keras.datasets import mnist\n","from keras.models import Sequential\n","from keras.utils.np_utils import to_categorical\n","from keras.layers import Dense\n","from keras.optimizers import Adam\n","from keras.backend import clear_session\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"yvUzG0pp3_M9","colab_type":"code","colab":{}},"source":["(train_X , train_y), (test_X , test_y) = mnist.load_data(\"dsmnist.csv\")"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"TpBf2Vl94oEs","colab_type":"code","colab":{}},"source":["test_X = test_X.reshape(-1 , 28*28)\n","train_X = train_X.reshape(-1 ,  28*28)\n","test_X = test_X.astype(\"float32\")\n","train_X = train_X.astype(\"float32\")"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"zSQUPzYTPBZx","colab_type":"code","colab":{}},"source":["test_y = to_categorical(test_y)\n","train_y = to_categorical(train_y)"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"SL-b6CwJW0uI","colab_type":"code","colab":{}},"source":["model = Sequential()\n","model.add(Dense(units = 20 , input_dim = 28*28 , activation = 'relu'))\n","model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))\n","model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))\n","model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))\n","model.compile( optimizer= \"Adam\" , loss='categorical_crossentropy', metrics=['accuracy'] )"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"GFlv3iiJXCQo","colab_type":"code","colab":{}},"source":["fit_model = model.fit(train_X ,  train_y , epochs = 2 , verbose =  False)\n"],"execution_count":0,"outputs":[]},{"cell_type":"code","metadata":{"id":"Xa0ZTtujXIGk","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":33},"outputId":"ee98fc8c-f803-4c7f-a97d-707de8815234","executionInfo":{"status":"ok","timestamp":1590336815932,"user_tz":-330,"elapsed":1346,"user":{"displayName":"Manisha trivedi","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14Ggm-17rkxTp2MePwfpKL2UkwRFram32oTRKZ3cEeA=s64","userId":"08983864404515422164"}}},"source":["text = fit_model.history\n","accuracy = text['accuracy'][1] * 100\n","accuracy = int(accuracy)\n","f= open(\"accuracy.txt\",\"w+\")\n","f.write(str(accuracy))\n","f.close()\n","print(\"Accuracy for the model is : \" , accuracy ,\"%\")"],"execution_count":29,"outputs":[{"output_type":"stream","text":["Accuracy for the model is :  91 %\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"Jnt6KYjfXQyt","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]}]}