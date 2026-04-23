# JavaScript Interview Questions and Answers

## Table of Contents
1. [Basic JavaScript](#basic-javascript)
2. [Functions](#functions)
3. [Objects and Arrays](#objects-and-arrays)
4. [Asynchronous JavaScript](#asynchronous-javascript)
5. [ES6+ Features](#es6-features)
6. [DOM Manipulation](#dom-manipulation)
7. [Error Handling](#error-handling)
8. [Advanced Concepts](#advanced-concepts)

---

## Basic JavaScript

### 1. What are the different data types in JavaScript?

**Answer:**
JavaScript has two categories of data types:

**Primitive Types:**
- `number` - Represents both integers and floating-point numbers
- `string` - Represents text data
- `boolean` - Represents true/false values
- `undefined` - Represents a variable that has been declared but not assigned
- `null` - Represents an intentional absence of value
- `symbol` - Represents a unique identifier (ES6)
- `bigint` - Represents large integers (ES2020)

**Non-Primitive (Reference) Types:**
- `object` - Includes objects, arrays, functions, dates, etc.

```javascript
// Examples
let num = 42;              // number
let str = "Hello";         // string
let bool = true;           // boolean
let undef;                 // undefined
let empty = null;          // null
let sym = Symbol('id');    // symbol
let bigNum = 123n;         // bigint
let obj = {name: "John"};  // object
```

### 2. What is the difference between `==` and `===`?

**Answer:**
- `==` (loose equality): Performs type coercion before comparison
- `===` (strict equality): Compares both value and type without coercion

```javascript
// Loose equality (==)
5 == "5"        // true (string "5" is converted to number 5)
true == 1       // true (true is converted to 1)
null == undefined // true

// Strict equality (===)
5 === "5"       // false (different types)
true === 1      // false (different types)
null === undefined // false
```

### 3. What is hoisting in JavaScript?

**Answer:**
Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their scope during compilation. However, only declarations are hoisted, not initializations.

```javascript
// Variable hoisting with var
console.log(x); // undefined (not an error)
var x = 5;

// Equivalent to:
var x;
console.log(x); // undefined
x = 5;

// Function hoisting
sayHello(); // "Hello!" - works because function declarations are fully hoisted

function sayHello() {
    console.log("Hello!");
}

// let and const are hoisted but not initialized (Temporal Dead Zone)
console.log(y); // ReferenceError
let y = 10;
```

### 4. What is the difference between `var`, `let`, and `const`?

**Answer:**

| Feature | var | let | const |
|---------|-----|-----|--------|
| Scope | Function/Global | Block | Block |
| Hoisting | Yes (initialized with undefined) | Yes (but TDZ) | Yes (but TDZ) |
| Re-declaration | Allowed | Not allowed | Not allowed |
| Re-assignment | Allowed | Allowed | Not allowed |

```javascript
// var - function scoped
function example() {
    if (true) {
        var x = 1;
    }
    console.log(x); // 1 (accessible outside block)
}

// let - block scoped
function example2() {
    if (true) {
        let y = 1;
    }
    console.log(y); // ReferenceError: y is not defined
}

// const - block scoped, cannot be reassigned
const z = 1;
z = 2; // TypeError: Assignment to constant variable
```

---

## Functions

### 5. What are the different ways to create functions in JavaScript?

**Answer:**

```javascript
// 1. Function Declaration
function add(a, b) {
    return a + b;
}

// 2. Function Expression
const subtract = function(a, b) {
    return a - b;
};

// 3. Arrow Function (ES6)
const multiply = (a, b) => a * b;

// 4. Function Constructor (rarely used)
const divide = new Function('a', 'b', 'return a / b');

// 5. IIFE (Immediately Invoked Function Expression)
(function() {
    console.log("IIFE executed");
})();
```

### 6. What is a closure? Provide an example.

**Answer:**
A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function has finished executing.

```javascript
function outerFunction(x) {
    // This is the outer function's scope
    
    function innerFunction(y) {
        // This inner function has access to x
        console.log(x + y);
    }
    
    return innerFunction;
}

const closure = outerFunction(10);
closure(5); // 15

// Practical example - Counter
function createCounter() {
    let count = 0;
    
    return {
        increment: () => ++count,
        decrement: () => --count,
        getCount: () => count
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2
```

### 7. What is the difference between `call()`, `apply()`, and `bind()`?

**Answer:**
All three methods are used to set the `this` context for functions.

```javascript
const person = {
    name: "John",
    greet: function(greeting, punctuation) {
        return `${greeting}, I'm ${this.name}${punctuation}`;
    }
};

const anotherPerson = { name: "Jane" };

// call() - takes arguments individually
console.log(person.greet.call(anotherPerson, "Hello", "!")); 
// "Hello, I'm Jane!"

// apply() - takes arguments as an array
console.log(person.greet.apply(anotherPerson, ["Hi", "."])); 
// "Hi, I'm Jane."

// bind() - returns a new function with bound context
const boundGreet = person.greet.bind(anotherPerson);
console.log(boundGreet("Hey", "!!!")); 
// "Hey, I'm Jane!!!"
```

---

## Objects and Arrays

### 8. How do you deep clone an object in JavaScript?

**Answer:**

```javascript
// Method 1: JSON.parse(JSON.stringify()) - Limited (no functions, dates, etc.)
const obj1 = { a: 1, b: { c: 2 } };
const cloned1 = JSON.parse(JSON.stringify(obj1));

// Method 2: Recursive function
function deepClone(obj) {
    if (obj === null || typeof obj !== "object") return obj;
    if (obj instanceof Date) return new Date(obj.getTime());
    if (obj instanceof Array) return obj.map(item => deepClone(item));
    if (typeof obj === "object") {
        const clonedObj = {};
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                clonedObj[key] = deepClone(obj[key]);
            }
        }
        return clonedObj;
    }
}

// Method 3: Using Lodash library
// const cloned = _.cloneDeep(obj);

// Method 4: Using structuredClone (modern browsers)
const cloned4 = structuredClone(obj1);
```

### 9. What are different ways to iterate over an array?

**Answer:**

```javascript
const arr = [1, 2, 3, 4, 5];

// 1. for loop
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

// 2. for...of loop
for (let item of arr) {
    console.log(item);
}

// 3. forEach()
arr.forEach((item, index) => {
    console.log(item, index);
});

// 4. map() - returns new array
const doubled = arr.map(item => item * 2);

// 5. filter() - returns filtered array
const evens = arr.filter(item => item % 2 === 0);

// 6. reduce() - reduces to single value
const sum = arr.reduce((acc, item) => acc + item, 0);

// 7. for...in loop (not recommended for arrays)
for (let index in arr) {
    console.log(arr[index]);
}
```

---

## Asynchronous JavaScript

### 10. What is the difference between synchronous and asynchronous code?

**Answer:**
- **Synchronous**: Code executes line by line, blocking further execution until current operation completes
- **Asynchronous**: Code can execute without blocking, allowing other operations to continue

```javascript
// Synchronous
console.log("1");
console.log("2");
console.log("3");
// Output: 1, 2, 3 (in order)

// Asynchronous
console.log("1");
setTimeout(() => console.log("2"), 0);
console.log("3");
// Output: 1, 3, 2 (setTimeout is async)
```

### 11. Explain Promises and provide examples.

**Answer:**
A Promise is an object representing the eventual completion or failure of an asynchronous operation.

```javascript
// Creating a Promise
const myPromise = new Promise((resolve, reject) => {
    const success = true;
    
    setTimeout(() => {
        if (success) {
            resolve("Operation successful!");
        } else {
            reject("Operation failed!");
        }
    }, 1000);
});

// Using Promise
myPromise
    .then(result => console.log(result))
    .catch(error => console.error(error))
    .finally(() => console.log("Operation completed"));

// Promise.all() - waits for all promises
const promise1 = Promise.resolve(3);
const promise2 = new Promise(resolve => setTimeout(() => resolve('foo'), 1000));
const promise3 = Promise.resolve(42);

Promise.all([promise1, promise2, promise3])
    .then(values => console.log(values)); // [3, "foo", 42]

// Promise.race() - returns first resolved/rejected promise
Promise.race([promise1, promise2, promise3])
    .then(value => console.log(value)); // 3
```

### 12. What is async/await? How does it work?

**Answer:**
async/await is syntactic sugar over Promises, making asynchronous code look more like synchronous code.

```javascript
// Using Promises
function fetchUserData() {
    return fetch('/api/user')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            return data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Using async/await
async function fetchUserDataAsync() {
    try {
        const response = await fetch('/api/user');
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Error handling with async/await
async function example() {
    try {
        const result1 = await asyncOperation1();
        const result2 = await asyncOperation2(result1);
        return result2;
    } catch (error) {
        console.error('Error in async operation:', error);
    }
}
```

---

## ES6+ Features

### 13. What are template literals and how do they work?

**Answer:**
Template literals are string literals that allow embedded expressions and multi-line strings using backticks.

```javascript
const name = "John";
const age = 30;

// Traditional string concatenation
const message1 = "Hello, my name is " + name + " and I'm " + age + " years old.";

// Template literals
const message2 = `Hello, my name is ${name} and I'm ${age} years old.`;

// Multi-line strings
const multiLine = `
    This is a
    multi-line
    string
`;

// Tagged template literals
function highlight(strings, ...values) {
    return strings.reduce((result, string, i) => {
        return result + string + (values[i] ? `<mark>${values[i]}</mark>` : '');
    }, '');
}

const highlighted = highlight`Hello ${name}, you are ${age} years old!`;
```

### 14. Explain destructuring assignment with examples.

**Answer:**
Destructuring allows unpacking values from arrays or properties from objects into distinct variables.

```javascript
// Array destructuring
const arr = [1, 2, 3, 4, 5];
const [first, second, ...rest] = arr;
console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]

// Object destructuring
const person = {
    name: "John",
    age: 30,
    city: "New York",
    country: "USA"
};

const { name, age, ...address } = person;
console.log(name);    // "John"
console.log(age);     // 30
console.log(address); // { city: "New York", country: "USA" }

// Renaming variables
const { name: fullName, age: years } = person;
console.log(fullName); // "John"
console.log(years);    // 30

// Default values
const { name: personName, job = "Unemployed" } = person;
console.log(job); // "Unemployed"

// Nested destructuring
const user = {
    id: 1,
    profile: {
        name: "Jane",
        settings: {
            theme: "dark"
        }
    }
};

const { profile: { name: userName, settings: { theme } } } = user;
console.log(userName); // "Jane"
console.log(theme);    // "dark"
```

### 15. What are arrow functions and how do they differ from regular functions?

**Answer:**

```javascript
// Regular function
function regular(a, b) {
    return a + b;
}

// Arrow function
const arrow = (a, b) => a + b;

// Key differences:

// 1. 'this' binding
const obj = {
    name: "John",
    regularMethod: function() {
        console.log(this.name); // "John"
        
        setTimeout(function() {
            console.log(this.name); // undefined (or global object)
        }, 1000);
    },
    
    arrowMethod: function() {
        console.log(this.name); // "John"
        
        setTimeout(() => {
            console.log(this.name); // "John" (inherits from parent scope)
        }, 1000);
    }
};

// 2. No arguments object
function regularFunc() {
    console.log(arguments); // Arguments object available
}

const arrowFunc = () => {
    console.log(arguments); // ReferenceError: arguments is not defined
    // Use rest parameters instead: (...args) => console.log(args)
};

// 3. Cannot be used as constructors
function RegularConstructor() {
    this.name = "Regular";
}
const instance1 = new RegularConstructor(); // Works

const ArrowConstructor = () => {
    this.name = "Arrow";
};
// const instance2 = new ArrowConstructor(); // TypeError

// 4. No hoisting for arrow functions (they're expressions)
sayHello(); // Works - function declaration is hoisted

function sayHello() {
    console.log("Hello!");
}

// sayGoodbye(); // ReferenceError - cannot access before initialization
const sayGoodbye = () => console.log("Goodbye!");
```

---

## DOM Manipulation

### 16. How do you select and manipulate DOM elements?

**Answer:**

```javascript
// Selecting elements
const elementById = document.getElementById('myId');
const elementsByClass = document.getElementsByClassName('myClass');
const elementsByTag = document.getElementsByTagName('div');
const querySelector = document.querySelector('.myClass');
const querySelectorAll = document.querySelectorAll('.myClass');

// Creating elements
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello World';
newDiv.className = 'new-element';
newDiv.setAttribute('data-id', '123');

// Manipulating content
element.textContent = 'New text content';
element.innerHTML = '<strong>Bold text</strong>';
element.setAttribute('class', 'new-class');
element.style.color = 'red';
element.style.fontSize = '16px';

// Adding/removing classes
element.classList.add('new-class');
element.classList.remove('old-class');
element.classList.toggle('active');
element.classList.contains('active'); // returns boolean

// Inserting elements
parentElement.appendChild(newDiv);
parentElement.insertBefore(newDiv, referenceElement);
element.insertAdjacentHTML('beforeend', '<p>New paragraph</p>');

// Removing elements
element.remove();
parentElement.removeChild(element);

// Event handling
element.addEventListener('click', function(event) {
    console.log('Element clicked!');
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Stop event bubbling
});

// Event delegation
document.addEventListener('click', function(event) {
    if (event.target.matches('.dynamic-button')) {
        console.log('Dynamic button clicked!');
    }
});
```

---

## Error Handling

### 17. How do you handle errors in JavaScript?

**Answer:**

```javascript
// try...catch...finally
try {
    // Code that might throw an error
    let result = riskyOperation();
    console.log(result);
} catch (error) {
    // Handle the error
    console.error('An error occurred:', error.message);
} finally {
    // This block always executes
    console.log('Cleanup operations');
}

// Throwing custom errors
function divide(a, b) {
    if (b === 0) {
        throw new Error('Division by zero is not allowed');
    }
    return a / b;
}

try {
    divide(10, 0);
} catch (error) {
    console.error(error.message); // "Division by zero is not allowed"
}

// Different error types
try {
    JSON.parse('invalid json');
} catch (error) {
    if (error instanceof SyntaxError) {
        console.log('JSON syntax error');
    } else if (error instanceof ReferenceError) {
        console.log('Reference error');
    } else {
        console.log('Unknown error');
    }
}

// Async error handling
async function asyncErrorHandling() {
    try {
        const response = await fetch('/api/data');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch error:', error);
        throw error; // Re-throw if needed
    }
}

// Promise error handling
fetchData()
    .then(data => processData(data))
    .catch(error => {
        console.error('Promise chain error:', error);
    });

// Global error handling
window.addEventListener('error', function(event) {
    console.error('Global error:', event.error);
});

window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
    event.preventDefault(); // Prevent default browser behavior
});
```

---

## Advanced Concepts

### 18. What is the Event Loop in JavaScript?

**Answer:**
The Event Loop is the mechanism that handles asynchronous operations in JavaScript's single-threaded environment.

```javascript
// Call Stack, Web APIs, and Event Loop demonstration
console.log('1'); // Goes to call stack, executes immediately

setTimeout(() => {
    console.log('2'); // Goes to Web APIs, then to callback queue
}, 0);

Promise.resolve().then(() => {
    console.log('3'); // Goes to microtask queue (higher priority)
});

console.log('4'); // Goes to call stack, executes immediately

// Output: 1, 4, 3, 2

// The Event Loop process:
// 1. Call Stack executes synchronous code
// 2. Microtasks (Promises) have higher priority than macrotasks (setTimeout)
// 3. Event Loop checks if call stack is empty before moving tasks from queues
```

### 19. What are Generators and how do they work?

**Answer:**
Generators are functions that can be paused and resumed, yielding multiple values over time.

```javascript
// Generator function
function* numberGenerator() {
    console.log('Generator started');
    yield 1;
    console.log('After first yield');
    yield 2;
    console.log('After second yield');
    yield 3;
    console.log('Generator finished');
}

// Using generator
const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }

// Infinite generator
function* infiniteSequence() {
    let i = 0;
    while (true) {
        yield i++;
    }
}

const infinite = infiniteSequence();
console.log(infinite.next().value); // 0
console.log(infinite.next().value); // 1
console.log(infinite.next().value); // 2

// Generator with input
function* echoGenerator() {
    const input1 = yield 'First yield';
    console.log('Received:', input1);
    const input2 = yield 'Second yield';
    console.log('Received:', input2);
    return 'Done';
}

const echo = echoGenerator();
console.log(echo.next());           // { value: 'First yield', done: false }
console.log(echo.next('Hello'));    // { value: 'Second yield', done: false }
console.log(echo.next('World'));    // { value: 'Done', done: true }
```

### 20. What is the difference between `null` and `undefined`?

**Answer:**

```javascript
// undefined - variable declared but not assigned
let a;
console.log(a); // undefined
console.log(typeof a); // "undefined"

// null - intentional absence of value
let b = null;
console.log(b); // null
console.log(typeof b); // "object" (this is a known JavaScript quirk)

// Comparison
console.log(null == undefined);  // true (loose equality)
console.log(null === undefined); // false (strict equality)

// Common scenarios
function example(param) {
    console.log(param); // undefined if not passed
}

const obj = {
    prop1: "value",
    prop2: null,
    // prop3 is undefined (not defined)
};

console.log(obj.prop1); // "value"
console.log(obj.prop2); // null
console.log(obj.prop3); // undefined

// Checking for null/undefined
if (value == null) {
    // This catches both null and undefined
}

if (value === null) {
    // This only catches null
}

if (value === undefined) {
    // This only catches undefined
}

if (typeof value === 'undefined') {
    // Safe way to check for undefined
}
```

### 21. Explain Promises and async/await with simple examples. What are the advantages of async/await over Promises?

**Answer:**

**Promises:**
A Promise is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. It has three states: pending, fulfilled, or rejected.

```javascript
// Simple Promise example
function fetchUserData(userId) {
    return new Promise((resolve, reject) => {
        // Simulate API call with setTimeout
        setTimeout(() => {
            if (userId > 0) {
                resolve({ 
                    id: userId, 
                    name: `User ${userId}`, 
                    email: `user${userId}@example.com` 
                });
            } else {
                reject(new Error('Invalid user ID'));
            }
        }, 1000);
    });
}

// Using the Promise
fetchUserData(1)
    .then(user => {
        console.log('User data:', user);
        // You can chain more .then() calls here
        return user.email;
    })
    .then(email => {
        console.log('User email:', email);
    })
    .catch(error => {
        console.error('Error:', error.message);
    })
    .finally(() => {
        console.log('Operation completed');
    });
```

**Async/Await:**
async/await is syntactic sugar built on top of Promises that makes asynchronous code look and behave more like synchronous code.

```javascript
// Same example using async/await
async function getUserData(userId) {
    try {
        const user = await fetchUserData(userId);
        console.log('User data:', user);
        
        const email = user.email;
        console.log('User email:', email);
        
        return user;
    } catch (error) {
        console.error('Error:', error.message);
    } finally {
        console.log('Operation completed');
    }
}

// Call the async function
getUserData(1);

// Multiple async operations
async function fetchMultipleUsers() {
    try {
        // Sequential execution (one after another)
        const user1 = await fetchUserData(1);
        const user2 = await fetchUserData(2);
        console.log('Sequential:', [user1, user2]);
        
        // Parallel execution (both at the same time)
        const [user3, user4] = await Promise.all([
            fetchUserData(3),
            fetchUserData(4)
        ]);
        console.log('Parallel:', [user3, user4]);
    } catch (error) {
        console.error('Error in fetching multiple users:', error.message);
    }
}
```

**Real-world API example:**
```javascript
// Using fetch API with Promises
function getWeather(city) {
    return fetch(`https://api.weather.com/v1/weather?q=${city}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Weather data:', data);
            return data;
        })
        .catch(error => {
            console.error('Weather fetch error:', error);
        });
}

// Same API call using async/await
async function getWeatherAsync(city) {
    try {
        const response = await fetch(`https://api.weather.com/v1/weather?q=${city}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Weather data:', data);
        return data;
    } catch (error) {
        console.error('Weather fetch error:', error);
    }
}
```

**Advantages of async/await over Promises:**

1. **Readability**: Code looks more like synchronous code, easier to read and understand
2. **Error Handling**: Single try/catch block instead of multiple .catch() chains
3. **Debugging**: Easier to set breakpoints and debug step-by-step
4. **No Callback Hell**: Avoids deeply nested .then() chains
5. **Conditional Logic**: Easier to write conditional asynchronous logic

```javascript
// Complex logic with Promises (harder to read)
function complexOperationWithPromises() {
    return fetchUserData(1)
        .then(user => {
            if (user.email.includes('admin')) {
                return fetchAdminSettings(user.id)
                    .then(settings => {
                        return { user, settings, isAdmin: true };
                    });
            } else {
                return fetchUserSettings(user.id)
                    .then(settings => {
                        return { user, settings, isAdmin: false };
                    });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Same logic with async/await (much cleaner)
async function complexOperationWithAsyncAwait() {
    try {
        const user = await fetchUserData(1);
        
        let settings;
        let isAdmin = false;
        
        if (user.email.includes('admin')) {
            settings = await fetchAdminSettings(user.id);
            isAdmin = true;
        } else {
            settings = await fetchUserSettings(user.id);
        }
        
        return { user, settings, isAdmin };
    } catch (error) {
        console.error('Error:', error);
    }
}
```

**Important Notes:**
- `async` functions always return a Promise
- `await` can only be used inside `async` functions
- `await` pauses the function execution until the Promise resolves
- Use `Promise.all()` for parallel execution of multiple async operations
- Always use try/catch for error handling in async functions

### 22. Explain the different Promise APIs (Promise.all, Promise.race, Promise.allSettled, Promise.any) with examples.

**Answer:**

JavaScript provides several static methods on the Promise constructor to handle multiple asynchronous operations. Each has different behavior and use cases.

**1. Promise.all()**
Waits for ALL promises to resolve. If ANY promise rejects, the entire operation fails immediately.

```javascript
// Example functions that return promises
function fetchUser(id) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(`User ${id}`), id * 100);
    });
}

function fetchPosts(userId) {
    return new Promise((resolve) => {
        setTimeout(() => resolve([`Post 1 by ${userId}`, `Post 2 by ${userId}`]), 200);
    });
}

function fetchComments(postId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (postId === 'invalid') {
                reject(new Error('Invalid post ID'));
            } else {
                resolve([`Comment 1 on ${postId}`, `Comment 2 on ${postId}`]);
            }
        }, 150);
    });
}

