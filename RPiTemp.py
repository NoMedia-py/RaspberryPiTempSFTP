import pysftp

tempPath = '/sys/class/thermal/thermal_zone0/temp'

try:
    sftp = pysftp.Connection('the ip of your Pi (run ifconfig)', username='your Pi username', password='your Pi password')
    print('connection successfully etablished')
except:
    print('failed to etablish connection to target server')
    exit()

file = sftp.open(tempPath)
raw = file.read()
file.close()

temp = int( bytes.decode( raw[:len(raw) - 1] )) / 1000

print(temp)

sftp.close()