import numpy as np
import cv2

class Noisy(object):
    def __init__(self, noise_type="gauss"):
        """
        Initialize the Noisy data augmentation object.

        Args:
            noise_type (str): The type of noise to apply. "gauss" for Gaussian noise and "sp" for salt-and-pepper noise.
        """
        self.noise_type = noise_type
        
    def __call__(self, img, bboxes):
        """
        Apply the specified type of noise to the input image.

        Args:
            img (numpy.ndarray): The input image.
            bboxes (numpy.ndarray): Bounding boxes associated with the image.

        Returns:
            numpy.ndarray: The image with the applied noise.
            numpy.ndarray: The unchanged bounding boxes, as the noise does not affect the bounding boxes.
        """
        # Apply Gaussian noise to the image
        if self.noise_type == "gauss":
            image = img.copy() 
            mean = 0
            st = 0.7
            gauss = np.random.normal(mean, st, image.shape)
            gauss = gauss.astype('uint8')
            image = cv2.add(image, gauss)
            return image, bboxes
    
        # Apply salt-and-pepper noise to the image
        elif self.noise_type == "sp":
            image = img.copy() 
            prob = 0.05
            if len(image.shape) == 2:
                black = 0
                white = 255            
            else:
                colorspace = image.shape[2]
                if colorspace == 3:  # RGB
                    black = np.array([0, 0, 0], dtype='uint8')
                    white = np.array([255, 255, 255], dtype='uint8')
                else:  # RGBA
                    black = np.array([0, 0, 0, 255], dtype='uint8')
                    white = np.array([255, 255, 255, 255], dtype='uint8')
            probs = np.random.random(image.shape[:2])
            image[probs < (prob / 2)] = black
            image[probs > 1 - (prob / 2)] = white
            return image, bboxes