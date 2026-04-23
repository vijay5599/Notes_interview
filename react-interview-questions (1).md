# React Interview Questions and Answers

## Table of Contents
1. [Basic React Concepts](#basic-react-concepts)
2. [Components and JSX](#components-and-jsx)
3. [State and Props](#state-and-props)
4. [React Hooks](#react-hooks)
5. [Event Handling](#event-handling)
6. [Performance Optimization](#performance-optimization)
7. [Advanced Concepts](#advanced-concepts)
8. [Testing](#testing)

---

## Basic React Concepts

### 1. What is React?
**Answer:** React is a JavaScript library for building user interfaces, particularly web applications. It was developed by Facebook and is component-based, allowing developers to create reusable UI components. React follows a declarative programming paradigm and uses a virtual DOM for efficient rendering.

**Key Features:**
- Component-based architecture
- Virtual DOM
- Unidirectional data flow
- JSX syntax
- Strong ecosystem and community support

### 2. What is Virtual DOM?
**Answer:** Virtual DOM is a programming concept where a "virtual" representation of the real DOM is kept in memory and synced with the real DOM through a process called reconciliation. 

**Benefits:**
- **Performance**: Batch updates and minimal DOM manipulation
- **Predictability**: Easier to debug and understand
- **Cross-browser compatibility**: React handles browser differences

**How it works:**
1. State changes trigger a new virtual DOM tree
2. React compares (diffs) the new tree with the previous one
3. Only the differences are updated in the real DOM

### 3. What is JSX?
**Answer:** JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code within JavaScript. It makes React components more readable and writable.

```jsx
// JSX
const element = <h1>Hello, World!</h1>;

// Compiled JavaScript
const element = React.createElement('h1', null, 'Hello, World!');
```

**JSX Rules:**
- Must have one parent element (or use React.Fragment)
- Use camelCase for attributes (e.g., `className` instead of `class`)
- Close all tags
- Use curly braces `{}` for JavaScript expressions

### 4. What is the difference between React and ReactDOM?
**Answer:** 
- **React**: The core library that provides component functionality, state management, and lifecycle methods
- **ReactDOM**: A separate package that provides DOM-specific methods for React components

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

// React creates components
const App = () => <h1>Hello World</h1>;

// ReactDOM renders them to the DOM
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

---

## Components and JSX

### 5. What are the different types of components in React?
**Answer:** There are two main types of components:

**1. Functional Components:**
```jsx
const MyComponent = (props) => {
  return <div>Hello, {props.name}!</div>;
};
```

**2. Class Components:**
```jsx
class MyComponent extends React.Component {
  render() {
    return <div>Hello, {this.props.name}!</div>;
  }
}
```

**Key Differences:**
- Functional components are simpler and preferred (with hooks)
- Class components have built-in lifecycle methods
- Functional components use hooks for state and lifecycle

### 6. What is the difference between Controlled and Uncontrolled components?
**Answer:** 

**Controlled Components:**
- Form data is handled by React component state
- Input values are controlled by React

```jsx
const ControlledInput = () => {
  const [value, setValue] = useState('');
  
  return (
    <input 
      value={value} 
      onChange={(e) => setValue(e.target.value)} 
    />
  );
};
```

**Uncontrolled Components:**
- Form data is handled by the DOM itself
- Use refs to access form values

```jsx
const UncontrolledInput = () => {
  const inputRef = useRef();
  
  const handleSubmit = () => {
    console.log(inputRef.current.value);
  };
  
  return <input ref={inputRef} />;
};
```

### 7. What are React Fragments?
**Answer:** React Fragments let you group multiple elements without adding extra nodes to the DOM.

```jsx
// Long syntax
const MyComponent = () => {
  return (
    <React.Fragment>
      <h1>Title</h1>
      <p>Description</p>
    </React.Fragment>
  );
};

// Short syntax
const MyComponent = () => {
  return (
    <>
      <h1>Title</h1>
      <p>Description</p>
    </>
  );
};
```

---

## State and Props

### 8. What is the difference between State and Props?
**Answer:** 

| Props | State |
|-------|-------|
| Read-only data passed from parent | Mutable data owned by component |
| Cannot be changed by component | Can be changed using setState/useState |
| Used for component communication | Used for component's internal data |
| Functional components receive as parameters | Managed within the component |

```jsx
// Props example
const Child = ({ name, age }) => (
  <div>{name} is {age} years old</div>
);

const Parent = () => (
  <Child name="John" age={25} />
);

// State example
const Counter = () => {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};
```

### 9. How do you pass data between components?
**Answer:** 

**1. Parent to Child (Props):**
```jsx
const Parent = () => {
  const data = "Hello from parent";
  return <Child message={data} />;
};

const Child = ({ message }) => <div>{message}</div>;
```

**2. Child to Parent (Callback Functions):**
```jsx
const Parent = () => {
  const handleChildData = (data) => {
    console.log(data);
  };
  
  return <Child onData={handleChildData} />;
};

const Child = ({ onData }) => (
  <button onClick={() => onData("Hello from child")}>
    Send Data
  </button>
);
```

**3. Between Siblings (Lift State Up):**
```jsx
const Parent = () => {
  const [sharedData, setSharedData] = useState('');
  
  return (
    <>
      <Child1 data={sharedData} setData={setSharedData} />
      <Child2 data={sharedData} />
    </>
  );
};
```

---

## React Hooks

### 10. What are React Hooks?
**Answer:** Hooks are functions that let you use state and other React features in functional components. They were introduced in React 16.8.

**Rules of Hooks:**
1. Only call hooks at the top level (not inside loops, conditions, or nested functions)
2. Only call hooks from React functions (components or custom hooks)

### 11. Explain useState Hook
**Answer:** `useState` is a hook that allows you to add state to functional components.

```jsx
const Counter = () => {
  const [count, setCount] = useState(0); // Initial state is 0
  
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);
  const reset = () => setCount(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
};
```

**Key Points:**
- Returns an array with current state and setter function
- Setter function can accept a new value or a function
- State updates are asynchronous and may be batched

### 12. Explain useEffect Hook
**Answer:** `useEffect` is a hook that lets you perform side effects in functional components (data fetching, subscriptions, DOM manipulation).

```jsx
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  // Effect runs after every render
  useEffect(() => {
    const fetchUser = async () => {
      setLoading(true);
      try {
        const response = await fetch(`/api/users/${userId}`);
        const userData = await response.json();
        setUser(userData);
      } catch (error) {
        console.error('Error fetching user:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchUser();
  }, [userId]); // Dependency array - effect runs when userId changes
  
  // Cleanup function
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);
    
    return () => clearInterval(timer); // Cleanup
  }, []);
  
  if (loading) return <div>Loading...</div>;
  
  return <div>Welcome, {user?.name}!</div>;
};
```

**Common useEffect Patterns:**
```jsx
// Run once (componentDidMount)
useEffect(() => {
  // code
}, []);

// Run on every render (componentDidUpdate)
useEffect(() => {
  // code
});

// Run when specific value changes
useEffect(() => {
  // code
}, [dependency]);

// Cleanup (componentWillUnmount)
useEffect(() => {
  return () => {
    // cleanup code
  };
}, []);
```

### 13. What are other commonly used hooks?
**Answer:** 

**useContext:**
```jsx
const ThemeContext = React.createContext();

const App = () => (
  <ThemeContext.Provider value="dark">
    <ThemedComponent />
  </ThemeContext.Provider>
);

const ThemedComponent = () => {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Themed content</div>;
};
```

**useReducer:**
```jsx
const initialState = { count: 0 };

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
};

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return (
    <div>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
};
```

**useMemo:**
```jsx
const ExpensiveComponent = ({ items }) => {
  const expensiveValue = useMemo(() => {
    return items.reduce((sum, item) => sum + item.value, 0);
  }, [items]);
  
  return <div>Total: {expensiveValue}</div>;
};
```

**useCallback:**
```jsx
const Parent = ({ items }) => {
  const [count, setCount] = useState(0);
  
  const handleItemClick = useCallback((id) => {
    console.log(`Clicked item ${id}`);
  }, []); // Dependencies array
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      {items.map(item => (
        <Child key={item.id} item={item} onClick={handleItemClick} />
      ))}
    </div>
  );
};
```

---

## Event Handling

### 14. How do you handle events in React?
**Answer:** React uses SyntheticEvents, which are wrappers around native events that provide consistent behavior across browsers.

```jsx
const EventExample = () => {
  const handleClick = (e) => {
    e.preventDefault(); // Prevent default behavior
    e.stopPropagation(); // Stop event bubbling
    console.log('Button clicked!');
    console.log('Event type:', e.type);
    console.log('Target:', e.target);
  };
  
  const handleInputChange = (e) => {
    console.log('Input value:', e.target.value);
  };
  
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      console.log('Enter key pressed!');
    }
  };
  
  return (
    <div>
      <button onClick={handleClick}>Click me</button>
      <input onChange={handleInputChange} onKeyPress={handleKeyPress} />
    </div>
  );
};
```

### 15. What is Event Delegation in React?
**Answer:** React automatically implements event delegation by attaching event listeners to the root element and handling events through event bubbling.

```jsx
// React handles this automatically
const ListComponent = () => {
  const handleItemClick = (e) => {
    // e.target will be the clicked list item
    console.log('Clicked item:', e.target.textContent);
  };
  
  return (
    <ul onClick={handleItemClick}>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
  );
};
```

---

## Performance Optimization

### 16. How do you optimize React performance?
**Answer:** 

**1. React.memo:**
```jsx
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{data.value}</div>;
});

// With custom comparison
const MyComponent = React.memo(({ user }) => {
  return <div>{user.name}</div>;
}, (prevProps, nextProps) => {
  return prevProps.user.id === nextProps.user.id;
});
```

**2. useMemo for expensive calculations:**
```jsx
const FilteredList = ({ items, filter }) => {
  const filteredItems = useMemo(() => {
    return items.filter(item => item.name.includes(filter));
  }, [items, filter]);
  
  return (
    <ul>
      {filteredItems.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
};
```

**3. useCallback for stable references:**
```jsx
const ParentComponent = ({ items }) => {
  const [count, setCount] = useState(0);
  
  const handleItemClick = useCallback((id) => {
    // Handle click
  }, []);
  
  return (
    <div>
      <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
      {items.map(item => (
        <MemoizedChild key={item.id} item={item} onClick={handleItemClick} />
      ))}
    </div>
  );
};
```

**4. Code Splitting with React.lazy:**
```jsx
const LazyComponent = React.lazy(() => import('./LazyComponent'));

const App = () => (
  <Suspense fallback={<div>Loading...</div>}>
    <LazyComponent />
  </Suspense>
);
```

### 17. What is React.memo and when should you use it?
**Answer:** `React.memo` is a higher-order component that memoizes the result of a component. It only re-renders if props change.

```jsx
// Without React.memo - re-renders every time parent renders
const Child = ({ name }) => {
  console.log('Child rendered');
  return <div>Hello {name}</div>;
};

// With React.memo - only re-renders when name prop changes
const MemoizedChild = React.memo(({ name }) => {
  console.log('Memoized Child rendered');
  return <div>Hello {name}</div>;
});

const Parent = () => {
  const [count, setCount] = useState(0);
  const [name] = useState('John');
  
  return (
    <div>
      <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
      <Child name={name} /> {/* Re-renders on every count change */}
      <MemoizedChild name={name} /> {/* Only renders once */}
    </div>
  );
};
```

---

## Advanced Concepts

### 18. What is Context API?
**Answer:** Context API provides a way to pass data through the component tree without passing props down manually at every level.

```jsx
// Create Context
const ThemeContext = React.createContext();
const UserContext = React.createContext();

// Provider Component
const App = () => {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState({ name: 'John', role: 'admin' });
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <UserContext.Provider value={{ user, setUser }}>
        <Header />
        <MainContent />
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
};

// Consumer Component
const Header = () => {
  const { theme, setTheme } = useContext(ThemeContext);
  const { user } = useContext(UserContext);
  
  return (
    <header className={theme}>
      <h1>Welcome, {user.name}!</h1>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
};

// Custom Hook for Context
const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};
```

### 19. What are Higher-Order Components (HOC)?
**Answer:** HOCs are functions that take a component and return a new enhanced component.

```jsx
// HOC for authentication
const withAuth = (WrappedComponent) => {
  return (props) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    
    useEffect(() => {
      // Check authentication
      const token = localStorage.getItem('token');
      setIsAuthenticated(!!token);
    }, []);
    
    if (!isAuthenticated) {
      return <div>Please log in</div>;
    }
    
    return <WrappedComponent {...props} />;
  };
};

// Usage
const Dashboard = () => <div>Dashboard Content</div>;
const AuthenticatedDashboard = withAuth(Dashboard);

// HOC for loading state
const withLoading = (WrappedComponent) => {
  return ({ isLoading, ...props }) => {
    if (isLoading) {
      return <div>Loading...</div>;
    }
    return <WrappedComponent {...props} />;
  };
};
```

### 20. What are Render Props?
**Answer:** Render props is a technique for sharing code between components using a prop whose value is a function.

```jsx
// Mouse tracker with render props
const MouseTracker = ({ render }) => {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  
  const handleMouseMove = (e) => {
    setPosition({ x: e.clientX, y: e.clientY });
  };
  
  return (
    <div onMouseMove={handleMouseMove}>
      {render(position)}
    </div>
  );
};

// Usage
const App = () => (
  <MouseTracker
    render={({ x, y }) => (
      <div>Mouse position: {x}, {y}</div>
    )}
  />
);

// Alternative: children as function
const MouseTracker2 = ({ children }) => {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  
  const handleMouseMove = (e) => {
    setPosition({ x: e.clientX, y: e.clientY });
  };
  
  return (
    <div onMouseMove={handleMouseMove}>
      {children(position)}
    </div>
  );
};

// Usage
const App2 = () => (
  <MouseTracker2>
    {({ x, y }) => <div>Mouse: {x}, {y}</div>}
  </MouseTracker2>
);
```

### 21. What is Error Boundary?
**Answer:** Error Boundaries are React components that catch JavaScript errors anywhere in their child component tree and display a fallback UI.

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    });
    
    // Log error to error reporting service
    console.error('Error caught by boundary:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Something went wrong!</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
          </details>
        </div>
      );
    }
    
    return this.props.children;
  }
}

// Usage
const App = () => (
  <ErrorBoundary>
    <Header />
    <MainContent />
    <Footer />
  </ErrorBoundary>
);

// Functional component version using react-error-boundary library
import { ErrorBoundary } from 'react-error-boundary';

const ErrorFallback = ({ error, resetErrorBoundary }) => (
  <div role="alert">
    <h2>Something went wrong:</h2>
    <pre>{error.message}</pre>
    <button onClick={resetErrorBoundary}>Try again</button>
  </div>
);

const App = () => (
  <ErrorBoundary
    FallbackComponent={ErrorFallback}
    onError={(error, errorInfo) => {
      console.error('Error logged:', error, errorInfo);
    }}
  >
    <MainApp />
  </ErrorBoundary>
);
```

### 22. What is Reconciliation?
**Answer:** Reconciliation is the process by which React updates the DOM by comparing the new virtual DOM tree with the previous one.

**How it works:**
1. When state changes, React creates a new virtual DOM tree
2. React compares (diffs) the new tree with the previous tree
3. React calculates the minimum number of changes needed
4. React updates only the changed elements in the real DOM

**Key Algorithms:**
- **Diffing Algorithm**: Compares trees level by level
- **Keys**: Help React identify which items have changed, added, or removed

```jsx
// Without keys - React can't efficiently update
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => <li>{item.name}</li>)} {/* BAD */}
  </ul>
);

