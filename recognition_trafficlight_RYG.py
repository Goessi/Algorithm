# 把所有图片弄成统一大小
def standardize_input(image):    
    standard_im = np.copy(image)
    standard_im = cv2.resize(standard_im,(32,32))
    return standard_im
    
# 数字化标签
def one_hot_encode(label):    
    one_hot_encoded = [] 
    if label == 'red':
        one_hot_encoded = [1,0,0]
    elif label == 'yellow':
        one_hot_encoded = [0,1,0]
    elif label == 'green':
        one_hot_encoded = [0,0,1]    
    return one_hot_encoded
    
# 结合
def standardize(image_list):    
    # Empty image data array
    standard_list = []
    # Iterate through all the image-label pairs
    for item in image_list:
        image = item[0]
        label = item[1]
        # Standardize the image
        standardized_im = standardize_input(image)
        # One-hot encode the label
        one_hot_label = one_hot_encode(label)    
        # Append the image, and it's one hot encoded label to the full, processed list of image data 
        standard_list.append((standardized_im, one_hot_label))        
    return standard_list
    
#############################################feature create##########################################################
def create_feature(rgb_image):
    
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    #resize again
    hsv = hsv[:,5:25,:] # 9*20
    feature = [1,0,0]
    
    if red_mask1(hsv) or red_mask2(hsv):
        feature = [1,0,0]
    elif yellow_mask(hsv):
        feature = [0,1,0]
    elif green_mask(hsv):
        feature = [0,0,1]
    
    
    return feature
def red_mask1(hsv_image):
    lower_r = np.array([156,43,46])
    higher_r = np.array([180,255,255])
    mask = cv2.inRange(hsv_image,lower_r,higher_r)
    masked_image = np.copy(hsv_image)
    masked_image[mask == 0] = [0,0,0]
    m1 = masked_image[3:12,:,:]
    m2 = masked_image[12:20,:,:]
    m3 = masked_image[20:29,:,:]
    br1 = np.sum(m1)/(20*9)
    br2 = np.sum(m2)/(20*9)
    br3 = np.sum(m3)/(20*9)
    
    if br1 - br2>20 and br1-br3>20:
        return True
    else:
        return False
def red_mask2(hsv_image):
    lower_r = np.array([0,43,46])
    higher_r = np.array([10,255,255])
    mask = cv2.inRange(hsv_image,lower_r,higher_r)
    masked_image = np.copy(hsv_image)
    masked_image[mask == 0] = [0,0,0]
    m1 = masked_image[3:12,:,:]
    m2 = masked_image[12:20,:,:]
    m3 = masked_image[20:29,:,:]
    br1 = np.sum(m1)/(20*9)
    br2 = np.sum(m2)/(20*9)
    br3 = np.sum(m3)/(20*9)
    
    if br1 - br2>20 and br1 -br3>20:
        return True
    else:
        return False
def yellow_mask(hsv_image):
    lower_y = np.array([11,43,46])
    higher_y = np.array([34,255,255])
    mask = cv2.inRange(hsv_image,lower_y,higher_y)
    masked_image = np.copy(hsv_image)
    masked_image[mask == 0] = [0,0,0]
    m1 = masked_image[3:12,:,:]
    m2 = masked_image[12:20,:,:]
    m3 = masked_image[20:29,:,:]
    br1 = np.sum(m1)/(20*9)
    br2 = np.sum(m2)/(20*9)
    br3 = np.sum(m3)/(20*9)
    
    if br2 - br1>20 and br2- br3>20:
        return True
    else:
        return False
def green_mask(hsv_image):
    lower_g = np.array([35,43,46])
    higher_g = np.array([99,255,255])
    mask = cv2.inRange(hsv_image,lower_g,higher_g)
    masked_image = np.copy(hsv_image)
    masked_image[mask == 0] = [0,0,0]
    m1 = masked_image[3:12,:,:]
    m2 = masked_image[12:20,:,:]
    m3 = masked_image[20:29,:,:]
    br1 = np.sum(m1)/(20*9)
    br2 = np.sum(m2)/(20*9)
    br3 = np.sum(m3)/(20*9)
    
    if br3 - br1>20 and br3- br2>20:
        return True
    else:
        return False
   ##############################################################featur create###########################################
def estimate_label(rgb_image):
    feature = create_feature(rgb_image)   
    return feature
