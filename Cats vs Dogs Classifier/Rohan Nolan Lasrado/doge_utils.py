#given path to image and int sz, center crop image to a square and resize to sz x sz, return image
def im_process(path, sz):
    img = Image.open(path)
    im_shape = img.size
    if im_shape[1]<im_shape[0]:
        left = im_shape[0]//2-im_shape[1]//2
        top = 0
        right = im_shape[0]//2-im_shape[1]//2+im_shape[1]
        bottom = im_shape[1]
        img = img.crop((left, top, right, bottom))
    else:
        left = 0
        top = im_shape[1]//2-im_shape[0]//2
        right = im_shape[0]
        bottom = im_shape[1]//2-im_shape[0]//2+im_shape[0]
        img = img.crop((left, top, right, bottom))
    img = img.resize((sz, sz))
    x = np.asarray(img)
    return x
    
#Load the nth batch from the training data of size m
def load_dataset(batch = 0, m = 4000):
    m20 = m//20
    m10 = m//10
    X = np.zeros((m, 256, 256, 3))
    
    #for that sweet progressbar
    print("Loading: [" + "."*10 + "*" + "]")
    count = 0
    
    #populate X
    for i in range(m//2):
        X[i, :, :, :] = im_process("train/cat." + str(batch + i) + ".jpg", 256)
        X[m//2+i, :, :, :] = im_process("train/dog." + str(batch + i) + ".jpg", 256)
        if i%m20 == 0:
            clear_output(wait = True)
            count+=1
            print("Loading: [" + ">"*count + "."*(10-count) + "*" + "]")
    
    #define and populate lables
    Y = np.zeros((m, 1))
    Y[m//2:] = 1
    
    #shuffle
    rand_idx = np.arange(m)
    np.random.shuffle(rand_idx)
    
    print("Shuffling: [" + "."*10 + "*" + "]")
    count = 0
    for i in range(m):
        X[i, :, :, :], X[rand_idx[i], :, :, :] = X[rand_idx[i], :, :, :].copy(), X[i, :, :, :].copy()
        Y[i], Y[rand_idx[i]] = Y[rand_idx[i]].copy(), Y[i].copy()
        if i%m10 == 0:
            clear_output(wait = True)
            count+=1
            print("Shuffling: [" + ">"*count + "."*(10-count) + "*" + "]")
    
    #split into train and validation sets
    X_train = X[0:9*m//10, :, :, :]
    Y_train = Y[0:9*m//10]
    X_test = X[9*m//10:m, :, :, :]
    Y_test = Y[9*m//10:m]
    
    clear_output(wait = True)
    print("Shuffling: [" + ">"*11 + "]")
    
    return X_train, Y_train, X_test, Y_test