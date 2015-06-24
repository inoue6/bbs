#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import MySQLdb
import urllib
from string import Template
cgitb.enable()

def main():
    thread_id=cgi.FieldStorage()
    print t.substitute(thread_id=thread_id["thread"].value)

t=Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>thread${thread_id}</title>
<font size=\"10\"><div align=\"center\">BBS</div></font>
<div align=\"center\">
<a href=\"thread.py\">戻る</a>
<table border=1>
<td valign=\"top\" width=\"583\" height=\"21\" bgcolor=\"#e8e8e8\">
コメント一覧
<tr>
<td>
コメント
</td>
</tr>
</table>
</div>
</td>
</html>
""")

main()