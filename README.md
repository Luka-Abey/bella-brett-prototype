### Welcome !
This is a repo to document a clothing brand site I am developing.

### Aims:
#### Completed:
- [x] Create template
- [x] Check deliverables
- [x] Finalise design stage one:
- [x] Aesthetic design
- [x] DB models design
- [x] Implement design stage one
- [x] Responsive navigation bar
- [x] Responsive page
- [x] Simple item upload, from Django admin
- [x] Image upload as part of item, from Django admin
- [x] Dynamically rendered HTML home/products page
- [x] Dynamically rendered HTML basket
- [x] User functionality integrated
- [x] Add to cart
- [x] Update cart/quantity
 
#### To Do:

[] Migrate database to PostgreSQL
[] Sort issues around deployment
[] Deploy
[] Checkout
[] Payment - research and conclude - Stripe or Banked or summet else?
[] Order summary/success
[] Order confirmation
[] Guest users



### Run Locally:

Create the directory you'd like to clone into, navigate to it, and open Git Bash. Run the following command:
```
git clone https://github.com/Luka-Abey/eCommerce.git
```

Once you have cloned the repo, navigate to eCommerce/src/eCommerce and here run the command:
```
winpty python manage.py createsuperuser
```

This runs you through an administrator setup, so that you can access the admin panel as well as the main site.
Following this, run:
```
<python manage.py makemigrations>
<python manage.py migrate>
```
And then:
```
<python manage.py runserver>
```
This will get the server running, by default on port 8000. To access the admin panel, add /admin to the URL. 

This is the 'behind the scenes' of the application, where you can add items and customers to the shop. 

If you follow the items section in the admin panel, you can add new items to the store, and add images corresponding to these items as well. The site has been optimised for images of 500 x 700 pixels.

To be able to add items to a cart you need to create a specific customer object, which can also be done in the admin panel. Once that is completed, this information will then be displayed on the home page product section, and can be added to cart.

I’ve configured the .gitignore to ignore media, so some icons such as up/down arrows for quantity selection in the basket, and the home page image banner will not be visible to you.

Thanks for looking, any tips/thoughts please PR/open issues away.
