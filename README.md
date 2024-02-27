# Toy Shop Django Project

## Overview

This Django project, named Toy Shop, is an online web application that serves as a toy store. It includes features such as a blog for articles, a product catalog, a shopping basket for adding products, and a payment system for processing orders.

## Features

1. **Blog Module**: Allows users to read and explore articles categorized by different topics.

2. **Product Module**: Provides a product catalog with details such as product name, description, category, stock, and price.

3. **Shopping Basket**: Users can add products to their shopping basket for a seamless shopping experience.

4. **Payment System**: Integrates a payment system for users to complete their orders securely.

## Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/toy-shop.git
   ```

2. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database.

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the Django admin panel.

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

5. Run the development server.

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://localhost:8000/](http://localhost:8000/).

## Usage

1. Access the Django admin panel to manage content.

   - [http://localhost:8000/admin/](http://localhost:8000/admin/)

2. Explore the main pages:

   - Home: [http://localhost:8000/](http://localhost:8000/)
   - Blog: [http://localhost:8000/blog/](http://localhost:8000/blog/)
   - Product Catalog: [http://localhost:8000/product/product_list/](http://localhost:8000/product/product_list/)
   - Shopping Basket: [http://localhost:8000/shopping_basket/view_cart/](http://localhost:8000/shopping_basket/view_cart/)
   - Payment: [http://localhost:8000/peyment/](http://localhost:8000/peyment/)

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an [issue](https://github.com/your-username/toy-shop/issues) or create a [pull request](https://github.com/your-username/toy-shop/pulls).

## License

This project is licensed under the [MIT License](LICENSE).