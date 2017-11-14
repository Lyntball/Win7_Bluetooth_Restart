##This is a small program to call and restart the Bluetooth service when needed
##on a Win7 PC

##Created By Lynton Brown##

import win32serviceutil ##Import the win32serviceutil Library

service_names = ['Bluetooth Device Monitor','Bluetooth Media Service', 
                                  'Bluetooth OBEX Service', 'Bluetooth Support Service'] ##Table to hold all Services to be called (for later expantion)
for service in service_names: ##For loop to go through each service name
##    win32serviceutil.StartService(service) ##Start Service called in for loop ##Commented out after finding out about Restart
##    win32serviceutil.StopService(service) ##Stop Service called in for loop ##Commented out after finding out about Restart
    win32serviceutil.RestartService(service) ##Restart Service called in for loop
