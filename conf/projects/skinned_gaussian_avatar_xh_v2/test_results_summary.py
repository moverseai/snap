import os
import yaml
import pandas as pd
import rich

class NoTagConstructor(yaml.SafeLoader):
    def construct_undefined(self, node):
        return None  # Replace unknown objects with None

def get_nested_value(dictionary, key_path, default="N/A"):
    """Retrieve a value from a nested dictionary using a dotted key path."""
    keys = key_path.split(".")
    value = dictionary
    try:
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        return default
    
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
        run_info_names = [
            # "COV_STEPS", 
            # "COLOR_STEPS", 
            # "GEOM_STEPS", 
            # "COMB_STEPS", 
            "SPLATS_PATH", 
            "METHOD", 
            # "comb_LR", 
            "SH_EPOCH", 
            # "ORDER",
            "model.monads.gaussian_splat_parameters.scale",
            ]
        
        run_info = []
        for name in run_info_names:
            run_info.append(get_nested_value(config, name, "N/A"))
        # cov_steps = config.get("COV_STEPS", "N/A")
        # color_steps = config.get("COLOR_STEPS", "N/A")
        # geom_steps = config.get("GEOM_STEPS", "N/A")
        # comb_steps = config.get("COMB_STEPS", "N/A")
        # train_folder_path = config.get("SPLATS_PATH", "N/A")
        # method = config.get("METHOD", "N/A")
        
        datasets = config.get("data", {}).get("train", {}).get("iterator", {}).get("datasets", {})
        if not datasets:
            return None
        
        dataset_name = next(iter(datasets))  # Get the first key
        dataset_info_all = datasets.get(dataset_name, {})
        dataset_info_names = ["subject", "split", "take"]
        dataset_info = []
        for name in dataset_info_names:
            dataset_info.append(dataset_info_all.get(name, "N/A"))
        dataset_info_names.insert(0, "Dataset")
        dataset_info.insert(0, dataset_name)
        # subject = dataset_info_all.get("subject", "N/A")
        # split = dataset_info_all.get("split", "N/A")
        # take = dataset_info_all.get("take", "N/A")
        
        return dataset_info_names + run_info_names, dataset_info + run_info
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
            yaml_info_names, yaml_info = extract_test_yaml_info(yaml_path)
            if yaml_info:
                # dataset, subject, split, test_take, cov_steps, color_steps, geom_steps, comb_steps, train_folder_path, method = yaml_info
                train_take = extract_train_yaml_info(os.path.join(yaml_info[yaml_info_names.index("SPLATS_PATH")], "config_resolved.yaml"))
                train_config_path = os.path.join(yaml_info[yaml_info_names.index("SPLATS_PATH")], "config_resolved.yaml")
                del yaml_info[yaml_info_names.index("SPLATS_PATH")]
                yaml_info_names.remove("SPLATS_PATH")
                data_list.append(yaml_info + [train_take, test_avg_results.iloc[0]['psnr'], test_avg_results.iloc[0]['lpips'], test_avg_results.iloc[0]['ssim'], train_config_path])
                

    df = pd.DataFrame(data_list, columns=yaml_info_names + ["Train_Take", "PSNR", "LPIPS", "SSIM", "Train Config"])
    # df = df.sort_values(by=["PSNR", "SSIM", "Dataset", "subject", "Train_Take", "take", "METHOD", "COV_STEPS", "COLOR_STEPS", "GEOM_STEPS", "COMB_STEPS"], ascending=False)
    df = df.sort_values(by=[
        "Dataset", 
        "subject", 
        "take", 
        "METHOD",
        "PSNR",
        # "LPIPS",
        # "SSIM",
        # "SH_EPOCH", 
        # "comb_LR",
        # "ORDER",
        "model.monads.gaussian_splat_parameters.scale",
        ], ascending=False)
    
    # print(df.to_string(index=False))
    rich.print(df.to_markdown())

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Summarize experiment results from YAML and PLY files.")
    # parser.add_argument("root_dir", type=str, help="Path to the root directory containing experiment folders.")
    # args = parser.parse_args()
    
    root_dir = "C:/Users/info/Documents/GitHub/snap/multirun/2025-04-03"
    main(root_dir)