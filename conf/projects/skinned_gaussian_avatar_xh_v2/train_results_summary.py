import os
import yaml
import pandas as pd
import rich

class NoTagConstructor(yaml.SafeLoader):
    def construct_undefined(self, node):
        return None  # Replace unknown objects with None
    
def find_files(root_dir, filename):
    """ Recursively find all files with a given name inside a root directory. """
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        if filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))
    return file_paths

def extract_yaml_info(yaml_path):
    """ Extract relevant information from the YAML file. """
    try:
        NoTagConstructor.add_constructor(None, NoTagConstructor.construct_undefined)

        with open(yaml_path, 'r') as f:
            config = yaml.load(f, Loader=NoTagConstructor)
        
        run_info_names = ["COV_STEPS", "COLOR_STEPS", "GEOM_STEPS", "COMB_STEPS", "METHOD", "comb_LR", "SH_EPOCH"]
        run_info = []
        for name in run_info_names:
            run_info.append(config.get(name, "N/A"))
        # cov_steps = config.get("COV_STEPS", "N/A")
        # color_steps = config.get("COLOR_STEPS", "N/A")
        # geom_steps = config.get("GEOM_STEPS", "N/A")
        # comb_steps = config.get("COMB_STEPS", "N/A")
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

def main(root_dir):
    ply_files = find_files(root_dir, "splat.ply")
    data_list = []
    
    for ply_path in ply_files:
        parent_folder = os.path.dirname(ply_path)
        yaml_path = os.path.join(parent_folder, "config_resolved.yaml")
        
        if os.path.exists(yaml_path):
            yaml_info_names, yaml_info = extract_yaml_info(yaml_path)
            if yaml_info:
                # dataset_name, subject, split, take, cov_steps, color_steps, geom_steps, comb_steps, method = yaml_info
                data_list.append(yaml_info + [yaml_path])
    df = pd.DataFrame(data_list, columns=yaml_info_names + ["Train Config"])
    # df.loc[len(df)] = yaml_info + [yaml_path]
    df = df.sort_values(by=["Dataset", "subject", "take", "METHOD", "COV_STEPS", "COLOR_STEPS", "GEOM_STEPS", "COMB_STEPS", "comb_LR", "SH_EPOCH"])
    # print(df.to_markdown())
    rich.print(df.to_markdown())

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Summarize experiment results from YAML and PLY files.")
    # parser.add_argument("root_dir", type=str, help="Path to the root directory containing experiment folders.")
    # args = parser.parse_args()
    
    root_dir = "C:/Users/info/Documents/GitHub/snap/multirun/2025-03-05/17-28-16"
    main(root_dir)