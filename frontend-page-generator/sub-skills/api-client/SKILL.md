# API 客户端子技能

## 概述
提供统一的 API 客户端封装，包含请求、缓存、错误处理等功能。

## API 客户端类

```javascript
class ApiClient {
  constructor(baseURL, options = {}) {
    this.baseURL = baseURL;
    this.timeout = options.timeout || 10000;
    this.headers = {
      'Content-Type': 'application/json',
      ...options.headers
    };
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(url, {
        ...options,
        headers: { ...this.headers, ...options.headers },
        signal: controller.signal
      });
      clearTimeout(timeoutId);
      if (!response.ok) throw await this.handleError(response);
      return await response.json();
    } catch (error) {
      clearTimeout(timeoutId);
      throw this.normalizeError(error);
    }
  }

  get(endpoint, params) {
    const query = params ? `?${new URLSearchParams(params)}` : '';
    return this.request(`${endpoint}${query}`);
  }

  post(endpoint, data) {
    return this.request(endpoint, { method: 'POST', body: JSON.stringify(data) });
  }

  put(endpoint, data) {
    return this.request(endpoint, { method: 'PUT', body: JSON.stringify(data) });
  }

  delete(endpoint) {
    return this.request(endpoint, { method: 'DELETE' });
  }
}
```

## 错误处理

```javascript
const errorMessages = {
  400: '请求参数错误',
  401: '未授权，请重新登录',
  403: '没有权限执行此操作',
  404: '请求的资源不存在',
  408: '请求超时，请稍后重试',
  500: '服务器错误，请稍后重试',
  502: '服务暂时不可用',
  503: '服务维护中，请稍后重试'
};

export function handleApiError(error, showMessage = true) {
  const status = error.status || 500;
  const message = error.message || errorMessages[status] || '未知错误';
  if (status === 401) {
    localStorage.removeItem('token');
    window.location.href = '/login';
    return;
  }
  if (showMessage) console.error(`[API Error ${status}]:`, message);
  return { status, message };
}
```

## 缓存管理

```javascript
class CacheManager {
  constructor(prefix = 'app_cache') {
    this.prefix = prefix;
    this.memoryCache = new Map();
  }

  set(key, value, ttl = 300000) {
    const item = { value, expiry: Date.now() + ttl };
    this.memoryCache.set(key, item);
    try {
      localStorage.setItem(`${this.prefix}:${key}`, JSON.stringify(item));
    } catch (e) {
      this.cleanup();
    }
  }

  get(key) {
    let item = this.memoryCache.get(key);
    if (!item) {
      try {
        const stored = localStorage.getItem(`${this.prefix}:${key}`);
        if (stored) {
          item = JSON.parse(stored);
          this.memoryCache.set(key, item);
        }
      } catch { return null; }
    }
    if (!item) return null;
    if (Date.now() > item.expiry) { this.remove(key); return null; }
    return item.value;
  }

  remove(key) {
    this.memoryCache.delete(key);
    localStorage.removeItem(`${this.prefix}:${key}`);
  }

  cleanup() {
    const now = Date.now();
    for (const [key, item] of this.memoryCache) {
      if (now > item.expiry) this.remove(key);
    }
  }
}

export const cache = new CacheManager();
```

## 请求状态管理 (Vue 3)

```javascript
import { ref } from 'vue';

export function useApi(apiFunc) {
  const data = ref(null);
  const loading = ref(false);
  const error = ref(null);

  const execute = async (...args) => {
    loading.value = true;
    error.value = null;
    try {
      data.value = await apiFunc(...args);
      return data.value;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  return { data, loading, error, execute };
}
```
