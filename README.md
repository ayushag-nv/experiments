# TheAgentCompany Experiments
This repository contains the trajectories and jsonl files for the experiments conducted by The Agent Company.

The repository is organized as follows:
```
experiments/
├── evaluation/
│ ├── 1.0.0/
|   ├── <date>_<model>
│   │ ├── README.md
│   │ ├── results/<task_id>.json (Evaluator records, checkpoint Scores)
│   │ ├── screenshots/<task_id>/<step>.png (Screenshot Logs)
│   │ └── trajectories/<task_id>.json.gz (Compressed Agent Trajectries)
│   └── ...
```
<details>
<summary>More about how the repository is organized</summary>
The `evaluation/` folder is organized such that the top level directories are different versions of TheAgentCompany (currently only 1.0.0).
Data for models that were run on that corresponding version are included as subfolders.
Each subfolder contains all the evaluation results for each task with detailed evaluator records, checkpoint scores, agent execution logs, and screenshots (if applicable, e.g. using browser).
These logs are publicly accessible and meant to enable greater reproducibility and transparency of the experiments.
</details>

## 🏆 Leaderboard Participation

If you are interested in submitting your model to the [The Agent Company Leaderboard](https://the-agent-company.com/), please do the following:
1. Fork this repository.
2. Clone your fork.
3. Run evaluation and submit the results.
4. Within the folder, please include the following **required** assets:
- trajectories in json or json.gz format
- eval*.json, one for each task
- README.md with the model name, version, result summary, and any other relevant information
5. Create a pull request to this repository with the new folder.

Please check out this [doc](https://github.com/TheAgentCompany/TheAgentCompany?tab=readme-ov-file#quick-start) to run evaluation.

## ✅ Result Verification

If you are interested in receiving the "verified" checkmark ✓ on your submission, please do the following:

1. Create an issue
2. In the issue, provide us instructions on how to run your model on TheAgentCompany.
3. We will run your model on a random subset of TheAgentCompany and verify the results.

## 📞 Contact
Questions? Please create an issue. Otherwise, you can also contact fangzhex@cs.cmu.edu, yufans@alumni.cmu.edu, boxuanli@alumni.cmu.edu

## ✍️ Citation
```
@misc{xu2024theagentcompanybenchmarkingllmagents,
      title={TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks}, 
      author={Frank F. Xu and Yufan Song and Boxuan Li and Yuxuan Tang and Kritanjali Jain and Mengxue Bao and Zora Z. Wang and Xuhui Zhou and Zhitong Guo and Murong Cao and Mingyang Yang and Hao Yang Lu and Amaad Martin and Zhe Su and Leander Maben and Raj Mehta and Wayne Chi and Lawrence Jang and Yiqing Xie and Shuyan Zhou and Graham Neubig},
      year={2024},
      eprint={2412.14161},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.14161}, 
}
```
