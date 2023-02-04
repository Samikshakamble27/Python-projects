import qrcode

img = qrcode.make("https://www.linkedin.com/in/samiksha-kamble-54976122b/")
img.save('saved.png')
img.show('saved.png')
