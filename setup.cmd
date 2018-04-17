@echo off
set venvdir=C:\Projects\.virtualenvs\infosys_cui_env
python -m venv %venvdir%
set envpip=%venvdir%\Scripts\pip.exe
%envpip% install rasa_nlu[spacy]
%envpip% install rasa_core
%envpip% freeze > requirements.txt