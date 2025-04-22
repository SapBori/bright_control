# bright_control



- Setting Display Light in Set Time

1. Check Display in Shown Us (echo $DISPLAY)
1. If Not Printed ':0' open light_down.sh and light_up.sh files and Modify DISPLAY:(:'Monitor Number' ) 
1. open cron_script.txt and copy Script
2. open terminal and Type crontab -e
3. select ***/nano
4. paste cron_script (Maybe Shitf+insert is Copy Key in nano)
5. save crontab (ctrl+s)
6. DONE!!!




## crontab Time 

- minute hour day month year 
- Every 12 pm  >> 0 12 * * *
- Only Period 2 minute >> */2 * * * *
  
