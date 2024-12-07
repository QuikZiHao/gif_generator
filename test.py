import cv2
import os
import numpy as np

def pixel_difference(image1, image2):
    """Calculate the sum of pixel-wise absolute differences."""
    diff = cv2.absdiff(image1, image2)
    diff_score = np.sum(diff)
    return diff_score

def compare_with_first_frame(directory):
    # Get all files in the directory, sorted
    frame_files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    if not frame_files:
        print("No image files found in the directory.")
        return []
    
    # Load the first frame
    first_frame = cv2.imread(frame_files[0])
    if first_frame is None:
        print(f"Failed to load the first frame: {frame_files[0]}")
        return []
    
    results = []
    
    # Compare every other frame to the first frame
    for i in range(1, len(frame_files)):
        current_frame = cv2.imread(frame_files[i])
        if current_frame is None:
            print(f"Failed to load frame: {frame_files[i]}")
            continue
        
        # Calculate similarity (e.g., pixel difference)
        similarity = pixel_difference(first_frame, current_frame)
        results.append((frame_files[0], frame_files[i], similarity))
    
    # Sort results by similarity score (ascending)
    sorted_results = sorted(results, key=lambda x: x[2])
    return sorted_results

# Example usage
directory = r"fastapi_app\temp\test"
sorted_similarities = compare_with_first_frame(directory)

cal = 0
# Print the sorted results
print("Sorted similarities (from smaller to bigger):")
for first_frame, current_frame, similarity in sorted_similarities:
    cal +=1
    print(f"Difference between {first_frame} and {current_frame}: {similarity}")
    if cal == 30:
        break
