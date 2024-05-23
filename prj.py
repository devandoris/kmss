from pdfquery import PDFQuery

pdf = PDFQuery('devraj.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')
# Extract the text from the elements
#text = [t.text for t in text_elements]
text=""
for t in text_elements:
  text+=t.text

print(text)

l=[]
t=""
c=1
for i in range(len(text)):
  if(text[i]==' '):
    l.append((c,t))
    c=c+1
    t=""
  else:
    t+=text[i]
print(l)

import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="Devaraj123@",database="resume")
curs=conn.cursor()
print(conn)
sql="insert into letters(id,word) values(%s,%s)"
#val=[(1,"a"),(2,"b")]
curs.executemany(sql,l)
conn.commit()
conn.close()