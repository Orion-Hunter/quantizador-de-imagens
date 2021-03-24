import cv2

def gera_histograma(img):
    # http://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html#gsc.tab=0
    # calcHist(images, channels, mask, histSize, ranges)
    # histSize: representa BIN count (pode agrupar intervalo de pixels)
    # ranges: ex: [0, 256]
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    #plt.plot(hist)
    #plt.show()
    return hist