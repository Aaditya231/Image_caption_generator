import os
import pickle
import numpy as np
from tqdm.notebook import tqdm

from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import load_model

from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Model
from keras.utils import to_categorical, plot_model,load_img, img_to_array
from keras.layers import Input, Dense, LSTM, Embedding, Dropout, add

tokenizer = Tokenizer()
tokenizer_path = 'tokenizer.pkl'  # Replace with the actual path to your tokenizer pickle file
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

max_length = 74 
# with open(os.path.join('captions.txt'), 'r') as f:
#     next(f)
#     captions_doc = f.read()
# mapping = {}
# # process lines
# for line in tqdm(captions_doc.split('\n')):
#     # split the line by comma(,)
#     tokens = line.split(',')
#     if len(line) < 2:
#         continue
#     image_id, caption = tokens[0], tokens[1:]
#     # remove extension from image ID
#     image_id = image_id.split('.')[0]
#     # convert caption list to string
#     caption = " ".join(caption)
#     # create list if needed
#     if image_id not in mapping:
#         mapping[image_id] = []
#     # store the caption
#     mapping[image_id].append(caption)
# def clean(mapping):
#     for key, captions in mapping.items():
#         for i in range(len(captions)):
#             # take one caption at a time
#             caption = captions[i]
#             # preprocessing steps
#             # convert to lowercase
#             caption = caption.lower()
#             # delete digits, special chars, etc., 
#             caption = caption.replace('[^A-Za-z]', '')
#             # delete additional spaces
#             caption = caption.replace('\s+', ' ')
#             # add start and end tags to the caption
#             caption = 'startseq ' + " ".join([word for word in caption.split() if len(word)>1]) + ' endseq'
#             captions[i] = caption
# clean(mapping)
# all_captions = []
# for key in mapping:
#     for caption in mapping[key]:
#         all_captions.append(caption)
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(all_captions)
# vocab_size = len(tokenizer.word_index) + 1


model_path = 'main_model.h5'  # Replace with the actual path to your H5 model file
model = load_model(model_path)
def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

# generate caption for an image
def predict_caption(model, image, tokenizer, max_length):
    # add start tag for generation process
    in_text = 'startseq'
    # iterate over the max length of sequence
    for i in range(max_length):
        # encode input sequence
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        # pad the sequence
        sequence = pad_sequences([sequence], max_length)
        # predict next word
        yhat = model.predict([image, sequence], verbose=0)
        # get index with high probability
        yhat = np.argmax(yhat)
        # convert index to word
        word = idx_to_word(yhat, tokenizer)
        # stop if word not found
        if word is None:
            break
        # append word as input for generating next word
        in_text += " " + word
        # stop if we reach end tag
        if word == 'endseq':
            break
      
    return in_text


vgg_model = VGG16()
# restructure the model
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)
in_text = 'startseq'
image_path = 'test2.jpg'
# load image
image = load_img(image_path, target_size=(224, 224))
# convert image pixels to numpy array
image = img_to_array(image)
# reshape data for model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# preprocess image for vgg
image = preprocess_input(image)
# extract features
feature = vgg_model.predict(image, verbose=0)
# predict from the trained model


def generate_caption_for_image(image_path):
    # Load image
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    
    # Extract features
    feature = vgg_model.predict(image, verbose=0)
    
    # Initialize the caption for this image
    
    
    # Generate caption for the image
    caption = predict_caption(model, feature, tokenizer, max_length)
    
    return caption

# # Specify the path to your images
# image_paths = ['test2.jpg']  # Replace with your image file paths
# res = generate_caption_for_image(image_path)
# print(res)
# for image_path in image_paths:
#     caption = generate_caption_for_image(image_path)
#     caption = caption.replace("startseq", "").replace("endseq", "")
#     print(caption)
    
    