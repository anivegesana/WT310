cl /W4 /EHsc /I ..\YOKOGAWA\tmctl5101\vc /I ..\wingetopt\src ..\wingetopt\src\*.c ..\WT310\*.cpp ..\YOKOGAWA\tmctl5101\vc\tmctl64.lib /link /out:WT310.exe
copy ..\YOKOGAWA\tmctl5101\dll\* .
del *.obj
