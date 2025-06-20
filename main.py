import datetime
import sqlite3


def get_date():
    today = datetime.date.today()
    return f"{today.day}/{today.month}/{today.year}"


def db_dml_operation(q):
    con = sqlite3.connect("library_db.db")
    con.execute(q)
    con.commit()
    con.close()


def db_select_operation(q):
    con = sqlite3.connect("library_db.db")
    cur = con.cursor()
    cur.execute(q)
    data = cur.fetchall()
    cur.close()
    con.close()
    return data

def issue_book(book_num, student_enroll):
    today = get_date()
    q = "insert into all_issued(senroll, bknum, idate, rstatus) values({0}, {1}, '{2}', 'NO')".format(student_enroll, book_num, today)
    db_dml_operation(q)
    return "Book Issued..."


def return_book(book_num):
    rdate = get_date()
    q = "update all_issued set rdate='{0}', rstatus='YES' where bknum={1} and rstatus='NO'".format(rdate, book_num)
    db_dml_operation(q)
    return "Book Returned.."


def view_not_ret():
    q = "select senroll, bknum, idate from all_issued where rstatus='NO'"
    return db_select_operation(q)



def search_stud(senroll):
    q = "select sname, semail, smob from all_studs where senroll=" + senroll
    data = db_select_operation(q)
    return data


def search_book(bnum):
    q = "select btitle, bauth, bpublication from all_books where bknum=" + bnum
    data = db_select_operation(q)
    return data



def stud_history(senr):
    q = "select bknum, idate, rdate, rstatus from all_issued where senroll=" + senr
    data = db_select_operation(q)
    return data


def book_history(bnum):
    q = "select senroll, idate, rdate, rstatus from all_issued where bknum=" + bnum
    data = db_select_operation(q)
    return data


def add_new_book(bknum, btitle, bauth, bpublication):
    q = "insert into all_books values({0}, '{1}', '{2}', '{3}')".format(bknum, btitle, bauth, bpublication)
    db_dml_operation(q)


def add_new_stud(senroll, sname, smob, semail):
    q = "insert into all_studs values({0}, '{1}', '{2}', {3})".format(senroll, sname, semail, smob)
    db_dml_operation(q)