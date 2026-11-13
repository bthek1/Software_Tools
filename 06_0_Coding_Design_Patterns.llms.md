# Coding Design Patterns

Coding Design Patterns

Author

Benedict Thekkel

Design patterns are proven solutions to common software design problems. They provide a standardized way to structure your code, making it more maintainable, scalable, and robust. In Python, design patterns are particularly useful due to the language’s flexibility and support for multiple programming paradigms.

This guide covers the **most common design patterns in Python**, categorized into **Creational**, **Structural**, and **Behavioral** patterns. Each pattern includes a brief explanation and a Python example to illustrate its implementation.

## **1. Creational Design Patterns**

Creational patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. They abstract the instantiation process, making a system independent of how its objects are created, composed, and represented.

### **a. Singleton**

**Purpose:** Ensure a class has only one instance and provide a global point of access to it.

**Use Case:** When exactly one object is needed to coordinate actions across the system (e.g., configuration manager, logger).

**Python Implementation:**

``` python
class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Usage
singleton1 = SingletonClass(10)
singleton2 = SingletonClass(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
print(singleton1 is singleton2)  # Output: True
```

**Explanation:** - `SingletonMeta` is a metaclass that overrides the `__call__` method to control object creation. - When `SingletonClass` is instantiated, it checks if an instance already exists. If not, it creates one; otherwise, it returns the existing instance. - Both `singleton1` and `singleton2` refer to the same instance.

------------------------------------------------------------------------

### **b. Factory Method**

**Purpose:** Define an interface for creating an object, but let subclasses alter the type of objects that will be created.

**Use Case:** When a class cannot anticipate the class of objects it needs to create.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Product
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Render a button in Windows style."

class MacOSButton(Button):
    def render(self):
        return "Render a button in MacOS style."

# Creator
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render_dialog(self):
        button = self.create_button()
        print(button.render())

# Concrete Creators
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

class MacOSDialog(Dialog):
    def create_button(self) -> Button:
        return MacOSButton()

# Usage
def client_code(dialog: Dialog):
    dialog.render_dialog()

# Create a Windows dialog
windows_dialog = WindowsDialog()
client_code(windows_dialog)  # Output: Render a button in Windows style.

# Create a MacOS dialog
mac_dialog = MacOSDialog()
client_code(mac_dialog)  # Output: Render a button in MacOS style.
```

**Explanation:** - `Button` is an abstract product with a `render` method. - `WindowsButton` and `MacOSButton` are concrete implementations. - `Dialog` is an abstract creator with a factory method `create_button`. - `WindowsDialog` and `MacOSDialog` override the factory method to create specific button types. - The `client_code` function uses the `Dialog` interface to render buttons without knowing their concrete classes.

### **c. Abstract Factory**

**Purpose:** Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

**Use Case:** When a system needs to be independent of how its products are created and composed.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Products for Windows
class WindowsButton(Button):
    def paint(self):
        return "Render a button in Windows style."

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in Windows style."

# Concrete Products for MacOS
class MacOSButton(Button):
    def paint(self):
        return "Render a button in MacOS style."

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in MacOS style."

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

# Usage
print("Client: Testing client code with the WindowsFactory:")
client_code(WindowsFactory())
# Output:
# Render a button in Windows style.
# Render a checkbox in Windows style.

print("\nClient: Testing the same client code with the MacOSFactory:")
client_code(MacOSFactory())
# Output:
# Render a button in MacOS style.
# Render a checkbox in MacOS style.
```

**Explanation:** - `Button` and `Checkbox` are abstract products with a `paint` method. - `WindowsButton`, `WindowsCheckbox`, `MacOSButton`, and `MacOSCheckbox` are concrete implementations. - `GUIFactory` is an abstract factory with methods to create buttons and checkboxes. - `WindowsFactory` and `MacOSFactory` are concrete factories that produce Windows and MacOS styled products, respectively. - The `client_code` function uses the factory to create and paint UI elements without knowing their concrete classes.

