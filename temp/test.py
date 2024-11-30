import numpy as np
import torch
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
from PIL import Image, ImageDraw, ImageOps


def show_mask(mask, ax, random_color=False, borders = True):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask = mask.astype(np.uint8)
    mask_image =  mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    if borders:
        import cv2
        contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        # Try to smooth contours
        contours = [cv2.approxPolyDP(contour, epsilon=0.01, closed=True) for contour in contours]
        mask_image = cv2.drawContours(mask_image, contours, -1, (1, 1, 1, 0.5), thickness=2) 
    ax.imshow(mask_image)

image = Image.open(r"../assests/image.webp")
image = np.array(image.convert("RGB"))
checkpoint = r"../sam2/checkpoints/sam2.1_hiera_large.pt"
model_cfg = r"../sam2/configs/sam2.1/sam2.1_hiera_l.yaml"
predictor = SAM2ImagePredictor(build_sam2(model_cfg, checkpoint))
input_point = np.array([[211,299]])
input_labels= np.array([1])

with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
    predictor.set_image(image)
    masks, scores, _  = predictor.predict(
            point_coords=input_point,
            point_labels=input_labels,
            multimask_output=False)
    
# Convert the mask to a PIL image (scale to 0-255 for visibility)
mask_image = Image.fromarray((masks[0] * 255).astype(np.uint8))

# Convert the original image to a PIL image if it's not already
original_image = Image.fromarray(image)

# Ensure the mask has an alpha channel for transparency
mask_image = mask_image.convert("L")  # Single-channel grayscale
mask_overlay = ImageOps.colorize(mask_image, black="black", white="red")  # Make the mask red

# Overlay the mask on the original image
result = Image.blend(original_image, mask_overlay, alpha=0.5)  # Adjust alpha for transparency

# Show the result
result.show()

    

    
