import cv2
import os

def get_image_patch(image, center, size):
    return image[center[1]-size//2:center[1]+size//2, center[0]-size//2:center[0]+size//2, :]

def main(image_path, insets_centers, insets_sizes, insets_rescaling, output_dir):

    image = cv2.imread(image_path)
    imageH, imageW, imageC = image.shape

    for inset_index, (center, size, rescale) in enumerate(zip(insets_centers, insets_sizes, insets_rescaling)):

        for i in range(3): # Gt, haha, our

            patch = get_image_patch(image, (center[0] + imageW//3*i, center[1]), size=size)

            upscaled_patch = cv2.resize(patch, (int(size*rescale), int(size*rescale)), interpolation=cv2.INTER_CUBIC)

            dest_patch_size = upscaled_patch.shape[1]
            dest_patch_center = (imageW//3*(i+1) - dest_patch_size//2, dest_patch_size*(inset_index+1) - dest_patch_size//2 + 20*(inset_index))

            image[dest_patch_center[1]-dest_patch_size//2:dest_patch_center[1]+dest_patch_size//2, dest_patch_center[0]-dest_patch_size//2:dest_patch_center[0]+dest_patch_size//2, :] = upscaled_patch
            
            cv2.rectangle(image, (dest_patch_center[0]-dest_patch_size//2,dest_patch_center[1]-dest_patch_size//2), (dest_patch_center[0]+dest_patch_size//2,dest_patch_center[1]+dest_patch_size//2), color=(0,0,0), thickness=2)
    
    cv2.line(image, (imageW//3, 0), (imageW//3, imageH), color=(0,0,0), thickness=2)
    cv2.line(image, (2*(imageW//3), 0), (2*(imageW//3), imageH), color=(0,0,0), thickness=2)
    cv2.line(image, (3*(imageW//3), 0), (3*(imageW//3), imageH), color=(0,0,0), thickness=2)

    subject, take, img_id = image_file_path.split("/")[-3::]
    cv2.imwrite(os.path.join(output_dir, subject + "_" + take + "_" + img_id + "_" + "inset" + ".png"), image)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Summarize experiment results from YAML and PLY files.")
    # parser.add_argument("results_dir", type=str, help="Path to the root directory containing experiment results of all methods.")
    # args = parser.parse_args()
    image_file_path = "D:/Kotarelas/gaussianSplatting/gaussianSplatsResults/test_images/combined_results_haha_our_method_white/00027/Take12/85.png"
    output_dir = "D:/Kotarelas/gaussianSplatting/gaussianSplatsResults/test_images/paper_figures/"
    os.makedirs(output_dir, exist_ok=True)

    insets_centers = [
        (293, 155),
        # (253, 481),
        # (275, 497),
    ]
    insets_sizes = [
        80,
        # 80,
        # 80,
    ]
    insets_rescaling = [
        1.5,
        # 1.5,
        # 1.5,
    ]
    main(image_file_path, insets_centers, insets_sizes, insets_rescaling, output_dir)