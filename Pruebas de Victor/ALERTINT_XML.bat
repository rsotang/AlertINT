echo on
Z:
cd Z:\Dosis pacientes\Alertas_Intervencionismo\SIEMENS_BIPLANO_ALERTIN
call :bytes1 *.xml
timeout /t 180

:bytes1
if %~z1 GTR 1000 (
BIPLANO.XLSM
del *.xml
) else (
del *.xml
)

cd Z:\Dosis pacientes\Alertas_Intervencionismo\SIEMENS_HEMODINAMICAS_ALERTIN
call :bytes2 *.xml
timeout /t 180

:bytes2
if %~z1 GTR 1000 (
ARTISZEE.XLSM
del *.xml
) else (
del *.xml
)

cd Z:\Dosis pacientes\Alertas_Intervencionismo\PRUEBAHIBRIDO
call :bytes3 *.xml

:bytes3
if %~z1 GTR 1000 (
HIBRIDO.XLSM
del *.xml
) else (
del *.xml
)

exit