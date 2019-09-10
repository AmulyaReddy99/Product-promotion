import psycopg2

try:
    con = psycopg2.connect(user="postgres",
                            password="",
                            host="localhost",
                            port="5432",
                            database="Promotions",
                            connect_timeout=3)
    cur = con.cursor()
except Exception as error:
    print("Error while connecting to PostgreSQL", error)

try:
	cur.execute('''CREATE TABLE public.categories(
		category VARCHAR(255) NOT NULL UNIQUE,
		category_id SERIAL PRIMARY KEY
		)''')
	con.commit()
except Exception as e:
	print("Error caught while creating categories TABLE:",e)



try:
	cur.execute('''CREATE TABLE public.products(
		product_id SERIAL PRIMARY KEY,
		category_id FOREIGN KEY NOT NULL,
		prod_title VARCHAR(255) NOT NULL,
		description VARCHAR(255) NOT NULL,
		image BYTEA,
		brand VARCHAR(255),
		price NUMERIC,
		rating NUMERIC
		)''')
	con.commit()
except Exception as e:
	print("Error caught while creating TABLE:",e)


# insert product
try:
	fetch = '''SELECT id from categrories where category==given_categ'''
	fetch = cur.execute(fetch)
	if(!fetch):
		cur.execute('''INSERT INTO categories''')
		cur.execute(fetch)
		category_id = fetch.id
	else:
		category_id = fetch.id
	cur.execute('''INSERT INTO public.products(
		product_id SERIAL PRIMARY KEY,
		category_id VARCHAR(255) NOT NULL,
		prod_title VARCHAR(255) NOT NULL,
		description VARCHAR(255) NOT NULL,
		image BYTEA,
		brand VARCHAR(255) NOT NULL,
		price NUMERIC,
		rating NUMERIC
		)''')
	con.commit()
except Exception as e:
	print("Error caught while creating TABLE:",e)


# suggestions
try:
	fetch = '''SELECT id from categrories where category==category_id LIMIT 10'''
	fetchall = cur.execute(fetch)
	cur.execute('''SELECT FROM public.products(
		product_id SERIAL PRIMARY KEY,
		category_id VARCHAR(255) NOT NULL,
		prod_title VARCHAR(255) NOT NULL,
		description VARCHAR(255) NOT NULL,
		image BYTEA,
		brand VARCHAR(255) NOT NULL,
		price NUMERIC,
		rating NUMERIC
		)''')

	fetch = '''SELECT id from categrories where category==category_id LIMIT 10'''
	fetchall = cur.execute(fetch)
	cur.execute('''INSERT INTO public.products(
		product_id SERIAL PRIMARY KEY,
		category_id VARCHAR(255) NOT NULL,
		prod_title VARCHAR(255) NOT NULL,
		description VARCHAR(255) NOT NULL,
		image BYTEA,
		brand VARCHAR(255) NOT NULL,
		price NUMERIC,
		rating NUMERIC
		)''')
	con.commit()
except Exception as e:
	print("Error caught while creating TABLE:",e)





