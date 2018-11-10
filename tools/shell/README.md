## 工作目录
```
$ cat ./fuck.sh
#!/bin/bash
cd /usr/local
pwd

$ ./fuck.sh && pwd
/usr/local
/Users/torapture

$ cat ./fuck.py
#!/usr/local/bin/python
import os
os.chdir("/Users/torapture/Codes")
print os.popen("pwd").read()

$ ./fuck.py && pwd
/Users/torapture/Codes
/Users/torapture
```

## 环境变量
```
$ export _GLOBAL="Aqours"
$ _LOCAL="Sunshine"
$ (pwd; echo "global=$_GLOBAL" "local=$_LOCAL")
/Users/torapture
global=Aqours local=Sunshine

$ cat fuck.sh
#!/bin/bash
echo "local=$_LOCAL"
echo "global=$_GLOBAL”

$./fuck.sh
local=
global=Aqours

$ cat fuck.py
import os
print os.environ.get("_GLOBAL", "unset_global")
print os.environ.get("_LOBAL", "unset_local”)
$ python fuck.py
Aqours
unset_local
```

## source
```
$ cat aqours.sh
#!/bin/bash
cd /etc && pwd
$ source aqours.sh && pwd
/etc
/etc

$ zsh aqours.sh && pwd
/etc
/Users/torapture
```