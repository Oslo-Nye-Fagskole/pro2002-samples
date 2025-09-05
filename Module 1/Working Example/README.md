# Working Example: OOP and SOLID in Action

This is a full working example provided *as-is* for review and practice. Within the ONF course module, all concepts shown here are introduced step by step, each with their own focused examples and explanations.

## Rundown of the Working Example

- **Encapsulation**: item details like price, stock, and labels are hidden inside classes with simple methods to expose just what's needed.
- **Inheritance and polymorphism**: different item types implement shared contracts, and the shop treats them uniformly without knowing their details.
- **Single Responsibility Principle**: each class has one clear job — items define behavior, the shop manages collections, the logger handles output, and display coordinates presentation.
- **Open/Closed Principle**: we added a new type (Warranty) without changing existing code.
- **Liskov Substitution Principle**: every item that implements the right contracts can be used anywhere an item is expected.  
- **Interface Segregation Principle**: splitting price, stock, and label into separate interfaces ensures digital items don't need meaningless stock methods.
- **Dependency Inversion Principle**: high-level flows (display, `Shop.total_price`) rely on abstractions (Logger, contracts) instead of concrete classes.
