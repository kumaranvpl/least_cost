Find least cost for buyer
===================


----------


Problem
-------------

> **Given:**

> - An ecommerce platform has sellers/buyers from various states and each seller may set different price for the product. The shipment may cut across multiple states and each state may levy a tax. Recommend the least cost option to the buyer.

> **Assumption:**

> - Buyers and sellers are from different states. Each seller sets different price for same product. **If buyer and seller are from same state, then that state tax only applied(much like intrastate tax and VAT). Else if the seller and buyer are from different states, then both seller state and buyer state taxes are applied(like interstate tax and CST).**


----------


Instruction
-------------------

Follow the following instructions to setup the project in your local machine

> **Steps:**

> - git clone or download the project
> - Use mysql-server version >= 5.6
>- Install following dependencies using apt-get
>->sudo apt-get install libmysqlclient-dev
>->sudo apt-get install python-mysqldb
>->sudo apt-get install python-dev
>- do **pip install -r requirements.txt**
> - Update config.json with your local environment settings.
> - Create an empty database and specify the database name in config.json
> - You can setup the db either by importing the .sql file(contains demo data) or by running the following migration **python manage.py db upgrade**(creates empty tables). 
> - To run flask server **python app.py**

----------


Available Routes
-------------

Go through **app.py** to see list of available routes

#### Routes 

- **/calculate_least_cost** to calculate least cost for buyer
- **/add_state** to add states(already all states are added in demo data)
- **/add_product** to add product
- **/add_seller** to add seller
- **/add_buyer** to add buyer
- **/add_selling** to add a selling entry which adds seller, product which this seller going to sell and base price(without tax) of the product from this seller


Contact
--------------------

I hope so these details are enough to run the project. [Mail me](mailto:kumaranvpl@gmail.com) if you have doubts or raise an issue.