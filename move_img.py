"""
Script that creates 2 folders for 2 classes and moves images of training
dataset to the corresponding folder according to its label.
"""

# Inside train_dir folder we create separate folders for each class
train_dir = "../data/train/"
#print(os.listdir(train_dir))

no_tumor = os.path.join(train_dir, '0')
os.mkdir(no_tumor)
has_tumor = os.path.join(train_dir, '1')
os.mkdir(has_tumor)

print(os.listdir(train_dir))

df_train.set_index('id', inplace=True)

# Transfer the train images
train_list = list(df_train.index)

for image in train_list:

    # the id in the csv file does not have the .tif extension therefore we add it here
    fname = image + '.tif'
    # get the label for a certain image
    target = df_train.loc[image, 'label']

    # these must match the folder names
    if target == '0':
        label = '0'
    if target == '1':
        label = '1'

    # source path to image
    src = os.path.join('../data/train', fname)
    # destination path to image
    dst = os.path.join(train_dir, label, fname)
    # copy the image from the source to the destination
    shutil.move(src, dst)

print(len(os.listdir('../data/train/0')))
print(len(os.listdir('../data/train/1')))
print(len(os.listdir('../data/train')))
print(len(os.listdir('../data/test/images')))