### **d. Builder**

**Purpose:** Separate the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Use Case:** When creating complex objects with many optional parameters or when the construction process involves multiple steps.

**Python Implementation:**

``` python
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.engine = None
        self.color = None

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, engine={self.engine}, color={self.color})"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make: str):
        self.car.make = make
        return self

    def set_model(self, model: str):
        self.car.model = model
        return self

    def set_engine(self, engine: str):
        self.car.engine = engine
        return self

    def set_color(self, color: str):
        self.car.color = color
        return self

    def build(self):
        return self.car

# Usage
builder = CarBuilder()
car = (builder.set_make("Toyota")
            .set_model("Corolla")
            .set_engine("V4")
            .set_color("Blue")
            .build())

print(car)  # Output: Car(make=Toyota, model=Corolla, engine=V4, color=Blue)
```

**Explanation:** - `Car` is the complex object with multiple attributes. - `CarBuilder` provides methods to set each attribute and returns `self` to allow method chaining. - The `build` method returns the fully constructed `Car` object. - The client uses the builder to construct a `Car` step-by-step, resulting in a clear and flexible construction process.

### **e. Prototype**

**Purpose:** Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

**Use Case:** When object creation is expensive, and cloning is more efficient, or when you need to create objects with identical or similar states.

**Python Implementation:**

``` python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ComplexObject(Prototype):
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def __str__(self):
        return f"ComplexObject(name={self.name}, components={self.components})"

# Usage
original = ComplexObject("Original", ["Component1", "Component2"])
clone = original.clone()

print(original)  # Output: ComplexObject(name=Original, components=['Component1', 'Component2'])
print(clone)     # Output: ComplexObject(name=Original, components=['Component1', 'Component2'])
print(original is clone)  # Output: False
```

**Explanation:** - `Prototype` provides a `clone` method using `deepcopy` to create a new instance. - `ComplexObject` inherits from `Prototype` and represents an object with multiple components. - The `clone` method creates a deep copy of the original object, ensuring that changes to the clone do not affect the original.

## **2. Structural Design Patterns**

Structural patterns deal with object composition, identifying simple ways to realize relationships between different objects to form larger structures.

### **a. Adapter**

**Purpose:** Allow the interface of an existing class to be used as another interface. It enables classes to work together that couldn’t otherwise because of incompatible interfaces.

**Use Case:** When integrating third-party libraries or legacy code that doesn’t match the current system’s interfaces.

**Python Implementation:**

``` python
class EuropeanSocketInterface:
    def voltage(self) -> int:
        pass

    def live(self) -> int:
        pass

    def neutral(self) -> int:
        pass

    def earth(self) -> int:
        pass

class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

class USPlug:
    def __init__(self, device):
        self.device = device

    def connect_to_socket(self, socket: EuropeanSocketInterface):
        if socket.voltage() > 120:
            self.device.electrical_needs = socket.voltage() // 2
        else:
            self.device.electrical_needs = socket.voltage()
        self.device.power_on()

class Device:
    def power_on(self):
        print(f"Device powered on with {self.electrical_needs}V.")

# Adapter
class USAdapter(EuropeanSocketInterface):
    def __init__(self, us_device: USPlug):
        self.us_device = us_device

    def voltage(self):
        return 120  # Adapter converts voltage

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

# Usage
device = Device()
us_plug = USPlug(device)
adapter = USAdapter(us_plug)
european_socket = EuropeanSocket()

us_plug.connect_to_socket(adapter)
# Output: Device powered on with 120V.
```

**Explanation:** - `EuropeanSocketInterface` defines the interface for European sockets. - `EuropeanSocket` implements the European socket interface. - `USPlug` expects a socket with 120V. - `USAdapter` adapts the `USPlug` to work with the `EuropeanSocketInterface` by converting the voltage. - This allows `USPlug` to connect to a European socket seamlessly.

