import psycopg2

try:
    con = psycopg2.connect(user="manikya",
                            password="manikyasaiteja",
                            host="devel.cbykvgbnlz7g.ap-south-1.rds.amazonaws.com",
                            port="5432",
                            database="development",
                            connect_timeout=3)
    cur = con.cursor()
except Exception as error:
    print("Error while connecting to PostgreSQL", error)

# try:
# 	cur.execute("CREATE SCHEMA Subscribers")
# 	cur.execute('''CREATE TABLE Subscribers.subscribers(
# 		email_id VARCHAR(255) NOT NULL,
# 		category VARCHAR(255) NOT NULL
# 		)''')
# 	con.commit()
# except Exception as e:
# 	print("Error caught while creating TABLE:",e)

# categories: financial results, management change updates, insider trading,
# special situations, KPI, IPO, Stars shareholdings, Super growth stories, Community stories

# try:
# 	cur.execute("CREATE SCHEMA Articles")
# 	cur.execute('''CREATE TABLE Articles.articles(
# 		article_id SERIAL PRIMARY KEY,
# 		title VARCHAR(255) NOT NULL,
# 		body VARCHAR(255) NOT NULL,
# 		image BYTEA,
# 		category_tag VARCHAR(255) NOT NULL,
# 		company VARCHAR(255) NOT NULL
# 		)''')
# 	con.commit()
# except Exception as e:
# 	print("Error caught while creating TABLE:",e)