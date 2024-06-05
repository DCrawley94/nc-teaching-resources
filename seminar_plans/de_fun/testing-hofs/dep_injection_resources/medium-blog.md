In this blog post, I want to introduce dependency injection starting by giving a real-life example case for dependency injection. It will be very easy to understand for you after you read the example.

Dependency injection is a way to implement Inversion of Control (IoC).

Since Python is a popular language it will be easier for you to understand the subject. Let’s imagine a real-life scenario involving a coffee shop to illustrate dependency injection:

# The Coffee Shop Without Dependency Injection

Imagine you walk into a small coffee shop called Joe’s Java. In this coffee shop, when you order a latte, the barista named Joe does everything from scratch. He grows his coffee beans in the back, milks the cow, and even handcrafts the cup you drink from. It’s a one-man show. If Joe decides to change the type of milk or coffee beans he uses, he has to adjust his entire process.

and let’s create an object-oriented demonstration for “Joe’s Java” coffee shop:

```py
class JoesJava:
    def __init__(self):
        self.cup = self.create_cup()
        self.milk = self.milk_cow()
        self.coffee_beans = self.grow_coffee_beans()

    def create_cup(self):
        return "Handcrafted clay cup"

    def milk_cow(self):
        return "Fresh cow's milk"

    def grow_coffee_beans(self):
        return "Home-grown Arabica beans"

    def make_latte(self):
        return f"Latte served in a {self.cup} with {self.milk} and made with {self.coffee_beans}"

joes_java = JoesJava()

latte = joes_java.make_latte()
print(latte)
```

# The Coffee Shop With Dependency Injection

Now, let’s consider a coffee shop named The Modern Mug, across the street that operates differently. Here, when you order a latte, the barista, Emma, takes the cup provided by a local potter, uses milk from a nearby dairy farm, and sources coffee beans from a variety of local and international growers.

Emma’s coffee shop is designed to be adaptable. She has several suppliers for cups, milk, and coffee beans. If she wants to switch suppliers, she doesn’t need to change how she makes coffee. She just accepts the new ingredients (dependencies) provided to her.

and let’s create an object-oriented demonstration for “The Modern Mug” coffee shop, too:

```py
class CupProvider:
    def provide_cup(self):
        pass

class MilkProvider:
    def provide_milk(self):
        pass

class CoffeeBeanProvider:
    def provide_coffee_beans(self):
        pass

class LocalPotterCupProvider(CupProvider):
    def provide_cup(self):
        return "Ceramic cup from local potter"

class DairyFarmMilkProvider(MilkProvider):
    def provide_milk(self):
        return "Organic cow's milk from nearby dairy farm"

class InternationalCoffeeBeanProvider(CoffeeBeanProvider):
    def provide_coffee_beans(self):
        return "Arabica beans from South America"

class CoffeeShop:
    def __init__(self, cup_provider, milk_provider, coffee_bean_provider):
        self.cup_provider = cup_provider
        self.milk_provider = milk_provider
        self.coffee_bean_provider = coffee_bean_provider
    def make_latte(self):
        cup = self.cup_provider.provide_cup()
        milk = self.milk_provider.provide_milk()
        coffee_beans = self.coffee_bean_provider.provide_coffee_beans()
        return f"Latte served in a {cup} with {milk} and made with {coffee_beans}"

cup_provider = LocalPotterCupProvider()
milk_provider = DairyFarmMilkProvider()
coffee_bean_provider = InternationalCoffeeBeanProvider()

the_modern_mug = CoffeeShop(cup_provider, milk_provider, coffee_bean_provider)

latte = the_modern_mug.make_latte()
print(latte)
```

Here’s how “The Modern Mug” coffee shop benefits from the dependency injection in its daily operations:

**Adaptability**: One day, the local dairy farm runs into a supply issue. Emma quickly switches to another dairy without disrupting her coffee-making process. She can do this because her coffee-making process isn’t tied to a single dairy supplier.

**Reusability**: Emma can now create customized drinks easily. She can inject different types of milk (almond, soy, oat) or different coffee blends based on the customer’s preference without altering her method of making a latte.

**Maintainability**: When a new potter offers her a better deal on cups, Emma can accept the offer without any impact on her coffee shop’s operations. She doesn’t need to retrain her staff or change any other part of her coffee-making process.

**Testability**: Emma wants to experiment with a new exotic coffee bean blend. Instead of changing her entire stock, she can simply introduce a small batch of the new blend into her process to see how her customers like it.

In this story, The Modern Mug operates on the principles of dependency injection. Emma’s ability to accept different dependencies (milk, coffee beans, cups) without changing the internal workings of her coffee-making process makes her business flexible and efficient, much like how dependency injection in software allows for flexibility, reusability, and ease of maintenance. Emma has the potential to accelerate preparation timelines and has more control over his work.

# Using Dependency Injection Libraries in Python

In the preceding section, we showed examples of dependency injection (DI) and discussed its advantages.

A DI framework streamlines the handling of dependencies, leading to better code maintainability. It automatically constructs and delivers the necessary dependencies to the components that need them, which minimizes the burden of manual dependency setup and redundant code.

Considering the variety of DI frameworks available in Python, our discussion will center on two of the most popular ones, as indicated by the number of stars they’ve received on GitHub.

