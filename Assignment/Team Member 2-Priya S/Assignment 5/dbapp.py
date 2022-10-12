import ibm_db

hostname="54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid="kgg08718"
pwd="deqP1YOEclGBm6Hm"
driver="(IBM DB2 ODBC DRIVER)"
db="bludb"
port="32733"
protocol="TCPIP"
cert="certificate.crt.crt"


dsn=("DATABASE={0};"
     "HOSTNAME={1};"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "pwd={5};"
     ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())
    

