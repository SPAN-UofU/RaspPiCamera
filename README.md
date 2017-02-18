# RaspPiCamera

clone this to /home/pi

make sure camera.py is executable (if not, chmod a+x camera.py)

Cron task at 9PM

crontab -e

add:

0 21 * * * /home/pi/RaspPiCamera/camera.py
