# UI 设计子技能

## 概述
提供标准化的 UI 设计规范，包括配色、排版、间距、圆角、阴影等。

## 配色规范

### 语义色
- **主色 (Primary)**: 品牌色，用于CTA、链接、选中状态
- **辅色 (Secondary)**: 辅助色，用于次要操作、标签
- **成功 (Success)**: #22c55e (绿色-500)
- **警告 (Warning)**: #f59e0b (琥珀-500)
- **错误 (Error)**: #ef4444 (红色-500)
- **信息 (Info)**: #3b82f6 (蓝色-500)

### 背景色
- **浅色背景**: #f8fafc (石板色-50)
- **卡片背景**: #ffffff (白色)
- **深色背景**: #0f172a (石板色-900)

### 文字色
- **主文字**: #1e293b (石板色-800)
- **次文字**: #64748b (石板色-500)
- **浅色文字**: #94a3b8 (石板色-400)

### 常用配色方案

| 风格 | 主色 | 适用场景 |
|------|------|---------|
| 专业蓝 | #3b82f6 | 企业、SaaS、工具 |
| 活力橙 | #f97316 | 电商、促销、社交 |
| 自然绿 | #22c55e | 健康、环保、农业 |
| 智慧紫 | #8b5cf6 | 教育、创意、科技 |
| 简约灰 | #6b7280 | 工具、效率、中性 |
| 热情红 | #ef4444 | 娱乐、游戏、紧急 |

## Tailwind CSS 配置模板

```javascript
tailwind.config = {
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
          900: '#1e3a8a'
        }
      }
    }
  }
}
```

## 排版规范

### 字体栈
- 中文: "PingFang SC", "Microsoft YaHei", sans-serif
- 英文: "Inter", system-ui, sans-serif
- 代码: "Fira Code", monospace

### 字号阶梯
- xs: 12px | sm: 14px | base: 16px | lg: 18px
- xl: 20px | 2xl: 24px | 3xl: 30px | 4xl: 36px

### 字重
- Regular: 400 | Medium: 500 | Semibold: 600 | Bold: 700

## 间距系统 (4px基准)
- space-1: 4px | space-2: 8px | space-3: 12px | space-4: 16px
- space-5: 20px | space-6: 24px | space-8: 32px | space-10: 40px
- space-12: 48px | space-16: 64px | space-20: 80px | space-24: 96px

## 圆角规范
- rounded-sm: 4px | rounded: 6px | rounded-md: 8px | rounded-lg: 12px
- rounded-xl: 16px | rounded-2xl: 24px | rounded-full: 9999px

## 阴影规范
- shadow-sm: 0 1px 2px rgba(0,0,0,0.05)
- shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)
- shadow-md: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06)
- shadow-lg: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)
- shadow-xl: 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04)

## 布局规范

### 容器宽度
- 手机: 100%
- 平板: 768px
- 桌面: 1024px / 1280px

### 断点
- sm: 640px | md: 768px | lg: 1024px | xl: 1280px | 2xl: 1536px

### 间距
- 区块间距: py-16 (64px) 或 py-20 (80px)
- 卡片间距: gap-4 (16px) 或 gap-6 (24px)
- 内边距: p-4 (16px) 或 p-6 (24px)