// Promise.all - All must succeed
async function loadDashboardData() {
    try {
        const [user, posts, comments] = await Promise.all([
            fetchUser(1),
            fetchPosts('user1'),
            fetchComments('post1')
        ]);
        
        console.log('All data loaded:', { user, posts, comments });
        return { user, posts, comments };
    } catch (error) {
        console.error('Failed to load dashboard:', error.message);
        // If ANY promise fails, this catch block runs
    }
}

loadDashboardData();
```

**2. Promise.race()**
Returns the result of the FIRST promise that settles (resolves or rejects).

```javascript
// Promise.race - First to finish wins
function timeoutAfter(ms) {
    return new Promise((_, reject) => {
        setTimeout(() => reject(new Error('Timeout')), ms);
    });
}

function fetchWithTimeout(url, timeout = 5000) {
    return Promise.race([
        fetch(url),
        timeoutAfter(timeout)
    ]);
}

// Example: Racing multiple API endpoints
async function getFastestResponse() {
    try {
        const result = await Promise.race([
            fetchUser(1),    // Resolves in 100ms
            fetchUser(2),    // Resolves in 200ms
            fetchUser(3)     // Resolves in 300ms
        ]);
        
        console.log('Fastest result:', result); // "User 1" (first to resolve)
    } catch (error) {
        console.error('Fastest operation failed:', error);
    }
}

