for i in range(5):
    print("Hello, World!")
    print("Andy")
import os

folder_path = "D:\\Andy\\andy_python"  
files = os.listdir(folder_path)  

file_list = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
print(file_list)

