# 泛微OA 数据表: `hpfieldlengthtemplate`

- **所属模块**: `门户管理`
- **数据库表名**: `hpfieldlengthtemplate`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `eid` | 元素id | `integer` | - | 否 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | - |
| 4 | `usertype` | 用户类型 | `integer` | - | 是 | - |
| 5 | `efieldid` | 元素显示字段id | `integer` | - | 否 | - |
| 6 | `charnum` | 显示字段字符长 | `integer` | - | 否 | - |
| 7 | `imgsize` | 图片尺寸 | `varchar2` | 1000 | 是 | - |
| 8 | `newstemplate` | 新闻模板 | `varchar2` | 1000 | 是 | - |
| 9 | `imgtype` | 图片类型 | `varchar2` | 1000 | 是 | - |
| 10 | `imgsrc` | 图片地址 | `varchar2` | 1000 | 是 | - |
