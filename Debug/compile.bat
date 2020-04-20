@echo OFF

cl 2>&1 | find /i "x64"

if not errorlevel 1 (
	cl /W4 /EHsc /I ..\YOKOGAWA\tmctl5101\vc /I ..\wingetopt\src ..\wingetopt\src\*.c ..\WT310\*.cpp ..\YOKOGAWA\tmctl5101\vc\tmctl64.lib /link /out:WT310.exe
	copy ..\YOKOGAWA\tmctl5101\dll\tmctl64.dll .
	copy ..\YOKOGAWA\tmctl5101\dll\YKMUSB64.dll .
) else (
	cl /W4 /EHsc /I ..\YOKOGAWA\tmctl5101\vc /I ..\wingetopt\src ..\wingetopt\src\*.c ..\WT310\*.cpp ..\YOKOGAWA\tmctl5101\vc\tmctl.lib /link /out:WT310.exe
	copy ..\YOKOGAWA\tmctl5101\dll\tmctl.dll .
	copy ..\YOKOGAWA\tmctl5101\dll\YKMUSB.dll .
)

del *.obj
