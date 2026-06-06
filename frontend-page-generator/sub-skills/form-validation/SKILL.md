# 表单验证子技能

## 概述
提供完整的表单验证解决方案，包括常用验证规则和验证器类。

## 验证规则

```javascript
export const validators = {
  required: (message = '此字段为必填项') => (value) => {
    if (value === undefined || value === null || value === '') return message;
    return null;
  },

  email: (message = '请输入有效的邮箱地址') => (value) => {
    if (!value) return null;
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? null : message;
  },

  phone: (message = '请输入有效的手机号') => (value) => {
    if (!value) return null;
    return /^1[3-9]\d{9}$/.test(value) ? null : message;
  },

  minLength: (min, message) => (value) => {
    if (!value) return null;
    return value.length >= min ? null : message || `至少需要${min}个字符`;
  },

  maxLength: (max, message) => (value) => {
    if (!value) return null;
    return value.length <= max ? null : message || `最多${max}个字符`;
  },

  pattern: (regex, message = '格式不正确') => (value) => {
    if (!value) return null;
    return regex.test(value) ? null : message;
  },

  match: (field, message = '两次输入不一致') => (value, formData) => {
    return value === formData[field] ? null : message;
  },

  range: (min, max, message) => (value) => {
    if (value === undefined || value === null) return null;
    const num = Number(value);
    return num >= min && num <= max ? null : message || `请输入${min}-${max}之间的数值`;
  },

  custom: (validatorFn, message) => (value, formData) => {
    return validatorFn(value, formData) ? null : message;
  }
};
```

## 表单验证器类

```javascript
export class FormValidator {
  constructor(rules = {}) {
    this.rules = rules;
  }

  validate(formData) {
    const errors = {};
    let isValid = true;

    for (const [field, fieldRules] of Object.entries(this.rules)) {
      for (const rule of fieldRules) {
        const error = rule(formData[field], formData);
        if (error) {
          errors[field] = error;
          isValid = false;
          break;
        }
      }
    }

    return { isValid, errors };
  }
}
```

## 使用示例

```javascript
const loginRules = {
  username: [validators.required('请输入用户名'), validators.minLength(3)],
  password: [validators.required('请输入密码'), validators.minLength(6)],
  email: [validators.required(), validators.email()]
};

const formValidator = new FormValidator(loginRules);
const { isValid, errors } = formValidator.validate(formData);

if (!isValid) {
  console.log('验证失败:', errors);
}
```