We’re going to delve into three distinct methods for dependency management. Initially, we will develop a bespoke DI mechanism to gain a deeper insight into how DI frameworks function. Subsequently, we will delve into two specific Python DI frameworks: Dependency Injector and Injector, to evaluate their characteristics and how they are used.

# Dependency Injector

To use the dependency-injector library in Python, you would first need to install the library using pip:

`pip install dependency-injector`

Then we can define our providers and containers. Below is an example of how you can restructure “The Modern Mug” coffee shop’s way of working using the dependency-injector library:

```py
from dependency_injector import containers, providers


class CupProvider:
    def provide_cup(self):
        pass

class MilkProvider:
    def provide_milk(self):
        pass

class CoffeeBeanProvider:
    def provide_coffee_beans(self):
        pass

class LocalPotterCupProvider(CupProvider):
    def provide_cup(self):
        return "Ceramic cup from local potter"

class DairyFarmMilkProvider(MilkProvider):
    def provide_milk(self):
        return "Organic cow's milk from nearby dairy farm"

class InternationalCoffeeBeanProvider(CoffeeBeanProvider):
    def provide_coffee_beans(self):
        return "Arabica beans from South America"

class CoffeeShop:
    def __init__(self, cup_provider, milk_provider, coffee_bean_provider):
        self.cup_provider = cup_provider
        self.milk_provider = milk_provider
        self.coffee_bean_provider = coffee_bean_provider
    def make_latte(self):
        cup = self.cup_provider.provide_cup()
        milk = self.milk_provider.provide_milk()
        coffee_beans = self.coffee_bean_provider.provide_coffee_beans()
        return f"Latte served in a {cup} with {milk} and made with {coffee_beans}"

class Container(containers.DeclarativeContainer):
    cup_provider = providers.Factory(LocalPotterCupProvider)
    milk_provider = providers.Factory(DairyFarmMilkProvider)
    coffee_bean_provider = providers.Factory(InternationalCoffeeBeanProvider)
    coffee_shop = providers.Factory(
        CoffeeShop,
        cup_provider=cup_provider,
        milk_provider=milk_provider,
        coffee_bean_provider=coffee_bean_provider,
    )

container = Container()
the_modern_mug = container.coffee_shop()

latte = the_modern_mug.make_latte()
print(latte)
```

In this example above, we defined a Container class and the library’s Factory provider to declare our dependencies (CupProvider, MilkProvider, CoffeeBeanProvider) and the CoffeeShop itself. When we want to create a CoffeeShop instance, we can now do so using the container.coffee_shop() factory method, which automatically injects the dependencies into our class. This setup allows us to easily replace or configure dependencies without changing the CoffeeShop class or its consumers. We can use it straightforwardly to manage complex dependency injections and configurations, especially in larger applications.

# Rodi

rodi is a dependency injection package for Python. One of my friends suggested me to check out this package and I liked it. It is designed to provide an easy and lightweight way to manage dependencies in Python applications, following the principles of inversion of control (IoC) to help develop loosely coupled code. We can declare our services and their dependencies, and then the container will take care of creating and injecting those dependencies when needed inside the project. First, you need to install the “rodi” package using pip:

`pip install rodi`
After installing the package, you can write your application like this:

```py
import rodi

class CupProvider:
    def provide_cup(self):
        return "Ceramic cup from local potter"
class MilkProvider:
    def provide_milk(self):
        return "Organic cow's milk from nearby dairy farm"
class CoffeeBeanProvider:
    def provide_coffee_beans(self):
        return "Arabica beans from South America"

class CoffeeShop:
    def __init__(self, cup_provider: CupProvider, milk_provider: MilkProvider, coffee_bean_provider: CoffeeBeanProvider):
        self.cup_provider = cup_provider
        self.milk_provider = milk_provider
        self.coffee_bean_provider = coffee_bean_provider
    def make_latte(self):
        cup = self.cup_provider.provide_cup()
        milk = self.milk_provider.provide_milk()
        coffee_beans = self.coffee_bean_provider.provide_coffee_beans()
        return f"Latte served in a {cup} with {milk} and made with {coffee_beans}"

container = rodi.Container()
container.register(CupProvider)
container.register(MilkProvider)
container.register(CoffeeBeanProvider)
container.register(CoffeeShop, constructor=[CupProvider, MilkProvider, CoffeeBeanProvider])
coffee_shop: CoffeeShop = container.resolve(CoffeeShop)
latte = coffee_shop.make_latte()
print(latte)
```

# Dependency Injection in FastAPI

FastAPI, a modern web framework for building APIs with Python 3.7+, is designed to be fast and easy to use. One of its standout features is the built-in support for dependency injection, which streamlines the process of managing dependencies for your endpoints. I genuinely like the way dependency injection in FastAPI. Let’s take a look at how it’s done:

```py
from fastapi import FastAPI, Depends

app = FastAPI()
def get_query(token: str):
    return {"token": token}

# Endpoint that depends on the `get_query` function
@app.get("/items/")
async def read_items(token: str = Depends(get_query)):
    return {"token": token}

```

In the code above, Depends is a special class provided by FastAPI. When you include a parameter in your path operation function with a default value set to an instance of Depends that calls another function, FastAPI will understand that it needs to call that dependency function and use the result as the argument for your path operation function.

I’ve seen Django Injector package. It provides a FastAPI-like dependency injection experience. I loved it. You can give it a try, too.
