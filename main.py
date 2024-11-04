
from data_collection.collect_kernel_data import collect_data
from rl_tuner.tuner import train_model

def main():
    print("Starting data collection...")
    collect_data(interval=5, output_file="system_data.json")
    
    print("Training model for kernel tuning...")
    train_model()

if __name__ == "__main__":
    main()
