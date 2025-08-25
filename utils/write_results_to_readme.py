import os 
import sys 
import shutil


summarize_results_script = "/home/ayushag/Work/experiments/utils/summarize_results.py"

if __name__ == "__main__":
    eval_dir = sys.argv[1]

    reference_dir_name = "OpenHands_0.28.1-nemotron-49b-v1.5"

    if reference_dir_name not in os.listdir(eval_dir):
        raise ValueError(f"Reference directory {reference_dir_name} not found in {eval_dir}")
    
    for dir_name in os.listdir(eval_dir):
        if dir_name == reference_dir_name:
            continue
        
        base_dir = os.path.join(eval_dir, dir_name)
        results_dir = os.path.join(base_dir, "results")
        
        if not os.path.exists(results_dir):
            print(f"Results directory {results_dir} not found for {dir_name}")
            continue

        readme_file = os.path.join(base_dir, "README.md")
        
        os.system(f"python3 {summarize_results_script} {results_dir}")# >> {readme_file}")
        
        


        