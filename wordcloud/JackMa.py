import requests

import xml.sax
import xml.sax.handler
import xml.etree.ElementTree as Etree

import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# import pprint


xml_url = 'http://comment.bilibili.com/116788897.xml'
xml_savePath = 'JackMa.txt'
img_path = 'JackMa.png'


def getHTMLText(url):
    try:
        '''Sends a GET request.'''
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        return r.text
    except:
        return "产生异常"


def xmlParse(xml):
    '''Parse XML document from string constant.'''
    root = Etree.fromstring(xml)
    '''
    Find all matching subelements by tag name or path.
    Here we need to find all subelements with tag 'd'. 
    '''
    barrages = root.findall('d')
    with open(xml_savePath, "w", encoding='utf-8') as f:
        for barrage in barrages:
            f.write(barrage.text+'\n')


def get_cloud():
    f = open(xml_savePath, 'r', encoding='UTF-8').read()
    '''The main function that segments an entire sentence that contains Chinese characters into seperated words.'''
    cut_text = " ".join(jieba.cut(f))
    '''Opens and identifies the given image file.'''
    alice_mask = np.array(Image.open(img_path))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    '''Generate wordcloud from text.'''
    wordcloud = WordCloud(

        # Parameters:
        # font_path : string Font path to the font that will be used (OTF or TTF). Defaults to DroidSansMono path on a Linux machine. If you are on another OS or don't have this font, you need to adjust this path.
        # background_color : color value (default="black") Background color for the word cloud image.
        # width : int (default=400) Width of the canvas.
        # height : int (default=200) Height of the canvas.
        # mask : nd-array or None (default=None) If not None, gives a binary mask on where to draw words. If mask is not None, width and height will be ignored and the shape of mask will be used instead. All white (#FF or #FFFFFF) entries will be considerd "masked out" while other entries will be free to draw on. [This changed in the most recent version!]
        # stopwords : set of strings or None The words that will be eliminated. If None, the build-in STOPWORDS list will be used. Ignored if using generate_from_frequencies.

        font_path="C:/Windows/Fonts/simfang.ttf",
        background_color="white", width=1920, height=1080, mask=alice_mask, stopwords=stopwords).generate(cut_text)
    '''Export to image file.'''
    wordcloud.to_file(r"wordcloud.png")

    '''
    Display an image, i.e. data on a 2D regular raster.
    # Parameters:
    # X : array-like or PIL image
    # interpolation[str](optional) :  Supported values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
    '''
    plt.imshow(wordcloud, interpolation="bilinear")
    '''
    Convenience method to get or set some axis properties.
    # Parameters:
    # option[bool/str] : 'off' Turn off axis lines and labels. Same as False.
    '''
    plt.axis("off")
    '''Display a figure.'''
    plt.show()


def main():
    txt_xml = getHTMLText(xml_url)
    xmlParse(txt_xml)
    get_cloud()


if __name__ == "__main__":
    main()
