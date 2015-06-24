#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import MySQLdb
from string import Template
cgitb.enable()

def main():
    print t.substitute()

t=Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>thread</title>
<font size=\"10\"><div align=\"center\">BBS</div></font>
<div align=\"center\">
<table border=1>
<td valign=\"top\" width=\"583\" height=\"21\" bgcolor=\"#e8e8e8\">
スレッド一覧
</td>
<tr>
<td><a href=\"comment.py?thread=1\">スレッド１</a></td>
</tr>
<tr>
<td><a href=\"comment.py?thread=2\">スレッド２</a></td>
</tr>
</table>
</div>


<h>太郎</h>
<p>押されたボタンは[]です</p>
</html>
""")

main()