Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Users\marce\Documents\Python Projects\my-project\run.bat" & Chr(34), 0
Set WshShell = Nothing