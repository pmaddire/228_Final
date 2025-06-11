# 228_Final

Animal Motion Imitation, code base adjusted from https://github.com/erwincoumans/motion_imitation. Note that this was tested on windows 10 and has had some dependency issues on OS systems. 

## Setup

1. **Install MPC extension:**
   ```bash
   python3 setup.py install --user
   ```

2. **Install Requirements:**
   ```bash
   pip3 install -r requirements.txt
   ```
(Requires python 3.7)
## Model Training

The reward function is located in `envs/env_wrappers/imitation_task.py` for testing different weight schemes.

Use flags in `run.py` for training.

### Basic Training Example:
```bash
python3 motion_imitation/run.py --mode train --motion_file motion_imitation/data/motions/dog_pace.txt --int_save_freq 10000000 --visualize
```

This will begin training a forward walking policy and will show you a visualization of the simulated robot. The model will be stored in the output folder.

### Parallel Training with MPI:
If you have MPI setup, you can train multiple models at the same time that will aggregate their learning:

```bash
mpiexec -n 8 python3 motion_imitation/run.py --mode train --motion_file motion_imitation/data/motions/dog_pace.txt --int_save_freq 10000000 --total_timesteps 2000000
```

This will train 8 models in parallel for 2 million timesteps.

### Continue Training:
If you want to continue training a model, add the `--model_file "model path"` flag.

## Model Testing

### Basic Testing:
```bash
python3 motion_imitation/run.py --mode test --motion_file motion_imitation/data/motions/dog_pace.txt --model_file "model_path" --visualize
```

This will show you a comparison of your model vs the Reference Motion.

### Testing Our Models:

**Baseline test:**
```bash
python3 motion_imitation/run.py --mode test --motion_file motion_imitation/data/motions/dog_pace.txt --model_file output/Baseline/baseline_2to10mill.zip --visualize
```

**Physics based test:**
```bash
python3 motion_imitation/run.py --mode test --motion_file motion_imitation/data/motions/dog_pace.txt --model_file output/Physics_trained/Physics_2to10mill.zip --visualize
```

## Viewing Training Data

1. Run TensorBoard:
   ```bash
   tensorboard --logdir=output
   ```

2. Open http://localhost:6006 in your browser
