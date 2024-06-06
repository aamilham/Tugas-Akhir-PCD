import cv2
from matplotlib import pyplot as plt

table_data = []
column_labels = ["Image Name", "Original Size (KB)", "Encoded Size (KB)", "Compression Ratio"]

m = 0.5
for i in range(9):
    image_path = f"../asset/pisang{i}.jpg"
    img = cv2.imread(image_path)
    compressed = cv2.resize(img, None, fx=m, fy=m, interpolation=cv2.INTER_NEAREST)
    table_data.append([f"pisang{i}.jpg", f"{img.nbytes / 1024:.2f}", f"{compressed.nbytes / 1024:.2f}", f"{compressed.nbytes / img.nbytes:.2f}"])

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=table_data, colLabels=column_labels, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
plt.show()
    