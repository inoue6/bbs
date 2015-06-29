#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import MySQLdb
import urllib
from string import Template
import datetime
cgitb.enable()

def show_comment(thread_id):
    connector = MySQLdb.connect(host = "localhost", db = "test", user = "inoue", passwd = "inoPWit", charset = "utf8")
    cursor = connector.cursor()

    cursor.execute(select_id.substitute(thread_id = thread_id))
    result = cursor.fetchall()

    i = 0
    for row in result:
        i += 1
        print comments.substitute(number = i, name = row[2].encode("utf-8"), date = str(row[3]), comment = row[4].encode("utf-8"))

def insert_comment(thread_id, name, comment):
    connector = MySQLdb.connect(host = "localhost", db = "test", user = "inoue", passwd = "inoPWit", charset = "utf8")
    cursor = connector.cursor()

    #cursor.execute("select thread_id  from test.comments order by thread_id desc;")
    #result = cursor.fetchone()
    #if result == None:
    #    thread_id = 1
    #else:
    #    thread_id = result[0]

    insert_text = Template("""select comment_id from test.comments order by comment_id desc;""")
    cursor.execute(insert_text.substitute())
    result = cursor.fetchone()
    if result == None:
        comment_id = 1
    else:
        comment_id = result[0] + 1

    d = datetime.datetime.today()
    date = str(d.year) + "/" + str(d.month) + "/" + str(d.day) + "/" + str(d.hour) + "/" + str(d.minute) + "/" + str(d.second)
    
#    sql = "insert into test.comments values(\"1\", \"1\", \"inoue\", \"2015/6/26/10:20\", \"スレッドを作成しました。\")"
sql1 = "insert into test.comments values(\"" + str(comment_id) + "\", \"" + str(thread_id) + "\", \"" + name + "\",\"" + date + "\", \"" + comment +"\", \"false \")"
    cursor.execute(sql1)

    insert_text = Template("""select comment_number from test.threads where thread_id = " + str(thread_id) + ";""")
    cursor.execute(insert_text.substitute())
    result = cursor.fetchone()
    if result == None:
        comment_number = 1
    else:
        comment_number = result[0] + 1

    sql2 = "update test.threads set comment_number = " + str(comment_number)
    sql3 = "update test.threads set update_day = " + date
    cursor.execute(sql2)
    cursor.execute(sql3)

    connector.commit()

    cursor.close()
    connector.close()

def main():
    form = cgi.FieldStorage()
    thread_id = form.getvalue("thread", "none")
    name = form.getvalue("name","none")
    date = form.getvalue("date","none")
    comment = form.getvalue("comment","none")
    if form.has_key("name"):
        insert_comment(thread_id, name, comment)

    print html1.substitute(thread_id = thread_id)

    show_comment(thread_id)

    print html2.substitute(form = comment_box.substitute(thread_id = thread_id))

html1 = Template("""Content-Type: text/html;charset=utf-8\n\n
<!doctype html>
<html>
<title>thread${thread_id}</title>
<font size=\"10\"><div align=\"center\">BBS</div></font>
<div align=\"center\">
<a href=\"thread.py\">戻る</a>
<br><br>
""")

html2 = Template("""
${form}
</div>
</html>
""")

comments = Template("""
<br>
<table border=1>
<tr><td width=\"580\">${number} ${name} ${date}</td></tr>
<tr><td>${comment}</td></tr>
</table>
""")

comment_box = Template("""
<br><br>
<form action=\"http://ubuntu7/inoue/comment.py?thread=${thread_id}\" method=\"post\">
<table border=1><tr><td width=\"400\">
<p>　名前：<input type=\"text\" name=\"name\" size=\"40\"></p>
<p>　コメント<br><div align=\"center\"><textarea name=\"comment\" cols=\"40\" rows=\"10\" ></textarea></p>
<input type=\"submit\" value=\"送信\">
<input type=\"reset\" value=\"リセット\"></div><br>
</td></tr></table>
</form>
""")

select_id = Template("""select * from test.comments where thread_id = ${thread_id};""")


main()