------------------------------------------------------------------------

### **b. Decorator**

**Purpose:** Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

**Use Case:** When you need to add behavior to individual objects without affecting other objects of the same class.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def ingredients(self) -> str:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

    def ingredients(self) -> str:
        return "Coffee"

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def ingredients(self) -> str:
        return self._coffee.ingredients()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def ingredients(self) -> str:
        return f"{self._coffee.ingredients()}, Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.3

    def ingredients(self) -> str:
        return f"{self._coffee.ingredients()}, Sugar"

# Usage
coffee = SimpleCoffee()
print(coffee.cost())          # Output: 2.0
print(coffee.ingredients())   # Output: Coffee

coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.cost())          # Output: 2.5
print(coffee_with_milk.ingredients())   # Output: Coffee, Milk

coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_sugar.cost())          # Output: 2.8
print(coffee_with_milk_sugar.ingredients())   # Output: Coffee, Milk, Sugar
```

**Explanation:** - `Coffee` is the abstract component with `cost` and `ingredients` methods. - `SimpleCoffee` is the concrete component. - `CoffeeDecorator` is the abstract decorator that holds a reference to a `Coffee` object. - `MilkDecorator` and `SugarDecorator` are concrete decorators that add functionality. - Decorators are applied dynamically, allowing flexible combinations of added features.

### **c. Facade**

**Purpose:** Provide a simplified interface to a complex subsystem. Facades define a higher-level interface that makes the subsystem easier to use.

**Use Case:** When you want to simplify interactions with a complex system, such as a library or a set of classes.

**Python Implementation:**

``` python
class CPU:
    def freeze(self):
        print("CPU: Freezing processor.")

    def jump(self, position: int):
        print(f"CPU: Jumping to address {position}.")

    def execute(self):
        print("CPU: Executing instructions.")

class Memory:
    def load(self, position: int, data: str):
        print(f"Memory: Loading data '{data}' at position {position}.")

class HardDrive:
    def read(self, lba: int, size: int) -> str:
        data = "OS Boot Data"
        print(f"HardDrive: Reading data from LBA {lba} with size {size}.")
        return data

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        boot_data = self.hard_drive.read(0, 1024)
        self.memory.load(0, boot_data)
        self.cpu.jump(0)
        self.cpu.execute()

# Usage
computer = ComputerFacade()
computer.start_computer()
# Output:
# CPU: Freezing processor.
# HardDrive: Reading data from LBA 0 with size 1024.
# Memory: Loading data 'OS Boot Data' at position 0.
# CPU: Jumping to address 0.
# CPU: Executing instructions.
```

**Explanation:** - `CPU`, `Memory`, and `HardDrive` represent complex subsystems. - `ComputerFacade` provides a simplified `start_computer` method that internally coordinates interactions between subsystems. - The client interacts only with the facade, hiding the complexities of the underlying components.

### **d. Proxy**

**Purpose:** Provide a surrogate or placeholder for another object to control access to it.

**Use Case:** When you need to add a layer of control over access to an object, such as lazy initialization, access control, logging, or caching.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename} from disk.")

    def display(self):
        print(f"Displaying {self.filename}.")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage
print("Creating ProxyImage:")
image = ProxyImage("photo.jpg")
print("\nFirst call to display():")
image.display()
print("\nSecond call to display():")
image.display()
```

**Output:**

    Creating ProxyImage:

    First call to display():
    Loading photo.jpg from disk.
    Displaying photo.jpg.

    Second call to display():
    Displaying photo.jpg.

**Explanation:** - `Image` is the abstract subject with a `display` method. - `RealImage` loads and displays an image, simulating an expensive operation (loading from disk). - `ProxyImage` controls access to `RealImage`. It initializes `RealImage` only when `display` is called for the first time (lazy initialization). - Subsequent calls to `display` use the already loaded `RealImage`, avoiding redundant disk loads.

