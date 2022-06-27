import pyqrcode
url = "Any-Valid-URL"
img = pyqrcode.create(url)
img.png('fileName.png', scale=4)
