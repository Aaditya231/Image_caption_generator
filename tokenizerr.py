import pickle
import os
from tqdm.notebook import tqdm
from keras.preprocessing.text import Tokenizer
with open(os.path.join('captions.txt'), 'r', encoding='utf-8') as f:
    next(f)
    captions_doc = f.read()
mapping = {}
# process lines
for line in tqdm(captions_doc.split('\n')):
    # split the line by comma(,)
    tokens = line.split(',')
    if len(line) < 2:
        continue
    image_id, caption = tokens[0], tokens[1:]
    # remove extension from image ID
    image_id = image_id.split('.')[0]
    # convert caption list to string
    caption = " ".join(caption)
    # create list if needed
    if image_id not in mapping:
        mapping[image_id] = []
    # store the caption
    mapping[image_id].append(caption)
def clean(mapping):
    for key, captions in mapping.items():
        for i in range(len(captions)):
            # take one caption at a time
            caption = captions[i]
            # preprocessing steps
            # convert to lowercase
            caption = caption.lower()
            # delete digits, special chars, etc., 
            caption = caption.replace('[^A-Za-z]', '')
            # delete additional spaces
            caption = caption.replace('\s+', ' ')
            # add start and end tags to the caption
            caption = 'startseq ' + " ".join([word for word in caption.split() if len(word)>1]) + ' endseq'
            captions[i] = caption
clean(mapping)
all_captions = []
for key in mapping:
    for caption in mapping[key]:
        all_captions.append(caption)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(caption.split()) for caption in all_captions)
tokenizer_file_path = 'tokenizer.pkl'  # Replace with the desired file path

# Save the tokenizer as a .pkl file
with open(tokenizer_file_path, 'wb') as tokenizer_file:
    pickle.dump(tokenizer, tokenizer_file)