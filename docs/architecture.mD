# Architecture Decision Records (ADRs)

## ADR 1: Frontend
**Decision**: Tkinter was chosen for its simplicity and integration with Python. It provides a straightforward way to design GUIs without requiring extensive setup or third-party libraries. 


## ADR 2: Programming Language
**Decision**: Python was chosen for its simplicity,  robust libraries and frameworks that facilitate database interaction (via PyMongo) and GUI development.


## ADR 3: Database
**Decision**: MongoDB was chosen for its schema-less nature, allowing flexible data storage. The collection-based structure and ease of use with python suited well with project requirements.


## ADR 4: testing
**Decision**: Python provides unittest library, which made unit testing easier and TDD was followed.   MagicMock and patch component of the library made testing of database and GUI elements simpler 

## ADR 5: Structure
**Decision**: The system follows a modular architecture with distinct classes to handle specific responsibilities, fostering clarity and maintainability. High-level interaction includes user input through the `SimpleBudgetApp` GUI, data processing by `FinanceTracker`, representation via `Expense` and `Budget`, and persistent storage in MongoDB. Testing classes validate these components independently. 

## ADR 5: Design Pattern and SOLID Principles
**Decision**: 
1. Model-View-Controller (MVC): 

   - Model: `Expense`, `Budget`, and MongoDB interactions in `FinanceTracker`. 

   - View: The Tkinter GUI in `SimpleBudgetApp`. 

   - Controller: `FinanceTracker`, which coordinates between the Model and View. 

   - Benefits: Clear separation of concerns, easier maintainability, and independent updates to GUI or backend logic. 

2. Dependency Injection: 

   - Used in testing to mock dependencies, ensuring reliable and isolated tests. 

3. Repository Pattern: 

   - `FinanceTracker` acts as a repository, centralizing data access logic to MongoDB for abstraction and maintainability. 

4. Observer-Like Behavior: 

   - GUI dynamically updates user views, mimicking the Observer pattern to enhance user experience. 

5. Single Responsibility Principle (SRP): 

   - Each class is focused on a specific responsibility, improving modularity and maintainability. 

6. Exception Handling: 

   - Robust exception handling ensures stability by gracefully managing errors and providing clear feedback to users.  
                


            