// With keys - React can efficiently update
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => <li key={item.id}>{item.name}</li>)} {/* GOOD */}
  </ul>
);
```

---

## Testing

### 23. How do you test React components?
**Answer:** There are several approaches to testing React components:

**1. Unit Testing with Jest and React Testing Library:**
```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('renders counter with initial value', () => {
  render(<Counter initialValue={0} />);
  expect(screen.getByText('Count: 0')).toBeInTheDocument();
});

test('increments counter when button is clicked', () => {
  render(<Counter initialValue={0} />);
  const button = screen.getByRole('button', { name: /increment/i });
  
  fireEvent.click(button);
  
  expect(screen.getByText('Count: 1')).toBeInTheDocument();
});

test('calls onCountChange when count changes', () => {
  const mockOnCountChange = jest.fn();
  render(<Counter initialValue={0} onCountChange={mockOnCountChange} />);
  
  const button = screen.getByRole('button', { name: /increment/i });
  fireEvent.click(button);
  
  expect(mockOnCountChange).toHaveBeenCalledWith(1);
});
```

**2. Testing Hooks:**
```jsx
import { renderHook, act } from '@testing-library/react';
import useCounter from './useCounter';

test('should increment counter', () => {
  const { result } = renderHook(() => useCounter(0));
  
  act(() => {
    result.current.increment();
  });
  
  expect(result.current.count).toBe(1);
});
```

**3. Testing with Context:**
```jsx
import { render, screen } from '@testing-library/react';
import { ThemeProvider } from './ThemeContext';
import ThemedButton from './ThemedButton';