getFastestResponse();
```

**3. Promise.allSettled()**
Waits for ALL promises to settle (resolve or reject) and returns results for all of them.

```javascript
// Promise.allSettled - Wait for all, get all results
async function loadAllDataWithErrors() {
    const promises = [
        fetchUser(1),                    // Will succeed
        fetchPosts('user1'),             // Will succeed
        fetchComments('invalid'),        // Will fail
        fetchUser(2)                     // Will succeed
    ];
    
    const results = await Promise.allSettled(promises);
    
    results.forEach((result, index) => {
        if (result.status === 'fulfilled') {
            console.log(`Promise ${index} succeeded:`, result.value);
        } else {
            console.log(`Promise ${index} failed:`, result.reason.message);
        }
    });
    
    // Separate successful and failed results
    const successful = results
        .filter(result => result.status === 'fulfilled')
        .map(result => result.value);
        
    const failed = results
        .filter(result => result.status === 'rejected')
        .map(result => result.reason);
    
    return { successful, failed };
}

loadAllDataWithErrors();
```

**4. Promise.any()**
Returns the result of the FIRST promise that resolves successfully. If ALL promises reject, it returns an AggregateError.

```javascript
// Promise.any - First successful result
function unreliableService(id, failureRate = 0.5) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() < failureRate) {
                reject(new Error(`Service ${id} failed`));
            } else {
                resolve(`Data from service ${id}`);
            }
        }, Math.random() * 1000);
    });
}

