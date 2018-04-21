import psycopg2
con = psycopg2.connect(host='localhost', database='development',
user='bio', password='bio')
cur = con.cursor()

cur.execute('select * from sensors')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()

