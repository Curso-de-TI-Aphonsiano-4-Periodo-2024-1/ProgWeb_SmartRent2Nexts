@echo off
setlocal
pushd %~dp0
:: Verificando se o Python está instalado
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Python está instalado e configurado na PATH
cd ..
python SmartRent2Nexts.py

:: Pula para o final do script
goto:eof

:: Caso não esteja instaldo, mostrar erro!
:errorNoPython
echo.
echo Error^: Python not installed
pause

popd
endlocal