Prquisites:
download python
If you're on linux run this command in terminal:
"$ sudo apt-get update python
$ sudo apt-get install python3.6"

If you're on windows machine
go to >> https://www.python.org/downloads/

to check if python is installed run:
"python --version"

prequisites: 
1. pip install selenium
2. pip install pytest
3. pip install allure-pytest

install allure using "scoop" (package manager for Win)
when scoop is installed:
run command in PowerShell >> scoop install allure

this will automatically install allure on your windows machine
(also you'll need java runtime for that download here: https://www.java.com/download/ie_manual.jsp)

than start creating your autotests

when autotests are created run a command: 
"pytest -v -s --alluredir="C:\prog\for_allure\allure_reports" test_all.py"

when autotests are done run: 
"allure serve {path to reports}"

tests will be running and allure reports will be generated