async function getDataFromAnyService() {
    try {
        // Try multiple unreliable services
        const result = await Promise.any([
            unreliableService(1, 0.8), // 80% failure rate
            unreliableService(2, 0.6), // 60% failure rate
            unreliableService(3, 0.4)  // 40% failure rate
        ]);
        
        console.log('Got data from:', result);
        return result;
    } catch (error) {
        // This only happens if ALL promises reject
        console.error('All services failed:', error);
        if (error instanceof AggregateError) {
            error.errors.forEach((err, index) => {
                console.log(`Service ${index + 1} error:`, err.message);
            });
        }
    }
}

getDataFromAnyService();
```

**Real-world Use Cases:**

```javascript
// 1. Loading multiple resources for a page
async function loadPageData() {
    try {
        // All required for page to function
        const [userData, settingsData] = await Promise.all([
            fetchUser(currentUserId),
            fetchUserSettings(currentUserId)
        ]);
        
        // Optional data - don't let failures block the page
        const optionalData = await Promise.allSettled([
            fetchRecommendations(currentUserId),
            fetchNotifications(currentUserId),
            fetchAnalytics(currentUserId)
        ]);
        
        return { userData, settingsData, optionalData };
    } catch (error) {
        console.error('Failed to load essential page data:', error);
    }
}

