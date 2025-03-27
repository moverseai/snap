import os
import numpy as np
import argparse
import glob
import cv2
    
"""
Test images folder structure must be:

'results_dir'(path given as input)
    |
    |-----method1
    |        |
    |        |-----subjectX
    |                |
    |                |-----TakeY
    |                        |
    |                        |-----gt
    |                        |-----pred
    |
    |-----method2
            .
            .
            .
            .

Images must have their id at the end of their name
"""
def collect_corresponding_images_from_all_methods(methods_prediction_images_rel_paths, methods_gt_images_rel_paths, subject, take, index, results_dir):
    return [os.path.join(results_dir, list(methods_prediction_images_rel_paths.keys())[0], methods_gt_images_rel_paths[list(methods_prediction_images_rel_paths.keys())[0]][subject][take][index])] + [os.path.join(results_dir, method, methods_prediction_images_rel_paths[method][subject][take][index]) for method in list(methods_prediction_images_rel_paths.keys())]

def merge_images_side_by_side(image_paths):
    images = [cv2.imread(image_path) for image_path in image_paths]
    # Ensure all images have the same height
    heights = [image.shape[0] for image in images]
    max_height = max(heights)
    resized_images = [cv2.resize(image, (int(image.shape[1] * max_height / image.shape[0]), max_height)) for image in images]
    # Concatenate images horizontally
    merged_image = np.hstack(resized_images)
    return merged_image

def main(results_dir):
    methods_folders = [f for f in os.listdir(results_dir) if os.path.isdir(os.path.join(results_dir, f))]

    methods_prediction_images_rel_paths = {}
    methods_gt_images_rel_paths = {}
    zero_indexed = {}
    for method_folder in methods_folders:
        
        method_all_images = glob.glob("**/*.png", root_dir=os.path.join(results_dir, method_folder), recursive=True)
        method_all_pred_images = sorted([im for im in method_all_images if "pred" in im], key=lambda x: int(os.path.basename(x).split("_")[-1].split(".")[0]))
        method_all_gt_images = sorted([im for im in method_all_images if "gt" in im], key=lambda x: int(os.path.basename(x).split("_")[-1].split(".")[0]))
        
        methods_prediction_images_rel_paths[method_folder] = {}
        methods_gt_images_rel_paths[method_folder] = {}
        zero_indexed[method_folder] = any([int(os.path.basename(image).split("_")[-1].split(".")[0]) == 0 for image in method_all_images])

        for image_rel_path in method_all_pred_images:
            subject, take, part, name = image_rel_path.split("\\")
            index = int(name.split("_")[-1].split(".")[0]) #- (1 * (not zero_indexed[method_folder]))

            if subject not in methods_prediction_images_rel_paths[method_folder]:
                methods_prediction_images_rel_paths[method_folder][subject] = {}
            if take not in methods_prediction_images_rel_paths[method_folder][subject]:
                methods_prediction_images_rel_paths[method_folder][subject][take] = {}
            methods_prediction_images_rel_paths[method_folder][subject][take][index] = image_rel_path
        
        for image_rel_path in method_all_gt_images:
            subject, take, part, name = image_rel_path.split("\\")
            index = int(name.split("_")[-1].split(".")[0]) #- (1 * (not zero_indexed[method_folder]))

            if subject not in methods_gt_images_rel_paths[method_folder]:
                methods_gt_images_rel_paths[method_folder][subject] = {}
            if take not in methods_gt_images_rel_paths[method_folder][subject]:
                methods_gt_images_rel_paths[method_folder][subject][take] = {}
            methods_gt_images_rel_paths[method_folder][subject][take][index] = image_rel_path

    for subject, takes in methods_prediction_images_rel_paths[methods_folders[0]].items():
        for take, images in takes.items():
            output_dir = os.path.join(os.path.dirname(results_dir), "combined_results_" + "_".join(methods_folders), subject, take)
            os.makedirs(output_dir, exist_ok=True)

            for image_index, image_rel_path in images.items():
                corresponding_images_full_paths = collect_corresponding_images_from_all_methods(methods_prediction_images_rel_paths, methods_gt_images_rel_paths, subject, take, image_index, results_dir)

                merged_images = merge_images_side_by_side(corresponding_images_full_paths)

                cv2.imwrite(os.path.join(output_dir, str(image_index) + ".png"), merged_images)
        


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Summarize experiment results from YAML and PLY files.")
    # parser.add_argument("results_dir", type=str, help="Path to the root directory containing experiment results of all methods.")
    # args = parser.parse_args()
    results_dir = "D:/Kotarelas/gaussianSplatting/gaussianSplatsResults/test_images/all_results"
    main(results_dir)