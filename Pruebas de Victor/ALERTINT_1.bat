echo on

Z:
cd Z:\Dosis pacientes\Alertas_Intervencionismo\GE_VASCULAR\
DatosVascular.xlsm
del *.txt
timeout /t 180

cd Z:\Dosis pacientes\Alertas_Intervencionismo\PHILIPS_HEMODINAMICAS\
DatosHemodinamicaPhilips.xlsm
del *.txt

exit

