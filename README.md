[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18148318&assignment_repo_type=AssignmentRepo)
# Assignment-01
## **Overview**
This assignment involves analyzing StackOverflow post data using **shell scripting (Bash)** and **Python (pandas)**.  
We perform the following tasks:

1. **System Information Collection**  
   - Gather system OS, CPU, memory, pip, and Jupyter installation details.
   
2. **Counting Python-related Posts (Shell Script)**  
   - A shell script (`count_python.sh`) counts the number of lines containing the word `"python"` in the extracted CSV files.

3. **Counting GitHub Mentions in Posts (Python Script)**  
   - A Python script (`count_github.py`) analyzes StackOverflow posts and counts how many contain `"GitHub"`, using **pandas** for data processing.


---

## **How to Run the Scripts**
### **1️⃣un `count_python.sh` (Bash)**
This script counts occurrences of `"python"` in the CSV dataset.

#### **Usage:**
```sh
chmod +x _output/count_python.sh  # Ensure script is executable
./_output/count_python.sh

##### ** Expected Output:**
Number of lines containing 'python': XXXX

### **2 Run 'count_github.py'(Python)**
#### ** Install Dependencies and Run Script**
pip3 install --user pandas
python3 _output/count_github.py
##### ** Expected Output**
Total lines containing 'GitHub': XXXX

Author Name : Chengjie Lu
Computing ID : CJL0212
