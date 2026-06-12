# Next.js Interview Questions and Answers

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Rendering Strategies](#rendering-strategies)
3. [App Router vs Pages Router](#app-router-vs-pages-router)
4. [Routing & Data Fetching](#routing--data-fetching)
5. [Performance & Optimization](#performance--optimization)
6. [Advanced Features](#advanced-features)

---

## Core Concepts

### 1. What is Next.js and how does it differ from React?

**Answer:**
Next.js is a React framework built by Vercel that provides building blocks for creating fast web applications. 

**Key differences:**
- **React** is a JavaScript library for building user interfaces. It primarily uses Client-Side Rendering (CSR).
- **Next.js** is a full-stack framework built on top of React. It provides built-in features like Server-Side Rendering (SSR), Static Site Generation (SSG), routing, API routes, and optimized assets.

While React requires you to set up routing (e.g., React Router) and configure tools for server-side rendering, Next.js handles these out of the box with an opinionated structure.

### 2. What are React Server Components (RSC) in Next.js?

**Answer:**
React Server Components are components that render exclusively on the server. They are the default in the Next.js App Router.

**Benefits:**
- **Zero Bundle Size:** They don't add to the JavaScript bundle sent to the client.
- **Direct Backend Access:** They can directly access databases, file systems, and internal services without needing an API layer.
- **Better Security:** Sensitive data and tokens stay on the server.
- **Faster Initial Load:** The client receives ready-to-display HTML instead of a blank page that requires JavaScript execution to render.

To make a component render on the client instead, you use the `"use client"` directive at the top of the file.

---

## Rendering Strategies

### 3. Explain the different rendering strategies in Next.js: CSR, SSR, SSG, and ISR.

**Answer:**
- **Client-Side Rendering (CSR):** The browser downloads a minimal HTML page and a JavaScript bundle. React executes in the browser to fetch data and render the UI. (Slower initial load, bad for SEO).
- **Server-Side Rendering (SSR):** The page is generated on the server on *every single request*. The client receives fully formed HTML. (Great for SEO, always up-to-date data, slower response time than SSG).
- **Static Site Generation (SSG):** The HTML is generated at *build time*. The same HTML is reused for every request and served via CDN. (Extremely fast, great for SEO, data might become stale).
- **Incremental Static Regeneration (ISR):** A hybrid of SSG and SSR. Pages are statically generated at build time, but can be updated in the background after a specified timeout (`revalidate`) without rebuilding the entire site.

### 3.1. Deep Dive: Server-Side Rendering (SSR)
**What is it?** SSR pre-renders a page on the server *on each request*. When a user requests a page, the server fetches the required data, generates the HTML, and sends it to the client.
**When to use it?** When you have highly dynamic data that changes frequently and needs to be up-to-date for every user request (e.g., personalized dashboards, e-commerce shopping carts).
**Implementation:**
- **Pages Router:** Use `getServerSideProps`.
- **App Router:** Use `fetch` with `{ cache: 'no-store' }` or dynamic functions (like `cookies()`, `headers()`).

### 3.2. Deep Dive: Static Site Generation (SSG)
**What is it?** SSG pre-renders a page on the server *at build time*. The HTML is generated once and reused for all subsequent requests, usually served from a CDN.
**When to use it?** For pages where the data does not change frequently and can be shared across all users (e.g., blog posts, marketing pages, documentation).
**Implementation:**
- **Pages Router:** Use `getStaticProps` (and `getStaticPaths` for dynamic routes).
- **App Router:** Use `fetch` with `{ cache: 'force-cache' }` (which is the default) and `generateStaticParams` for dynamic routes.

### 3.3. Deep Dive: Incremental Static Regeneration (ISR)
**What is it?** ISR allows you to update static pages *after* you've built your site without needing to rebuild the entire application. It serves the stale static page while regenerating a fresh one in the background.
**When to use it?** When you have a massive number of pages (e.g., millions of products) where building all of them at once would take too long, or when you want SSG performance but data updates periodically.
**Implementation:**
- **Pages Router:** Return `revalidate: [seconds]` from `getStaticProps`.
- **App Router:** Use `fetch` with `{ next: { revalidate: [seconds] } }` or export `const revalidate = [seconds]` at the segment level.

### 4. How does Hydration work in Next.js?

**Answer:**
Hydration is the process where a server-rendered HTML page is made interactive on the client side. 
1. The server sends static HTML to the browser for immediate display (fast Time to First Byte - TTFB).
2. The browser downloads the JavaScript bundle in the background.
3. React "attaches" event listeners and state to the existing HTML elements, bringing the page to life. This process is called hydration.

---

## App Router vs Pages Router

### 5. What are the main differences between the App Router and Pages Router?

**Answer:**
| Feature | App Router (`app/`) | Pages Router (`pages/`) |
|---------|---------------------|--------------------------|
| **Components** | Server Components by default | Client Components by default |
| **Routing** | Folder-based with `page.js` | File-based (e.g., `about.js`) |
| **Layouts** | Built-in `layout.js` that doesn't re-render | Required custom `_app.js` or wrapper components |
| **Data Fetching**| Native `fetch` with caching/revalidation | `getServerSideProps`, `getStaticProps` |
| **API** | Route Handlers (`route.js`) | API Routes (`api/` folder) |

### 6. What is the purpose of `layout.js` in the App Router?

**Answer:**
`layout.js` defines a UI that is shared between multiple routes. On navigation, layouts preserve state, remain interactive, and do not re-render. 

For example, a root `layout.js` might contain your `<nav>` and `<footer>`, while a nested `app/dashboard/layout.js` might contain a sidebar specific to the dashboard section.

---

## Routing & Data Fetching

### 7. How do you create dynamic routes in Next.js?

**Answer:**
In both the App and Pages routers, you use square brackets around folder or file names.

**App Router example:**
Path: `app/blog/[slug]/page.js`
It will match URLs like `/blog/hello-world` or `/blog/nextjs-tips`.
You access the dynamic segment via the `params` prop passed to the page component:
```javascript
export default function BlogPost({ params }) {
  return <h1>Post ID: {params.slug}</h1>;
}
```

**Catch-all routes:** Using `[...slug]` matches `/blog/a`, `/blog/a/b`, etc.
**Optional catch-all:** Using `[[...slug]]` matches `/blog`, `/blog/a`, etc.

### 8. How has data fetching changed in the Next.js App Router?

**Answer:**
In the Pages router, you used specific exported functions like `getServerSideProps` or `getStaticProps`.

In the App router, you use the standard Web `fetch()` API directly inside Server Components, which Next.js has extended to include caching and revalidation options.

```javascript
// Server Component
export default async function Page() {
  // SSR (Server-Side Rendering) - Fetches fresh data on every request
  const res1 = await fetch('https://api.example.com/data', { cache: 'no-store' });
  
  // SSG (Static Site Generation) - Fetches once at build time
  const res2 = await fetch('https://api.example.com/data', { cache: 'force-cache' });
  
  // ISR (Incremental Static Regeneration) - Revalidates every 10 seconds
  const res3 = await fetch('https://api.example.com/data', { next: { revalidate: 10 } });
  
  return <div>...</div>;
}
```

---

## Performance & Optimization

### 9. How does Next.js optimize Images?

**Answer:**
Next.js provides the `<Image />` component from `next/image` which automatically optimizes images by:
1. **Size Optimization:** Automatically serving correctly sized images for each device, using modern formats like WebP or AVIF.
2. **Visual Stability:** Preventing Cumulative Layout Shift (CLS) automatically by requiring `width` and `height` props.
3. **Faster Page Loads:** Images are lazy-loaded by default. They only load when they enter the viewport.
4. **Asset Flexibility:** On-demand image resizing, even for images hosted on remote servers (like AWS S3).

### 10. How does Next.js handle Font Optimization?

**Answer:**
The `next/font` module automatically optimizes fonts (including custom fonts) and removes external network requests for improved privacy and performance.
It downloads the font files at build time and hosts them alongside your static assets, ensuring no layout shift (Zero CLS) and faster load times.

```javascript
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

---

## Advanced Features

### 11. What is Middleware in Next.js?

**Answer:**
Middleware allows you to run code *before* a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

It runs on the Edge (like Vercel Edge Functions), making it extremely fast.
Common use cases:
- Authentication and Authorization
- Server-side redirects based on user roles
- A/B testing
- Bot protection
- i18n routing

### 12. How do you handle SEO in Next.js (App Router)?

**Answer:**
Next.js 13+ introduced a new Metadata API that can be used in any `page.js` or `layout.js` (Server Components only).

You can export a static `metadata` object or a dynamic `generateMetadata` function.

```javascript
// Static metadata
export const metadata = {
  title: 'My Next.js Blog',
  description: 'A blog built with Next.js App Router',
}

// Dynamic metadata
export async function generateMetadata({ params }) {
  const post = await fetchPost(params.id)
  return {
    title: post.title,
    description: post.summary,
  }
}
```

### 13. What are Server Actions in Next.js?

**Answer:**
Server Actions are asynchronous functions that run exclusively on the server. They can be called directly from Client Components or Server Components to handle form submissions and data mutations.

This eliminates the need to manually create an API endpoint (Route Handler) just to update a database.

```javascript
// app/actions.js
'use server'

export async function createPost(formData) {
  const title = formData.get('title')
  // Mutate data in the database
  await db.posts.insert({ title })
}

// app/page.js
import { createPost } from './actions'

export default function Page() {
  return (
    <form action={createPost}>
      <input type="text" name="title" />
      <button type="submit">Submit</button>
    </form>
  )
}
```