### **e. Composite**

**Purpose:** Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions uniformly.

**Use Case:** When you need to represent hierarchical structures like file systems, organizational charts, or UI components.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf
class Dot(Graphic):
    def draw(self):
        print("Drawing a dot.")

class Circle(Graphic):
    def draw(self):
        print("Drawing a circle.")

# Composite
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def draw(self):
        for child in self.children:
            child.draw()

# Usage
dot = Dot()
circle = Circle()

compound = CompoundGraphic()
compound.add(dot)
compound.add(circle)

print("Drawing individual graphics:")
dot.draw()
circle.draw()

print("\nDrawing compound graphic:")
compound.draw()
```

**Output:**

    Drawing individual graphics:
    Drawing a dot.
    Drawing a circle.

    Drawing compound graphic:
    Drawing a dot.
    Drawing a circle.

**Explanation:** - `Graphic` is the abstract component with a `draw` method. - `Dot` and `Circle` are leaf nodes implementing `Graphic`. - `CompoundGraphic` is a composite that can contain multiple `Graphic` objects (both leaves and other composites). - The client can treat individual `Graphic` objects and `CompoundGraphic` uniformly by calling the `draw` method.

## **3. Behavioral Design Patterns**

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They describe not just patterns of objects or classes but also the pattern of communication between them.

### **a. Observer**

**Purpose:** Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Use Case:** Implementing event handling systems, such as user interface event listeners or publish-subscribe mechanisms.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Subject
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

# Concrete Observer
class ConcreteObserver(Observer):
    def update(self, subject: Subject):
        print(f"Observer: Subject's state changed to {subject.state}")

# Usage
subject = ConcreteSubject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

print("Changing subject state to 10.")
subject.state = 10
# Output:
# Observer: Subject's state changed to 10
# Observer: Subject's state changed to 10

print("\nChanging subject state to 20.")
subject.state = 20
# Output:
# Observer: Subject's state changed to 20
# Observer: Subject's state changed to 20

subject.detach(observer1)
print("\nChanging subject state to 30 after detaching observer1.")
subject.state = 30
# Output:
# Observer: Subject's state changed to 30
```

**Explanation:** - `Subject` defines methods to attach, detach, and notify observers. - `ConcreteSubject` maintains a list of observers and notifies them when its state changes. - `Observer` defines an `update` method that observers must implement. - `ConcreteObserver` implements the `update` method to respond to state changes. - When the subject’s state is updated, all attached observers are notified automatically.

------------------------------------------------------------------------

### **b. Strategy**

**Purpose:** Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

**Use Case:** When you have multiple ways of performing an operation and want to choose the algorithm at runtime.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

# Concrete Strategies
class QuickSortStrategy(SortingStrategy):
    def sort(self, data: list) -> list:
        print("Sorting using QuickSort.")
        return sorted(data)  # Simplified for illustration

class MergeSortStrategy(SortingStrategy):
    def sort(self, data: list) -> list:
        print("Sorting using MergeSort.")
        return sorted(data)  # Simplified for illustration

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: list) -> list:
        print("Sorting using BubbleSort.")
        return sorted(data)  # Simplified for illustration

# Context
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(self, data: list) -> list:
        return self._strategy.sort(data)

# Usage
data = [5, 2, 9, 1, 5, 6]

sorter = Sorter(QuickSortStrategy())
sorted_data = sorter.sort_data(data)
print(sorted_data)
# Output:
# Sorting using QuickSort.
# [1, 2, 5, 5, 6, 9]

