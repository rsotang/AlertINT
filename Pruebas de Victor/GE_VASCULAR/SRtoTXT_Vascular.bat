echo on
Z:
cd Z:\Dosis pacientes\Alertas_Intervencionismo\GE_VASCULAR\
dir /b /a-d *.dcm > ficheros.TXT
FOR	%%a IN (ficheros.txt) DO (
	IF %%~za NEQ 0 (
		goto:grupo

	)
)

del ficheros.txt
del Export.bat
del *.xml
del *.dcm
exit

:grupo
rename.xlsm
call Export.bat
python XMLaTXT.py
del ficheros.txt
del Export.bat
del *.xml
del *.dcm
for /F "delims=" %%f in ('dir /b /s *1.2.840*.txt') do xcopy /Y "%%f" "Z:\Dosis pacientes\Alertas_Intervencionismo\Historial pacientes\Angiografo GE"

dir /b /a-d *.txt > contador.TXT
contador.xlsm
del contador.TXT

exit