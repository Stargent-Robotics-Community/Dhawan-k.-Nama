import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import pyttsx3 as pts
import random

paper=0
scissor=0

engine=pts.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
def speak(input):
    engine.say(input)
    engine.runAndWait()




def gen_labels():
        labels = {}
        with open("labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels
    






# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('stone.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
result = np.argmax(prediction[0])
print(prediction)
#print(gen_labels()[str(result)])
a=gen_labels()[str(result)]
print(a)








#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    
    
    
    
    
if str(a) == comp_pick:
    print('tie,you both select same')
    speak('tie,you both select same')
elif str(a) == 'Stone' and comp_pick == 'paper':
    print('you loose,computer select paper')
    speak('you loose,computer select paper')
elif str(a) == 'Stone' and comp_pick == 'scissors':
    print('you win,computer select scissors')
    speak('you win,computer select scissors')
elif str(a) == 'PAPER' and comp_pick == 'scissors':
    print('you loose,computer select scissors')
    speak('you loose,computer select scissors')
elif str(a) == 'PAPER' and comp_pick == 'rock':
    print('you win,computer select rock')
    speak('you win,computer select rock')
elif str(a) == 'scissor' and comp_pick == 'rock':
    print('you loose,computer select rock')
    speak('you loose,computer select rock')
elif str(a) == 'scissor' and comp_pick == 'paper':
    print('you win ,computer select paper')
    speak('you win ,computer select paper')
else:
    print('invalid: choose any one -- rock, paper, scissors')





    
    speak('invalid: choose any one -- rock, paper, scissors')
