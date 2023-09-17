from sql_connection import get_sql_connection



def get_all_products(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM plant_nursery.product;"

    cursor.execute(query)

    response = []



    for(product_id, name, price_per_unit, quantity) in cursor:
        response.append(
        {
            'product_id' : product_id,
            'name' : name,
            'price_per_unit' : price_per_unit,
            'quantity' : quantity,
        }
    )
    

    return response



def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product" 
             "(name, quantity, price_per_unit)" 
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['quantity'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))

    print(delete_product(connection,13))