// 2. Implementing retry logic with timeout
async function fetchWithRetryAndTimeout(url, maxRetries = 3, timeout = 5000) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            const result = await Promise.race([
                fetch(url),
                new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Timeout')), timeout)
                )
            ]);
            return result;
        } catch (error) {
            console.log(`Attempt ${attempt} failed:`, error.message);
            if (attempt === maxRetries) {
                throw new Error(`Failed after ${maxRetries} attempts: ${error.message}`);
            }
            // Wait before retry
            await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
        }
    }
}

// 3. Load balancing across multiple APIs
async function loadBalancedRequest(data) {
    const apiEndpoints = [
        () => callAPI1(data),
        () => callAPI2(data),
        () => callAPI3(data)
    ];
    
    try {
        // Try to get response from any available API
        const result = await Promise.any(
            apiEndpoints.map(apiCall => apiCall())
        );
        return result;
    } catch (error) {
        throw new Error('All API endpoints are unavailable');
    }
}
```

**Summary:**

| Method | Behavior | Use Case |
|--------|----------|----------|
| `Promise.all()` | Fails fast, all must succeed | Critical operations where all data is required |
| `Promise.race()` | First to settle (resolve/reject) wins | Timeouts, performance racing |
| `Promise.allSettled()` | Wait for all, get all results | When you want partial success handling |
| `Promise.any()` | First successful result | Fallback services, load balancing |

**Key Points:**
- `Promise.all()` and `Promise.race()` are most commonly used
- `Promise.allSettled()` is great for "best effort" scenarios
- `Promise.any()` is useful for redundant services
- Always handle errors appropriately based on your use case
- Consider using these methods with `async/await` for cleaner code

---

## Quick Tips for Interviews

1. **Practice coding problems** - Be ready to write code on a whiteboard or computer
2. **Understand the fundamentals** - Don't just memorize, understand the concepts
3. **Be able to explain your code** - Walk through your thought process
4. **Know the latest features** - Stay updated with ES6+ features
5. **Practice debugging** - Be able to identify and fix common errors
6. **Understand browser APIs** - Know DOM manipulation, localStorage, fetch API
7. **Be familiar with frameworks** - React, Vue, Angular concepts
8. **Know testing basics** - Unit testing, integration testing concepts

---

## Common Coding Challenges

### FizzBuzz
```javascript
function fizzBuzz(n) {
    for (let i = 1; i <= n; i++) {
        if (i % 15 === 0) console.log("FizzBuzz");
        else if (i % 3 === 0) console.log("Fizz");
        else if (i % 5 === 0) console.log("Buzz");
        else console.log(i);
    }
}
```

### Palindrome Check
```javascript
function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
}
```

### Array Flattening
```javascript
function flattenArray(arr) {
    return arr.reduce((flat, item) => {
        return flat.concat(Array.isArray(item) ? flattenArray(item) : item);
    }, []);
}

// Using built-in method
const flattened = arr.flat(Infinity);
```

### Debounce Function
```javascript
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}
```

Good luck with your interview! 🚀 