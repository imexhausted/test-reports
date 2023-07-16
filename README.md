

## Prequisites:  
### Download **python**  
If you're on linux run this command in terminal:  
```
sudo apt-get update python
```  

If you're on windows machine go to official python [page](https://www.python.org/downloads/)

to check if python is installed run:  
```
python --version
```
<br>

### Download required packages
```
pip install selenium
```
```
pip install pytest
```
```
pip install allure-pytest
```
<br>

### Install **Allure**
You can install **Allure** using [scoop](https://scoop.sh/) (package manager for Win)  
When scoop is installed:  
run command in **PowerShell**   
```
scoop install allure
```

This will automatically install allure on your windows machine  
Also you'll need **Java** runtime for **Allure**.
>[Download Java](https://www.java.com/download/ie_manual.jsp)

<br>

### Place for test reports
For **Allure** reports you'll need to add specific location to the repository  
using git-bash on Win or in linux terminal run:  
```
mkdir allure_reports
```
*name it whatewer you want*  
<br>
<br>
## How to Run
When autotests are created run a command:  
```
pytest -v -s --alluredir="./allure_reports" YOUR_TEST_NAME.py
```

when autotests are done run this command:  
```
allure serve ./allure_reports  
```
This command will convert reports created in ```allure_reports/``` to some kind of a website where you'll have all tests you ran.