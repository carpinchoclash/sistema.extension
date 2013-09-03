#!/bin/usr/env python 
import sys
import os

# 1. Write domain to hosts File
sitename = sys.argv[1]

f = open('/etc/hosts','a')
f.write('127.0.0.1    www.'+sitename+'.dev '+sitename+'.dev\n')
f.close()

# 2. Create site file in sites available
vHost = '''<VirtualHost *:80>
	ServerAdmin webmaster@localhost
        ServerName '''+sitename+'''.dev
        ServerAlias www.'''+sitename+'''.dev
	DocumentRoot /var/www/'''+sitename+'''/web
        ErrorLog /var/www/'''+sitename+'''/logs/error.log
        CustomLog /var/www/'''+sitename+'''/logs/access.log combined
</VirtualHost>'''

os.system('touch /etc/apache2/sites-available/'+sitename+'.dev')
f = open('/etc/apache2/sites-available/'+sitename+'.dev','a')
f.write(vHost+'\n')
f.close()

# 3. Enable site
os.system('a2ensite '+sitename+'.dev')


#.4 Create needed folders and assign user permissions:
os.system('mkdir /var/www/'+sitename)
os.system('mkdir /var/www/'+sitename+'/logs')
os.system('touch /var/www/'+sitename+'/logs/access.log')
os.system('touch /var/www/'+sitename+'/logs/error.log')

os.system('chown carpincho /var/www/'+sitename+' -R')
os.system('chgrp carpincho /var/www/'+sitename+' -R')

os.system('cp /home/carpincho/pys/sources/symfony/* /var/www/'+sitename+' -R')
os.system('chmod 777 /var/www/'+sitename+'/app/cache -R')
os.system('chmod 777 /var/www/'+sitename+'/app/logs -R')

# 5. Reload Apache
os.system('/etc/init.d/apache2 reload')

# 6. Exit with a success msg
print '\n------------------------------------------------'
print '\nEl sitio '+sitename+' fue activado en Apache2'
print '\n------------------------------------------------'
