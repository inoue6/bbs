#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import MySQLdb
import urllib
from string import Template
cgitb.enable()

def insert_comment():
    data = cgi.FieldStorage()
    name = data.getvalue("name","none")
    date = data.getvalue("date","none")
    comment = data.getvalue("comment","none")

    connector = MySQLdb.connect(host = "localhost", db = test, user = "inoue", passwd = "inoPWit", charset $
    cursor = connector.cursor()

    cursor.execute("select thread_id from threads order by thread_id desc;")
    result = cursor.fetchall()
    thread_id = result[0]

    cursor.execute("select comment_id from comments order by comment_id desc;")
    result = cursor.fetchall()
    comment_id = result[0]

    sql = "insert into comments values(" + str(thread_id) + ", " + str(comment_id) + ", " +  name + ", " + $

def main():
    thread_id = cgi.FieldStorage()
    print t.substitute(thread_id = thread_id["thread"].value, form = form.substitute())
t = Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>thread${thread_id}</title>
<font size=\"10\"><div align=\"center\">BBS</div></font>
<div align=\"center\">
<a href=\"thread.py\">戻る</a>
<br><br>
<table border=1>
<tr><td width=\"580\">1 inoue 2015/6/25/9:46</td></tr>
<tr><td>あいうえおかきくけこさしすせそたちつてとなにぬねのがぎふへほまみむめもやゆよらりるれろわをん</td></$
</table>
<br>
<table border=1>
<tr><td width=\"580\">2 inoue 2015/6/25/9:47</td></tr>
<tr><td>アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン</td></$
</table>
<br>
<table border=1>
<tr><td width=\"580\">1 inoue 2015/6/25/9:46</td></tr>
<tr><td>あいうえおかきくけこさしすせそたちつてとなにぬねのがぎふへほまみむめもやゆよらりるれろわをん</td></$
</table>
<br>
<table border=1>
<tr><td width=\"580\">2 inoue 2015/6/25/9:47</td></tr>
<tr><td>アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン</td></$
</table>
${form}
</div>
</html>
""")

comments = Template("""
<br>
<table border=1>
<tr><td width=\"580\">${comment_id} ${name} ${date}</td></tr>
<tr><td>${comment}</td></$
</table>
""")

form = Template("""
<br><br>
<form action=\"http://ubuntu7/inoue/insert_comment.py\" method=\"post\">
<table border=1><tr><td width=\"400\">
<p>　名前：<input type=\"text\" name=\"name\" size=\"40\"></p>
<p>　コメント<br><div align=\"center\"><textarea name=\"comment\" cols=\"40\" rows=\"10\" ></textarea></p>
<input type=\"submit\" value=\"送信\">
<input type=\"reset\" value=\"リセット\"></div><br>
</td></tr></table>
</form>
""")

main()