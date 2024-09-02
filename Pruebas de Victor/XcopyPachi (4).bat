echo on

net use H: \\hcuvnasva01.grs.root\asvae\HCUV\Proteccion Radiologica

H:

cd "H:\Biplano\xml"
for /F "delims=" %%b in ('dir /b /s **.xml') do xcopy /Y "%%b" "Z:\Dosis pacientes\Angiografo biplano HCUV\Hojas xml\"

cd "H:\CareAnalytics\xml\"
for /F "delims=" %%d in ('dir /b /s **.xml') do xcopy /Y "%%d" "Z:\Dosis pacientes\HCUV - Hemodinamicas\Siemens Artis Zee\Hojas xml\"

cd "H:\Hibrido\xml"
for /F "delims=" %%q in ('dir /b /s **.xml') do xcopy /Y "%%q" "Z:\Dosis pacientes\Quirofano Hibrido HCUV\Hojas xml\"

net use H: /delete /y

exit
