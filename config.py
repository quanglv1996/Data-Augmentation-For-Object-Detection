class Map(dict):
    """
    A custom dictionary class that allows accessing dictionary keys as attributes.
    """

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


'''
Config for augmentation object detection
'''
# Configuration settings for various data augmentation techniques
config_augmentation = {
    'AdjustBrightneess': {
        'used': True,
        'brightness_factor': 1.5,
    },
    'AdjustContrast': {
        'used': True,
        'contrast_factor': 1.5,
    },
    'AdjustSaturation': {
        'used': True,
        'saturation_factor': 1.5,
    },
    'Cutout': {
        'used': True,
        'amount': .3,
    },
    'Filters': {
        'used': True
    },
    'GridMask': {
        'used': True,
        'use_h': True,
        'use_w': True,
        'rotate': 1,
        'offset': False,
        'ratio': .5,
        'mode': 0,
        'prob': .7
    },
    'RandomHorizontalFlip': {
        'used': True,
        'p': 1
    },
    'HorizontalFlip':{
        'used': True
    },
    'RandomHSV': {
        'used': True,
        'hue':100,
        'saturation':100,
        'brightness': 100
    },
    'LightingNoise':{
        'used': True,
    },
    'Mixup':{
        'used': True,
        'lambd': .3,
    },
    'Noisy':{
        'used': True,
        'noise_type': "gauss",
    },
    'Resize':{
        'used': True,
        'inp_dim': 512,
    },
    'RotateOnlyBboxes':{
        'used': True,
        'angle': 5.,
    },
    'RandomRotate':{
        'used': True,
        'angle': 5.,
    },
    'Rotate':{
        'used': True,
        'angle': 5,
    },
    'RandomScale': {
        'used': True,
        'scale': 0.5,
        'diff': True
    },
    'Scale': {
        'used': True,
        'scale_x': 0.5,
        'scale_y': True
    },
    'Sequence': {
        'used': True
    },
    'RandomShear': {
        'used': True,
        'shear_factor': 0.5
    },
    'Shear': {
        'used': True,
        'shear_factor': 0.5
    },
    'SmallObjectAugmentation': {
        'used': True,
    },
    'RandomTranslate': {
        'used': True,
        'translate': 0.2,
        'diff': True
    },
    'Translate': {
        'used': True,
        'translate': 0.2,
        'diff': True
    },
}

# Convert the augmentation configuration to a Map object
config_augmentation = Map(config_augmentation)

'''
Config for generation data
'''
# Configuration settings for generating data
config_data = {
    'path_data_raw': './assets/yolo',
    'path_save': './dataset',
    'label_mapping': {
        'dog': 0,
        'car': 1,
        'bike': 2,
    },
    'train_scale': 0.7,
    'val_scale': 0.2,
    'src_type_dataset': 'yolo',
    'dest_type_dataset': 'voc',
}

# Convert the data generation configuration to a Map object
config_data = Map(config_data)