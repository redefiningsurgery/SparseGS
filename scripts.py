import os

N = 8
objects = ["eygptian", "flower", "house", "pumpkin", "santa", "squirrel", "strawberry"]

for obj in objects:
    cmd = f"python prepare_gt_depth.py ../3dgs_scenes/{N}/{obj}/images C:/Users/guoyu/gyDocuments/cvpr25/3dgs_scenes/{N}/{obj}/depths"
    print(cmd)
    os.system(cmd)

    cmd = f"python train.py --source_path ../3dgs_scenes/{N}/{obj} --model_path ../3dgs_scenes/{N}/{obj} --beta 5.0 --lambda_pearson 0.05 --lambda_local_pearson 0.15 --box_p 128 --p_corr 0.5 --lambda_diffusion 0.001 --SDS_freq 0.1 --step_ratio 0.99 --lambda_reg 0.1 --prune_sched 20000 --prune_perc 0.98 --prune_exp 7.5 --iterations 30000 --checkpoint_iterations 30000"
    print(cmd)
    os.system(cmd)

    cmd = f"python render_json.py -m ../3dgs_scenes/{N}/{obj} -s ../3dgs_scenes/{N}/{obj} --out ../3dgs_scenes/{N}/{obj}/output --white_background"
    print(cmd)
    os.system(cmd)
    exit()
