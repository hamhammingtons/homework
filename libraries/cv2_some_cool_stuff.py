import cv2

file = cv2.imread(r"contents_imgAndEtc\canny.jpg")

gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

uncanny = cv2.Canny(gray, 50, 70)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
cv2.imshow("Original", file)
cv2.imshow("Gray", gray)
cv2.imshow("Canny", uncanny)
cv2.imshow("actually", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =========================================================================
#                         MINI CHEATSHEET
# =========================================================================
# +----------------+-------------------------+------------------------------+
# | METHOD         | PURPOSE                 | KEY PARAMETERS               |
# +----------------+-------------------------+------------------------------+
# | imread()       | Load image from disk    | (path)                       |
# |                |                         | Example: "folder/image.jpg" |
# |                |                         |                              |
# | cvtColor()     | Convert color space     | (src, cv2.COLOR_BGR2GRAY)    |
# |                |                         | Turns color → grayscale      |
# |                |                         |                              |
# | GaussianBlur() | Smooth image / remove   | (src, (w, h), 0)             |
# |                | noise before Canny      | w & h must be ODD numbers    |
# |                |                         | Example: (5, 5)              |
# |                |                         |                              |
# | Canny()        | Detect edges/outlines   | (src, low, high)             |
# |                |                         | low = weak edges             |
# |                |                         | high = strong edges          |
# |                |                         |                              |
# | imshow()       | Show image in window    | ("WindowName", image)        |
# |                |                         |                              |
# | waitKey()      | Pause program           | (0) = wait forever           |
# |                |                         |                              |
# | destroyAll...  | Close all OpenCV        | Frees memory                 |
# |                | windows                 |                              |
# +----------------+-------------------------+------------------------------+