test('renders with correct theme', () => {
  render(
    <ThemeProvider value="dark">
      <ThemedButton>Click me</ThemedButton>
    </ThemeProvider>
  );
  
  expect(screen.getByRole('button')).toHaveClass('dark-theme');
});
```

### 24. What testing libraries are commonly used with React?
**Answer:** 

**Testing Libraries:**
- **Jest**: JavaScript testing framework
- **React Testing Library**: Simple and complete testing utilities
- **Enzyme**: JavaScript testing utility (less popular now)
- **Cypress**: End-to-end testing
- **React Test Renderer**: For snapshot testing

**Example Test Structure:**
```jsx
// Button.test.jsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Button from './Button';

describe('Button Component', () => {
  test('renders button with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });
  
  test('calls onClick when clicked', async () => {
    const user = userEvent.setup();
    const handleClick = jest.fn();
    
    render(<Button onClick={handleClick}>Click me</Button>);
    
    await user.click(screen.getByRole('button'));
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  test('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

---

## Bonus Questions

### 25. What's new in React 18?
**Answer:** 

**Key Features:**
1. **Concurrent Rendering**: Allows React to interrupt rendering
2. **Automatic Batching**: Groups multiple state updates
3. **Suspense improvements**: Better loading states
4. **New Hooks**: useId, useDeferredValue, useTransition

```jsx
// useTransition for non-urgent updates
const SearchComponent = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isPending, startTransition] = useTransition();
  
  const handleSearch = (e) => {
    setQuery(e.target.value);
    
    startTransition(() => {
      // Non-urgent update
      setResults(searchData(e.target.value));
    });
  };
  
  return (
    <div>
      <input value={query} onChange={handleSearch} />
      {isPending && <div>Searching...</div>}
      <SearchResults results={results} />
    </div>
  );
};

// useDeferredValue for deferred updates
const FilteredList = ({ items, filter }) => {
  const deferredFilter = useDeferredValue(filter);
  const filteredItems = useMemo(() => {
    return items.filter(item => item.name.includes(deferredFilter));
  }, [items, deferredFilter]);
  
  return <List items={filteredItems} />;
};
```

### 26. What are some React best practices?
**Answer:** 

**1. Component Organization:**
```jsx
// Keep components small and focused
const UserCard = ({ user }) => (
  <div className="user-card">
    <UserAvatar src={user.avatar} />
    <UserInfo name={user.name} email={user.email} />
    <UserActions userId={user.id} />
  </div>
);

// Use composition over inheritance
const Modal = ({ children, onClose }) => (
  <div className="modal-overlay" onClick={onClose}>
    <div className="modal-content" onClick={e => e.stopPropagation()}>
      {children}
    </div>
  </div>
);
```

**2. State Management:**
```jsx
// Keep state as low as possible
// Lift state up when needed
// Use context sparingly (avoid overuse)

// Good: Local state
const Counter = () => {
  const [count, setCount] = useState(0);
  return <div>Count: {count}</div>;
};

// Good: Shared state lifted up
const App = () => {
  const [users, setUsers] = useState([]);
  
  return (
    <>
      <UserList users={users} />
      <AddUserForm onAddUser={user => setUsers([...users, user])} />
    </>
  );
};
```

**3. Performance:**
```jsx
// Use keys properly
{items.map(item => <Item key={item.id} data={item} />)}

// Memoize expensive calculations
const expensiveValue = useMemo(() => calculateValue(data), [data]);

// Use callback for stable references
const handleClick = useCallback((id) => {
  onClick(id);
}, [onClick]);
```

**4. Error Handling:**
```jsx
// Always use Error Boundaries
// Handle async errors properly
const DataComponent = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetchData()
      .then(setData)
      .catch(setError);
  }, []);
  
  if (error) return <ErrorMessage error={error} />;
  if (!data) return <Loading />;
  
  return <DataDisplay data={data} />;
};
```

---

## Summary

This guide covers the most important React interview questions and concepts. Key areas to focus on:

1. **Fundamentals**: Components, JSX, Virtual DOM
2. **State Management**: useState, props, lifting state up
3. **Effects**: useEffect, cleanup, dependencies
4. **Performance**: React.memo, useMemo, useCallback
5. **Advanced Patterns**: Context, HOCs, render props
6. **Testing**: React Testing Library, Jest
7. **Modern React**: Hooks, Concurrent features

**Interview Tips:**
- Understand the "why" behind React concepts
- Practice coding examples
- Be ready to discuss trade-offs and alternatives
- Know when to use different patterns and optimizations
- Stay updated with latest React features and best practices 

---

## Tricky & Advanced Interview Questions

### 27. Why would you choose `useState` over `useReducer`? When should you use each?
**Answer:** 

**Use `useState` when:**
- Managing simple state (primitives, single values)
- State transitions are straightforward 
- No complex state logic
- Component state is independent

```jsx
const Toggle = () => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <button onClick={() => setIsOpen(!isOpen)}>
      {isOpen ? 'Close' : 'Open'}
    </button>
  );
};
```

**Use `useReducer` when:**
- Complex state objects with multiple sub-values
- State logic involves multiple actions
- Next state depends on the previous one
- Want to optimize performance for components that trigger deep updates

```jsx
const formReducer = (state, action) => {
  switch (action.type) {
    case 'SET_FIELD':
      return { ...state, [action.field]: action.value };
    case 'SET_ERROR':
      return { ...state, errors: { ...state.errors, [action.field]: action.error } };
    case 'RESET':
      return initialState;
    default:
      return state;
  }
};

const ContactForm = () => {
  const [state, dispatch] = useReducer(formReducer, {
    name: '', email: '', message: '', errors: {}
  });
  
  // Complex state management with multiple related fields
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!state.name) {
      dispatch({ type: 'SET_ERROR', field: 'name', error: 'Required' });
    }
    // ... more validation logic
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input 
        value={state.name}
        onChange={(e) => dispatch({ 
          type: 'SET_FIELD', 
          field: 'name', 
          value: e.target.value 
        })}
      />
      {state.errors.name && <span>{state.errors.name}</span>}
    </form>
  );
};
```

**Why `useReducer` is better for complex state:**
- **Predictable state updates**: All state changes go through the reducer
- **Easier testing**: Pure function, easy to test in isolation  
- **Better debugging**: Clear action types make debugging easier
- **Performance**: Prevents unnecessary re-renders with stable dispatch function

### 28. Explain the internal workings of `useEffect`. Why do we need the dependency array?
**Answer:** 

**Behind the scenes, `useEffect`:**

1. **Effect scheduling**: React schedules effects to run after the DOM has been updated
2. **Cleanup tracking**: React tracks cleanup functions and calls them before the next effect or unmount
3. **Dependency comparison**: React uses `Object.is()` to compare each dependency
4. **Effect queue**: Multiple effects are queued and executed in the order they were defined

```jsx
const DataComponent = ({ userId }) => {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    console.log('Effect runs');
    
    // This runs AFTER the DOM update
    const controller = new AbortController();
    
    fetch(`/api/users/${userId}`, { 
      signal: controller.signal 
    })
      .then(res => res.json())
      .then(setUser);
    
    // Cleanup function - runs before next effect or unmount
    return () => {
      console.log('Cleanup runs');
      controller.abort(); // Cancel the request
    };
  }, [userId]); // Dependency array
  
  return <div>{user?.name}</div>;
};
```

**Why dependency array is crucial:**

```jsx
// ❌ WRONG - Missing dependency
const BadExample = ({ userId }) => {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId dependency!
  
  // Effect won't re-run when userId changes
  // Will always fetch the same user
};

// ✅ CORRECT - Include all dependencies
const GoodExample = ({ userId }) => {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Effect re-runs when userId changes
};

// ⚠️ STALE CLOSURE PROBLEM
const StaleClosureExample = () => {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    const timer = setInterval(() => {
      setCount(count + 1); // Always uses initial count (0)!
    }, 1000);
    
    return () => clearInterval(timer);
  }, []); // Empty dependency array captures stale count
  
  // Fix: Use functional update
  useEffect(() => {
    const timer = setInterval(() => {
      setCount(prev => prev + 1); // Uses current count
    }, 1000);
    
    return () => clearInterval(timer);
  }, []); // Now it's safe to omit count
};
```

**Advanced Effect Patterns:**

```jsx
// Custom hook for API calls
const useApi = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let cancelled = false;
    
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();
        
        if (!cancelled) {
          setData(result);
          setError(null);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    
    fetchData();
    
    return () => {
      cancelled = true; // Prevent state updates if component unmounts
    };
  }, [url]);
  
  return { data, loading, error };
};
```

### 29. Why do React Hooks exist? What problems do they solve compared to class components?
**Answer:** 

**Problems with Class Components:**

1. **Complex lifecycle methods**: Logic scattered across different lifecycle methods
2. **Wrapper hell**: HOCs and render props created deeply nested components  
3. **Hard to reuse stateful logic**: No good way to share stateful logic between components
4. **`this` binding confusion**: Need to bind methods or use arrow functions
5. **Bundle size**: Classes don't minify as well as functions

```jsx
// ❌ Class component problems
class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null,
      posts: [],
      loading: true
    };
    
    // Binding nightmare
    this.handleUserUpdate = this.handleUserUpdate.bind(this);
  }
  
  // Logic scattered across multiple methods
  componentDidMount() {
    this.fetchUser();
    this.subscribeToUserUpdates();
    document.title = `Profile: ${this.props.userId}`;
  }
  
  componentDidUpdate(prevProps) {
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
      document.title = `Profile: ${this.props.userId}`;
    }
  }
  
  componentWillUnmount() {
    this.unsubscribeFromUserUpdates();
  }
  
  fetchUser = async () => {
    // Fetch logic...
  }
  
  subscribeToUserUpdates = () => {
    // Subscription logic...
  }
  
  unsubscribeFromUserUpdates = () => {
    // Cleanup logic...
  }
  
  handleUserUpdate = (updatedUser) => {
    this.setState({ user: updatedUser });
  }
  
  render() {
    const { user, loading } = this.state;
    if (loading) return <Loading />;
    return <UserCard user={user} />;
  }
}
```

**How Hooks solve these problems:**

```jsx
// ✅ Hooks solution - cleaner and more reusable
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  // Related logic grouped together
  useEffect(() => {
    let cancelled = false;
    
    const fetchUser = async () => {
      setLoading(true);
      try {
        const userData = await api.getUser(userId);
        if (!cancelled) {
          setUser(userData);
          setLoading(false);
        }
      } catch (error) {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    
    fetchUser();
    
    return () => {
      cancelled = true;
    };
  }, [userId]);
  
  // Document title effect
  useEffect(() => {
    document.title = `Profile: ${userId}`;
    
    return () => {
      document.title = 'My App';
    };
  }, [userId]);
  
  // Real-time updates
  useEffect(() => {
    const unsubscribe = subscribeToUserUpdates(userId, setUser);
    return unsubscribe;
  }, [userId]);
  
  if (loading) return <Loading />;
  return <UserCard user={user} />;
};

// Custom hook - reusable stateful logic!
const useUser = (userId) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    // Same fetch logic as above
  }, [userId]);
  
  return { user, loading, error };
};

// Now any component can use this logic
const AnotherComponent = ({ userId }) => {
  const { user, loading, error } = useUser(userId);
  
  if (loading) return <Loading />;
  if (error) return <Error message={error} />;
  return <div>{user.name}</div>;
};
```

**Key advantages of Hooks:**

1. **Colocation**: Related logic stays together
2. **Reusability**: Custom hooks allow sharing stateful logic
3. **Simplicity**: No class syntax, no `this` binding
4. **Better testing**: Easier to test custom hooks in isolation
5. **Performance**: Functions optimize better than classes
6. **Developer experience**: Better tree-shaking, smaller bundles

### 30. Explain React's reconciliation process and why keys are crucial
**Answer:** 

**Reconciliation Algorithm:**

React uses a diffing algorithm to compare the new virtual DOM tree with the previous one. The algorithm is O(n) instead of O(n³) because of these assumptions:

1. **Different element types produce different trees**
2. **Stable keys help identify which items have changed**

```jsx
// ❌ Without keys - React can't efficiently reconcile
const TodoList = ({ todos }) => {
  return (
    <ul>
      {todos.map(todo => (
        <li>{todo.text}</li> // No key!
      ))}
    </ul>
  );
};

// When a new todo is added at the beginning:
// OLD: [<li>Buy milk</li>, <li>Walk dog</li>]
// NEW: [<li>Buy eggs</li>, <li>Buy milk</li>, <li>Walk dog</li>]

// React sees: First li changed from "Buy milk" to "Buy eggs"
//             Second li changed from "Walk dog" to "Buy milk"  
//             Third li is new "Walk dog"
// Result: All DOM nodes are updated/recreated!
```

```jsx
// ✅ With proper keys - efficient reconciliation
const TodoList = ({ todos }) => {
  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li> // Stable, unique key
      ))}
    </ul>
  );
};

// With keys, React understands:
// OLD: [<li key="1">Buy milk</li>, <li key="2">Walk dog</li>]
// NEW: [<li key="3">Buy eggs</li>, <li key="1">Buy milk</li>, <li key="2">Walk dog</li>]

// React sees: key="3" is new (insert at beginning)
//             key="1" and key="2" are the same (just moved)
// Result: Only one DOM insertion!
```

**Key Rules and Anti-patterns:**

```jsx
// ❌ NEVER use array index as key when list can change
const BadExample = ({ items }) => (
  <ul>
    {items.map((item, index) => (
      <li key={index}>{item.name}</li> // BAD!
    ))}
  </ul>
);

// ❌ NEVER use random values as keys
const WorsExample = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={Math.random()}>{item.name}</li> // TERRIBLE!
    ))}
  </ul>
);

// ✅ Use stable, unique identifiers
const GoodExample = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.name}</li> // GOOD!
    ))}
  </ul>
);

// ✅ Create stable keys if you don't have IDs
const AcceptableExample = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={`${item.name}-${item.category}`}>{item.name}</li>
    ))}
  </ul>
);
```

**How reconciliation affects performance:**

```jsx
// Component that demonstrates reconciliation impact
const ExpensiveListItem = ({ item, onUpdate }) => {
  const [internalState, setInternalState] = useState(item.value);
  
  // Expensive calculation
  const expensiveValue = useMemo(() => {
    console.log('Expensive calculation for', item.id);
    return item.data.reduce((sum, val) => sum + val * val, 0);
  }, [item.data]);
  
  useEffect(() => {
    console.log('Effect ran for item', item.id);
    setInternalState(item.value);
  }, [item.value]);
  
  return (
    <div>
      <span>{item.name}: {expensiveValue}</span>
      <input 
        value={internalState}
        onChange={(e) => setInternalState(e.target.value)}
      />
    </div>
  );
};

// With proper keys: Only new items run expensive calculations
// Without keys: ALL items re-run calculations when list changes!
```

### 31. What happens behind the scenes when you call `setState` or a state setter from `useState`?
**Answer:** 

**State Update Process:**

1. **State update is scheduled** (not immediately applied)
2. **React batches updates** for performance
3. **Reconciliation process** starts
4. **Re-render is scheduled**
5. **Effects are scheduled** to run after DOM updates

```jsx
const StateInternalsExample = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  const handleClick = () => {
    console.log('Before setState:', count); // 0
    
    setCount(count + 1);
    console.log('After setState:', count); // Still 0! (not immediate)
    
    setCount(count + 1); // This won't increment to 2!
    console.log('After second setState:', count); // Still 0!
    
    // Both setCount calls use the same stale value (0)
    // Final result: count becomes 1, not 2
  };
  
  const handleCorrectIncrement = () => {
    // Use functional updates for correct behavior
    setCount(prev => prev + 1); // prev = current value
    setCount(prev => prev + 1); // prev = updated value
    // Result: count increases by 2
  };
  
  const handleBatchedUpdates = () => {
    // These are automatically batched in React 18
    setCount(c => c + 1);
    setName('John');
    // Only triggers ONE re-render, not two!
  };
  
  return (
    <div>
      <p>Count: {count}</p>
      <p>Name: {name}</p>
      <button onClick={handleClick}>Wrong increment</button>
      <button onClick={handleCorrectIncrement}>Correct increment</button>
      <button onClick={handleBatchedUpdates}>Batched updates</button>
    </div>
  );
};
```

**State Update Timing:**

```jsx
const TimingExample = () => {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    console.log('Effect runs, count is:', count);
  }, [count]);
  
  const handleAsyncUpdate = async () => {
    console.log('1. Before setState:', count);
    
    setCount(count + 1);
    console.log('2. After setState (sync):', count); // Still old value
    
    // In older React versions, async updates weren't batched
    setTimeout(() => {
      setCount(prev => prev + 1); // This creates separate render
    }, 0);
    
    // Promise updates  
    Promise.resolve().then(() => {
      setCount(prev => prev + 1); // In React 18, this is batched too
    });
    
    console.log('3. End of function:', count); // Still old value
  };
  
  // The actual update happens after this function completes
  // Then useEffect runs with the new value
  
  return <button onClick={handleAsyncUpdate}>Async updates</button>;
};
```

**React 18 Automatic Batching:**

```jsx
// React 18 batches ALL updates automatically
const React18Batching = () => {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);
  
  function handleClick() {
    // Batched: only one render
    setCount(c => c + 1);
    setFlag(f => !f);
  }
  
  function handleAsyncClick() {
    // React 18: Even async updates are batched!
    setTimeout(() => {
      setCount(c => c + 1);
      setFlag(f => !f);
      // Only one render, not two
    }, 1000);
    
    fetch('/api').then(() => {
      setCount(c => c + 1);
      setFlag(f => !f);
      // Also batched in React 18
    });
  }
  
  // To opt out of batching (rarely needed):
  function handleUnbatchedClick() {
    import { flushSync } from 'react-dom';
    
    flushSync(() => {
      setCount(c => c + 1);
    }); // First render
    
    flushSync(() => {
      setFlag(f => !f);
    }); // Second render
  }
  
  console.log('Render count:', count, flag);
  
  return <div>/* JSX */</div>;
};
```

### 32. How does React Fiber architecture improve performance?
**Answer:** 

React Fiber is a complete rewrite of React's core algorithm that enables **concurrent rendering** and **interruptible work**.

**Key improvements:**

1. **Work can be paused and resumed**: Break large updates into smaller chunks
2. **Priority-based scheduling**: High-priority updates (user input) can interrupt low-priority ones (data fetching)
3. **Better error boundaries**: More granular error handling
4. **Async rendering**: Preparation work can happen off the main thread

```jsx
// Before Fiber: Blocking updates
const HeavyComponent = ({ items }) => {
  // This would block the main thread until finished
  const processedItems = items.map(item => {
    // Heavy computation
    return expensiveProcessing(item);
  });
  
  return (
    <div>
      {processedItems.map(item => <ItemCard key={item.id} item={item} />)}
    </div>
  );
};

// With Fiber: Interruptible rendering
const FiberOptimizedComponent = ({ items }) => {
  const [isPending, startTransition] = useTransition();
  const [processedItems, setProcessedItems] = useState([]);
  
  const handleHeavyUpdate = () => {
    // Low priority update - can be interrupted
    startTransition(() => {
      const processed = items.map(item => expensiveProcessing(item));
      setProcessedItems(processed);
    });
  };
  
  return (
    <div>
      <button onClick={handleHeavyUpdate}>
        {isPending ? 'Processing...' : 'Process Items'}
      </button>
      {processedItems.map(item => <ItemCard key={item.id} item={item} />)}
    </div>
  );
};
```

**Time slicing example:**
```jsx
// Fiber breaks this into multiple frames
const renderManyItems = () => {
  return (
    <div>
      {Array.from({ length: 10000 }, (_, i) => (
        <ExpensiveItem key={i} data={items[i]} />
      ))}
    </div>
  );
};

// Instead of blocking for 100ms straight,
// Fiber might render:
// Frame 1: Items 0-100 (16ms)
// Frame 2: Handle user input (16ms) 
// Frame 3: Items 101-200 (16ms)
// Frame 4: Handle user input (16ms)
// ... and so on
```

### 33. Explain the difference between client-side and server-side rendering in React
**Answer:** 

**Client-Side Rendering (CSR):**
- HTML is generated in the browser using JavaScript
- Initial page load sends minimal HTML
- React hydrates and renders the full UI

```jsx
// CSR - App renders entirely in browser
const App = () => {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // Data fetching happens after initial render
    fetch('/api/data').then(res => res.json()).then(setData);
  }, []);
  
  if (!data) return <div>Loading...</div>; // User sees this first
  
  return <UserDashboard data={data} />;
};
```

**Server-Side Rendering (SSR):**
- HTML is generated on the server
- Full HTML sent to browser
- React hydrates the existing HTML

```jsx
// SSR - getServerSideProps runs on server
export async function getServerSideProps(context) {
  // This runs on the server before rendering
  const data = await fetch('http://localhost:3001/api/data');
  const userData = await data.json();
  
  return {
    props: { userData } // Passed to component as props
  };
}

const Dashboard = ({ userData }) => {
  // Component receives pre-fetched data
  // HTML is already rendered when it reaches browser
  return <UserDashboard data={userData} />;
};
```

**Static Site Generation (SSG):**
```jsx
// SSG - Built at build time
export async function getStaticProps() {
  // This runs at BUILD TIME, not request time
  const posts = await fetch('https://api.blog.com/posts');
  const blogPosts = await posts.json();
  
  return {
    props: { blogPosts },
    revalidate: 3600 // Regenerate every hour
  };
}

const BlogPage = ({ blogPosts }) => {
  // This page is pre-generated as static HTML
  return (
    <div>
      {blogPosts.map(post => <BlogPost key={post.id} post={post} />)}
    </div>
  );
};
```

**Performance implications:**

| Aspect | CSR | SSR | SSG |
|--------|-----|-----|-----|
| **First Paint** | Slow | Fast | Fastest |
| **SEO** | Poor | Good | Excellent |
| **Server Load** | Low | High | Low |
| **Caching** | Client-side | Limited | Excellent |
| **Dynamic Content** | Excellent | Good | Limited |

### 34. What are React design patterns you should know?
**Answer:** 

**1. Compound Components Pattern:**
```jsx
// Allow components to work together while maintaining flexibility
const Modal = ({ children, isOpen, onClose }) => {
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {children}
      </div>
    </div>
  );
};

Modal.Header = ({ children }) => <div className="modal-header">{children}</div>;
Modal.Body = ({ children }) => <div className="modal-body">{children}</div>;
Modal.Footer = ({ children }) => <div className="modal-footer">{children}</div>;

// Usage - flexible composition
const App = () => (
  <Modal isOpen={true} onClose={closeModal}>
    <Modal.Header>
      <h2>Confirm Action</h2>
    </Modal.Header>
    <Modal.Body>
      <p>Are you sure you want to delete this item?</p>
    </Modal.Body>
    <Modal.Footer>
      <button onClick={handleDelete}>Delete</button>
      <button onClick={closeModal}>Cancel</button>
    </Modal.Footer>
  </Modal>
);
```

**2. Provider Pattern:**
```jsx
// Centralize state management and avoid prop drilling
const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);
  
  const value = {
    theme,
    setTheme,
    user,
    setUser,
    // Computed values
    isDark: theme === 'dark',
    isAuthenticated: !!user
  };
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

// Custom hook for consuming context
const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};

// Usage anywhere in the tree
const Header = () => {
  const { theme, setTheme, user } = useTheme();
  
  return (
    <header className={theme}>
      <h1>Welcome {user?.name}</h1>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
};
```

**3. Custom Hooks Pattern:**
```jsx
// Extract and reuse stateful logic
const useAsync = (asyncFunction, dependencies = []) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let cancelled = false;
    
    const execute = async () => {
      try {
        setLoading(true);
        setError(null);
        const result = await asyncFunction();
        
        if (!cancelled) {
          setData(result);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    
    execute();
    
    return () => {
      cancelled = true;
    };
  }, dependencies);
  
  return { data, loading, error };
};

// Reusable across components
const UserProfile = ({ userId }) => {
  const { data: user, loading, error } = useAsync(
    () => fetch(`/api/users/${userId}`).then(res => res.json()),
    [userId]
  );
  
  if (loading) return <Loading />;
  if (error) return <Error message={error} />;
  
  return <UserCard user={user} />;
};

const PostList = () => {
  const { data: posts, loading, error } = useAsync(
    () => fetch('/api/posts').then(res => res.json()),
    []
  );
  
  // Same loading/error handling logic reused
  if (loading) return <Loading />;
  if (error) return <Error message={error} />;
  
  return <PostGrid posts={posts} />;
};
```