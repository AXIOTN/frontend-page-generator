# 常用 SVG 图标模板

## 基础 SVG 结构

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- 路径内容 -->
</svg>
```

## 常用图标路径

### 导航类

```svg
<!-- home.svg -->
<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
<polyline points="9 22 9 12 15 12 15 22"/>

<!-- menu.svg -->
<line x1="4" x2="20" y1="12" y2="12"/>
<line x1="4" x2="20" y1="6" y2="6"/>
<line x1="4" x2="20" y1="18" y2="18"/>

<!-- close.svg -->
<path d="M18 6 6 18"/>
<path d="m6 6 12 12"/>

<!-- left.svg (chevron-left) -->
<path d="m15 18-6-6 6-6"/>

<!-- right.svg (chevron-right) -->
<path d="m9 18 6-6-6-6"/>

<!-- arrow-left.svg -->
<path d="m12 19-7-7 7-7"/>
<path d="M19 12H5"/>

<!-- arrow-right.svg -->
<path d="m12 5 7 7-7 7"/>
<path d="M5 12h14"/>
```

### 用户类

```svg
<!-- user.svg -->
<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
<circle cx="12" cy="7" r="4"/>

<!-- users.svg -->
<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
<circle cx="9" cy="7" r="4"/>
<path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
<path d="M16 3.13a4 4 0 0 1 0 7.75"/>

<!-- settings.svg -->
<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
<circle cx="12" cy="12" r="3"/>
```

### 操作类

```svg
<!-- search.svg -->
<circle cx="11" cy="11" r="8"/>
<path d="m21 21-4.3-4.3"/>

<!-- heart.svg -->
<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>

<!-- star.svg -->
<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>

<!-- eye.svg -->
<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
<circle cx="12" cy="12" r="3"/>

<!-- mail.svg -->
<rect width="20" height="16" x="2" y="4" rx="2"/>
<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
```

### 内容类

```svg
<!-- file-text.svg -->
<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/>
<polyline points="14 2 14 8 20 8"/>
<line x1="16" x2="8" y1="13" y2="13"/>
<line x1="16" x2="8" y1="17" y2="17"/>
<line x1="10" x2="8" y1="9" y2="9"/>

<!-- book-open.svg -->
<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>

<!-- code.svg -->
<polyline points="16 18 22 12 16 6"/>
<polyline points="8 6 2 12 8 18"/>
```

### 状态类

```svg
<!-- check-circle.svg -->
<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
<path d="m9 11 3 3L22 4"/>

<!-- info.svg -->
<circle cx="12" cy="12" r="10"/>
<path d="M12 16v-4"/>
<path d="M12 8h.01"/>

<!-- alert-triangle.svg -->
<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
<path d="M12 9v4"/>
<path d="M12 17h.01"/>

<!-- alert-circle.svg -->
<circle cx="12" cy="12" r="10"/>
<line x1="12" x2="12" y1="8" y2="12"/>
<line x1="12" x2="12.01" y1="16" y2="16"/>
```

### 媒体类

```svg
<!-- image.svg -->
<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>
<circle cx="9" cy="9" r="2"/>
<path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>

<!-- video.svg -->
<path d="m22 8-6 4 6 4V8Z"/>
<rect width="14" height="12" x="2" y="6" rx="2" ry="2"/>

<!-- film.svg -->
<rect width="18" height="18" x="3" y="3" rx="2"/>
<path d="M7 3v18"/>
<path d="M3 7.5h4"/>
<path d="M3 12h18"/>
<path d="M3 16.5h4"/>
<path d="M17 3v18"/>
<path d="M17 7.5h4"/>
<path d="M17 16.5h4"/>
```

### 社交类

```svg
<!-- github.svg -->
<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
<path d="M9 18c-4.51 2-5-2-7-2"/>
```

### 其他

```svg
<!-- calendar.svg -->
<rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
<line x1="16" x2="16" y1="2" y2="6"/>
<line x1="8" x2="8" y1="2" y2="6"/>
<line x1="3" x2="21" y1="10" y2="10"/>

<!-- clock.svg -->
<circle cx="12" cy="12" r="10"/>
<polyline points="12 6 12 12 16 14"/>

<!-- map-pin.svg -->
<line x1="2" x2="5" y1="12" y2="12"/>
<line x1="19" x2="22" y1="12" y2="12"/>
<line x1="12" x2="12" y1="2" y2="5"/>
<line x1="12" x2="12" y1="19" y2="22"/>
<circle cx="12" cy="12" r="7"/>
<circle cx="12" cy="12" r="3"/>

<!-- graduation-cap.svg -->
<path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
<path d="M6 12v5c3 3 10 3 12 0v-5"/>

<!-- building.svg -->
<rect width="16" height="20" x="4" y="2" rx="2" ry="2"/>
<path d="M9 22v-4h6v4"/>
<path d="M8 6h.01"/>
<path d="M16 6h.01"/>
<path d="M12 6h.01"/>
<path d="M12 10h.01"/>
<path d="M12 14h.01"/>
<path d="M16 10h.01"/>
<path d="M16 14h.01"/>
<path d="M8 10h.01"/>
<path d="M8 14h.01"/>

<!-- compass.svg -->
<circle cx="12" cy="12" r="10"/>
<polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>

<!-- target.svg -->
<circle cx="12" cy="12" r="10"/>
<circle cx="12" cy="12" r="6"/>
<circle cx="12" cy="12" r="2"/>

<!-- layout-grid.svg -->
<rect width="7" height="7" x="3" y="3" rx="1"/>
<rect width="7" height="7" x="14" y="3" rx="1"/>
<rect width="7" height="7" x="14" y="14" rx="1"/>
<rect width="7" height="7" x="3" y="14" rx="1"/>

<!-- pen-tool.svg -->
<path d="m12 19 7-7 3 3-7 7-3-3z"/>
<path d="m18 13-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>
<path d="m2 2 7.586 7.586"/>
<circle cx="11" cy="11" r="2"/>
```

## 使用方式

### HTML
```html
<img src="icons/home.svg" alt="首页" width="24" height="24">
```

### React (内联)
```tsx
const HomeIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
    <polyline points="9 22 9 12 15 12 15 22"/>
  </svg>
);
```

### React (lucide-react)
```tsx
import { Home } from 'lucide-react';
<Home size={24} />
```
