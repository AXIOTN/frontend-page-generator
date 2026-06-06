# frontend-page-generator
# 前端页面生成器 (Frontend Page Generator)

专业级前端页面生成技能，支持 React/Vue3/Next.js/Nuxt.js 等主流框架。包含 UI 设计规范、后端 API 对接、功能实现、动画效果四大模块。

## 技术栈优先级

| 优先级 | 技术栈 | 适用场景 |
|-------|--------|---------|
| 1 | React + TypeScript + Tailwind CSS | 复杂应用、企业项目 |
| 2 | Vue 3 + TypeScript + Element Plus | 中后台、管理系统 |
| 3 | Next.js / Nuxt.js | SSR/SSG 全栈应用 |
| 4 | HTML + Tailwind + Alpine.js | 快速原型、简单页面 |

## 子技能调用

| 子技能 | 路径 | 用途 |
|-------|------|------|
| ui-design | `sub-skills/ui-design/SKILL.md` | 配色、排版、间距规范 |
| api-client | `sub-skills/api-client/SKILL.md` | API 封装、缓存、错误处理 |
| form-validation | `sub-skills/form-validation/SKILL.md` | 表单验证规则和验证器 |
| animations | `sub-skills/animations/SKILL.md` | CSS 过渡、滚动动画、GSAP |
| icons | `sub-skills/icons/SKILL.md` | 图标管理（本地+Lucide+AI 生成） |

## 工具箱

| 工具 | 路径 | 用途 |
|-----|------|------|
| generate_page.py | `scripts/generate_page.py` | 快速生成页面模板 |
| icon_manager.py | `scripts/icon_manager.py` | 管理本地图标库 |

## 本地图标库

**位置**: `icons/` 目录（技能内置，29 个常用图标）

### 图标列表

| 图标 | 文件名 | 用途 |
|------|--------|------|
| 📖 | book-open.svg | 书籍、文档 |
| 🏢 | building.svg | 建筑、公司 |
| 📅 | calendar.svg | 日历、日期 |
| ✅ | check-circle.svg | 完成、确认 |
| ⏰ | clock.svg | 时间、时钟 |
| ❌ | close.svg | 关闭、取消 |
| 💻 | code.svg | 代码、开发 |
| 🧭 | compass.svg | 导航、探索 |
| 👁️ | eye.svg | 查看、可见 |
| 📄 | file-text.svg | 文件、文档 |
| 🎬 | film.svg | 视频、电影 |
| 🐙 | github.svg | GitHub |
| 🎓 | graduation-cap.svg | 教育、毕业 |
| ❤️ | heart.svg | 喜欢、收藏 |
| 🏠 | home.svg | 首页、主页 |
| ℹ️ | info.svg | 信息、帮助 |
| 🔲 | layout-grid.svg | 布局、网格 |
| ⬅️ | left.svg | 左箭头、返回 |
| ✉️ | mail.svg | 邮件、联系 |
| 📍 | map-pin.svg | 位置、地图 |
| ☰ | menu.svg | 菜单、导航 |
| ✒️ | pen-tool.svg | 设计、绘图 |
| ➡️ | right.svg | 右箭头、前进 |
| 🔍 | search.svg | 搜索、查找 |
| ⚙️ | settings.svg | 设置、配置 |
| ⭐ | star.svg | 评分、收藏 |
| 🎯 | target.svg | 目标、定位 |
| 👤 | user.svg | 用户、个人 |
| 👥 | users.svg | 用户组、团队 |

## 图标使用规范（三级优先级）

```
1. 本地图标库（优先） → icons/ 目录
2. Lucide 图标库 → https://lucide.dev/icons/
3. AI 自动生成 SVG → 保存到项目和技能目录
```

**禁止使用 Emoji 作为图标**

## 配色规范

使用 ui-design 子技能获取配色规范，或根据项目需求自定义配色。

### 常见配色方案参考

| 色系 | 适用场景 | 示例 |
|------|----------|------|
| 蓝色系 | 专业、可信赖 | 企业官网、金融应用 |
| 绿色系 | 健康、自然 | 健康应用、环保主题 |
| 紫色系 | 创意、智慧 | 设计工具、教育平台 |
| 橙色系 | 活力、热情 | 运动应用、社交平台 |
| 灰色系 | 简约、专注 | 工具类应用、后台管理 |



## 交付检查清单

### 技术栈
- [ ] 优先使用 React/Vue 3 等主流框架
- [ ] 使用 TypeScript 进行类型定义
- [ ] 组件化开发，单一职责

### 代码质量
- [ ] 所有组件有明确的 props 接口定义
- [ ] 异步操作有 try-catch 错误处理
- [ ] 表单有完整的验证逻辑
- [ ] API 调用有 loading 和 error 状态处理

### CSS/Tailwind
- [ ] 没有使用全局 CSS 重置
- [ ] Tailwind 配置保持简洁
- [ ] 自定义样式只写 Tailwind 无法表达的

### UI/UX
- [ ] 响应式布局适配移动端/平板/桌面
- [ ] 所有交互元素有 hover/active 状态
- [ ] 表单验证有清晰的错误提示
- [ ] 加载状态有骨架屏或 loading 动画

### 图标使用
- [ ] 没有使用 Emoji 作为图标
- [ ] 按优先级使用图标：本地 → Lucide → AI 生成
- [ ] 图标大小统一（通常 16px/20px/24px）

### 动画效果
- [ ] 页面加载有入场动画
- [ ] 按钮和卡片有 hover 效果
- [ ] 动画不影响性能（使用 transform/opacity）

### 可访问性
- [ ] 图片有 alt 属性
- [ ] 表单有 label 关联
- [ ] 支持键盘导航

## 目录结构

```
frontend-page-generator/
├── SKILL.md                 # 技能主文件
├── README.md                # 本文档
├── icons/                   # 本地图标库（29个SVG图标）
├── scripts/                 # 工具脚本
│   ├── generate_page.py     # 页面模板生成器
│   └── icon_manager.py      # 图标管理工具
├── sub-skills/              # 子技能模块
│   ├── ui-design/           # UI设计规范
│   ├── api-client/          # API客户端封装
│   ├── form-validation/     # 表单验证
│   ├── animations/          # 动画效果
│   └── icons/               # 图标管理
├── templates/               # 项目模板
│   └── react-flask-fullstack.md
└── references/              # 参考文档
    └── svg-icon-templates.md
```

## 快速开始

1. **生成页面模板**
   ```bash
   python scripts/generate_page.py --framework react --template dashboard
   ```

2. **管理图标库**
   ```bash
   python scripts/icon_manager.py --list      # 列出所有图标
   python scripts/icon_manager.py --add icon.svg  # 添加新图标
   ```

3. **调用子技能**
   - UI 设计规范：参考 `sub-skills/ui-design/SKILL.md`
   - API 封装：参考 `sub-skills/api-client/SKILL.md`
   - 表单验证：参考 `sub-skills/form-validation/SKILL.md`
   - 动画效果：参考 `sub-skills/animations/SKILL.md`
   - 图标管理：参考 `sub-skills/icons/SKILL.md`

## 触发词

当用户提到以下关键词时，可触发此技能：
- 生成前端页面
- 创建网页
- 前端开发
- React 项目
- Vue 项目
- 页面设计
- UI 开发


