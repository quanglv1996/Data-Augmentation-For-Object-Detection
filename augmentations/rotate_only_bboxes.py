import torchvision.transforms.functional as F
import numpy as np

class RotateOnlyBboxes(object):
    def __init__(self, angle=5):
        """
        Initialize the Rotate_Only_Bboxes data augmentation object.

        Args:
            angle (float): The specified rotation angle in degrees.
        """
        self.angle = angle

    def __call__(self, img, bboxes):
        """
        Rotate the image and adjust the bounding box coordinates accordingly.

        Args:
            img (numpy.ndarray): The input image.
            bboxes (numpy.ndarray): Bounding boxes associated with the image.

        Returns:
            numpy.ndarray: The rotated image.
            numpy.ndarray: The adjusted bounding boxes.
        """
        # Create a new image and boxes to avoid modifying the original data
        new_image = img.copy()
        boxes = bboxes.copy()

        # Convert the new image to a tensor
        new_image = F.to_tensor(new_image)

        # Iterate through each bounding box and rotate the corresponding region in the image
        for i in range(boxes.shape[0]):
            x_min, y_min, x_max, y_max, id = map(int, boxes[i])

            # Extract the region corresponding to the bounding box
            bbox = new_image[:, y_min:y_max+1, x_min:x_max+1]
            bbox = F.to_pil_image(bbox)

            # Rotate the region by the specified angle
            bbox = bbox.rotate(self.angle)

            # Replace the region in the new image with the rotated region
            new_image[:, y_min:y_max+1, x_min:x_max+1] = F.to_tensor(bbox)

        # Convert the new image back to a PIL image and then to a numpy array
        img = F.to_pil_image(new_image)
        img = np.array(img)[:, :, ::-1].copy()

        # Return the rotated image and the original bounding boxes
        return img, boxes