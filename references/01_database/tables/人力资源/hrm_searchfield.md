# 泛微OA 数据表: `hrm_searchfield`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_searchfield`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 否 | - |
| 2 | `fieldname` | 数据库字段名 | `varchar2` | 240 | 是 | - |
| 3 | `fieldlabel` | 字段显示名 | `varchar2` | 800 | 是 | - |
| 4 | `fieldhtmltype` | 字段类型 | `integer` | - | 是 | 1、单行文本框 2、多行文本框  3、浏览按钮 4、Check框 5、选择框 |
| 5 | `type` | 字段二级类型 | `integer` | - | 是 | 浏览框--单人力 |
| 6 | `fieldorder` | 字段顺序 | `integer` | - | 是 | - |
| 7 | `isuse` | 是否使用 | `integer` | - | 是 | - |
| 8 | `isquicksearch` | 快速搜索 | `integer` | - | 是 | - |
| 9 | `isscope` | 范围 | `integer` | - | 是 | - |
| 10 | `itemtitle` | 分组标题 | `varchar2` | 800 | 是 | 如：基本信息 、个人信息（保存的是标签） |
| 11 | `itemorder` | 顺序 | `varchar2` | 800 | 是 | - |
| 12 | `pageid` | 页面标识 | `varchar2` | 800 | 是 | - |
