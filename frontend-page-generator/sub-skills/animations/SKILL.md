# 动画效果子技能

## 概述
提供标准化的动画效果实现，包括 CSS 过渡、滚动动画、GSAP 高级动画等。

## CSS 过渡动画

```css
/* 基础过渡 */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.transition-fast {
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.transition-slow {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

/* 弹性过渡 */
.transition-bounce {
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

## 滚动触发动画

```javascript
export function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        if (entry.target.dataset.once === 'true') {
          observer.unobserve(entry.target);
        }
      } else {
        if (entry.target.dataset.once !== 'true') {
          entry.target.classList.remove('animate-in');
        }
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  document.querySelectorAll('[data-animate]').forEach(el => {
    observer.observe(el);
  });

  return observer;
}
```

## CSS 动画类

```css
/* 滚动动画基础样式 */
[data-animate] {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

[data-animate].animate-in {
  opacity: 1;
  transform: translateY(0);
}

[data-animate="fade-left"] {
  transform: translateX(-30px);
}

[data-animate="fade-left"].animate-in {
  transform: translateX(0);
}

[data-animate="fade-right"] {
  transform: translateX(30px);
}

[data-animate="fade-right"].animate-in {
  transform: translateX(0);
}

[data-animate="scale"] {
  transform: scale(0.95);
}

[data-animate="scale"].animate-in {
  transform: scale(1);
}
```

## GSAP 高级动画

```javascript
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// 数字递增动画
export function animateCounter(element, endValue, duration = 2) {
  const obj = { value: 0 };
  gsap.to(obj, {
    value: endValue,
    duration,
    ease: 'power2.out',
    onUpdate: () => {
      element.textContent = Math.round(obj.value).toLocaleString();
    }
  });
}

// 卡片悬浮效果
export function initCardHover() {
  document.querySelectorAll('.hover-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      gsap.to(card, {
        y: -10,
        boxShadow: '0 20px 40px rgba(0,0,0,0.15)',
        duration: 0.3,
        ease: 'power2.out'
      });
    });

    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        y: 0,
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
        duration: 0.3,
        ease: 'power2.out'
      });
    });
  });
}

// 视差滚动
export function initParallax() {
  document.querySelectorAll('[data-parallax]').forEach(el => {
    const speed = parseFloat(el.dataset.parallax) || 0.5;

    gsap.to(el, {
      yPercent: -20 * speed,
      ease: 'none',
      scrollTrigger: {
        trigger: el,
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  });
}
```

## 加载动画

```css
/* 骨架屏 */
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  border-radius: 4px;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* 旋转加载 */
.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f3f3f3;
  border-top: 3px solid #8b5cf6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 脉冲动画 */
.pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: .5; }
}
```

## 减少动画支持

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  
  [data-animate] {
    opacity: 1;
    transform: none;
  }
}
```
