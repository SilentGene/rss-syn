@echo off
@title bat auto commit and push code

E:
cd E:\Biology_data\0.Commands\2.MyPythonScript\rss-syn
python rss-syn.py
git add .
git commit -m "Auto Updated"
git push origin master