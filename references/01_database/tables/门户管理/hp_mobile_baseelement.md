# 泛微OA 数据表: `hp_mobile_baseelement`

- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_baseelement`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 元素id | `varchar2` | 1000 | 是 | - |
| 2 | `elementtype` | 元素类型 | `integer` | - | 否 | - |
| 3 | `title` | 默认标题 | `varchar2` | 1000 | 是 | - |
| 4 | `logo` | 默认图标路径 | `varchar2` | 1000 | 是 | - |
| 5 | `perpage` | 默认显示条数 | `integer` | - | 是 | - |
| 6 | `linkmode` | 默认链接方式 | `integer` | - | 是 | - |
| 7 | `moreurl` | 更多链接地址 | `varchar2` | 1000 | 是 | - |
| 8 | `elementdesc` | 详细描述 | `varchar2` | 1000 | 是 | - |
| 9 | `isuse` | 是否启用 | `integer` | - | 是 | - |
| 10 | `titleen` | 英文标题 | `varchar2` | 1000 | 是 | - |
| 11 | `titlethk` | 中文繁体标题 | `varchar2` | 1000 | 是 | - |
| 12 | `loginview` | 是否登录前元素 | `integer` | - | 是 | - |
| 13 | `isbase` | 是否基础元素 | `integer` | - | 是 | - |