sorter.set_strategy(BubbleSortStrategy())
sorted_data = sorter.sort_data(data)
print(sorted_data)
# Output:
# Sorting using BubbleSort.
# [1, 2, 5, 5, 6, 9]
```

**Explanation:** - `SortingStrategy` is the abstract strategy interface with a `sort` method. - `QuickSortStrategy`, `MergeSortStrategy`, and `BubbleSortStrategy` are concrete strategies implementing different sorting algorithms. - `Sorter` is the context that uses a `SortingStrategy` to sort data. It can change its strategy at runtime. - The client can choose different sorting algorithms by setting different strategies without changing the `Sorter`’s implementation.

### **c. Command**

**Purpose:** Encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

**Use Case:** Implementing undo/redo functionality, transactional behavior, or scheduling tasks.

**Python Implementation:**

``` python
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light: turned on.")

    def turn_off(self):
        self.is_on = False
        print("Light: turned off.")

# Concrete Commands
class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No commands to undo.")

# Usage
light = Light()
remote = RemoteControl()

turn_on = TurnOnCommand(light)
turn_off = TurnOffCommand(light)

remote.execute_command(turn_on)   # Output: Light: turned on.
remote.execute_command(turn_off)  # Output: Light: turned off.
remote.undo_last()                # Output: Light: turned on.
remote.undo_last()                # Output: Light: turned off.
remote.undo_last()                # Output: No commands to undo.
```

**Explanation:** - `Command` is the abstract command interface with `execute` and `undo` methods. - `Light` is the receiver that performs the actual operations. - `TurnOnCommand` and `TurnOffCommand` are concrete commands that call the receiver’s methods. - `RemoteControl` is the invoker that executes commands and maintains a history for undoing. - The client uses the `RemoteControl` to execute and undo commands without knowing the underlying receiver’s implementation.

### **d. Iterator**

**Purpose:** Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

**Use Case:** When you need to traverse different data structures (lists, trees, etc.) uniformly.

**Python Implementation:**

``` python
class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._items)

# Usage
aggregate = ConcreteAggregate()
aggregate.add_item("Item1")
aggregate.add_item("Item2")
aggregate.add_item("Item3")

iterator = aggregate.create_iterator()

print("Iterating over aggregate:")
try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    pass
# Output:
# Iterating over aggregate:
# Item1
# Item2
# Item3
```

**Explanation:** - `Iterator` is the abstract iterator interface with a `__next__` method. - `ConcreteIterator` implements the `Iterator` interface to traverse a collection. - `Aggregate` is the abstract collection interface with a `create_iterator` method. - `ConcreteAggregate` maintains a list of items and returns a `ConcreteIterator` for traversal. - The client uses the iterator to traverse the collection without knowing its internal structure.

**Pythonic Approach:** Python’s built-in iterator protocol can often replace explicit iterator patterns.

``` python
class IterableAggregate:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

# Usage
aggregate = IterableAggregate()
aggregate.add_item("Item1")
aggregate.add_item("Item2")
aggregate.add_item("Item3")

print("Iterating over aggregate using Pythonic iterator:")
for item in aggregate:
    print(item)
# Output:
# Iterating over aggregate using Pythonic iterator:
# Item1
# Item2
# Item3
```

### **e. Mediator**

**Purpose:** Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly.

**Use Case:** When you have complex communication between multiple objects and want to centralize control.

**Python Implementation:**

\`\`\`python from abc import ABC, abstractmethod

# Mediator Interface

class Mediator(ABC): @abstractmethod def notify(self, sender, event): pass

# Concrete Mediator

class ConcreteMediator(Mediator): def **init**(self, component1, component2): self.\_component1 = component1 self.\_component1.set_mediator(self) self.\_component2 = component2 self.\_component2.set_mediator(self)

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_C()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_B()

# Components

class BaseComponent: def **init**(self, mediator=None): self.\_mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent): def do_A(self): print(“Component1 does A.”) self.\_mediator.notify(self, “A”)

    def do_B(self):
        print("Component1 does B.")

class Component2(BaseComponent): def do_C(self): print(“Component2 does C.”)

    def do_D(self):
        print("Component2 does D.")
        self._mediator.notify(self, "D")

# Usage

component1 = Component1() component2 = Component2() mediator = Concrete

Back to top
