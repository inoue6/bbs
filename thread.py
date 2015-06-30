#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import MySQLdb
from string import Template
import datetime
cgitb.enable()

def show_thread():
	connector = MySQLdb.connect(host = "localhost", db = "test", user = "inoue", passwd = "inoPWit", charset = "utf8")
	cursor = connector.cursor()

	cursor.execute("select * from test.threads;")
	result = cursor.fetchall()

	for row in result:
		print threads.substitute(thread_id = row[0], thread_name = row[1].encode("utf-8"), creator_name = row[2].encode("utf-8"), comment_number = row[3], update_day = row[4])

threads = Template("""
<tr><td><table><tr><td width=\"300\"><a href=\"comment.py?thread=${thread_id}\">${thread_name}</a></td><td width=\"200\">${creator_name}</td><td width=\"100\"><div align=\"center\">${comment_number}</div></td><td width=\"200\"><div align=\"center\">${update_day}</div></td></tr></table></td></tr>
""")

def insert_thread(thread_name, creator_name):
	connector = MySQLdb.connect(host = "localhost", db = "test", user = "inoue", passwd = "inoPWit", charset = "utf8")
	cursor = connector.cursor()

	cursor.execute("select thread_id from test.threads order by thread_id desc;")
	result = cursor.fetchone()
	if result == None:
		thread_id = 1
	else:
		thread_id = result[0] + 1

	cursor.execute("select comment_id from test.comments order by comment_id desc;")
	result = cursor.fetchone()
	if result == None:
		comment_id = 1
	else:
		comment_id = result[0] + 1

	d = datetime.datetime.today()
	date = str(d.year) + "/" + str(d.month) + "/" + str(d.day) + "/" + str(d.hour) + "/" + str(d.minute) + "/" + str(d.second)
	
	sql1 = "insert into test.threads values(\"" + str(thread_id) +"\", \"" + thread_name + "\", \"" + creator_name + "\", \"1\", \"" + date + "\");"
	cursor.execute(sql1)

	sql2 = "insert into test.comments values(\"" + str(comment_id) + "\", \"" + str(thread_id) + "\", \"" + creator_name + "\", \"" + date + "\", \"新規スレッドを作成しました。\", \"false\");"
	cursor.execute(sql2)

	connector.commit()

	cursor.close()
	connector.close()

def main():
	form = cgi.FieldStorage()
	create_flag = form.getvalue("create_thread", "false")

	if create_flag == "true":
		print create_thread.substitute()
	else:
		print thread1.substitute()
		show_thread()
		print thread2.substitute()

	thread_name = form.getvalue("thread_name")
	creator_name = form.getvalue("creator_name")
	if 	form.has_key("thread_name"):
		insert_thread(thread_name, creator_name)

thread1 = Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>thread</title>
<font size=\"10\"><div align=\"center\">BBS</div></font>
<div align=\"center\">
<font><a href=\"thread.py?create_thread=true\">新規作成</a></font>
<form action=\"http://ubuntu7/inoue/thread.py?create_thread=false\"><input type=\"submit\" value=\"更新\"></form>
<br><br>
<table border=1>
<tr><td bgcolor=\"#e8e8e8\" valign=\"top\" width=\"800\"><div align=\"center\">スレッド一覧</div></td></tr>
<tr><td><table><tr><td width=\"300\">スレッド名<td><td width=\"200\">制作者</td><td width=\"100\"><div align=\"center\">コメント数</div></td><td width=\"200\"><div align=\"center\">最終更新時間</div></td></tr></table></td></tr>
""")

thread2 = Template("""
</table>
</div>
</html>
""")

create_thread = Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>create_thread</title>
<br><br><br>
<div align=\"center\">
<font size=30>スレッド作成</font>
<br><br>
<p><a href=\"thread.py?create_thread=false\">戻る</a></p>
<form action=\"http://ubuntu7/inoue/thread.py?create_thread=false\" method=\"post\">
<table border=1><tr><td width=\"400\">
<p>　　　　名前：<input type=\"text\" name=\"creator_name\" size=\"40\"></p>
<p>　スレッド名：<input type=\"text\" name=\"thread_name\" size=\"40\"></p>
<div align=\"center\">
<input type=\"submit\" value=\"作成\">
<input type=\"reset\" value=\"リセット\"></div><br>
</div>
</td></tr></table>
</form>
</div>
</html>
""")

main()
