"""
# want to make qr_code for phonepe..
# at first install "pip install qrcode" in terminal:-

here I didn't add phonepe qrcode link in image = qrcode.make("-------")..
but I added some different youtube link which we can open in simple camera from the phone
or will use scanner or phonepe or paytm app...

# we can save image in ".png" or ".jpg" format:-
"""

import qrcode

image = qrcode.make("https://www.youtube.com/watch?v=-GmJLI122ZM")

image.save("Gujju_Codebasics.png")

'''
# Now, we are making sentence and we want to read that line or sentences:-
# for that we will install "pip install opencv-python" in terminal.
'''

text = qrcode.make("Baby Yod ate 5 biscuits today..")
text.save("Baby_Yoda.jpg")

# now import opencv module.

import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("Baby_Yoda.jpg"))
print(val)


