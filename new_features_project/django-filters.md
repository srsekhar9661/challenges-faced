1. Creating Custom Filters

Where to Put Them: Create a directory called templatetags inside your app (if it doesn't exist already). This directory must contain an empty file named __init__.py to be recognized as a Python package.
The Code:

# myapp/templatetags/my_filters.py

from django import template

register = template.Library()  # Register your filters

@register.filter(name='multiply') 
def multiply(value, arg):
    """Multiplies the value by the argument."""
    return value * arg

@register.filter
def to_uppercase(value):
    """Converts a string to uppercase."""
    return value.upper() 
Explanation:
register = template.Library(): Creates a template library instance to register your filters.
@register.filter: The decorator that registers a function as a template filter. You can optionally provide a name argument (e.g., @register.filter(name='multiply')) to specify the filter's name in templates. If omitted, the function's name becomes the filter name.
The decorated functions (e.g., multiply, to_uppercase) define the filter's logic. They take at least one argument: the value being filtered. You can have additional arguments.
2. Using Custom Filters in Templates

Load Your Filters: At the top of your Django template, use the {% load %} tag to load your custom filter library:

{% load my_filters %} 
Apply the Filters:

<h1>{{ product.price|multiply:2 }}</h1>  
<p>{{ product.name|to_uppercase }}</p>
Explanation:
The pipe symbol (|) applies a filter to a variable.
product.price|multiply:2: Multiplies the product's price by 2.
product.name|to_uppercase: Converts the product's name to uppercase.

{% with new_price=product.price|multiply:2 %}
    <h1>The new price is: ${{ new_price }}</h1>
{% endwith %}
Example: Censoring Words

Let's create a filter to censor specific words from a text:


# myapp/templatetags/my_filters.py

from django import template

register = template.Library()

@register.filter
def censor_words(value, bad_words):
    """Replaces a list of bad words with asterisks."""
    for word in bad_words.split(','):
        value = value.replace(word, '*' * len(word))
    return value
In your template:


{% load my_filters %}

<p>{{ comment.text|censor_words:"badword1,badword2,badword3" }}</p>
Key Points & Best Practices:

Keep Filters Simple: Filters should ideally focus on presentation logic, not complex business logic.
Avoid Side Effects: Filters should be side-effect free. They should not modify the original data, only return a transformed version.
Test Your Filters: Write unit tests to ensure your custom filters work as expected.
Let me know if you'd like to explore more advanced filter use cases, such as filters that accept arguments from your context or filters that interact with your models!


