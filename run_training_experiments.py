import subprocess

# Path to your training script
training_script = 'train_pneumonia_model.py'

# Number of runs
num_runs = 10

# Run the training script 10 times sequentially
for i in range(num_runs):
    log_file = f'Logs_balanced/training_log_{i+1}.txt'
    subprocess.run(['python', training_script, '--log_file', log_file])
