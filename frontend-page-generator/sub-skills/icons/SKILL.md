# 图标管理子技能

## 概述
管理图标使用，采用三级优先级策略。

## 图标使用优先级

```
1. 本地图标库（优先）
   ↓ 未找到
2. Lucide 图标库（https://lucide.dev/icons/）
   ↓ 未找到
3. AI 自动生成 SVG 图标
```

## 1. 本地图标库

### 位置
```
icons/  （技能目录下）
```

### 可用图标（27个）

| 图标文件 | 用途 | 名称 |
|---------|------|------|
| home.svg | 首页 | home |
| user.svg | 用户 | user |
| users.svg | 用户组 | users |
| settings.svg | 设置 | settings |
| search.svg | 搜索 | search |
| menu.svg | 菜单 | menu |
| close.svg | 关闭 | close |
| heart.svg | 心形/喜欢 | heart |
| star.svg | 星标/收藏 | star |
| eye.svg | 查看 | eye |
| mail.svg | 邮件 | mail |
| calendar.svg | 日历 | calendar |
| clock.svg | 时钟 | clock |
| map-pin.svg | 位置 | map-pin |
| check-circle.svg | 成功 | check-circle |
| info.svg | 信息 | info |
| code.svg | 代码 | code |
| file-text.svg | 文件 | file-text |
| book-open.svg | 书籍 | book-open |
| building.svg | 建筑 | building |
| graduation-cap.svg | 毕业帽 | graduation-cap |
| pen-tool.svg | 画笔 | pen-tool |
| target.svg | 靶子 | target |
| film.svg | 影片 | film |
| compass.svg | 指南针 | compass |
| layout-grid.svg | 网格 | layout-grid |
| github.svg | GitHub | github |

### 使用方式

```html
<!-- 从本地图标库复制到项目 -->
<img src="images/icons/home.svg" alt="首页" width="24" height="24">

<!-- 或内联使用 -->
<svg width="24" height="24" class="icon">
  <use href="images/icons/home.svg#icon"></use>
</svg>
```

## 2. Lucide 图标库

### 当本地没有所需图标时，使用 Lucide 图标库

**官网**: https://lucide.dev/icons/

### 使用方式

```html
<!-- 方式1: 使用 Lucide JS 库 -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<i data-lucide="icon-name"></i>
<script>lucide.createIcons();</script>

<!-- 方式2: 直接使用 SVG（从官网复制） -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- 从 lucide.dev 复制的路径 -->
</svg>

<!-- 方式3: React 组件 -->
import { IconName } from 'lucide-react';
<IconName size={24} />

<!-- 方式4: Vue 组件 -->
import { IconName } from 'lucide-vue-next';
<IconName :size="24" />
```

### 常用 Lucide 图标

| 用途 | 图标名称 |
|------|---------|
| 首页 | home |
| 用户 | user |
| 设置 | settings |
| 搜索 | search |
| 菜单 | menu |
| 关闭 | x |
| 心形 | heart |
| 星标 | star |
| 分享 | share-2 |
| 评论 | message-circle |
| 查看 | eye |
| 时钟 | clock |
| 日历 | calendar |
| 邮件 | mail |
| 电话 | phone |
| 位置 | map-pin |
| 链接 | link |
| 下载 | download |
| 上传 | upload |
| 编辑 | edit |
| 删除 | trash |
| 添加 | plus |
| 返回 | arrow-left |
| 前进 | arrow-right |
| 上 | chevron-up |
| 下 | chevron-down |
| 左 | chevron-left |
| 右 | chevron-right |
| 外部链接 | external-link |
| 复制 | copy |
| 粘贴 | clipboard |
| 刷新 | refresh-cw |
| 加载 | loader |
| 成功 | check |
| 警告 | alert-triangle |
| 错误 | alert-circle |
| 信息 | info |
| 书签 | bookmark |
| 标签 | tag |
| 文件 | file |
| 文件夹 | folder |
| 图片 | image |
| 视频 | video |
| 音乐 | music |
| 代码 | code |
| 终端 | terminal |
| 数据库 | database |
| 服务器 | server |
| 云 | cloud |
| 锁 | lock |
| 解锁 | unlock |

## 3. AI 自动生成图标

### 当本地和 Lucide 都没有所需图标时，AI 自动生成

### 生成规则

1. **文件位置**: 保存到项目的 `images/icons/` 目录
2. **同时保存**: 复制一份到技能的 `icons/` 目录（扩充本地图标库）
3. **文件格式**: SVG 格式
4. **命名规范**: 使用 kebab-case，如 `blog-post.svg`
5. **尺寸规范**: 24x24，viewBox="0 0 24 24"
6. **颜色规范**: 使用 `currentColor` 继承文字颜色
7. **线条规范**: stroke-width="2"，stroke-linecap="round"，stroke-linejoin="round"

### SVG 模板

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- 图标路径 -->
</svg>
```

### 生成后操作

1. 将 SVG 文件保存到项目 `images/icons/` 目录
2. 将 SVG 文件复制到技能 `icons/` 目录（扩充本地图标库）
3. 在代码中使用生成的图标

## 使用流程

```
需要图标
    ↓
检查本地图标库（icons/ 目录）
    ↓ 找到
使用本地图标 ✅
    ↓ 未找到
检查 Lucide 图标库（https://lucide.dev/icons/）
    ↓ 找到
使用 Lucide 图标 ✅
    ↓ 未找到
AI 自动生成 SVG 图标
    ↓
保存到项目 images/icons/ 和技能 icons/ ✅
```

## 禁止事项

1. **禁止使用 Emoji 作为图标** - 显示不一致、无法控制样式
2. **禁止在没有检查本地和 Lucide 的情况下直接生成图标** - 浪费资源
