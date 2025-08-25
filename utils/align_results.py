import os 
import json 
import shutil 
import sys


reference_dir_name = "OpenHands_0.28.1-nemotron-49b-v1.5"

if __name__ == "__main__":
    eval_dir = sys.argv[1]

    if reference_dir_name not in os.listdir(eval_dir):
        raise ValueError(f"Reference directory {reference_dir_name} not found in {eval_dir}")
    
    files_in_reference_dir = os.listdir(os.path.join(eval_dir, reference_dir_name, "results"))

    
    for dir_name in os.listdir(eval_dir):
        if dir_name == reference_dir_name:
            print(f"Skipping {dir_name}")
            continue
        
        files_in_eval_dir = os.listdir(os.path.join(eval_dir, dir_name, "results"))
        print("Directory: ", dir_name)
        for file in files_in_eval_dir:
            if file not in files_in_reference_dir:
                print(f"File {file} not found in {reference_dir_name}")
                print("Removing file: ", os.path.join(eval_dir, dir_name, "results", file))
                #os.remove(os.path.join(eval_dir, dir_name, "results", file))
            

    
