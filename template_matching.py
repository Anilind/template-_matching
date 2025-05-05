import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the main image and template
image = cv2.imread("club_5.jpg",cv2.IMREAD_COLOR)
template = cv2.imread("club.jpg", cv2.IMREAD_COLOR)
h, w = template.shape[:2]

# Match the template
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold (tune this based on your images)
threshold = 0.85
locations = np.where(result >= threshold)

# Draw rectangles around all matches
detected = image.copy()
for pt in zip(*locations[::-1]):  # Switch columns and rows
    cv2.rectangle(detected, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Display the result
detected_rgb = cv2.cvtColor(detected, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 8))
plt.imshow(detected_rgb)
plt.title('Multiple Template Matches')
plt.axis('off')
plt.show()
#ajkdfhkasjdf hsafh sd