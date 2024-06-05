import cv2
import numpy as np

image_path = 'image.bmp'
img = cv2.imread(image_path)

def rle_encode(data):
    encoding = []
    i = 0
    while i < len(data):
        count = 1
        while i + count < len(data) and data[i] == data[i + count]:
            count += 1
        encoding.append((data[i], count))
        i += count
    return encoding

def rle_decode(encoding):
    total_length = sum(count for _, count in encoding)
    data = np.empty(total_length, dtype=int)
    
    index = 0
    for value, count in encoding:
        data[index:index+count] = value
        index += count
    
    return data

channels = cv2.split(img)
for channel in channels:
    channel = channel.flatten()
    print(f"Lenght of channel: {len(channel)}")
    encoding = rle_encode(channel)
    print(f"Lenght of encoding: {len(encoding*2)}")
    decoded = rle_decode(encoding)
    print(f"Lenght of decoded: {len(decoded)}")
    print(f"decoded identical to original channel: {np.array_equal(channel, decoded)}")
