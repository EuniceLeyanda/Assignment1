import psutil
import time

def monitor_cpu(threshold):
    try:
        print("Monitoring CPU usage...")
        while True:
            # psutil in-built method is check the CPU usage percent
            cpu_usage = psutil.cpu_percent(interval=0.5)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {threshold}%!")

    # except to handle keyboard interruption
    except KeyboardInterrupt:
        print("\nMonitoring Interrupted")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    threshold_percentage = 80
    monitor_cpu(threshold_percentage)
