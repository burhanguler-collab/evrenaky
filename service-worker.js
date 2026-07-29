const CACHE_NAME = 'project-cache-20260729-2113';
const ASSETS = [
  'index.html',
  'index.css',
  'app.js',
  'manifest.json',
  'Gorseller/pwa_icon.png'
];

// Install Event
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[Service Worker] Caching static shell');
      return cache.addAll(ASSETS);
    })
  );
});

// Activate Event
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME) {
            console.log('[Service Worker] Clearing old cache', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event (Network-First Fallback-to-Cache Strategy for dynamic book files, Cache-First for static assets)
self.addEventListener('fetch', event => {
  // Only handle HTTP/HTTPS protocols (avoid browser extensions/file protocols)
  if (!event.request.url.startsWith(self.location.origin)) {
    return;
  }

  // Network-First with Cache Fallback for dynamic content (like markdown files)
  if (event.request.url.includes('/Metin/') || event.request.url.endsWith('.md')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          // Open cache and put the updated markdown file in there dynamically
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, clone);
          });
          return response;
        })
        .catch(() => {
          // If offline, try to get it from cache
          return caches.match(event.request);
        })
    );
  } else {
    // Cache-First strategy for static shell assets (index.css, app.js, fonts, images)
    event.respondWith(
      caches.match(event.request).then(cachedResponse => {
        if (cachedResponse) {
          // Return cached asset, but fetch update in background (Stale-While-Revalidate)
          fetch(event.request).then(networkResponse => {
            if (networkResponse.status === 200) {
              caches.open(CACHE_NAME).then(cache => {
                cache.put(event.request, networkResponse);
              });
            }
          }).catch(() => {/* Ignore network errors offline */});
          return cachedResponse;
        }
        return fetch(event.request);
      })
    );
  }
});
