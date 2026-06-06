# React + Flask 全栈项目模板

## 技术栈

- 前端: React 18 + TypeScript + Tailwind CSS
- 后端: Python Flask + Flask-CORS
- 数据: JSON 文件存储

## 目录结构

```
project/
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── layout/      # Layout, Navbar, Footer
│   │   │   ├── common/      # Loading, Error, Empty
│   │   │   └── articles/    # ArticleCard, ArticleList, etc.
│   │   ├── pages/           # HomePage, ArticlesPage, etc.
│   │   ├── hooks/           # useArticles, useCategories, etc.
│   │   ├── services/        # API 服务 (axios)
│   │   ├── types/           # TypeScript 类型定义
│   │   ├── assets/icons/    # 本地图标库
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/
│   ├── app.py              # Flask API
│   ├── run.py              # 启动脚本
│   ├── requirements.txt
│   └── data/               # JSON 数据
│
├── start.bat               # 一键启动脚本
└── README.md
```

## 关键文件模板

### frontend/package.json 核心依赖

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "typescript": "^4.9.5",
    "axios": "^1.6.2",
    "lucide-react": "^0.294.0",
    "framer-motion": "^10.16.16",
    "react-markdown": "^9.0.1"
  },
  "devDependencies": {
    "tailwindcss": "^3.3.6",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

### frontend/tailwind.config.js

```javascript
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        }
      }
    }
  },
  plugins: [],
}
```

### frontend/src/services/api.ts 模式

```typescript
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

// 响应拦截器
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const message = error.response?.data?.message || '网络错误';
    return Promise.reject(error);
  }
);

export const articleApi = {
  getArticles: (params?: any) => api.get('/articles', { params }),
  getArticle: (id: number) => api.get(`/articles/${id}`),
  getTopArticles: () => api.get('/articles/top'),
  createArticle: (data: any) => api.post('/articles', data),
  updateArticle: (id: number, data: any) => api.put(`/articles/${id}`, data),
  deleteArticle: (id: number) => api.delete(`/articles/${id}`),
  likeArticle: (id: number) => api.post(`/articles/${id}/like`),
};

export default api;
```

### frontend/src/hooks/useArticles.ts 模式

```typescript
import { useState, useEffect, useCallback } from 'react';
import { articleApi } from '../services/api';

export function useArticles(initialQuery?: any) {
  const [articles, setArticles] = useState([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState(initialQuery || { page: 1, per_page: 10 });

  const fetchArticles = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await articleApi.getArticles(query);
      if (response.code === 200) {
        setArticles(response.data.articles);
        setTotal(response.data.total);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [query]);

  useEffect(() => { fetchArticles(); }, [fetchArticles]);

  return { articles, total, loading, error, query, updateQuery: setQuery, refetch: fetchArticles };
}
```

### backend/app.py 基础结构

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/articles', methods=['GET'])
def get_articles():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    # ... 查询逻辑
    return jsonify({'code': 200, 'data': {...}})

@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    # ... 查询逻辑
    return jsonify({'code': 200, 'data': article})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## 注意事项

1. Flask 需要安装 `flask-cors` 处理跨域
2. React 使用 `process.env.REACT_APP_API_URL` 配置后端地址
3. Windows 上使用 `start.bat` 一键启动前后端
4. JSON 文件存储适合小型项目，生产环境建议使用数据库
