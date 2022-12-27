import os
import cv2
import numpy as np

from glob import glob
from tqdm import tqdm
from runpy import run_path
from natsort import natsorted
from skimage import img_as_ubyte

import torch
import torch.nn.functional as F
import torchvision.transforms.functional as TF

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_weights_and_parameters(task, parameters):
    if task == 'real_denoising':
        weights = os.path.join('MIRNetv2', 'Real_Denoising', 'pretrained_models', 'real_denoising.pth')
    elif task == 'super_resolution':
        weights = os.path.join('MIRNetv2', 'Super_Resolution', 'pretrained_models', 'sr_x4.pth')
        parameters['scale'] =  4
    elif task == 'contrast_enhancement':
        weights = os.path.join('MIRNetv2', 'Enhancement', 'pretrained_models', 'enhancement_fivek.pth')
    elif task == 'lowlight_enhancement':
        weights = os.path.join('MIRNetv2', 'Enhancement', 'pretrained_models', 'enhancement_lol.pth')
    return weights, parameters

def load_model(task):
    # Get model weights and parameters
    parameters = {
        'inp_channels':3,
        'out_channels':3, 
        'n_feat':80,
        'chan_factor':1.5,
        'n_RRG':4,
        'n_MRB':2,
        'height':3,
        'width':2,
        'bias':False,
        'scale':1,
        'task': task
        }

    weights, parameters = get_weights_and_parameters(task, parameters)

    load_arch = run_path(os.path.join('MIRNetv2', 'basicsr', 'models', 'archs', 'mirnet_v2_arch.py'))
    model = load_arch['MIRNet_v2'](**parameters)
    model.to(device)

    checkpoint = torch.load(weights)
    model.load_state_dict(checkpoint['params'])
    model.eval()

    return model

def inference(model, image):
    img_multiple_of = 4
    with torch.no_grad():
        if torch.cuda.is_available():
            torch.cuda.ipc_collect()
            torch.cuda.empty_cache()
        # convert to float32 tensor and normalize by dividing with 255, rearrange axis from (h, w, c) to (c, h, w) and convert to batch (1, c, h, w) and shift to gpu
        input_ = torch.from_numpy(image).float().div(255.).permute(2,0,1).unsqueeze(0).to(device)

        # Pad the input if not_multiple_of 4
        h,w = input_.shape[2], input_.shape[3]
        H,W = ((h+img_multiple_of)//img_multiple_of)*img_multiple_of, ((w+img_multiple_of)//img_multiple_of)*img_multiple_of
        padh = H-h if h%img_multiple_of!=0 else 0
        padw = W-w if w%img_multiple_of!=0 else 0
        input_ = F.pad(input_, (0,padw,0,padh), 'reflect')

        restored = model(input_)
        restored = torch.clamp(restored, 0, 1)

        # Unpad the output
        restored = restored[:,:,:h,:w]

        restored = restored.permute(0, 2, 3, 1).cpu().detach().numpy()
        restored = img_as_ubyte(restored[0])

        return cv2.cvtColor(restored, cv2.COLOR_RGB2BGR)
