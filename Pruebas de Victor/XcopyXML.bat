echo on

net use H: \\hcuvnasva01.grs.root\asvae\HCUV

H:

cd "H:\Proteccion Radiologica\Hibrido\xml"
@echo off
    	for /f %%a in (' dir /o-d /b /a-d "202*.xml" ') do set "lastFile=%%~a" & goto :found
	:found
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\PRUEBAHIBRIDO\"
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\Historial pacientes\Hibrido"

cd "H:\Proteccion Radiologica\CareAnalytics\xml\"
    	for /f %%a in (' dir /o-d /b /a-d "202*.xml" ') do set "lastFile=%%~a" & goto :found2
	:found2
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\SIEMENS_HEMODINAMICAS_ALERTIN"
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\Historial pacientes\Hemodinamica Siemens"

cd "H:\Proteccion Radiologica\Biplano\xml\"
    	for /f %%a in (' dir /o-d /b /a-d "202*.xml" ') do set "lastFile=%%~a" & goto :found2
	:found2
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\SIEMENS_BIPLANO_ALERTIN"
	xcopy /Y "%lastFile%" "Z:\Dosis pacientes\Alertas_Intervencionismo\Historial pacientes\Biplano"

net use H: /delete /y

exit