import os
import yaml
import pandas as pd
import rich

class NoTagConstructor(yaml.SafeLoader):
    def construct_undefined(self, node):
        return None  # Replace unknown objects with None
    
def find_files(root_dir, desired_end):
    """ Recursively find all files with a given name inside a root directory. """
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith(desired_end):
                file_paths.append(os.path.join(dirpath, f))
    return file_paths

def extract_test_yaml_info(yaml_path):
    """ Extract relevant information from the YAML file. """
    try:
        NoTagConstructor.add_constructor(None, NoTagConstructor.construct_undefined)

        with open(yaml_path, 'r') as f:
            config = yaml.load(f, Loader=NoTagConstructor)
        
        cov_steps = config.get("COV_STEPS", "N/A")
        color_steps = config.get("COLOR_STEPS", "N/A")
        geom_steps = config.get("GEOM_STEPS", "N/A")
        train_folder_path = config.get("SPLATS_PATH", "N/A")
        method = config.get("METHOD", "N/A")
        
        datasets = config.get("data", {}).get("train", {}).get("iterator", {}).get("datasets", {})
        if not datasets:
            return None
        
        dataset = next(iter(datasets))  # Get the first key
        dataset_info = datasets.get(dataset, {})
        
        subject = dataset_info.get("subject", "N/A")
        split = dataset_info.get("split", "N/A")
        take = dataset_info.get("take", "N/A")
        
        return dataset, subject, split, take, cov_steps, color_steps, geom_steps, train_folder_path, method
    except Exception as e:
        print(f"Error reading YAML {yaml_path}: {e}")
        return None

def extract_train_yaml_info(yaml_path):
    """ Extract relevant information from the YAML file. """
    try:
        NoTagConstructor.add_constructor(None, NoTagConstructor.construct_undefined)

        with open(yaml_path, 'r') as f:
            config = yaml.load(f, Loader=NoTagConstructor)
        
        datasets = config.get("data", {}).get("train", {}).get("iterator", {}).get("datasets", {})
        if not datasets:
            return None
        
        dataset = next(iter(datasets))  # Get the first key
        dataset_info = datasets.get(dataset, {})
        
        take = dataset_info.get("take", "N/A")
        
        return take
    except Exception as e:
        print(f"Error reading YAML {yaml_path}: {e}")
        return None

def main(root_dir):
    csv_files = find_files(root_dir, "_test_average.csv")
    data_list = []
    
    for csv_path in csv_files:
        parent_folder = os.path.dirname(csv_path)
        test_avg_results = pd.read_csv(csv_path)
        yaml_path = os.path.join(parent_folder, "config_resolved.yaml")
        
        if os.path.exists(yaml_path):
            yaml_info = extract_test_yaml_info(yaml_path)
            if yaml_info:
                dataset, subject, split, test_take, cov_steps, color_steps, geom_steps, train_folder_path, method = yaml_info
                train_take = extract_train_yaml_info(os.path.join(train_folder_path, "config_resolved.yaml"))
                data_list.append([dataset, subject, train_take, test_take, method, cov_steps, color_steps, geom_steps, split, test_avg_results.iloc[0]['psnr'], test_avg_results.iloc[0]['lpips'], test_avg_results.iloc[0]['ssim'], os.path.join(train_folder_path, "config_resolved.yaml")])
    
    df = pd.DataFrame(data_list, columns=["Dataset", "Subject", "Train_Take", "Test_Take", "Method", "COV_STEPS", "COLOR_STEPS", "GEOM_STEPS", "Split", "PSNR", "LPIPS", "SSIM", "Train Config"])
    df = df.sort_values(by=["Dataset", "Subject", "Train_Take", "Test_Take", "Method", "COV_STEPS", "COLOR_STEPS", "GEOM_STEPS"])
    # print(df.to_string(index=False))
    rich.print(df.to_markdown())

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Summarize experiment results from YAML and PLY files.")
    # parser.add_argument("root_dir", type=str, help="Path to the root directory containing experiment folders.")
    # args = parser.parse_args()
    
    root_dir = "C:/Users/info/Documents/GitHub/snap/multirun/2025-03-05"
    main(root_dir)