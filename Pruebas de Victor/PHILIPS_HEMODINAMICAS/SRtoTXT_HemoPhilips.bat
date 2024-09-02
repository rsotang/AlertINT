echo on
Z:
cd Z:\Dosis pacientes\Alertas_Intervencionismo\PHILIPS_HEMODINAMICAS\
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
for /F "delims=" %%g in ('dir /b /s *1.3.46.670589.28*.txt') do xcopy /Y "%%g" "Z:\Dosis pacientes\Alertas_Intervencionismo\Historial pacientes\Hemodinamicas Philips"

dir /b /a-d *.txt > contador.TXT
contador.xlsm
del contador.TXT

exit


