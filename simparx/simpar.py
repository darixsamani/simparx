import matplotlib.pyplot as plt
from skimage import io
import cv2
import matplotlib.patches as mpatches
import numpy as np
import skimage
from pathlib import Path
from .exception import PathDoNotExiste
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
import math
from skimage.io import imsave

class Simpar:

    def __init__(self, path_image):
        self.path_image = Path(path_image)
        print("ath image : {path_image} {sefl.path_image}")
        if not self.path_image.exists:
            raise PathDoNotExiste
        self.image = io.imread(self.path_image)


    def BGR2GRAY(self, image):
        """
        cette fonction nous permet de convertir une image dgr en gray
        
        """
        gray_image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        return gray_image_1
    
    def filtrage_par_egalisateur_histogramme(self, Image):

        """
            En traitement d'images, l'égalisation d'histogramme est une méthode d'ajustement 
            du contraste d'une image numérique qui utilise l'histogramme. Elle consiste à 
            appliquer une transformation sur chaque pixel de l'image, et donc d'obtenir 
            une nouvelle image à partir d'une opération indépendante sur chacun des pixels.

        """

        h,centers = skimage.exposure.histogram(Image,source_range='dtype', normalize=True )
        cdf= h.cumsum()
        # op ér a t i on d ' é g al i s a t i o n
        resultat = 255 * cdf[Image]

        resultat = resultat.astype(np.uint8)


        return resultat
    
    def threholding_image(self, Image):
        """

            Dans le traitement d'images numériques, le seuillage est la méthode la plus simple de segmentation des images.
            A partir d'une image en niveaux de gris,
            le seuillage peut être utilisé pour créer des images binaires.
        
        """
        thresh_1 = threshold_otsu(Image)
        binary_1 = Image > thresh_1

        return  binary_1

    def zero_filter(self, gray_image):
        image_filtre  =  gray_image == 0

        return image_filtre
    
    def morphology_operation_binary_erosion(self, image_filtre):

        erose = skimage.morphology.binary_erosion(image_filtre, np.ones(shape=(1,1)), out=None)

        return erose
    
    def morphology_operation_binary_dilation(self, erose):
        dilate = skimage.morphology.binary_dilation(erose, np.ones(shape=(5,30)), out=None)

        return dilate
    
    def morphology_operation_close(self, dilate):

        close = skimage.morphology.closing(dilate, np.ones(shape=(10,10)), out=None)
        
        return close


    def find_block_paragraphe_and_draw(self, close):
                
        # apply threshold
        thresh = threshold_otsu(close)
        bw = closing(close > thresh, square(3))

        # remove artifacts connected to image border
        cleared = clear_border(bw)


        # label image regions
        label_image = label(cleared)
        
        fig, ax = plt.subplots(figsize=(50, 30))
        ax.imshow(self.image)

        for region in regionprops(label_image):
            y0, x0 = region.centroid
            orientation = region.orientation
            x1 = x0 + math.cos(orientation) * 0.5 * region.axis_minor_length
            y1 = y0 - math.sin(orientation) * 0.5 * region.axis_minor_length
            x2 = x0 - math.sin(orientation) * 0.5 * region.axis_major_length
            y2 = y0 - math.cos(orientation) * 0.5 * region.axis_major_length


            minr, minc, maxr, maxc = region.bbox
            bx = (minc, maxc, maxc, minc, minc)
            by = (minr, minr, maxr, maxr, minr)
            ax.plot(bx, by, '-b', linewidth=2.5)

        ax.set_axis_off()
        plt.tight_layout()
        plt.savefig(self.image_recognitive)
        self.image_reco = fig
        
    
    def start(self):

        image_gray = self.BGR2GRAY(self.image)

        image_filter_ega = self.filtrage_par_egalisateur_histogramme(image_gray)

        binary = self.threholding_image(image_filter_ega)

        image_filter = self.zero_filter(image_gray)

        erose = self.morphology_operation_binary_erosion(image_filter)

        dilate =  self.morphology_operation_binary_dilation(erose)

        close =  self.morphology_operation_close(dilate)

        self.find_block_paragraphe_and_draw(close)

    def save_image(self, name):

        imsave(f"{name}.png", self.image_reco)











    


