echo on

net use p: \\10.40.87.167\c$\pacs\data

p: 

for /F "delims=" %%a in ('dir /b /s *1.2.840*.dcm') do xcopy /Y "%%a" "Z:\Dosis pacientes\HCUV Angiografo GE\Ficheros SR\"
for /F "delims=" %%b in ('dir /b /s *1.3.46.670589.28*.dcm') do xcopy /Y "%%b" "Z:\Dosis pacientes\HCUV - Hemodinamicas\Hemodinamicas Philips\Ficheros SR\"
for /F "delims=" %%a in ('dir /b /s *1.3.46.670589.29*.dcm') do xcopy /Y "%%a" "Z:\Dosis pacientes\HCUV Angiografo Azurion\Ficheros SR\"
for /F "delims=" %%c in ('dir /b /s *1.3.46.670589.33*.dcm') do xcopy /Y "%%c" "Z:\Dosis pacientes\TC - Segovia\Informes SR\"
for /F "delims=" %%d in ('dir /b /s *1.2.840*.dcm') do xcopy /Y "%%d" "Z:\Dosis pacientes\Alertas_Intervencionismo\GE_VASCULAR"
for /F "delims=" %%e in ('dir /b /s *1.3.46.670589.28*.dcm') do xcopy /Y "%%e" "Z:\Dosis pacientes\Alertas_Intervencionismo\PHILIPS_HEMODINAMICAS"


dir /ad /b  | findstr /v /i "dbase$" > carpetas.txt
for /f "delims=" %%n in (carpetas.txt) do rmdir /s /q %%n
del carpetas.txt

net use p: /delete /y

exit
